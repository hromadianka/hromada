from django.urls import path
from . import views

urlpatterns = [
    path('', views.selfgov_list, name = 'selfgov_list'),
    path('create', views.selfgov_create, name = 'selfgov_create'),
    path('<uuid:selfgov_id>/', views.selfgov_detail, name = 'selfgov_detail'),
    path('<uuid:selfgov_id>/edit/', views.selfgov_edit, name = 'selfgov_edit')
]