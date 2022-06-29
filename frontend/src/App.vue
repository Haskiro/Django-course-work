<template>
  <div id="app">
    <header class="header">
      <div class="header__body container">
        <img class="header__logo" src="./assets/logo.svg" alt="Логотип">
        <nav class="header__nav nav">
          <ul class="nav__list">
            <li class="nav__item"><router-link to="/">Главная</router-link></li>
            <li class="nav__item"><router-link :to="{name: 'TrackList', params: {}}">Треки</router-link></li>
            <li class="nav__item"><router-link :to="{name: 'ArtistList', params: {}}">Исполнители</router-link></li>
            <li class="nav__item">Жанры</li>
            <li class="nav__item">Плейлисты</li>
          </ul>
        </nav>
        <button class="header__burger">
          <img src="./assets/burger.svg" alt="Меню">
        </button>
      </div>
    </header>
    <main class="main">
      <div class="container main__body">
        <router-view></router-view>
      </div>
    </main>
    <footer class="footer">
      <div class="footer__body container">
        <p class="footer__text footer__text_name">Кондратьев Павел Евгеньевич</p>
        <p class="footer__text footer__text_group">211-321</p>
      </div>
    </footer>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import '../public/reset.scss'

export default {
  name: 'App',
  data() {
    return {
      tracks: {},
      artists: {},
    }
  },
  components: {

  },
  mounted: function() {
    this.getTrackList().then(data => {
      this.tracks = data;
    });
    this.getArtistList().then(data => {this.artists = data});
  },
  methods: {
    getTrackList: async function() {
      const response = await fetch('http://127.0.0.1:8000/api/tracks/', {
        method: 'GET',
      });
      return response.json();
    },
    getArtistList: async function() {
      const response = await fetch('http://127.0.0.1:8000/api/artists/', {
        method: 'GET',
      });
      return response.json();
    },
    updateTrackList: function() {
      this.getTrackList().then(data => {this.tracks = data});
    }
  }
}
</script>

<style lang='scss'>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-direction: column;
  height: 100%;
}

html, body {
  height: 100%;
}

main {
  flex: 1 0 auto;
}

footer {
  flex: 0 0 auto;
}

.header {
		&__body {
      display: flex;
      justify-content: space-between;
      position: relative;
      padding-top: 20px;
      padding-bottom: 20px;
		}
		&__logo {
      height: 80px;
      width: 80px;
      align-self: center;
		}
		&__nav {

		}
		&__burger {
      display: none;
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      width: 70px;
      height: 70px;
      padding: 0;
      &>svg {
        cursor: pointer;
        width: 100%;
      }
		}
}
.container {
  max-width: 1200px;
  padding-left: 15px;
  padding-right: 15px;
  margin: 0px auto;
}
.nav {
  align-self: center;
		&__list {
      display: flex;
      gap: 20px;
		}
		&__item {
      cursor: pointer;
		}
}
.main {
		&__body {
		}
}
.footer {
  &__body {
    display: flex;
    justify-content: space-between;
    padding-top: 20px;
    padding-bottom: 20px;
  }
  &__text {
    font-size: 1.4rem;
    line-height: 1.3;
    &_name {
    }
    &_group {
    }
  }
}

</style>
