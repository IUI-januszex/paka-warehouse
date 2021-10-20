from django.db import models

#my_validator = RegexValidator(r"A", "Your string should contain letter A in it.")
class GlobalWarehouse(models.Model):
    idGlobalWarehouse=models.IntegerField(primary_key=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=6)


class LocalWarehouse(models.Model):
    idLocalWarehouse=models.IntegerField(primary_key=True)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    postalCode = models.CharField(max_length=6) 
    idGlobalWarehouse = models.ForeignKey(GlobalWarehouse, on_delete=models.CASCADE)


class RangePostalCode(models.Model):
    idRangePostalCode=models.CharField(max_length=6,primary_key=True)
    idLocalWarehouse = models.ForeignKey(LocalWarehouse, on_delete=models.CASCADE)


