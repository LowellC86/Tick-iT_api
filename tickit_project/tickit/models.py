from django.db import models

# Create your models here.
# tickit/models.py
class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name
      
class Event(models.Model): 
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=250)
    date = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    price = models.IntegerField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='fads')

    def __str__(self):
        return self.title
