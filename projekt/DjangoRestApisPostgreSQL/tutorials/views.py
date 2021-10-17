from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from tutorials.models import Magazyn_globalny
from tutorials.serializers import MagazynGlobalnySerializer
from tutorials.models import Magazyn_lokalny
from tutorials.serializers import MagazynLokalnySerializer
from rest_framework.decorators import api_view
import datetime
import re

def validTableNoneAndBlank(data):
    #sprawdza czy wszytskie pola nie sa nullami i czy nie są puste
    for key in data.keys():
        if(data[key] is None or data[key]==""):
            return "Nie poprawny "+key
    return True

def validPostalCode(data):
    postalCode=data["kod_pocztowy"]
    reg=r"[0-9]{2}-[0-9]{3}"
    if (re.match(reg,postalCode)):
        return True
    else:
        return "Nie poprawny kod pocztowy"

@api_view(['GET', 'POST', 'DELETE'])
def magazynGlobalny_list(request):
    if request.method == 'GET':
        magGlobalny = Magazyn_globalny.objects.all()
        magGlobalny_serializer = MagazynGlobalnySerializer(magGlobalny, many=True)
        return JsonResponse(magGlobalny_serializer.data, safe=False)
    elif request.method == 'POST':
        magGlobalny_data = JSONParser().parse(request)
        messageFromValid = validTableNoneAndBlank(magGlobalny_data)
        if(messageFromValid is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        messageFromValid = validPostalCode(magGlobalny_data)
        if(validPostalCode(magGlobalny_data) is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        magGlobalny_serializer = MagazynGlobalnySerializer(data=magGlobalny_data)
        if magGlobalny_serializer.is_valid():
            magGlobalny_serializer.save()
            return JsonResponse(magGlobalny_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(magGlobalny_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Magazyn_globalny.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'Magazyny zostaly usuniete'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def magazynGlobalny_detail(request, pk):
    try: 
        magGlobalny = Magazyn_globalny.objects.get(pk=pk) 
    except Magazyn_globalny.DoesNotExist: 
        return JsonResponse({'message': 'Magazyn globalny o takim pk nie istnieje'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        magGlobalny_serializer = MagazynGlobalnySerializer(magGlobalny) 
        return JsonResponse(magGlobalny_serializer.data) 
    elif request.method == 'PUT': 
        magGlobalny_data = JSONParser().parse(request) 
        messageFromValid = validTableNoneAndBlank(magGlobalny_data)
        if(messageFromValid is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        messageFromValid = validPostalCode(magGlobalny_data)
        if(validPostalCode(magGlobalny_data) is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        magGlobalny_serializer = MagazynGlobalnySerializer(magGlobalny, data=magGlobalny_data) 
        if magGlobalny_serializer.is_valid(): 
            magGlobalny_serializer.save() 
            return JsonResponse(magGlobalny_serializer.data) 
        return JsonResponse(magGlobalny_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        magGlobalny.delete() 
        return JsonResponse({'message': 'Magazyn zostal usuniety'}, status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET', 'POST', 'DELETE'])
def magazynLokalny_list(request):
    if request.method == 'GET':
        magLokalny = Magazyn_lokalny.objects.all()
        magLokalny_serializer = MagazynLokalnySerializer(magLokalny, many=True)
        return JsonResponse(magLokalny_serializer.data, safe=False)
    elif request.method == 'POST':
        magLokalny_data = JSONParser().parse(request)
        messageFromValid = validTableNoneAndBlank(magLokalny_data)
        if(messageFromValid is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        messageFromValid = validPostalCode(magLokalny_data)
        if(validPostalCode(magLokalny_data) is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        magLokalny_serializer = MagazynLokalnySerializer(data=magLokalny_data)
        if magLokalny_serializer.is_valid():
            magLokalny_serializer.save()
            return JsonResponse(magLokalny_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(magLokalny_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Magazyn_lokalny.objects.all().delete()
        return JsonResponse({"count":count[0],
            'message': 'Magazyny zostaly usuniete'}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def magazynLokalny_detail(request, pk):
    try: 
        magLokalny = Magazyn_lokalny.objects.get(pk=pk) 
    except Magazyn_lokalny.DoesNotExist: 
        return JsonResponse({'message': 'Magazyn Lokalny o takim pk nie istnieje'}, status=status.HTTP_404_NOT_FOUND) 
    if request.method == 'GET': 
        magLokalny_serializer = MagazynLokalnySerializer(magLokalny) 
        return JsonResponse(magLokalny_serializer.data) 
    elif request.method == 'PUT': 
        magLokalny_data = JSONParser().parse(request) 
        messageFromValid = validTableNoneAndBlank(magLokalny_data)
        if(messageFromValid is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        messageFromValid = validPostalCode(magLokalny_data)
        if(validPostalCode(magLokalny_data) is not True):
            datetime_object = datetime.datetime.now()
            return JsonResponse({
                'timestamp':datetime_object,
                'message':messageFromValid}, status=status.HTTP_400_BAD_REQUEST)
        magLokalny_serializer = MagazynLokalnySerializer(magLokalny, data=magLokalny_data) 
        if magLokalny_serializer.is_valid(): 
            magLokalny_serializer.save() 
            return JsonResponse(magLokalny_serializer.data) 
        return JsonResponse(magLokalny_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        magLokalny.delete() 
        return JsonResponse({'message': 'Magazyn zostal usuniety'}, status=status.HTTP_204_NO_CONTENT)