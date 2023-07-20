from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    photo_url = models.TextField()
    description = models.TextField(default='')
    events = models.ManyToManyField('Event', related_name='venues')  
    venue_url = models.URLField()  

    def __str__(self):
        return self.name

class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateField()
    genre = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_concert = models.BooleanField(default=True)
    is_sports_event = models.BooleanField(default=False)
    tickets = models.IntegerField(default=100)

    def __str__(self):
        return self.title
