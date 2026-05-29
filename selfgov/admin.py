from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import (
    Soviet,
    SovietType,
)


class SovietTypeAdmin(TranslatableAdmin):
    list_display = ("__str__", "order")
    ordering = ["order"]


admin.site.register(Soviet)
admin.site.register(SovietType, SovietTypeAdmin)
