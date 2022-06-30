<template>
  <div id="artist">
    <div class="artist__header">
      <img :src="artistDetails.photo" alt="Фотография" class="artist__photo" height="250" width="250">
      <div class="artist__block">
        <h1 class="artist__title">{{ artistDetails.nickname }}</h1>
        <p class="artist__text">{{ artistDetails.first_name }} {{ artistDetails.last_name }}</p>
        <p class="artist__text">{{ artistDetails.birth_date }}</p>
      </div>
    </div>
    <div class="artist__body">
      <p class="artist__text">{{ artistDetails.bio }}</p>
      <album-list :albums="artistDetails.albums_data" class="artist__albums"></album-list>
      <track-list :tracks="artistDetails.tracks_data" class="artist__tracks"></track-list>
    </div>
  </div>
</template>

<script>
import TrackList from '../components/TrackList.vue'
import AlbumList from '../components/AlbumList.vue'

export default {
  name: 'ArtistDetails',
  props: ['id'],
  data() {
    return {
      artistDetails: {},
    }
  },
  components: {
    TrackList,
    AlbumList
  },
  watch: {
    '$route.params.id': {
      immediate: true,
      handler() {
        this.refreshArtistDetails(this.id);
      },
    },
  },
  methods: {
    getArtistDetails: async function(artist_id) {
      const response = await fetch(`http://127.0.0.1:8000/api/artists/${artist_id}`, {
        method: 'GET',
      });
      return response.json();
    },
    refreshArtistDetails: function(artist_id) {
        this.getArtistDetails(artist_id).then(data => {this.artistDetails = data});
    },
  }
}
</script>

<style lang='scss' scoped>
.artist {
  &__header {
    display: flex;
    gap: 30px;
  }
  &__photo {
    width: 250px;
    height: 250px;
    object-fit: cover;
    border-radius: 15px;
  }
  &__block {
  }
  &__title {
    font-size: 1.4rem;
    line-height: 1.2;
    font-weight: 600;
  }
  &__text {
    max-width: 85ch;
  }
  &__body {
    margin-top: 50px;
  }
  &__tracks {
    margin-top: 50px;
  }
  &__albums {
    margin-top: 50px;
  }
}

</style>