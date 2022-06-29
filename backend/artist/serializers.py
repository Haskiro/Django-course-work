from dataclasses import fields
from rest_framework import serializers
from artist.models import Artist
from track.models import Track

class TrackSerializerForArtist(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['audio_file', 'cover']

class ArtistSerializer(serializers.ModelSerializer):
    tracks_data = TrackSerializerForArtist(source='tracks', many=True)
    class Meta:
        model = Artist
        fields = '__all__'
