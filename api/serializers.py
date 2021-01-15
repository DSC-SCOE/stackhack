from rest_framework import serializers
from django.contrib.auth.models import User
from .models import empData, empModel, leaveModel, attendanceModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = empModel
        fields = "__all__"


class EmployeeDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = empData
        fields = "__all__"
