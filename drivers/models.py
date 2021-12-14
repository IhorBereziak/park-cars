from django.db import models

class DriverModel(models.Model):
    class Meta:
        db_table = 'drivers'
        verbose_name = 'driver'
    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name