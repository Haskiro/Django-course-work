<template>
  <div id="tracks">
    <ul class="tracks__list">
      <li class="tracks__item" v-for="track in tracks" :key="track.id">
        <div class="tracks__card card-tracks">
          <p>{{ track.title }}</p>
          <audio controls :src="track.audio_file"></audio>
          <img :src="track.cover" alt="">
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'TrackList',
  props: ['tracks', 'artists'],
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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>