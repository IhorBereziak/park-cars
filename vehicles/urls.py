from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from vehicles.views import *

urlpatterns = [
    path('vehicle/', VehicleCreateListView.as_view(), name='vehicle_list_create'),
    # path('vehicle/<int:pk>/', ReadUpdateDeleteView.as_view(), name='vehicle_retriave_delete'),
    # path('driver/slug:slug/', DriverItemParamsView.as_view(), name='driver_item_params'),

]