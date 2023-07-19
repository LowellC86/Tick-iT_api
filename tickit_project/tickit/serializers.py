from rest_framework import serializers
from .models import Venue, Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )

    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )

    class Meta:
        model = Event
        fields = ('id' ,'date', 'genre', 'price', 'venue', 'is_concert', 'is_sports_event', 'venue_id')
        
class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many=True,
        read_only=True
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail'
    )

    class Meta:
        model = Venue
        fields = ('id', 'photo_url', 'events', 'venue_url') 
