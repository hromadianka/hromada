from django.db import models
from django.conf import settings
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Soviet(models.Model):
    class SovietType(models.IntegerChoices):
        GENERAL = 0, _('General')
        RESIDENCE = 1, _('Residence')
        STUDY = 2, _('Study')
        WORK = 3, _('Work')
        OTHER = 4, _('Other')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    moderated = models.BooleanField(default=False)
    chat_link = models.URLField(max_length=500, blank=True)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )

    soviet_type = models.PositiveSmallIntegerField(
        choices=SovietType.choices,
        default=SovietType.OTHER,
        db_index=True,
    )


