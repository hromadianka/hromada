from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ("username", "email", "groups"),
        }),
    )
    filter_horizontal = ("groups",)
    list_display = ("username", "email")
    readonly_fields = ("username", "email")
    search_fields = ("username", "email")


admin.site.register(User, UserAdmin)