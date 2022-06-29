from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from genre.models import Genre
from track.models import Track

class TrackSerializerForGenre(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__al__'

class GenreSerializer(serializers.ModelSerializer):
    tracks_data = TrackSerializerForGenre(source='tracks', many=True)
    class Meta:
        model = Genre
        exclude = ['tracks']