from django.contrib import admin
from .models import ServiceFeedback, GrantApplication


@admin.register(ServiceFeedback)
class ServiceFeedbackAdmin(admin.ModelAdmin):
    list_display = ('service_slug', 'email', 'created_at')
    list_filter = ('service_slug', 'created_at')
    search_fields = ('email', 'text')
    readonly_fields = ('created_at',)


@admin.register(GrantApplication)
class GrantApplicationAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'email', 'city', 'service_slug', 'created_at')
    list_filter = ('service_slug', 'created_at')
    search_fields = ('team_name', 'email', 'city')
    readonly_fields = ('created_at', 'latitude', 'longitude')
