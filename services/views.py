from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Service
from .forms import ServiceFeedbackForm, GrantApplicationForm


def services_list(request):
    services = Service.objects.filter(is_active=True)
    return render(request, 'services_list.html', {'services': services})


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)

    feedback_form = ServiceFeedbackForm()
    grant_form = GrantApplicationForm()

    if request.method == 'POST':
        if 'feedback_submit' in request.POST:
            feedback_form = ServiceFeedbackForm(request.POST)
            if feedback_form.is_valid():
                feedback = feedback_form.save(commit=False)
                feedback.service = service
                feedback.save()
                messages.success(request, 'Дякуємо за відгук!')
                return redirect('service_detail', slug=slug)

        elif 'grant_submit' in request.POST:
            grant_form = GrantApplicationForm(request.POST)
            if grant_form.is_valid():
                application = grant_form.save(commit=False)
                application.service = service
                application.save()
                messages.success(request, 'Заявку надіслано!')
                return redirect('service_detail', slug=slug)

    return render(request, 'service_detail.html', {
        'service': service,
        'feedback_form': feedback_form,
        'grant_form': grant_form,
    })
