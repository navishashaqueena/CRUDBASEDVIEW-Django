from django.db import models


class murid(models.Model):
    Nama = models.CharField(max_length=30)
    Alamat = models.CharField(max_length=30)
    Nilai = models.FloatField()
