from django.shortcuts import render, get_object_or_404, reverse
from .models import User_Profile
from django.http import HttpResponse

# Create your views here.

def display_profile(request):
    profiles = User_Profile.objects.all()

    context = {
        "profiles": profiles
    }

    return render(
        request,
        "profile/user_profile.html",
        context
    )