<template>
  <div id="album">
    <div class="album__header">
      <img :src="albumDetails.cover" alt="Фотография" class="album__photo" height="250" width="250">
      <h1 class="album__title">{{ albumDetails.title }}</h1>
    </div>
    <div class="album__body">
      <p class="album__text">{{ albumDetails.description }}</p>
      <track-list :tracks="albumDetails.tracks_data" class="album__tracks"></track-list>
    </div>
  </div>
</template>

<script>
import TrackList from '../components/TrackList.vue';

export default {
  name: 'AlbumDetails',
  props: ['id', 'cors'],
  data() {
    return {
      albumDetails: {},
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
        this.refreshAlbumDetails(this.id);
      },
    },
  },
  methods: {
    getAlbumDetails: async function(album_id) {
      const response = await fetch(`http://course-work-backend.std-1723.ist.mospolytech.ru/api/albums/${album_id}`, {
        method: 'GET',
      });
      return response.json();
    },
    refreshAlbumDetails: function(album_id) {
        this.getAlbumDetails(album_id).then(data => {this.albumDetails = data});
    },
  }
}
</script>

<style lang='scss' scoped>
.album {
  &__header {
    display: flex;
    gap: 30px;
    @media (max-width: 480px) {
      flex-direction: column-reverse;
    }
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