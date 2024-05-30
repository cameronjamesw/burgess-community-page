from django.shortcuts import render
from django.views import generic
from .models import Discussion

# Create your views here.

class DiscussionList(generic.ListView):
    queryset = Discussion.objects.all()
    template_name = "discussion_list"