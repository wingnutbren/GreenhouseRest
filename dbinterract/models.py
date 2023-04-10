from django.db import models

# Create your models here.
class Thermometer(models.Model):
    plain_name = models.CharField(max_length=30)
    device_mac = models.CharField(max_length=30) 
    device_lat = models.IntegerField()
    device_lon = models.IntegerField()
    device_ele = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.plain_name} ({self.id})"

    

class Temp(models.Model):
    therm = models.ForeignKey(Thermometer, on_delete=models.DO_NOTHING)
    datetime = models.IntegerField()
    ftemp = models.FloatField()
    
    def __str__(self) -> str:
        return str(f"{self.ftemp} : {self.therm}")

    
