from django import forms
from .models import Artikel, Kategori
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget

class ArtikelTambahForm(forms.ModelForm):
    # judul =
    # kategori =
    # pub_date =
    # created_by =
    # sumber =
    # disunting =
