from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from drivers.models import DriverModel

class DriverSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    class Meta:
        model = DriverModel
        fields = ('id', 'first_name', 'last_name', 'created_at',)