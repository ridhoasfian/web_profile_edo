from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ArtikelTambahForm(forms.Form):
    judul = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    isi = forms.CharField(widget=CKEditorUploadingWidget())
    created_by = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class KategoriTambahForm(forms.Form):
    nama = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
