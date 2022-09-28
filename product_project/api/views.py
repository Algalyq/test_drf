from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets


class List_Employee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
