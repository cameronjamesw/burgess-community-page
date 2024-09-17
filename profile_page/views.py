from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display_profile(request):
    return HttpResponse("This is the profile page!!")