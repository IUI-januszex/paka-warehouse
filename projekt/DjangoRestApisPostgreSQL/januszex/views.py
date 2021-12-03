from django.db import models
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

import sys
import inspect


@api_view(['GET', 'POST', 'DELETE'])
def globalWarehouseList(request):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    if request.method == 'GET':
        globalWarehouse = GlobalWarehouse.objects.all()
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse, many=True)
        afterChangeKeys=Tools.changeKeysGlobal(globalWarehouseSerializer)
        return JsonResponse(afterChangeKeys, safe=False)
    elif request.method == 'POST':
        try:
            globalWarehouseData = JSONParser().parse(request)
        except:
            return Tools.returnError("Not corect request")
        if (Tools.validNoneAndBlank(globalWarehouseData)is not True):
            return (Tools.validNoneAndBlank(globalWarehouseData))
        if (Tools.validPostalCode(globalWarehouseData['postalCode'])is not True):
            return (Tools.validPostalCode(globalWarehouseData['postalCode']))
        globalWarehouseSerializer = GlobalWarehouseSerializer(data=globalWarehouseData)
        if globalWarehouseSerializer.is_valid():
            globalWarehouseSerializer.save()
            afterChangeKeys=Tools.changeKeysGlobal(globalWarehouseSerializer)
            return JsonResponse(afterChangeKeys, status=status.HTTP_201_CREATED) 
        return Tools.returnError("Not corect data")
    elif request.method == 'DELETE':
        count = GlobalWarehouse.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'globalWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET', 'PUT', 'DELETE'])
def globalWarehouseDetail(request, pk):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    try: 
        globalWarehouse = GlobalWarehouse.objects.get(pk=pk) 
    except GlobalWarehouse.DoesNotExist: 
        return Tools.returnError("Not found GlobalWarehouse with this PK")
    if request.method == 'GET': 
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse) 
        afterChangeKeys=Tools.changeKeysGlobal(globalWarehouseSerializer)
        return JsonResponse(afterChangeKeys) 
    elif request.method == 'PUT': 
        try:
            globalWarehouseData = JSONParser().parse(request)
        except:
            return Tools.returnError("Not corect request")
        if (Tools.validNoneAndBlank(globalWarehouseData)is not True):
            return (Tools.validNoneAndBlank(globalWarehouseData))
        if (Tools.validPostalCode(globalWarehouseData['postalCode'])is not True):
            return (Tools.validPostalCode(globalWarehouseData['postalCode']))
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse, data=globalWarehouseData) 
        if globalWarehouseSerializer.is_valid(): 
            globalWarehouseSerializer.save() 
            afterChangeKeys=Tools.changeKeysGlobal(globalWarehouseSerializer)
            return JsonResponse(afterChangeKeys) 
        return Tools.returnError("Not corect data") 
    elif request.method == 'DELETE': 
        globalWarehouse.delete() 
        return JsonResponse({'message': 'globalWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET'])
def globalWarehouseFilter(request,pole,value):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    globalWarehouseSerializer=Tools.getGlobalWarehouseFilter(pole,value)
    if(globalWarehouseSerializer is None):
        return Tools.returnError("Not valid field")
    afterChangeKeys=Tools.changeKeysGlobal(globalWarehouseSerializer)
    return JsonResponse(afterChangeKeys, safe=False)
    

