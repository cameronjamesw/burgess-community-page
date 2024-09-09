from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Discussion
from .forms import CommentForm

# Create your views here.

class DiscussionList(generic.ListView):
    queryset = Discussion.objects.all()
    template_name = "discussion/index.html"

def discussion_content(request, slug):
    queryset = Discussion.objects.filter(status=1)
    discussion = get_object_or_404(queryset, slug=slug)
    comments = discussion.comments.all().order_by("-created_on")
    comment_count = discussion.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.discussion = discussion
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment successfully submitted, now awaiting approval'
        )

    comment_form = CommentForm()

    return render(
        request,
        "discussion/discussion_content.html",
        {"discussion": discussion,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form},
        
    )