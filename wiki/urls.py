from django.urls import path
from . import views

urlpatterns = [
    path('', views.wiki, name='wiki'),
    path("edit/<int:node_id>/", views.wiki_edit, name="wiki_edit"),
]