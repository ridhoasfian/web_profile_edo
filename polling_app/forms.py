from django import forms

class PollingTambahForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    choice1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    choice2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
