
from django.db import models

#my_validator = RegexValidator(r"A", "Your string should contain letter A in it.")
class Magazyn_globalny(models.Model):
    id_magazynu_globalnego=models.IntegerField(primary_key=True)
    miasto = models.CharField(max_length=200)
    ulica = models.CharField(max_length=200)
    numer = models.CharField(max_length=200)
    kod_pocztowy = models.CharField(max_length=6)


class Magazyn_lokalny(models.Model):
    id_magazynu_lokalnego=models.IntegerField(primary_key=True)
    id_magazynu_globalnego = models.ForeignKey(Magazyn_globalny, on_delete=models.CASCADE)
    miasto = models.CharField(max_length=200)
    ulica = models.CharField(max_length=200)
    numer = models.CharField(max_length=200)#sprawdzić czy da się dodac ze nie ma nuli i nie jest piste itp
    kod_pocztowy = models.CharField(max_length=6) # sprawdzić czy da się dodac RegEX

#sprawdzenie czy kod pocztowy jest poprawny 
# kod="26-664"
# reg=r"[0-9]{2}-[0-9]{3}"
# if (re.match(reg,kod)):