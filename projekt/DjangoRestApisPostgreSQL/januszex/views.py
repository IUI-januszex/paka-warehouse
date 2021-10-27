from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from januszex.models import GlobalWarehouse
from januszex.serializers import GlobalWarehouseSerializer
from januszex.models import LocalWarehouse
from januszex.serializers import LocalWarehouseSerializer
from januszex.models import RangePostalCode
from januszex.serializers import RangePostalCodeSerializer
from rest_framework.decorators import api_view
from januszex.methods import Tools



@api_view(['GET', 'POST', 'DELETE'])
def globalWarehouseList(request):
    if request.method == 'GET':
        globalWarehouse = GlobalWarehouse.objects.all()
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse, many=True)
        return JsonResponse(globalWarehouseSerializer.data, safe=False)
    elif request.method == 'POST':
        globalWarehouseData = JSONParser().parse(request)
        if (Tools.validNoneAndBlank(globalWarehouseData)is not True):
            return (Tools.validNoneAndBlank(globalWarehouseData))
        if (Tools.validPostalCode(globalWarehouseData['postalCode'])is not True):
            return (Tools.validPostalCode(globalWarehouseData['postalCode']))
        globalWarehouseSerializer = GlobalWarehouseSerializer(data=globalWarehouseData)
        if globalWarehouseSerializer.is_valid():
            globalWarehouseSerializer.save()
            return JsonResponse(globalWarehouseSerializer.data, status=status.HTTP_201_CREATED) 
        return Tools.returnError("Not corect data")
    elif request.method == 'DELETE':
        count = GlobalWarehouse.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'globalWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def globalWarehouseDetail(request, pk):
    try: 
        globalWarehouse = GlobalWarehouse.objects.get(pk=pk) 
    except GlobalWarehouse.DoesNotExist: 
        return Tools.returnError("Not found GlobalWarehouse with this PK")
    if request.method == 'GET': 
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse) 
        return JsonResponse(globalWarehouseSerializer.data) 
    elif request.method == 'PUT': 
        globalWarehouseData = JSONParser().parse(request) 
        if (Tools.validNoneAndBlank(globalWarehouseData)is not True):
            return (Tools.validNoneAndBlank(globalWarehouseData))
        if (Tools.validPostalCode(globalWarehouseData['postalCode'])is not True):
            return (Tools.validPostalCode(globalWarehouseData['postalCode']))

        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse, data=globalWarehouseData) 
        if globalWarehouseSerializer.is_valid(): 
            globalWarehouseSerializer.save() 
            return JsonResponse(globalWarehouseSerializer.data) 
        return Tools.returnError("Not corect data") 
    elif request.method == 'DELETE': 
        globalWarehouse.delete() 
        return JsonResponse({'message': 'globalWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)
 




@api_view(['GET', 'POST', 'DELETE'])
def localWarehouseList(request):
    if request.method == 'GET':
        localWarehouse = LocalWarehouse.objects.all()
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse, many=True)
        return JsonResponse(localWarehouseSerializer.data, safe=False)
    elif request.method == 'POST':
        localWarehouseData = JSONParser().parse(request)
        if (Tools.validNoneAndBlank(localWarehouseData)is not True):
            return (Tools.validNoneAndBlank(localWarehouseData))
        if (Tools.validPostalCode(localWarehouseData['postalCode'])is not True):
            return (Tools.validPostalCode(localWarehouseData['postalCode']))
        localWarehouseSerializer = LocalWarehouseSerializer(data=localWarehouseData)
        if localWarehouseSerializer.is_valid():
            localWarehouseSerializer.save()
            return JsonResponse(localWarehouseSerializer.data, status=status.HTTP_201_CREATED) 
        return Tools.returnError("Not corect data")
    elif request.method == 'DELETE':
        count = LocalWarehouse.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'localWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def localWarehouseDetail(request, pk):
    try: 
        localWarehouse = LocalWarehouse.objects.get(pk=pk) 
    except LocalWarehouse.DoesNotExist: 
        return Tools.returnError("Not found LocalWarehouse with this PK")
    if request.method == 'GET': 
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse) 
        return JsonResponse(localWarehouseSerializer.data) 
    elif request.method == 'PUT': 
        localWarehouseData = JSONParser().parse(request) 
        if (Tools.validNoneAndBlank(localWarehouseData)is not True):
            return (Tools.validNoneAndBlank(localWarehouseData))
        if (Tools.validPostalCode(localWarehouseData['postalCode'])is not True):
            return (Tools.validPostalCode(localWarehouseData['postalCode']))
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse, data=localWarehouseData) 
        if localWarehouseSerializer.is_valid(): 
            localWarehouseSerializer.save() 
            return JsonResponse(localWarehouseSerializer.data) 
        return Tools.returnError("Not corect data")
    elif request.method == 'DELETE': 
        localWarehouse.delete() 
        return JsonResponse({'message': 'localWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def rangePostalCodeList(request):
    if request.method == 'GET':
        rangePostalCode = RangePostalCode.objects.all()
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode, many=True)
        return JsonResponse(rangePostalCodeSerializer.data, safe=False)
    elif request.method == 'POST':
        rangePostalCodeData = JSONParser().parse(request)
        if (Tools.validNoneAndBlank(rangePostalCodeData)is not True):
            return (Tools.validNoneAndBlank(rangePostalCodeData))
        if (Tools.validPostalCode(rangePostalCodeData['postalCode'])is not True):
            return (Tools.validPostalCode(rangePostalCodeData['postalCode']))
        rangePostalCodeSerializer = RangePostalCodeSerializer(data=rangePostalCodeData)
        if rangePostalCodeSerializer.is_valid():
            rangePostalCodeSerializer.save()
            return JsonResponse(rangePostalCodeSerializer.data, status=status.HTTP_201_CREATED) 
        return Tools.returnError("Not corect data")
    elif request.method == 'DELETE':
        count = RangePostalCode.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'rangePostalCode have been removed'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def rangePostalCodeDetail(request, pk):
    try: 
        rangePostalCode = RangePostalCode.objects.get(pk=pk) 
    except RangePostalCode.DoesNotExist: 
        return Tools.returnError("Not found RangePostalCode with this PK")
    if request.method == 'GET': 
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode) 
        return JsonResponse(rangePostalCodeSerializer.data) 
    elif request.method == 'PUT': 
        rangePostalCodeData = JSONParser().parse(request) 
        if (Tools.validNoneAndBlank(rangePostalCodeData)is not True):
            return (Tools.validNoneAndBlank(rangePostalCodeData))
        if (Tools.validPostalCode(rangePostalCodeData['idRangePostalCode'])is not True):
            return (Tools.validPostalCode(rangePostalCodeData['idRangePostalCode']))
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode, data=rangePostalCodeData) 
        if rangePostalCodeSerializer.is_valid(): 
            rangePostalCodeSerializer.save() 
            return JsonResponse(rangePostalCodeSerializer.data) 
        return JsonResponse(rangePostalCodeSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        rangePostalCode.delete() 
        return JsonResponse({'message': 'rangePostalCode have been removed'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def getLocalWarehouseFromPostalCode(request):
    postalCode = JSONParser().parse(request)
    if (Tools.validPostalCode(postalCode['postalCode'])is not True):
        return (Tools.validPostalCode(postalCode['postalCode']))
    LocalWarehouse=Tools.getLocalWarehouseFromPostalCodeHelp(postalCode['postalCode'])
    if(LocalWarehouse is None):
        return Tools.returnError("We don't support this postal code")
    return JsonResponse({"idLocalWarehouse":LocalWarehouse}, safe=False)


@api_view(['GET'])
def getTrack(request):
    postalCodes = JSONParser().parse(request)
    if (Tools.validPostalCode(postalCodes['postalCodeSource'])is not True):
        return (Tools.validPostalCode(postalCodes['postalCodeSource']))
    if (Tools.validPostalCode(postalCodes['postalCodeDestination'])is not True):
        return (Tools.validPostalCode(postalCodes['postalCodeDestination']))
    sourceWarehouse=Tools.getLocalWarehouseFromPostalCodeHelp(postalCodes['postalCodeSource'])
    destinationWarehouse=Tools.getLocalWarehouseFromPostalCodeHelp(postalCodes['postalCodeDestination'])
    if(sourceWarehouse is None or destinationWarehouse is None):
        Tools.returnError("We do not support this postal code")
    track=Tools.getTrackHelp(sourceWarehouse,destinationWarehouse)
    jsonTrack=Tools.getJsonTrackFromList(track)
    if(jsonTrack is None):
        return Tools.returnError("We don't support this postal code")
    return JsonResponse(jsonTrack, safe=False)

    



