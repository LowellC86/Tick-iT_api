from django.shortcuts import render
from .models import Venue, Event
from rest_framework import generics
from .serializers import VenueSerializer, EventSerializer

# Create your views here.

class VenueList(generics.ListCreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class VenueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset=Event.objects.all()
    serializer_class = EventSerializer
