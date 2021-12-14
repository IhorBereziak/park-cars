from rest_framework import serializers

from rest_framework.serializers import ModelSerializer
from vehicles.models import VehicleModel
from drivers.models import DriverModel

class VehicleSerializer(ModelSerializer):
    driver_id = serializers.IntegerField()

    class Meta:
        model = VehicleModel
        fields = ('driver_id', 'make', 'model', 'plate_number', 'created_at',)

    def create(self, validated_data):
        validated_data['driver_id'] = DriverModel.objects.get(id=validated_data['driver_id'])
        return VehicleModel.objects.create(**validated_data)