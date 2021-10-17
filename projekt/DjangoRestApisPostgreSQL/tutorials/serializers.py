from rest_framework import serializers
from tutorials.models import Magazyn_globalny
from tutorials.models import Magazyn_lokalny
 
class MagazynGlobalnySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Magazyn_globalny
        fields = ('id_magazynu_globalnego',
                  'miasto',
                  'ulica',
                  'numer',
                  'kod_pocztowy')


class MagazynLokalnySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Magazyn_lokalny
        fields = ('id_magazynu_lokalnego',
                  'id_magazynu_globalnego',
                  'miasto',
                  'ulica',
                  'numer',
                  'kod_pocztowy')
