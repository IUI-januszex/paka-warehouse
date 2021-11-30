import datetime
from django.http.response import JsonResponse
from rest_framework import status
import rest_framework
from januszex.models import RangePostalCode
from januszex.serializers import RangePostalCodeSerializer
from januszex.models import LocalWarehouse
from januszex.serializers import LocalWarehouseSerializer
from januszex.models import GlobalWarehouse
from januszex.serializers import GlobalWarehouseSerializer
import re

class Tools():
    def returnError(message):
        datetime_object = datetime.datetime.now()
        return JsonResponse({
                'timestamp':datetime_object,
                'message':message}, status=status.HTTP_400_BAD_REQUEST)

    def validNoneAndBlank(data):
        for key in data.keys():
            if(data[key] is None or data[key]==""):
                return Tools.returnError("not valid '"+key+"'")
        return True

    def validPostalCode(postalCode):
        reg=r"^[0-9]{2}-[0-9]{3}$"
        if (re.match(reg,postalCode)):
            return True
        else:
            return Tools.returnError("not valid postal code")

    def getLocalWarehouseFromPostalCodeHelp(postalCode):
        rangePostalCode = RangePostalCode.objects.filter(idRangePostalCode=postalCode)
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode, many=True)
        if(len(rangePostalCodeSerializer.data)==0):
            return None
        idLocalWarehouse=(rangePostalCodeSerializer.data[0]['idLocalWarehouse'])
        return idLocalWarehouse

    def getTrackHelp(localWarehouse,globalWarehouse):
        if(localWarehouse is None or globalWarehouse is None):
            return [localWarehouse,None,None,globalWarehouse]
        if(localWarehouse==globalWarehouse):
            return [localWarehouse,None,None,globalWarehouse]
        localWarehouseSource = LocalWarehouse.objects.filter(idLocalWarehouse=localWarehouse)
        localWarehouseDestination=LocalWarehouse.objects.filter(idLocalWarehouse=globalWarehouse)
        localWarehouseSourceSerializer = LocalWarehouseSerializer(localWarehouseSource, many=True)
        localWarehouseDestinationSerializer = LocalWarehouseSerializer(localWarehouseDestination, many=True)
        globalSource=localWarehouseSourceSerializer.data[0]['idGlobalWarehouse']
        globalDestination=localWarehouseDestinationSerializer.data[0]['idGlobalWarehouse']
        if(globalSource==globalDestination):
            return [localWarehouse,globalSource,None,globalWarehouse]
        return [localWarehouse,globalSource,globalDestination,globalWarehouse]

    def getJsonTrackFromList(track):
        if(None in track):
            return None
        jsonTrack={
            "idLocalWarehouseSource":track[0],
            "idGlobalWarehouse1":track[1],
            "idGlobalWarehouse2":track[2],
            "idLocalWarehouseDestination":track[3]
        }
        return jsonTrack

    def getGlobalWarehouseFilter(field,value):
        if(field not in ['idGlobalWarehouse','city','street','number','postalCode','active']):
            return None
        try: 
            if(field=="idGlobalWarehouse"):
                globalWarehouse=GlobalWarehouse.objects.filter(idGlobalWarehouse=value)
            if(field=="city"):
                globalWarehouse=GlobalWarehouse.objects.filter(city=value)
            if(field=="street"):
                globalWarehouse=GlobalWarehouse.objects.filter(street=value)
            if(field=="number"):
                globalWarehouse=GlobalWarehouse.objects.filter(number=value)
            if(field=="postalCode"):
                globalWarehouse=GlobalWarehouse.objects.filter(postalCode=value)
            if(field=="active"):
                globalWarehouse=GlobalWarehouse.objects.filter(active=value)
        except GlobalWarehouse.DoesNotExist: 
            return None
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse,many=True) 
        return globalWarehouseSerializer
    
    def getLocalWarehouseFilter(field,value):
        if(field not in ['idLocalWarehouse','city','street','number','postalCode','active','idGlobalWarehouse']):
            return None
        try: 
            if(field=="idLocalWarehouse"):
                localWarehouse=LocalWarehouse.objects.filter(idLocalWarehouse=value)
            if(field=="city"):
                localWarehouse=LocalWarehouse.objects.filter(city=value)
            if(field=="street"):
                localWarehouse=LocalWarehouse.objects.filter(street=value)
            if(field=="number"):
                localWarehouse=LocalWarehouse.objects.filter(number=value)
            if(field=="postalCode"):
                localWarehouse=LocalWarehouse.objects.filter(postalCode=value)
            if(field=="active"):
                localWarehouse=LocalWarehouse.objects.filter(active=value)
            if(field=="idGlobalWarehouse"):
                localWarehouse=LocalWarehouse.objects.filter(idGlobalWarehouse=value)
        except LocalWarehouse.DoesNotExist: 
            return None
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse,many=True) 
        return localWarehouseSerializer


    def changeKeys(data):
        #nizej jesli pojedynczy json
        if isinstance(data.data,rest_framework.utils.serializer_helpers.ReturnDict):
            json=dict(data.data)
            if 'idGlobalWarehouse' in json.keys():
                json['idWarehouse'] = json.pop('idGlobalWarehouse')
            if 'idLocalWarehouse' in json.keys():
                json['idWarehouse'] = json.pop('idLocalWarehouse')
            return json

        #nizej jesli lista jsonow
        for i in data.data:
            if 'idGlobalWarehouse' in i.keys():
                i['idWarehouse'] = i.pop('idGlobalWarehouse')
            if 'idLocalWarehouse' in i.keys():
                i['idWarehouse'] = i.pop('idLocalWarehouse')
        return data.data




