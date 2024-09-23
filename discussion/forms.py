from .models import Discussion, Comment
from django import forms

# This is the Discussion Form where users can create a discussion 
class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ('title', 'excerpt', 'content')
        

# This is the Comment Form where users can create a comment 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)