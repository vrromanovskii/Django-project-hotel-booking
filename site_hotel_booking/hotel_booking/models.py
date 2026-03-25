

from django.db import models

# Create your models here.

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    has_bookings = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Bookings(models.Model):
    check_in = models.DateField(null=True)
    check_out = models.DateField(null=True)
    room = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100, default='guest')

    def __str__(self):
        return f"{self.guest_name} - {self.room.name} ({self.check_in} - {self.check_out})"
