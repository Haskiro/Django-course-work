<template>
  <div id="playlist">
    <div class="playlist__header">
      <img :src="playlistDetails.cover" alt="Фотография" class="playlist__photo" height="250" width="250">
      <h1 class="playlist__title">{{ playlistDetails.title }}</h1>
    </div>
    <div class="playlist__body">
      <p class="playlist__text">{{ playlistDetails.description }}</p>
      <track-list :tracks="playlistDetails.tracks_data" class="playlist__tracks"></track-list>
    </div>
  </div>
</template>

<script>
import TrackList from '../components/TrackList.vue';

export default {
  name: 'PlaylistDetails',
  props: ['id'],
  data() {
    return {
      playlistDetails: {},
    }
  },
  components: {
    TrackList
    // HelloWorld
  },
  watch: {
    '$route.params.id': {
      immediate: true,
      handler() {
        this.refreshPlaylistDetails(this.id);
      },
    },
  },
  methods: {
    getPlaylistDetails: async function(playlist_id) {
      const response = await fetch(`http://django-course-work.std-1723.ist.mospolytech.ru/api/playlists/${playlist_id}`, {
        method: 'GET',
      });
      return response.json();
    },
    refreshPlaylistDetails: function(playlist_id) {
        this.getPlaylistDetails(playlist_id).then(data => {this.playlistDetails = data});
    },
  }
}
</script>

<style lang='scss' scoped>
.playlist {
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
}
</style>