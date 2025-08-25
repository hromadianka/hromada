from django.contrib import admin
from .models import WikiNode, WikiEdit

# Register your models here.

admin.site.register(WikiNode)
admin.site.register(WikiEdit)