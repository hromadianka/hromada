import uuid
from django.db import models
from django.conf import settings


class SovietType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]
        verbose_name = "Soviet Type"
        verbose_name_plural = "Soviet Types"

    def __str__(self):
        return self.name


class Soviet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    chat_link = models.URLField(max_length=500, blank=True)

    soviet_type = models.ForeignKey(
        "SovietType",
        on_delete=models.PROTECT,
        related_name="soviets",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_soviets",
    )

    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )

    moderated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Soviet"
        verbose_name_plural = "Soviets"

    def __str__(self):
        return self.title
