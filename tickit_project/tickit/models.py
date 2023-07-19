from django.db import models

# Create your models here.
# tickit/models.py
from django.db import models


class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()
    genre = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    is_concert = models.BooleanField(default=True)
    is_sports_event = models.BooleanField(default=False)

    def __str__(self):
        return self.title
