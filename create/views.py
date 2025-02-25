from django.shortcuts import render
from project.models import Project

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from project.models import Project

@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()

        project = Project.objects.create(
            author=request.user,
            title=title,
            description=description
        )

        return redirect("project_detail", project_id=project.id)

    return render(request, 'create_project.html')
