from django import forms
from .models import Staff_Member

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Staff_Member
        fields = ('photo', 'camp', 'position', 'tenure', 'facts', 'memory' )
        labels = {
            'photo': 'Profile Photo',
            'tenure': 'Years Worked',
            'facts': 'Interesting Fact',
            'memory': 'Favourite Memory'
        }

