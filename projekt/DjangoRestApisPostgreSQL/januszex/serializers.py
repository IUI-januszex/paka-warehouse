from rest_framework import serializers
from januszex.models import GlobalWarehouse
from januszex.models import LocalWarehouse
from januszex.models import RangePostalCode

 
class GlobalWarehouseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GlobalWarehouse
        fields = ('idGlobalWarehouse',
                  'city',
                  'street',
                  'number',
                  'postalCode',
                  'active')


class LocalWarehouseSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = LocalWarehouse
        fields = ('idLocalWarehouse',
                  'city',
                  'street',
                  'number',
                  'postalCode',
                  'active',
                  'idGlobalWarehouse')


class RangePostalCodeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = RangePostalCode
        fields = ('idRangePostalCode',
                  'idLocalWarehouse')
