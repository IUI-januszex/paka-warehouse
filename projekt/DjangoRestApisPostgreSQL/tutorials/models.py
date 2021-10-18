from django.db import models

class GlobalWarehouse(models.Model):
    id_global_warehouse=models.IntegerField(primary_key=True)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    numer = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=6)

class LocalWarehouse(models.Model):
    id_local_warehouse=models.IntegerField(primary_key=True)
    id_global_warehouse = models.ForeignKey(GlobalWarehouse, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    numer = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=6)

