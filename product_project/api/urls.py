
from django.contrib import admin
from django.urls import path, include
from .views import BossViewSet, EmployeeViewSet, BossModel, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', EmployeeViewSet, basename='employee')
router.register('boss', BossViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('test/<int:pk>/', BossModel)
]
