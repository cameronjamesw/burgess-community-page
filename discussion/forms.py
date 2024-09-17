from .models import Discussion, Comment
from django import forms

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ('title', 'excerpt', 'content')
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)