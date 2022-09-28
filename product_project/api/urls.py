
from django.contrib import admin
from django.urls import path, include
from .views import List_Employee
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('all', List_Employee, basename='all_empl')

urlpatterns = [
    path('api/', include(router.urls) )
]
