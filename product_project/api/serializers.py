from rest_framework import serializers
from .models import Employee, Boss

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','Surename_empl','Name_empl', 'Salary', 'Post', 'Boss_id']


class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = ['id','Surename_Boss','Name_Boss', 'Post_Boss']