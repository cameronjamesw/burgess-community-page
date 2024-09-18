from django.shortcuts import render, get_object_or_404, reverse
from .models import User_Profile
from django.http import HttpResponse

# Create your views here.

def display_profile(request):
    user = request.user
    queryset = User_Profile.objects.all()
    profile = get_object_or_404(queryset)

    context = {
        "profile": profile
    }

    return render(
        request,
        "profile/user_profile.html",
        context
    )