from django import forms
from .models import *

class ScheduleTambahForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['nama', 'tanggal', 'deskripsi']
        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
            'tanggal':forms.DateTimeInput(attrs={'class':'form-control','id':'pilih_tanggal'}),
            'deskripsi':forms.Textarea(attrs={'class':'form-control'}),
        }
