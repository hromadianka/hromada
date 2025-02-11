from django.shortcuts import render
from django.contrib import messages
from .models import SurveyResponse

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')

def survey(request):
    if request.method == "POST":
        fields = [
            "age", "income-option", "social-status-option", "profession", "field",
            "education-option", "veterans-option", "dead-veterans-option",
            "birthplace", "residence", "participating-option",
            "participating-about-question", "participating-reasons-question",
            "participating-more-question", "interest-level-1", "interest-level-2",
            "why-interest-rate-question", "government-option", "government-additional-question"
        ]

        data = {field.replace("-", "_"): request.POST.get(field, None) for field in fields}
        SurveyResponse.objects.create(**data)
        
        messages.success(request, "Ваша відповідь успішно збережена. Ми дуже вдячні вам за участь❤")

    return render(request, "home_page.html")