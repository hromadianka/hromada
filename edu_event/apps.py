from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_subscribers_group(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    group, _ = Group.objects.get_or_create(name='Educational Events Subscribers')
    group.permissions.set(
        Permission.objects.filter(
            content_type__app_label='edu_event',
            codename='can_sign_up'
        )
    )


class EduEventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu_event'

    def ready(self):
        post_migrate.connect(create_subscribers_group, sender=self)
