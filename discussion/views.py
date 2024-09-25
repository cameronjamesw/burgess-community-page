from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from .models import Discussion, Comment
from .forms import DiscussionForm, CommentForm

# Create your views here.

# This is the discussion list view
def discussion_list(request):
    """
    This view renders the home page and displays the most
    recent list of discussions to the user, ordered by how
    recent the discussions have been created. This view
    also gives users the ability to create their own 
    discussions in the way of a validated form which is
    called through this view.

    **Context**

    ``discussions``
        All the accounts data with :model:`discussion.Discussion`

    ``discussion_form``
        An istance of :form:`discussion.DiscussionForm`

    **Template:**

    :template:`discussion/index.html`
    """
    discussions = Discussion.objects.all().order_by("-created_on")
   
    # This if statement refers to the Discussion Form
    if request.method == "POST":
        discussion_form = DiscussionForm(request.POST, request.FILES)
        if discussion_form.is_valid():
            discussion = discussion_form.save(commit=False)
            discussion.author = request.user

            # Slugify creates a slug based off of the title field 
            discussion.slug = slugify(discussion.title)
            discussion.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you, discussion submitted, awaiting approval!'
            )
    
    discussion_form = DiscussionForm()

    context = {
        "discussions": discussions,
        "discussion_form": discussion_form,
        }

    return render(
        request,
        "discussion/index.html",
        context,
    )

# This is the discussion content view
def discussion_content(request, slug):
    """
    This view renders the instance of the discussion
    within a seperate page, as well as displaying the 
    comments that relate to the discussion. The author
    of the discussion can also edit and update the
    discussion through this view. Users can create comments
    through this view too.

    **Context**

    ``discussion``
        The instance of the discussion being displayed
        from :model:`discussion.Discussion`

    ``comments``
        The approved comments that relate to the instance of the
        discussion

    ``comment_count``
        A count of approved comments relating to the discussion

    ``comment_form``
        An instance of :form:`discussion.CommentForm`
    
    ``discussion_form``
        An instance of :form:`discussion.DiscussionForm`

    **Template**

    :template:`discussion/discussion_content.html`
    """
    queryset = Discussion.objects.filter(status=1)
    discussion = get_object_or_404(queryset, slug=slug)

    # Comments are ordered by date created
    comments = discussion.comments.all().order_by("-created_on")
    comment_count = discussion.comments.filter(approved=True).count()

    # This if statement refers to the comment form
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

    discussion_form = DiscussionForm()
    comment_form = CommentForm()

    return render(
        request,
        "discussion/discussion_content.html",
        {"discussion": discussion,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "discussion_form": discussion_form
        },
    )

# This is the comment edit view 
def comment_edit(request, slug, comment_id):
    """
    Display an individual comment to edit

    **Context**

    ``discussion``
        The instance of the discussion being displayed
        from :model:`discussion.Discussion`

    ``comment``
        A single comment related to the discussion

    ``comment_form``
        An instance of :form:`discussion.CommentForm`

    """

    # This if statement refers to editing comment 
    if request.method == "POST":
        queryset = Discussion.objects.filter(status=1)
        discussion = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        # This if statement ensures users can only edit their 
        # own comments, otherwise throws an error 
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.discussion = discussion
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    # Upon submission, user is returned to the initial discussion
    return HttpResponseRedirect(reverse('discussion_content', args=[slug]))

# This view refers to deleting a comment
def comment_delete(request, slug, comment_id):
    """
    This view displays a singular comment for the
    user to delete

    **Context**

    ``discussion``
        The instance of the discussion being displayed
        from :model:`discussion.Discussion`

    ``comment``
        Refers to the comment related to the
        discussion that the user wants to delete
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

# This view refers to editing a discussion
def discussion_edit(request, slug):
    """
    This is the view to edit an exisitng discussion.

    **Context**

    ``discussion``
        The instance of the discussion being displayed
        from :model:`discussion.Discussion`

    ``discussion_form``
        An instance of :form:`discussion.DiscussionForm`
    """

    # This if statement ensures the method is correct for the
    # edit discussion form 
    if request.method == "POST":
        queryset = Discussion.objects.all()
        discussion = get_object_or_404(queryset, slug=slug)
        discussion_forn = DiscussionForm(data=request.POST, instance=discussion)

        # This if statement ensures only the author can
        # edit their own discussions
        if discussion_forn.is_valid() and discussion.author == request.user:
            discussion = discussion_forn.save(commit=False)
            discussion.approved = False
            discussion.save()
            messages.add_message(request, messages.SUCCESS, 'Discussion updated, now awaiting approval!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating discussion!')

        # The user will be returned to the home page
        return HttpResponseRedirect(reverse('home'))

# This view refers to deleting a discussion
def discussion_delete(request, slug):
    """
    This function allows the author to delete
    their own discussion from 
    :model:`discussion.Discussion`

    **Context**

    ``discussion``
        The instance of the discussion being displayed
        from :model:`discussion.Discussion`
    """
    queryset = Discussion.objects.all()
    discussion = get_object_or_404(queryset, slug=slug)

    # This if statement ensures only the author of the
    # discussion is able to delete it
    if discussion.author == request.user:
        discussion.delete()
        messages.add_message(request, messages.SUCCESS, 'Discussion successfully deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own discussions!')

    # This return statement sends the user to the home page
    # as the discussion no longer exsists
    return HttpResponseRedirect(reverse('home'))
