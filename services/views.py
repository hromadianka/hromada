from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ServiceFeedbackForm, GrantApplicationForm


def services_list(request):
    return render(request, 'services_list.html')


def social_support(request):
    feedback_form = ServiceFeedbackForm()
    grant_form = GrantApplicationForm()

    if request.method == 'POST':
        if 'feedback_submit' in request.POST:
            feedback_form = ServiceFeedbackForm(request.POST)
            if feedback_form.is_valid():
                feedback = feedback_form.save(commit=False)
                feedback.service_slug = 'social-support'
                feedback.save()
                messages.success(request, 'Дякуємо за відгук!')
                return redirect('social_support')

        elif 'grant_submit' in request.POST:
            grant_form = GrantApplicationForm(request.POST)
            if grant_form.is_valid():
                application = grant_form.save(commit=False)
                application.service_slug = 'social-support'
                application.save()
                messages.success(request, 'Заявку надіслано!')
                return redirect('service_detail')

    return render(request, 'social_support.html', {
        'feedback_form': feedback_form,
        'grant_form': grant_form,
    })
