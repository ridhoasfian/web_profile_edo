from django.db import models

# Create your models here.
class TestUpload(models.Model):
    nama = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='gambar/%Y/%m/%d/')
