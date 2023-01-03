from django.db import models

# Create your models here.


class Scanner(models.Model):
    nama = models.CharField(max_length=9)
    jumlah = models.TextField()

    def __str__(self):
        return self.nama


class Sortir(models.Model):
    barcode = models.CharField(max_length=40)
    jumlah = models.IntegerField(null=True)
    tanggal = models.DateTimeField()
    scanner_id = models.ForeignKey(
        Scanner, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.jumlah