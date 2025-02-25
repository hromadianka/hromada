from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.http import HttpResponseForbidden, JsonResponse

# Create your views here.

def project_detail(request, project_id):
    project = get_object_or_404(Project, id = project_id)

    return render(request, 'project_detail.html', {'project': project})

@login_required
def project_delete(request, project_id):
    if request.method == "POST":
        project = get_object_or_404(Project, id=project_id)

        if project.author != request.user:
            return HttpResponseForbidden(_("You are not allowed to delete this project"))

        project.delete()
        return JsonResponse({"message": _("Project deleted successfully")})

    return JsonResponse({"error": _("Invalid request")}, status=400) 

@login_required
def project_edit(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if project.author != request.user:
        return HttpResponseForbidden(_("You are not allowed to edit this project"))

    if request.method == 'POST':
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        if title:
            project.title = title
            project.description = description
            project.save()
            return redirect("project_detail", project_id=project.id)

    return render(request, 'project_edit.html', {"project": project})