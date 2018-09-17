from django import forms
from .models import Artikel, Kategori
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget

class ArtikelTambahForm(forms.Form):
    # pass
    judul = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # kategori =
    # pub_date =
    # created_by =
    # sumber =
    # disunting =
