from django.shortcuts import render
from project.models import Project

# Create your views here.

def search(request):
    all_projects = Project.objects.all()
    return render(request, 'search.html', {'all_projects': all_projects})