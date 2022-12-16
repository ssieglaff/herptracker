from django.db import models

# Create your models here.

class Herp(models.Model):
    species = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    svl = models.IntegerField()
    tail = models.IntegerField()
    tibia = models.IntegerField()
    notes = models.TextField()

class Observation(models.Model):
    herp = models.ForeignKey("Herp", null=True, blank=True, on_delete=models.SET_NULL)
    trapType = models.CharField(max_length=30, null=True, blank=True)
    latitute = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timeSet = models.DateTimeField(null=True, blank=True)
    timeChecked = models.DateTimeField()

