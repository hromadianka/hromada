from django.db import models
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.

class WikiNode(MPTTModel):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('ru', 'Русский'),
        ('ua', 'Українська'),
        ('ct', 'Qırımtatarca'),
    ]

    parent = TreeForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE, related_name='children'
    )
    content = RichTextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True, null=True)
    
    is_moderated = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, editable=False)

    class MPTTMeta:
        order_insertion_by = ['order', 'created_at']

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = self.created_at or now() 

        if not self.order:
            self.order = int(self.created_at.timestamp())

        super().save(*args, **kwargs)

    def __str__(self):
        return self.content[:50]

class WikiEdit(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('ru', 'Русский'),
        ('ua', 'Українська'),
        ('ct', 'Qırımtatarca'),
    ]

    node = models.ForeignKey(WikiNode, on_delete=models.CASCADE, related_name='edits')
    proposed_content = RichTextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ['created_at']

    def apply_edit(self):
        if self.is_approved:
            self.node.content = self.proposed_content
            self.node.save()