@api_view(['GET', 'POST', 'DELETE'])
def localWarehouseList(request):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    if request.method == 'GET':
        localWarehouse = LocalWarehouse.objects.all()
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse, many=True)
        afterChangeKeys=Tools.changeKeysLocal(localWarehouseSerializer)
        return JsonResponse(localWarehouseSerializer.data, safe=False)
    elif request.method == 'POST':
        try:
            localWarehouseData = JSONParser().parse(request)
        except:
            return Tools.returnError("Not corect request")
        if (Tools.validNoneAndBlank(localWarehouseData)is not True):
            return (Tools.validNoneAndBlank(localWarehouseData))
        if (Tools.validPostalCode(localWarehouseData['postalCode'])is not True):
            return (Tools.validPostalCode(localWarehouseData['postalCode']))
        localWarehouseSerializer = LocalWarehouseSerializer(data=localWarehouseData)
        if localWarehouseSerializer.is_valid():
            localWarehouseSerializer.save()
            afterChangeKeys=Tools.changeKeysLocal(localWarehouseSerializer)
            return JsonResponse(afterChangeKeys, status=status.HTTP_201_CREATED) 
        return Tools.returnError("Not corect data")
    elif request.method == 'DELETE':
        count = LocalWarehouse.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'localWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def localWarehouseDetail(request, pk):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    try: 
        localWarehouse = LocalWarehouse.objects.get(pk=pk) 
    except LocalWarehouse.DoesNotExist: 
        return Tools.returnError("Not found LocalWarehouse with this PK")
    if request.method == 'GET': 
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse) 
        afterChangeKeys=Tools.changeKeysLocal(localWarehouseSerializer)
        return JsonResponse(afterChangeKeys) 
    elif request.method == 'PUT': 
        try:
            localWarehouseData = JSONParser().parse(request)
        except:
            return Tools.returnError("Not corect request")
        if (Tools.validNoneAndBlank(localWarehouseData)is not True):
            return (Tools.validNoneAndBlank(localWarehouseData))
        if (Tools.validPostalCode(localWarehouseData['postalCode'])is not True):
            return (Tools.validPostalCode(localWarehouseData['postalCode']))
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse, data=localWarehouseData) 
        if localWarehouseSerializer.is_valid(): 
            localWarehouseSerializer.save() 
            afterChangeKeys=Tools.changeKeysLocal(localWarehouseSerializer)
            return JsonResponse(afterChangeKeys) 
        return Tools.returnError("Not corect data")
    elif request.method == 'DELETE': 
        localWarehouse.delete() 
        return JsonResponse({'message': 'localWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def localWarehouseFilter(request,pole,value):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    localWarehouseSerializer=Tools.getLocalWarehouseFilter(pole,value)
    if(localWarehouseSerializer is None):
        return Tools.returnError("Not valid field")
    afterChangeKeys=Tools.changeKeysLocal(localWarehouseSerializer)
    return JsonResponse(afterChangeKeys, safe=False) 

@api_view(['GET', 'POST', 'DELETE'])
def rangePostalCodeList(request):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    if request.method == 'GET':
        rangePostalCode = RangePostalCode.objects.all()
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode, many=True)
        afterChangeKeys=Tools.changeKeysLocal(rangePostalCodeSerializer)
        return JsonResponse(afterChangeKeys, safe=False) 
    elif request.method == 'POST':
        try:
            rangePostalCodeData = JSONParser().parse(request)
        except:
            return Tools.returnError("Not corect request")
        if (Tools.validNoneAndBlank(rangePostalCodeData)is not True):
            return (Tools.validNoneAndBlank(rangePostalCodeData))
        if (Tools.validPostalCode(rangePostalCodeData['idRangePostalCode'])is not True):
            return (Tools.validPostalCode(rangePostalCodeData['idRangePostalCode']))
        rangePostalCodeSerializer = RangePostalCodeSerializer(data=rangePostalCodeData)
        if rangePostalCodeSerializer.is_valid():
            rangePostalCodeSerializer.save()
            afterChangeKeys=Tools.changeKeysLocal(rangePostalCodeSerializer)
            return JsonResponse(afterChangeKeys, status=status.HTTP_201_CREATED) 
        return Tools.returnError("Not corect data")
    elif request.method == 'DELETE':
        count = RangePostalCode.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'rangePostalCode have been removed'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def rangePostalCodeDetail(request, pk):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    try: 
        rangePostalCode = RangePostalCode.objects.get(pk=pk) 
    except RangePostalCode.DoesNotExist: 
        return Tools.returnError("Not found RangePostalCode with this PK")
    if request.method == 'GET': 
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode) 
        afterChangeKeys=Tools.changeKeysLocal(rangePostalCodeSerializer)
        return JsonResponse(afterChangeKeys) 
    elif request.method == 'PUT': 
        try:
            rangePostalCodeData = JSONParser().parse(request)
        except:
            return Tools.returnError("Not corect request")
        rangePostalCodeData['idRangePostalCode']=pk
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode, data=rangePostalCodeData) 
        if rangePostalCodeSerializer.is_valid(): 
            rangePostalCodeSerializer.save() 
            afterChangeKeys=Tools.changeKeysLocal(rangePostalCodeSerializer)
            return JsonResponse(afterChangeKeys) 
        return JsonResponse(rangePostalCodeSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        rangePostalCode.delete() 
        return JsonResponse({'message': 'rangePostalCode have been removed'}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def getLocalWarehouseFromPostalCode(request):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    try:
        postalCode = JSONParser().parse(request)
    except:
        return Tools.returnError("Not corect request")
    if (Tools.validPostalCode(postalCode['postalCode'])is not True):
        return (Tools.validPostalCode(postalCode['postalCode']))
    LocalWarehouse=Tools.getLocalWarehouseFromPostalCodeHelp(postalCode['postalCode'])
    if(LocalWarehouse is None):
        return Tools.returnError("We don't support this postal code")
    return JsonResponse({"idWarehouse":LocalWarehouse}, safe=False)


@api_view(['GET'])
def getTrack(request):
    if(not Tools.permission(sys._getframe().f_code.co_name,request.method,request.headers.get('Authorization'))):
        return Tools.returnError("Permission denied (JWT)")
    try:
        postalCodes = JSONParser().parse(request)
    except:
        return Tools.returnError("Not corect request")
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






