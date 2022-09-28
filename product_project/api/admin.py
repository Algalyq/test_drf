from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display = ['Surename_empl', 'Name_empl', 'Post', 'Salary']
