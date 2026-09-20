import string
from datetime import timedelta

from django.contrib.auth.decorators import permission_required, login_required
from django.db import IntegrityError
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.translation import gettext
from django.views.decorators.http import require_http_methods

from .models import EduEvent, EduEventRegistration


def edu_event_list(request):
    now = timezone.now()
    context = {
        'events': EduEvent.objects.filter(start_date__gte=now).order_by('start_date'),
        'recent': EduEvent.objects
                .filter(start_date__lt=now, start_date__gte=now - timedelta(weeks=2))
                .order_by('-start_date')[:24]
    }
    return render(request, "edu_event_list.html", context)

@require_http_methods(["POST"])
@permission_required('edu_event.can_sign_up')
@login_required
def edu_event_signup(request, edu_event_id):
    event = get_object_or_404(EduEvent, pk=edu_event_id)
    registration = None
    for _ in range(10):
        try:
            registration, _ = EduEventRegistration.objects.get_or_create(
                event=event,
                user=request.user,
            )
            break
        except IntegrityError:
            # random code repeated for different attendees under the same event, try again
            pass
    context = {
        'event': event,
        'registration': registration,
    }
    return render(request, "edu_event_signup.html", context)


def edu_event_detail(request, edu_event_id):
    event = get_object_or_404(EduEvent, pk=edu_event_id)
    authenticated = request.user.is_authenticated
    can_sign_up = request.user.has_perm('edu_event.can_sign_up')
    can_list_attendees = request.user == event.author or request.user.is_superuser

    registration = None
    if can_sign_up:
        try:
            registration = EduEventRegistration.objects.get(event=event, user=request.user)
        except EduEventRegistration.DoesNotExist:
            pass

    context = {
        'authenticated': authenticated,
        'can_sign_up': can_sign_up,
        'registration': registration,
        'event': event,
        'is_author': request.user == event.author,
        'is_superuser': request.user.is_superuser,
    }
    return render(request, "edu_event_detail.html", context)


@login_required
def edu_event_registrations_list(request, edu_event_id):
    event = get_object_or_404(EduEvent, pk=edu_event_id)
    if request.user != event.author and not request.user.is_superuser:
        return HttpResponseForbidden(gettext("You are not allowed to see the list of attendees for this event."))
    registrations = EduEventRegistration.objects.filter(event=event).order_by("user__username")
    context = { 'event': event, 'registrations': registrations }
    return render(request, "edu_event_registrations_list.html", context)