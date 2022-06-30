<template>
  <track-list :tracks="tracks"></track-list>
</template>

<script>
import TrackList from '../components/TrackList.vue'

export default {
  name: 'TrackListPage',
  data() {
    return {
      tracks: null,
    }
  },
  components: {
    TrackList
    
  },
  methods: {
    getTrackList: async function() {
      const response = await fetch('http://127.0.0.1:8000/api/tracks/', {
        method: 'GET',
      });
      return response.json();
    },
  },
  mounted: function() {

  },
  created() {
    this.getTrackList().then(data => {this.tracks = data});
  }
}
</script>

<style lang='scss' scoped>

</style>