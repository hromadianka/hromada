from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    EduEvent,
    EduEventType, EduEventRegistration,
)


class EduEventTypeAdmin(TranslatableAdmin):
    list_display = ("__str__", "order")
    ordering = ["order"]


class EduEventAdmin(TranslatableAdmin):
    list_display = ("__str__", "start_date")


class EduEventRegistrationAdmin(admin.ModelAdmin):
    list_display = ("event_title", "username", "code", "checked_in")
    search_fields = ("user__username", "event__translations__title", "code")
    ordering = ("-event__start_date", "checked_in", "user__username")
    list_filter = ("event__start_date", "checked_in")


admin.site.register(EduEvent, EduEventAdmin)
admin.site.register(EduEventType, EduEventTypeAdmin)
admin.site.register(EduEventRegistration, EduEventRegistrationAdmin)
