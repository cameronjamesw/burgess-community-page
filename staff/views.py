from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from .models import Staff_Member
from .forms import ProfileForm

# Create your views here.

# This view is to display the staff profiles
def display_staff(request):
    """
    This view renders the staff profile page to
    the user and displays all the instances from
    :model:`staff.Staff_Member`. Also allows the 
    user to create their own staff profile through
    creating an instance of :form:`staff.ProfileForm`.

    **Context**

    ``staff_profiles``
        Refers to all the objects with :model:`staff.Staff_Member`.

    ``profile_form``
        An instance of :form:`staff.ProfileForm`

    **Template**

    :template:`staff/staff_profile.html`
    """
    staff_profiles = Staff_Member.objects.all()

    # This empty list is populated with users upon the view loading
    current_profiles = []

    for profile in staff_profiles:
        current_profiles.append(profile.user)
    

    # This if statement is regarding the Staff Profile Form 
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)

        # This if statement ensures there are no duplicate profiles
        if request.user not in current_profiles:
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

def display_burgess_staff(request):
    """
    This view renders the staff profile page to
    the user but only displays instance from
    :model:`staff.Staff_Member` that have a camp
    value of 0 or Burgess.

    **Context**

    ``staff_profiles``
        Refers to all the objects with :model:`staff.Staff_Member`.

    **Template**

    :template:`staff/staff_profile.html`
    """
    staff_profiles = Staff_Member.objects.filter(camp=0)

    context = {
        'staff_profiles': staff_profiles
    }

    return render(
        request,
        "staff/staff_profile.html",
        context
    )

def display_hayward_staff(request):
    """
    This view renders the staff profile page to
    the user but only displays instance from
    :model:`staff.Staff_Member` that have a camp
    value of 1 or Hayward.

    **Context**

    ``staff_profiles``
        Refers to all the objects with :model:`staff.Staff_Member`.

    **Template**

    :template:`staff/staff_profile.html`
    """
    staff_profiles = Staff_Member.objects.filter(camp=1)

    context = {
        'staff_profiles': staff_profiles
    }

    return render(
        request,
        "staff/staff_profile.html",
        context
    )