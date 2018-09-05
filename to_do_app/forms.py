from django import forms

class ToDoForm(forms.Form):
    text = forms.CharField(max_length=200,
    widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukkan Yang Ingin Anda Kerjakan !', 'aria-label':'Todo', 'aria-describedby':'add-btn'}))
