from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    isi = RichTextUploadingField()
    created_by = models.CharField(max_length=200)
    sumber = models.CharField(max_length=500)
    pub_date = models.DateField()
    edit_date = models.DateField()

class Kategori(models.Model):
    artikel = models.ForeignKey('Artikel', on_delete=models.CASCADE)
    nama = models.CharField(max_length=200)
