from django.db import models

# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    pub_date = models.DateField()
    created_by = models.CharField(max_length=200)
    sumber = models.CharField(max_length=200)
    edit_date = models.DateField()
    def __str__(self):
        return self.judul

class Kategori(models.Model):
    artikel = models.ForeignKey('Artikel', on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    def __str__(self):
        return self.nama
