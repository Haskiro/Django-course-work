from rest_framework import serializers
from playlist.models import Playlist
from track.serializers import TrackSerializer

class PlaylistSerializer(serializers.ModelSerializer):
    tarcks_data = TrackSerializer(source='tracks', many=True)
    class Meta:
        model = Playlist
        exclude = ['tracks']