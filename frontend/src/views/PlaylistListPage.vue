<template>
  <div id="playlists">
    <h1 class="playlists__heading">Плейлисты</h1>
    <ul class="playlists__list">
      <li class="playlists__item" v-for="playlist in playlists" :key="playlist.id">
        <router-link :to="{name: 'PlaylistDetails', params: {id: playlist.id, cors: cors }}" class="playlists__card card-playlists" tag="div">
            <img class="card-playlists__img" :src="playlist.cover" alt="Обложка Трека" height=250>
            <p class="card-playlists__text">{{ playlist.title }}</p>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'PlaylistListPage',
  data() {
    return {
        playlists: null,
        cors: '',
    }
  },
  mounted() {
  },
  created() {
    this.cors = localStorage.getItem('cors');
    this.getPlaylistList().then(data => {this.playlists = data});
  },
  components: {
    // HelloWorld
  },
  methods: {
    getPlaylistList: async function() {
      const response = await fetch(`${this.cors}course-work-backend.std-1723.ist.mospolytech.ru/api/playlists/`, {
        method: 'GET',
      });
      return response.json();
    },
  }
}
</script>

<style lang='scss' scoped>
.playlists {
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
        @media (max-width: 1024px) {
          grid-template-columns: repeat(3, 1fr);
        }
        @media (max-width: 768px) {
          grid-template-columns: repeat(2, 1fr);
        }
        @media (max-width: 480px) {
          grid-template-columns: repeat(1, 1fr);
        }  
    }
    &__item {
        grid-column: span 1;
    }
    &__card {
    }
}
.card-playlists {
    text-align: center;
    display: block;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    padding: 10px;
    cursor: pointer;
    transition: 0.2s ease;
    &:hover {
      transform: scale(1.05);
      transition: 0.2s ease;
    }
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