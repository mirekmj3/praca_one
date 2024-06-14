from django.db import models

# Create your models here.

class SWATH (models.Model):
    Hp_26695 = models.CharField(max_length=100)
    comp_delta = models.FloatField(max_length=100)
    comp_wt = models.FloatField(max_length=100)
    delta_wt = models.FloatField(max_length=100)

    class Meta:
        ordering = ('Hp_26695',)