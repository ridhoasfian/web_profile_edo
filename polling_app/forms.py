from django import forms
from .models import Poll, Choice

class PollingTambahForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    choice1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    choice2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class PollingEditForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['text']
        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control'}),
        }

class ChoiceTambahForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['text']
        widgets = {
            'text':forms.TextInput(attrs={'class':'form-control', 'placeholder':'choice text'}),
        }
