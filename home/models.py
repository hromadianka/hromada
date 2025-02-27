from django.db import models

# Create your models here.

class SurveyResponse(models.Model):
    age = models.PositiveIntegerField()
    income_option = models.CharField(max_length=255)
    social_status_option = models.CharField(max_length=255)
    profession = models.CharField(max_length=255, blank=True, null=True)
    field = models.CharField(max_length=255, blank=True, null=True)
    education_option = models.CharField(max_length=255)
    veterans_option = models.CharField(max_length=255, blank=True, null=True)
    dead_veterans_option = models.CharField(max_length=255, blank=True, null=True)
    birthplace = models.CharField(max_length=255)
    residence = models.CharField(max_length=255)
    participating_option = models.CharField(max_length=255)
    participating_about_question = models.TextField(blank=True, null=True)
    participating_reasons_question = models.TextField(blank=True, null=True)
    participating_more_question = models.TextField(blank=True, null=True)
    interest_level_1 = models.CharField(max_length=255)
    interest_level_2 = models.CharField(max_length=255)
    why_interest_rate_question = models.TextField(blank=True, null=True)
    government_option = models.CharField(max_length=255)
    government_additional_question = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SurveyResponse {self.id} - {self.age} years old"


class SocialReason(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('ru', 'Русский'),
        ('ua', 'Українська'),
        ('ct', 'Qırımtatarca'),
    ]

    text = models.CharField(max_length=255, blank=True, null=True)
    was_approved = models.BooleanField(default=False)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True)

    def __str__(self):
        return self.text