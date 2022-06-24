<template>
  <div id="artists">
    <h1 class="artists__heading">Список исполнителей</h1>
    <ul class="artists__list">
      <li class="artists__item" v-for="artist in artists" :key="artist.id">
        <div class="artists__card card-artists">
            <img class="card-artists__img" :src="artist.photo" alt="Обложка Трека">
            <p class="card-artists__text">{{ artist.nickname }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'ArtistList',
  props: ['artists'],
  data() {
    return {

    }
  },
  components: {
    // HelloWorld
  },
  methods: {
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
        border-radius: 20px;
        box-shadow: 0 0 10px rgba(0,0,0,0.5);
        padding: 10px;
        cursor: pointer;
    }
}
.card-artists {
    text-align: center;
    &__img {
        width: 100%;
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