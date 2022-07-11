<template>
  <div id="app">
    <header-main v-if="accessToken" @logout='logout' :user='user' :cors='cors'></header-main>
    <!-- <header-auth v-else></header-auth> -->
    <main class="main">
      <div class="container main__body">
        <login-page v-if="!accessToken" @login='login'></login-page>
        <router-view v-else></router-view>
      </div>
    </main>
    <footer class="footer">
      <div class="footer__body container">
        <p class="footer__text">Кондратьев Павел Евгеньевич 211-321</p>
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
      accessToken: '',
      loginData: {},
      user: {},
      cors: 'https://justcors.com/tl_034cbc1/http://'
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
  methods: {
    auth: async function() {
      const response = await fetch(`${this.cors}course-work-backend.std-1723.ist.mospolytech.ru/api/auth/login/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.loginData)
      });
      return response.json();
    },
    getUserInfo: async function() {
      const response = await fetch(`${this.cors}course-work-backend.std-1723.ist.mospolytech.ru/api/auth/me/`, {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + this.accessToken,
        },
      });
      return response.json();
    },
    login: function(data) {
      this.loginData = data;
      this.auth().then(data => {
        this.accessToken = data.access;
        localStorage.setItem('accessToken', this.accessToken);
        this.getUserInfo().then(data => {this.user = data})
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
    padding-top: 50px;
    padding-bottom: 50px;
  }
  &__text {
    font-size: 1.4rem;
    line-height: 1.3;
    text-align: center;
  }
}

</style>
