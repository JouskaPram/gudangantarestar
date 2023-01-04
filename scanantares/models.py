from django.db import models
from django.utils import timezone

class Scanner(models.Model):
    name = models.CharField(max_length=9)

    def __str__(self):
        return self.name


class Sortir(models.Model):
    barcode = models.CharField(max_length=40)
    scanner_id = models.ForeignKey(
        Scanner, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.barcode