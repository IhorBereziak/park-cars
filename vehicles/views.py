from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import VehicleModel
from .serializers import VehicleSerializer

class VehicleCreateListView(ListCreateAPIView):
    serializer_class = VehicleSerializer
    queryset = VehicleModel.objects.all()


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = VehicleModel.objects.all()