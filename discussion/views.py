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
    comments = discussion.comments.all().order_by("-created_on")
    comment_count = discussion.comments.filter(approved=True).count()

    return render(
        request,
        "discussion/discussion_content.html",
        {"discussion": discussion,
        "comments": comments,
        "comment_count": comment_count},
    )