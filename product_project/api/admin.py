from django.contrib import admin
from .models import Employee, Boss

@admin.register(Employee)
class EmployeeModel(admin.ModelAdmin):
    list_display = ['Surename_empl', 'Name_empl', 'Post', 'Salary']


@admin.register(Boss)
class BossModel(admin.ModelAdmin):
    list_display = ['Surename_Boss', 'Name_Boss', 'Post_Boss']
