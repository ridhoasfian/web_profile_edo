from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Artikel(models.Model):
    class Meta:
        ordering = ['-edit_date',]

    kategori = models.ManyToManyField('Kategori')
    foto_sampul = models.ImageField(default='default.png', upload_to='foto_sampul_artikel/%Y/%m/%d/', blank=True)
    judul = models.CharField(max_length=200)
    isi = RichTextUploadingField()
    created_by = models.CharField(max_length=200)
    sumber = models.CharField(max_length=500)
    sumber_url = models.CharField(max_length=800, blank=True, null=True)
    pub_date = models.DateField()
    edit_date = models.DateField()
    def __str__(self):
        return self.judul

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Kategori(models.Model):
    class Meta:
        ordering = ['nama',]

    nama = models.CharField(max_length=200)
    def __str__(self):
        return self.nama

    def artikel_berdasarkan_kategori(self):
        return self.artikel_set.all()














#
