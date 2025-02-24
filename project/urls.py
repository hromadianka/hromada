from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:project_id>/', views.project_detail, name = 'project_detail')
]