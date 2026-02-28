from django.contrib import admin
from .models import (
    Soviet,
    SovietType,
)

admin.site.register(Soviet)
admin.site.register(SovietType)
