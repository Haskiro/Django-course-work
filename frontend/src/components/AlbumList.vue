<template>
  <div class="artist__album album">
    <h1 class="album__heading">Альбомы</h1>
    <ul class="album__list">
      <li class="album__item" v-for="album in albums" :key="album.id">
        <router-link :to="{path: '/albums/'+album.id, params: {cors: cors}}" class="album__card card-album" tag="div">
            <img class="card-album__img" :src="album.cover" alt="Обложка Альбома" height=250>
            <p class="card-album__text">{{ album.title }}</p>
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'AlbumList',
  props: ['albums', 'cors'],
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang='scss'>
  .album {
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
  .card-album {
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
