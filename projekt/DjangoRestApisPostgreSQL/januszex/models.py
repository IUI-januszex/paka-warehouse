from django.db import models

#my_validator = RegexValidator(r"A", "Your string should contain letter A in it.")
class GlobalWarehouse(models.Model):
    idGlobalWarehouse=models.IntegerField(primary_key=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    numer = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=6)


class LocalWarehouse(models.Model):
    idLocalWarehouse=models.IntegerField(primary_key=True)
    idGlobalWarehouse = models.ForeignKey(GlobalWarehouse, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    ulica = models.CharField(max_length=255)
    numer = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=6) 


class RangePostalCode(models.Model):
    idRangePostalCode=models.IntegerField(primary_key=True)
    idLocalWarehouse = models.ForeignKey(LocalWarehouse, on_delete=models.CASCADE)


