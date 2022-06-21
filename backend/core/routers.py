from email.policy import default
from django.db import router
from rest_framework.routers import DefaultRouter
from artist.views import ArtistViewSet
from album.views import AlbumViewSet
from track.views import TrackViewSet
from playlist.views import PlaylistViewSet
from genre.views import GenreViewSet

router = DefaultRouter()
 
router.register('artist', ArtistViewSet)
router.register('album', AlbumViewSet)
router.register('genre', GenreViewSet)
router.register('playlist', PlaylistViewSet)
router.register('tracks', TrackViewSet)
