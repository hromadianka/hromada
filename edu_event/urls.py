from django.urls import path
from . import views


urlpatterns = [
    path("", views.edu_event_list, name="edu_event_list"),
    path('<uuid:edu_event_id>/', views.edu_event_detail, name = 'edu_event_detail'),
    path('<uuid:edu_event_id>/signup/', views.edu_event_signup, name='edu_event_signup'),
    path('<uuid:edu_event_id>/registrations/', views.edu_event_registrations_list, name='edu_event_registrations_list'),
]
