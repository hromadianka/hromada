from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from project.models import Project
from django.http import JsonResponse
from django.contrib.auth import logout
from django.utils.translation import gettext as _

User = get_user_model() 

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user) 
            login(request, new_user)
            return redirect("account")
    else:
        user_form = UserRegistrationForm()

    return render(request, "account/register.html", {"user_form": user_form})

@login_required
def account(request):
    projects = Project.objects.filter(author=request.user)
    return render(request, "account/account.html", {"user": request.user, "projects": projects})

@login_required
def delete_data(request):
    if request.method == "POST":
        user = request.user

        Project.objects.filter(author=user).delete()

        user.delete()
        logout(request)

        return JsonResponse({"message": _("Account deleted")})

    return JsonResponse({"error": _("Invalid request")}, status=400)