from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:project_id>/', views.project_detail, name = 'project_detail'),
    path('<uuid:project_id>/edit/', views.project_edit, name = 'project_edit'),
    path('<uuid:project_id>/delete/', views.project_delete, name = 'project_delete')
]