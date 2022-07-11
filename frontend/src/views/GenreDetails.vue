<template>
  <div id="genre">
    <div class="genre__header">
      <img :src="genreDetails.cover" alt="Фотография" class="genre__photo" height="250" width="250">
      <h1 class="genre__title">{{ genreDetails.title }}</h1>
    </div>
    <div class="genre__body">
      <p class="genre__text">{{ genreDetails.description }}</p>
      <track-list :tracks="genreDetails.tracks_data" class="genre__tracks"></track-list>
    </div>
  </div>
</template>

<script>
import TrackList from '../components/TrackList.vue';

export default {
  name: 'GenreDetails',
  props: ['id', 'cors'],
  data() {
    return {
      genreDetails: {},
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
        this.refreshGenreDetails(this.id);
      },
    },
  },
  methods: {
    getGenreDetails: async function(genre_id) {
      const response = await fetch(`${this.cors}course-work-backend.std-1723.ist.mospolytech.ru/api/genres/${genre_id}`, {
        method: 'GET',
      });
      return response.json();
    },
    refreshGenreDetails: function(genre_id) {
        this.getGenreDetails(genre_id).then(data => {this.genreDetails = data});
    },
  }
}
</script>

<style lang='scss' scoped>
.genre {
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