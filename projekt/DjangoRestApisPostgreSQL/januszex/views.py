from django.shortcuts import render

# Create your views here.
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
import datetime
import re

def validTableNoneAndBlank(data):
    #sprawdza czy wszytskie pola nie sa nullami i czy nie są puste
    for key in data.keys():
        if(data[key] is None or data[key]==""):
            return "Nor correct "+key
    return True

def validPostalCode(data):
    postalCode=data["PostacCode"]
    reg=r"[0-9]{2}-[0-9]{3}"
    if (re.match(reg,postalCode)):
        return True
    else:
        return "Not correcrt PostalCode"

@api_view(['GET', 'POST', 'DELETE'])
def globalWarehouseList(request):
    if request.method == 'GET':
        globalWarehouse = GlobalWarehouse.objects.all()
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse, many=True)
        return JsonResponse(globalWarehouseSerializer.data, safe=False)
    elif request.method == 'POST':
        globalWarehouseSerializerData = JSONParser().parse(request)
        messageFromValid = validTableNoneAndBlank(globalWarehouseSerializerData)
        if(messageFromValid is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        messageFromValid = validPostalCode(globalWarehouseSerializerData)
        if(validPostalCode(globalWarehouseSerializerData) is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        globalWarehouseSerializer = GlobalWarehouseSerializer(data=globalWarehouseSerializerData)
        if globalWarehouseSerializer.is_valid():
            globalWarehouseSerializer.save()
            return JsonResponse(globalWarehouseSerializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(globalWarehouseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = GlobalWarehouse.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'GlobalWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def globalWarehouseDetail(request, pk):
    try: 
        globalWarehouse = GlobalWarehouse.objects.get(pk=pk) 
    except GlobalWarehouse.DoesNotExist: 
        return JsonResponse({'message': 'Not found GlobalWarehouse with this PK'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse) 
        return JsonResponse(globalWarehouseSerializer.data) 
    elif request.method == 'PUT': 
        globalWarehouseData = JSONParser().parse(request) 
        messageFromValid = validTableNoneAndBlank(globalWarehouseData)
        if(messageFromValid is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        messageFromValid = validPostalCode(globalWarehouseData)
        if(validPostalCode(globalWarehouseData) is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        globalWarehouseSerializer = GlobalWarehouseSerializer(globalWarehouse, data=globalWarehouseData) 
        if globalWarehouseSerializer.is_valid(): 
            globalWarehouseSerializer.save() 
            return JsonResponse(globalWarehouseSerializer.data) 
        return JsonResponse(globalWarehouseSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 
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
        localWarehouseSerializerData = JSONParser().parse(request)
        messageFromValid = validTableNoneAndBlank(localWarehouseSerializerData)
        if(messageFromValid is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        messageFromValid = validPostalCode(localWarehouseSerializerData)
        if(validPostalCode(localWarehouseSerializerData) is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        localWarehouseSerializer = LocalWarehouseSerializer(data=localWarehouseSerializerData)
        if localWarehouseSerializer.is_valid():
            localWarehouseSerializer.save()
            return JsonResponse(localWarehouseSerializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(localWarehouseSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = LocalWarehouse.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'LocalWarehouse have been removed'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def localWarehouseDetail(request, pk):
    try: 
        localWarehouse = LocalWarehouse.objects.get(pk=pk) 
    except LocalWarehouse.DoesNotExist: 
        return JsonResponse({'message': 'Not found LocalWarehouse with this PK'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse) 
        return JsonResponse(localWarehouseSerializer.data) 
    elif request.method == 'PUT': 
        localWarehouseData = JSONParser().parse(request) 
        messageFromValid = validTableNoneAndBlank(localWarehouseData)
        if(messageFromValid is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        messageFromValid = validPostalCode(localWarehouseData)
        if(validPostalCode(localWarehouseData) is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        localWarehouseSerializer = LocalWarehouseSerializer(localWarehouse, data=localWarehouseData) 
        if localWarehouseSerializer.is_valid(): 
            localWarehouseSerializer.save() 
            return JsonResponse(localWarehouseSerializer.data) 
        return JsonResponse(localWarehouseSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 
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
        rangePostalCodeSerializerData = JSONParser().parse(request)
        rangePostalCodeSerializer = RangePostalCodeSerializer(data=rangePostalCodeSerializerData)
        if rangePostalCodeSerializer.is_valid():
            rangePostalCodeSerializer.save()
            return JsonResponse(rangePostalCodeSerializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(rangePostalCodeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = RangePostalCode.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'RangePostalCode have been removed'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def rangePostalCodeDetail(request, pk):
    try: 
        rangePostalCode = RangePostalCode.objects.get(pk=pk) 
    except RangePostalCode.DoesNotExist: 
        return JsonResponse({'message': 'Not found RangePostalCode with this PK'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode) 
        return JsonResponse(rangePostalCodeSerializer.data) 
    elif request.method == 'PUT': 
        rangePostalCodeData = JSONParser().parse(request) 
        rangePostalCodeSerializer = RangePostalCodeSerializer(rangePostalCode, data=rangePostalCodeData) 
        if rangePostalCodeSerializer.is_valid(): 
            rangePostalCodeSerializer.save() 
            return JsonResponse(rangePostalCodeSerializer.data) 
        return JsonResponse(rangePostalCodeSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        rangePostalCode.delete() 
        return JsonResponse({'message': 'rangePostalCode have been removed'}, status=status.HTTP_204_NO_CONTENT)