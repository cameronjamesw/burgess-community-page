from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from .models import Staff_Member
from .forms import ProfileForm

# Create your views here.

# This view is to display the staff profiles
def display_staff(request):
    staff_profiles = Staff_Member.objects.all()

# This if statement is regarding the Staff Profile Form 
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.post)
        if profile_form.is_valid():
            staff_profile = profile_form.save(commit=False)
            staff_profile.user = request.user
            staff_profile.save()
            messages.add_message(
                request, messgaes.SUCCESS,
                "Staff profile successfully created!"
            )
        else:
            messages.add_message(
                request, ERROR,
                "Error creating staff profile, please try again."
            )


    profile_form = ProfileForm()

    context = {
        "staff_profiles": staff_profiles,
        "profile_form": profile_form
    }

    

    return render(
        request,
        "staff/staff_profile.html",
        context
    )