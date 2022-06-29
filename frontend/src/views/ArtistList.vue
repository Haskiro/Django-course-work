<template>
  <div id="artists">
    <h1 class="artists__heading">Список исполнителей</h1>
    <ul class="artists__list">
      <li class="artists__item" v-for="artist in artists" :key="artist.id">
        <router-link :to="{name: 'ArtistDetails', params: {id: artist.id }}" class="artists__card card-artists" @click="refreshArtistDetails(artist.id)">
            <img class="card-artists__img" :src="artist.photo" alt="Обложка Трека" height=250>
            <p class="card-artists__text">{{ artist.nickname }}</p>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'ArtistList',
  data() {
    return {
        artistDetails: {},
        artists: null,
    }
  },
  mounted() {
  },
  created() {
    this.getArtistList().then(data => {this.artists = data});
  },
  components: {
    // HelloWorld
  },
  methods: {
    getArtistList: async function() {
      const response = await fetch('http://127.0.0.1:8000/api/artists/', {
        method: 'GET',
      });
      return response.json();
    },
  }
}
</script>

<style lang='scss' scoped>
.artists {
    &__heading {
        text-align: center;
        font-size: 1.4rem;
        line-height: 1.2;
        font-weight: 700;
        margin-bottom: 30px;
    }
    &__list {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 30px;
    }
    &__item {
        grid-column: span 1;
    }
    &__card {
    }
}
.card-artists {
    text-align: center;
    display: block;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    padding: 10px;
    cursor: pointer;
    &__img {
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 15px;
        margin-bottom: 15px;
    }
    &__text {
        font-weight: 600;
        font-size: 1.1rem;
        line-height: 1.2;
        }
}


</style>