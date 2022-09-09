<template>
  <header class="header">
      <div class="header__body container">
        <div class="header__user">
          <p class="header__text">{{ user.first_name }}</p>
          <button class="header__button" @click="logout">Выйти</button>
        </div>
        <nav class="header__nav nav" v-bind:class="{ active: navIsActive }">
          <ul class="nav__list" justify="center">
            <li class="nav__item" @click="hideNav"><router-link :to="{name: 'UserPage'}" tag="span">Профиль</router-link></li>
            <li class="nav__item" @click="hideNav"><router-link :to="{name: 'TrackList'}" tag="span">Треки</router-link></li>
            <li class="nav__item" @click="hideNav"><router-link :to="{name: 'ArtistList'}" tag="span">Исполнители</router-link></li>
            <li class="nav__item" @click="hideNav"><router-link :to="{name: 'GenreList'}" tag="span">Жанры</router-link></li>
            <li class="nav__item" @click="hideNav"><router-link :to="{name: 'PlaylistList'}" tag="span">Плейлисты</router-link></li>
          </ul>
        </nav>
        <button class="header__burger" @click="showNav">
          <img src="../assets/burger.svg" alt="Меню">
        </button>
      </div>
    </header>
</template>

<script>
export default {
  name: 'HeaderMain',
  props: ['user'],
  data() {
    return {
      navIsActive: false,
      cors: '',
    }
  },
  methods: {
    logout: function() {
      this.$emit('logout', null);
    },
    showNav: function() {
      this.navIsActive = !this.navIsActive;
    },
    hideNav: function() {
      this.navIsActive = false;
    }
  },
  created() {
    this.cors = localStorage.getItem('cors');
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang='scss'>
.header {
  &__body {
    display: flex;
    justify-content: space-between;
    position: relative;
    padding-top: 20px;
    padding-bottom: 20px;
  }
  &__user {
    display: flex;
    position: relative;
    z-index: 10;
    gap: 30px;
    align-items: center;
    @media (max-width: 450px) {
      gap: 15px;
    }
  }
  &__text {
    font-weight: 600;
    font-size: 1.1rem;
    line-height: 1.3;
    @media (max-width: 450px) {
      font-size: 1rem;
    }
  }
  &__button {
    border: none;
    border-radius: 10px;
    box-shadow: 0 0 5px rgba(0,0,0,0.5);
    background: white;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 1rem;
    transition: 0.2s ease;
    @media (max-width: 450px) {
      font-size: 0.9rem;
      padding: 8px 17px;
    }
    &:hover {
      transform: scale(1.05);
      transition: 0.2s ease;
    }
  }
  &__nav {
    position: absolute;
    transition: 0.3s linear;
    left: 0;
    top: -532px;
    visibility: hidden;
    @media (min-width: 768px) {
        position: relative;
        visibility: visible;
        top: auto;
        left: auto;
        right: 0;
    }
    &.active {
        top: 0;
        visibility: visible;
    }
  }
  &__burger {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    width: 50px;
    height: 50px;
    padding: 0;
    z-index: 10;
    &>svg {
      cursor: pointer;
      width: 100%;
    }
    @media (min-width: 768px) {
        display: none;
    }

  }
}
// .nav {
//   align-self: center;
//   &__list {
//     display: flex;
//     gap: 20px;
//   }
//   &__item {
//     cursor: pointer;
//     &:hover {
//       color: purple;
//     }
//   }
// }
.nav {
    padding: 60px 0px 100px;
    width: 100vw;
    z-index: 9;
    height: 532px;
    align-items: center;
    background: white;
    @media (min-width: 768px) {
        background: none;
        height: auto;
        width: auto;
        padding: 0px;
    }
    &__list {
        max-width: 200px;
        margin: 60px auto 0px;
        @media (min-width: 768px) {
            display: flex;
            gap: 20px;
            margin: 0px;
            max-width: none;
            align-items: center;
        }
    }
    &__item {
        text-align: center;
        margin-bottom: 30px;
        &:nth-last-child(-n + 1) {
            margin-bottom: 0px;
        }
        cursor: pointer;
        font-size: 1.3rem;
        &:hover {
          color: purple;
        }
        @media (min-width: 768px) {
          margin-bottom: 0px;
          font-size: 1rem;
        }
    }
}

</style>
