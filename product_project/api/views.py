from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Boss
from .serializers import EmployeeSerializer, BossSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.decorators import action
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import JsonResponse

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, ) 

class BossViewSet(viewsets.ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, )
    
     
def BossModel(self,pk=None):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, ) 
    try:
        Empl = Employee.objects.all().filter(Boss_id=pk)
        serializer = EmployeeSerializer(Empl,many=True)
    except ObjectDoesNotExist:
        return HttpResponse("Does not exist")
    return JsonResponse(serializer.data,safe=False)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
