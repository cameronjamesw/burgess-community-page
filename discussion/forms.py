from django import forms
from .models import Discussion, Comment

# This is the Discussion Form where users can create a discussion


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ('title', 'featured_image', 'excerpt', 'content')
        labels = {
            'featured_image': 'Discussion Photo',
        }


# This is the Comment Form where users can create a comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
