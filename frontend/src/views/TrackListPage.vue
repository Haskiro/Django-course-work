<template>
  <track-list :tracks="tracks"></track-list>
</template>

<script>
import TrackList from '../components/TrackList.vue'

export default {
  name: 'TrackListPage',
  props: ['cors'],
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
      const response = await fetch(`${this.cors}course-work-backend.std-1723.ist.mospolytech.ru/api/tracks/`, {
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