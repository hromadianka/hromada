from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('survey/', views.survey, name="survey"),
    path("choose-tasks/", views.choose_tasks, name="choose_tasks"),
]