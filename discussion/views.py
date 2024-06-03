from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Discussion

# Create your views here.

class DiscussionList(generic.ListView):
    queryset = Discussion.objects.all()
    template_name = "discussion/index.html"

def discussion_content(request, slug):
    queryset = Discussion.objects.filter(status=1)
    discussion = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "discussion/discussion_content.html",
        {"discussion": discussion},
    )