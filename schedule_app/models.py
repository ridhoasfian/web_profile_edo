from django.db import models

# Create your models here.
class Schedule(models.Model):
    class Meta:
        ordering = ['-tanggal']

    nama = models.CharField(max_length=200)
    tanggal = models.DateTimeField()
    deskripsi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nama
