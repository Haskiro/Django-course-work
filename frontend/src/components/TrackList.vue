<template>
  <div id="tracks">
    <h1 class="tracks__heading">Список треков</h1>
    <ul class="tracks__list">
      <li class="tracks__item" v-for="track in tracks" :key="track.id">
        <div class="tracks__card card-tracks">
          <div class="card-tracks__block">
            <img class="card-tracks__img" :src="track.cover" alt="Обложка Трека" width="80" height="80">
            <div class="card-tracks__text">
              <p class="card-tracks__title">{{ track.title }}</p>
              <p class="card-tracks__artists"><router-link class="card-tracks__link" v-for="artist in track.artists_data" :key="artist.id" :to="{name: 'ArtistDetails', params: {id: artist.id}}" tag="span">{{ artist.nickname }}&nbsp;&nbsp;</router-link></p>
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
  @media (max-width: 600px) {
    gap: 15px;
  }
  @media (max-width: 600px) {
    gap: 10px;
    padding: 5px 10px;
  }
  &__block {
    display: flex;
    gap: 30px;
    align-items: center;
    @media (max-width: 600px) {
    gap: 15px;
    }
    @media (max-width: 450px) {
      gap: 10px;
    }
  }
  &__img {
    width: 80px;
    height: 80px;
    object-fit: cover;
    border-radius: 15px;
    @media (max-width: 600px) {
      width: 60px;
      height: 60px;
    }
    @media (max-width: 450px) {
      width: 45px;
      height: 45px;
      border-radius: 10px;
    }
    @media (max-width: 410px) {
      display: none;
    }
  }
  &__text {
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 30ch;
  }
  &__title {
    font-weight: 600;
    font-size: 1.1rem;
    line-height: 1.2;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    width: 15ch;
    @media (max-width: 600px) {
      font-size: 0.9rem;
      width: 10ch;
    }
  }
  &__artists {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    width: 15ch;
    cursor: pointer;
    @media (max-width: 600px) {
      font-size: 0.8rem;
      width: 10ch;
    }
  }
  &__link {
    &:hover {
      color: purple;
    }
  } 
  &__audio {
    display: inline-block;
    border-radius: 10px;
  }
}
</style>
