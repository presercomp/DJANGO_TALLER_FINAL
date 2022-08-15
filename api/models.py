from typing_extensions import Required
from django.db import models

# Create your models here.
class Reservation(models.Model):
    id = models.IntegerField(primary_key=True)
    reserverName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=12)
    date = models.DateField()
    hour = models.TimeField()
    diners = models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15')])
    state = models.CharField(choices=[('RESERVADO', 'RESERVADO'), ('COMPLETADA', 'COMPLETADA'), ('ANULADA', 'ANULADA'), ('NO ASISTEN', 'NO ASISTEN')], max_length=10)
    observations = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.reserverName + " " + self.phoneNumber + " " + self.date + " " + self.hour + " " + self.diners + " " + self.state