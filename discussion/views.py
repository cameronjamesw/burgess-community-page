from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def discussion_page(request):
    return HttpResponse("This is the discussion page!")