from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from .models import Staff_Member
from .forms import ProfileForm

# Create your views here.

# This view is to display the staff profiles
def display_staff(request):
    staff_profiles = Staff_Member.objects.all()
    user = request.user
    users = Staff_Member.objects.filter(user=user)

    # This empty list is populated with users upon the view loading
    current_profiles = []

    for profile in staff_profiles:
        current_profiles.append(profile.user)
    

    # This if statement is regarding the Staff Profile Form 
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST)

        # This if statement ensures there are no duplicate profiles
        if request.user not in current_profiles:
            print(request.user)
            if profile_form.is_valid():
                staff_profile = profile_form.save(commit=False)
                staff_profile.user = request.user
                staff_profile.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "Staff profile successfully created, awaiting approval!"
                )
            else:
                messages.add_message(
                    request, messages.ERROR,
                    "Error creating staff profile, please try again."
                )
        else:
            messages.add_message(
                request, messages.ERROR,
                "You can only have one profile!"
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