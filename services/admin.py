from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Service, ServiceFeedback, GrantApplication


@admin.register(Service)
class ServiceAdmin(TranslatableAdmin):
    list_display = ('slug', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ()}
    readonly_fields = ('created_at',)


@admin.register(ServiceFeedback)
class ServiceFeedbackAdmin(admin.ModelAdmin):
    list_display = ('service', 'email', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('email', 'text')
    readonly_fields = ('created_at',)


@admin.register(GrantApplication)
class GrantApplicationAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'email', 'city', 'service', 'created_at')
    list_filter = ('service', 'created_at')
    search_fields = ('team_name', 'email', 'city')
    readonly_fields = ('created_at', 'latitude', 'longitude')
