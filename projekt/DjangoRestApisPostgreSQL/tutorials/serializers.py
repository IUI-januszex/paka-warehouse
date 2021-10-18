from rest_framework import serializers
from tutorials.models import LocalWarehouse
from tutorials.models import GlobalWarehouse
 
class GlobalWarehouseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GlobalWarehouse
        fields = ('id_global_warehouse',
                  'city',
                  'street',
                  'numer',
                  'postal_code')


class LocalWarehouseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = LocalWarehouse
        fields = ('id_local_warehouse',
                  'id_global_warehouse',
                  'city',
                  'street',
                  'numer',
                  'postal_code')
