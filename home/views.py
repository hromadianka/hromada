from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SurveyResponse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _
from project.models import Project
from .models import SocialReason
from django.http import JsonResponse
from django.utils.translation import get_language

# Create your views here.

def home_page(request):
    featured_projects = Project.objects.filter(is_featured=True).order_by("-created_at")

    selected_language = get_language()
    social_reasons = SocialReason.objects.filter(was_approved=True, language=selected_language)

    context = {
        'featured_projects': featured_projects,
        'social_reasons': social_reasons,
    }
    return render(request, 'home_page.html', context)

def survey(request):
    if request.method == "POST":
        fields = [
            "age", "income-option", "profession", "field", "education-option", 
            "veterans-option", "dead-veterans-option", "birthplace", 
            "residence", "participating-about-question", "participating-reasons-question",
            "participating-more-question", "interest-level-1", "interest-level-2",
            "why-interest-rate-question", "government-additional-question"
        ]

        checkbox_fields = ["social-status-option", "participating-option", "government-option"]

        data = {field.replace("-", "_"): request.POST.get(field, None) for field in fields}

        for field in checkbox_fields:
            data[field.replace("-", "_")] = ", ".join(request.POST.getlist(field))

        SurveyResponse.objects.create(**data)

        messages.success(request, _("Survey Success Message"))

    return redirect("home_page")


def choose_tasks(request):
    if request.method == "POST":
        selected_tasks = request.POST.getlist("tasks")

        task_mapping = {
            _("Task 4"): _("Task 4") + ' <a href="mailto:go-hromada@proton.me">go-hromada@proton.me</a>',
            _("Task 5"): _("Task 5") + ' <a href="mailto:go-hromada@proton.me">go-hromada@proton.me</a>',
        }

        task_list = "".join(f"<li>{task_mapping.get(task, task)}</li>" for task in selected_tasks)

        if selected_tasks:
            messages.success(request, mark_safe(
                _("Tasks Success Message") + f"<ul>{task_list}</ul>"
            ))
        else:
            messages.warning(request, _("Tasks Failure Message"))

    return redirect("home_page")

def add_reason(request):
    if request.method == 'POST':
        reason_text = request.POST.get('reason_text')

        if not reason_text:
            return JsonResponse({"error": "Reason cannot be empty"}, status=400)

        SocialReason.objects.create(text=reason_text)
        return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"}, status=400)