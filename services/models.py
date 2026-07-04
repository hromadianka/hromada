from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Service(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        short_description=models.TextField(),
        instruction=models.TextField(),
    )
    slug = models.SlugField(max_length=100, unique=True)
    brochure_url = models.URLField(help_text="Посилання на брошурку в Canva")
    brochure_embed_url = models.URLField(
        blank=True,
        help_text="Embed-посилання для iframe (якщо є, наприклад Canva embed link)"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True) or self.slug

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServiceFeedback(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='feedbacks')

    email = models.EmailField(blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'


class GrantApplication(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='grant_applications')

    team_name = models.CharField(max_length=255)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)   # з embed-мапи
    longitude = models.FloatField(null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Grant application'
        verbose_name_plural = 'Grant applications'
