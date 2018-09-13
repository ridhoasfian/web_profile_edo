from django import forms
from .models import Kategori

class TambahAnggaranForm(forms.Form):
    nama = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'nama anggaran', 'style':'margin:5px'}))
    budget = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'budget', 'style':'margin:5px'}))

class SubmitBiayaForm(forms.Form):
    keperluan = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Keperluan', 'style':'margin:5px'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Amount', 'style':'margin:5px'}))
    kategori = forms.ModelChoiceField(queryset=Kategori.objects.all(), widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Kategori', 'style':'margin:5px'}))
