from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def project_detail(request, project_id):
    project = get_object_or_404(Project, id = project_id)

    return render(request, 'project_detail.html', {'project': project})