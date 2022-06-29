from rest_framework import serializers
from playlist.models import Playlist
from track.models import Track

class TrackSerializerForPlaylist(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__al__'

class PlaylistSerializer(serializers.ModelSerializer):
    tarcks_data = TrackSerializerForPlaylist(source='tracks', many=True)
    class Meta:
        model = Playlist
        exclude = ['tracks']