from django import forms
from .models import TestUpload

class TestUploadForm(forms.ModelForm):
    class Meta:
        model = TestUpload
        fields = ['nama', 'foto']
        widgets = {

        }
