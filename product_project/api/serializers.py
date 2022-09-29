from rest_framework import serializers
from .models import Employee, Boss
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','Surename_empl','Name_empl', 'Salary', 'Post', 'Boss_id']


class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = ['id','Surename_Boss','Name_Boss', 'Post_Boss']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password':{
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user 
