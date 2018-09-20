from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

class ArtikelTambahForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'created_by', 'sumber', 'kategori']
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'created_by':forms.TextInput(attrs={'class':'form-control'}),
            'sumber':forms.TextInput(attrs={'class':'form-control'}),
        }

class ArtikelEditForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'created_by', 'sumber', 'kategori']
        widgets = {
            'judul':forms.TextInput(attrs={'class':'form-control'}),
            'created_by':forms.TextInput(attrs={'class':'form-control'}),
            'sumber':forms.TextInput(attrs={'class':'form-control'}),
        }

class KategoriTambahForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama']
        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
        }

class KategoriEditForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama']
        widgets = {
            'nama':forms.TextInput(attrs={'class':'form-control'}),
        }
