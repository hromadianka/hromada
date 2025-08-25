from django.shortcuts import render
from project.models import Project

# Create your views here.

def search(request):
    all_projects = Project.objects.all()
<<<<<<< HEAD
    return render(request, 'search.html', {'all_projects': all_projects})
=======
    return render(request, 'search.html', {'all_projects': all_projects})
>>>>>>> fb87a540d7a93b6cebf9f384edcba23faec54191
