import datetime
from django.http.response import JsonResponse
from rest_framework import status
from januszex.models import RangePostalCode
from januszex.serializers import RangePostalCodeSerializer
from januszex.models import LocalWarehouse
from januszex.serializers import LocalWarehouseSerializer
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
            "idGloablWarehouse2":track[2],
            "idLocalWarehouseDestination":track[3]
        }
        return jsonTrack
