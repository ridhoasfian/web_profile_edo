from django.db import models

# Create your models here.
class Kota(models.Model):
    nama = models.CharField(max_length=200)
    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Kota'
        ordering = ('-id',)
