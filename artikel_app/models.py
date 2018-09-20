from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Artikel(models.Model):
    kategori = models.ManyToManyField('Kategori')
    judul = models.CharField(max_length=200)
    isi = RichTextUploadingField()
    created_by = models.CharField(max_length=200)
    sumber = models.CharField(max_length=500)
    pub_date = models.DateField()
    edit_date = models.DateField()
    def __str__(self):
        return self.judul

class Kategori(models.Model):
    nama = models.CharField(max_length=200)
    def __str__(self):
        return self.nama
