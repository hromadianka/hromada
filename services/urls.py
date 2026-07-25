from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_list, name='services_list'),
    path('social-support/', views.social_support, name='social_support'),
]
