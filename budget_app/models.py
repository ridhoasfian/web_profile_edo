from django.db import models

# Create your models here.
class Anggaran(models.Model):
    nama = models.CharField(max_length=200)
    budget = models.IntegerField()
    def __str__(self):
        return self.nama

    def budget_sisa(self):
        biaya_list = Biaya.objects.filter(anggaran=self)
        total_biaya_amount = 0
        for biaya in biaya_list:
            total_biaya_amount += biaya.amount
        return self.budget - total_biaya_amount

    def jumlah_transaksi(self):
        biaya_list = Biaya.objects.filter(anggaran=self)
        return len(biaya_list)

    
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Kategori(models.Model):
    anggaran = models.ForeignKey('Anggaran', on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
    def __str__(self):
        return self.nama


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Biaya(models.Model):
    anggaran = models.ForeignKey('Anggaran', on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=30, decimal_places=2)
    kategori = models.ForeignKey('Kategori', on_delete=models.CASCADE)
    def __str__(self):
        return self.nama

    class Meta:
        ordering =('-id',)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
