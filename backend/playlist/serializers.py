from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from playlist.models import Playlist

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'