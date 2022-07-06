<template>
  <div id="app">
    <header-main v-if="accessToken" @logout='logout'></header-main>
    <!-- <header-auth v-else></header-auth> -->
    <main class="main">
      <div class="container main__body">
        <router-view v-if="accessToken"></router-view>
        <login-page v-else @login='login'></login-page>
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
// import HeaderAuth from './components/HeaderAuth.vue'
import HeaderMain from './components/HeaderMain.vue'
import LoginPage from './components/LoginPage.vue'

export default {
  name: 'App',
  data() {
    return {
      tracks: {},
      artists: {},
      accessToken: '',
      loginData: {},
      user: {}
    }
  },
  components: {
    HeaderMain,
    LoginPage
  },
  created() {
    this.accessToken = localStorage.getItem('accessToken');
    this.getUserInfo().then(data => {this.user = data})
    if (this.user.code == "token_not_valid") {
      this.accessToken = '';
      localStorage.setItem('accessToken', '');
    }

  },
  mounted: function() {
    this.getTrackList().then(data => {
      this.tracks = data;
    });
    this.getArtistList().then(data => {this.artists = data});
  },
  methods: {
    getTrackList: async function() {
      const response = await fetch('http://django-course-work.std-1723.ist.mospolytech.ru/api/tracks/', {
        method: 'GET',
      });
      return response.json();
    },
    getArtistList: async function() {
      const response = await fetch('http://django-course-work.std-1723.ist.mospolytech.ru/api/artists/', {
        method: 'GET',
      });
      return response.json();
    },
    updateTrackList: function() {
      this.getTrackList().then(data => {this.tracks = data});
    },
    auth: async function() {
      const response = await fetch(`http://django-course-work.std-1723.ist.mospolytech.ru/api/auth/login/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.loginData)
      });
      return response.json();
    },
    getUserInfo: async function() {
      const response = await fetch(`http://django-course-work.std-1723.ist.mospolytech.ru/api/auth/me/`, {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + this.accessToken
        },
      });
      return response.json();
    },
    login: function(data) {
      this.loginData = data;
      this.auth().then(data => {
        this.accessToken = data.access;
        localStorage.setItem('accessToken', this.accessToken);
        // if (this.accessToken != '') {
        //   history.pushState(null, null, '/me');
        // }
      })
    },
    logout: function() {
      this.accessToken = '';
      localStorage.setItem('accessToken', '');
    }
    // .then(data => {this.accessToken = data.access})
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

.container {
  max-width: 1200px;
  padding-left: 15px;
  padding-right: 15px;
  margin: 0px auto;
}

.main {
		&__body {
		}
}
.footer {
  &__body {
    display: flex;
    justify-content: space-between;
    padding-top: 50px;
    padding-bottom: 50px;
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
