from .models import Staff_Member
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Staff_Member
        fields = ('photo', 'camp', 'position', 'tenure', 'facts', 'memory' )

