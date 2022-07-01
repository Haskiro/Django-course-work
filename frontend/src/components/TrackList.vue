<template>
  <div id="tracks">
    <h1 class="tracks__heading">Список треков</h1>
    <ul class="tracks__list">
      <li class="tracks__item" v-for="track in tracks" :key="track.id">
        <div class="tracks__card card-tracks">
          <div class="card-tracks__block">
            <img class="card-tracks__img" :src="track.cover" alt="Обложка Трека">
            <div class="card-tracks__text">
              <p class="card-tracks__title">{{ track.title }}</p>
              <router-link v-for="artist in track.artists_data" :key="artist.id" class="card-tracks__artists" :to="{name: 'ArtistDetails', params: {id: artist.id}}" tag="span">{{ artist.nickname }}&nbsp;&nbsp;</router-link>
            </div>
          </div>
          <audio class="card-tracks__audio" controls :src="track.audio_file"></audio>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'TrackList',
  props: ['tracks'],
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang='scss'>
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
    cursor: pointer;
    &:hover {
      color: purple;
    }
  }
  &__audio {
  }
}
</style>
