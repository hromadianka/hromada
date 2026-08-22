from django.db import models


class ServiceFeedback(models.Model):
    service_slug = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'


class GrantApplication(models.Model):
    service_slug = models.CharField(max_length=100)
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
