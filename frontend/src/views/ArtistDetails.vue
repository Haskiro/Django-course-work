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
      <div class="artist__tracks tracks">
        <h1 class="tracks__heading">Список треков</h1>
        <ul class="tracks__list">
          <li class="tracks__item" v-for="track in artistDetails.tracks_data" :key="track.id">
            <div class="tracks__card card-tracks">
              <div class="card-tracks__block">
                <img class="card-tracks__img" :src="track.cover" alt="Обложка Трека">
                <div class="card-tracks__text">
                  <p class="card-tracks__title">{{ track.title }}</p>
                  <p class="card-tracks__artists"><span v-for="artist in track.artists_data" :key="artist.id"><router-link :to="{path: '/artists/'+artist.id}">{{ artist.nickname }}&nbsp;</router-link></span></p>
                </div>
              </div>
              <audio class="card-tracks__audio" controls :src="track.audio_file"></audio>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'ArtistDetails',
  props: ['id'],
  data() {
    return {
      artistDetails: {},
    }
  },
  components: {
    // HelloWorld
  },
  created() {
    this.refreshArtistDetails(this.id);
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
}
.tracks {
  &__heading {
    text-align: center;
    font-size: 1.4rem;
    line-height: 1.2;
    font-weight: 700;
    margin-bottom: 30px;
  }
  &__list {
  }
  &__item {
    max-width: 700px;
    margin: 20px auto;
  }
  &__card {
  }
}
.card-tracks {
  display: flex;
  padding: 10px;
  gap: 30px;
  align-items: center;
  justify-content: space-between;
  border-radius: 20px;
  box-shadow: 0 0 10px rgba(0,0,0,0.5);
  &__block {
    display: flex;
    gap: 30px;
    align-items: center;
  }
  &__img {
    width: 80px;
    height: 80px;
    object-fit: cover;
    border-radius: 15px;
  }
  &__text {
  }
  &__title {
    font-weight: 600;
    font-size: 1.1rem;
    line-height: 1.2;
  }
  &__artists {
  }
  &__audio {
  }
}

</style>