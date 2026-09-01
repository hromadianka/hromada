import string
import uuid
from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField


class EduEventType(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    translations = TranslatedFields(
        name=models.CharField(max_length=64),
        description=models.CharField(max_length=128),
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Lowest number appears first",
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Educational Event Type"
        verbose_name_plural = "Educational Event Types"

    def __str__(self):
        return self.safe_translation_getter(
            "name",
            language_code="en",
            any_language=True,
        )


class EduEvent(TranslatableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        description=RichTextField(blank=True),
        address=models.CharField(max_length=512),
    )
    event_type = models.ForeignKey(
        "EduEventType",
        on_delete=models.PROTECT,
        related_name="events",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_edu_events",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()

    class Meta:
        permissions = (
            ("can_sign_up", "Can sign up to Educational Events"),
        )
        ordering = ["start_date"]
        verbose_name = "Educational Event"
        verbose_name_plural = "Educational Events"

    def __str__(self):
        return self.safe_translation_getter(
            "title",
            language_code="en",
            any_language=True,
        )


def _generate_code():
    return get_random_string(length=8, allowed_chars=string.ascii_uppercase)


class EduEventRegistration(models.Model):
    event = models.ForeignKey(
        "EduEvent",
        on_delete=models.CASCADE,
        related_name="registrations"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="edu_event_registrations"
    )
    code = models.CharField(max_length=8, default=_generate_code)
    checked_in = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Educational Event Registration"
        verbose_name_plural = "Educational Event Registrations"
        constraints = [
            # can't do CompositePrimaryKey in Django 5.0.9
            # doing this instead
            models.UniqueConstraint(
                fields=["event", "user"],
                name="unique_user_per_event",
            ),
            # codes must be unique for each user in a single event
            models.UniqueConstraint(
                fields=["event", "code"],
                name="unique_code_per_event",
            ),
        ]

    def event_title(self):
        return self.event.title

    def username(self):
        return self.user.username