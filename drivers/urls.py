from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from drivers.views import *

urlpatterns = [
    path('driver/', DriverCreateListView.as_view(), name='driver_list_create'),
    path('driver/<int:pk>/', ReadUpdateDeleteView.as_view(), name='driver_retriave_delete'),
    # path('driver/<int:day>-<int:month>-<int:year>', DriverItemParamsView.as_view(), name='driver_item_params'),

]