from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from drivers.models import DriverModel
from drivers.serializers import DriverSerializer

class DriverCreateListView(ListCreateAPIView):
    serializer_class = DriverSerializer
    queryset = DriverModel.objects.all()


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = DriverModel.objects.all()


class DriverItemParamsView(ListCreateAPIView):
    serializer_class = DriverSerializer

    def get_queryset(self):
        # qs = DriverModel.objects.all()
        # params = self.request.query_params
        # first_name = params.get('first_name', None)
        # print(first_name)
        # if first_name:
        #     qs = qs.filter(first_name__contains=first_name)
        # return qs
        # qs = DriverModel.objects.all().filter()
        # first_name = self.request.query_params.get('first_name')
        # if first_name:
        #     qs = qs.filter(first_name__iexact=first_name)
        # drivers = DriverSerializer(qs, many=True).data
        # return Response(drivers, status.HTTP_201_CREATED)
        pass