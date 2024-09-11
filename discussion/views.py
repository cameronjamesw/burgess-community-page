from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Discussion, Comment
from .forms import DiscussionForm, CommentForm

# Create your views here.

def discussion_list(request):
    discussions = Discussion.objects.all().order_by("-created_on")
   
    if request.method == "POST":
        discussion_form = DiscussionForm(data=request.POST)
        if discussion_form.is_valid():
            discussion = discussion_form.save(commit=False)
            discussion.author = request.author
            discussion.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you, discussion submitted'
            )
    
    discussion_form = DiscussionForm()

    context = {
        "discussions": discussions,
        "discussion_form": discussion_form
        }

    return render(
        request,
        "discussion/index.html",
        context,
    )

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
        'Comment submitted and awaiting approval'
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

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Discussion.objects.filter(status=1)
        discussion = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.discussion = discussion
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('discussion_content', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Discussion.objects.filter(status=1)
    discussion = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('discussion_content', args=[slug]))