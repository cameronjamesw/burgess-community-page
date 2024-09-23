from django.shortcuts import render, get_object_or_404, reverse
from .models import Staff_Member
from django.http import HttpResponse

# Create your views here.

# This view is to display the staff profiles
def display_staff(request):
    staff_profiles = Staff_Member.objects.all()

    context = {
        "staff_profiles": staff_profiles
    }

    return render(
        request,
        "staff/staff_profile.html",
        context
    )