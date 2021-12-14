from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

DriverModel = get_user_model()

class VehicleModel(models.Model):
    class Meta:
        db_table = 'vehicles'
        verbose_name = 'vehicle'
    driver_id = models.ForeignKey(DriverModel, on_delete=models.CASCADE)
    make = models.CharField(verbose_name='Make', max_length=250)
    model = models.CharField(verbose_name='Model', max_length=250)
    plate_number = models.CharField(verbose_name='Plate_number', max_length=12,validators = [RegexValidator('^[A-Z]{2}\s\d{4}\s[A-Z]{2}$')], unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.make