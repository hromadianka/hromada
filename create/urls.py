from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.create_project, name="create_project")
]