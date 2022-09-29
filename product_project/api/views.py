from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Boss
from .serializers import EmployeeSerializer, BossSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_list_or_404,get_object_or_404
from rest_framework.decorators import action
from django.core import serializers

from django.http import JsonResponse

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class BossViewSet(viewsets.ModelViewSet):
    queryset = Boss.objects.all()
    serializer_class = BossSerializer


def BossModel(self,pk=None):
    Empl = Employee.objects.all().filter(Boss_id=pk)
    serializer = EmployeeSerializer(Empl,many=True)
    return JsonResponse(serializer.data,safe=False)