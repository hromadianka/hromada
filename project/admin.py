from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'is_approved']
    list_filter = ['is_approved']
    actions = ['approve_projects']

    def get_readonly_fields(self, request, obj=None):
        if obj and not obj.is_approved:
            return ['is_featured']
        return []

    def approve_projects(self, request, queryset):
        queryset.update(is_approved=True)
    approve_projects.short_description = "Approve selected projects"