from django.urls import path
from . import views

urlpatterns = [
    path('', views.wiki, name='wiki'),
    path("edit/<int:node_id>/", views.wiki_edit, name="wiki_edit"),
    path("add/", views.wiki_add, name="wiki_add"),
    path("add/<int:parent_id>/", views.wiki_add, name="wiki_add_child"),
]