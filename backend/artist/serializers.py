from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from artist.models import Artist
from track.models import Track
from album.models import Album

class AlbumSetializerForArtist(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['title', 'cover']

class TrackSerializerForArtist(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['audio_file', 'cover']

class ArtistSerializer(serializers.ModelSerializer):
    tracks_data = TrackSerializerForArtist(source='tracks', many=True)
    albums_data = AlbumSetializerForArtist(source='albums', many=True)
    class Meta:
        model = Artist
        fields = '__all__'
