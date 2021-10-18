from rest_framework import serializers
from tutorials.models import Magazyn_globalny
from tutorials.models import Magazyn_lokalny
 
class GlobalWarehouseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Magazyn_globalny
        fields = ('id_global_warehouse',
                  'city',
                  'street',
                  'numer',
                  'postal_code')


class LocalWarehouseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Magazyn_lokalny
        fields = ('id_local_warehouse',
                  'id_global_warehouse',
                  'city',
                  'street',
                  'numer',
                  'postal_code')
