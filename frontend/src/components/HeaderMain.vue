<template>
  <header class="header">
      <div class="header__body container">
        <div class="header__user">
          <p class="header__text">{{ user.first_name }}</p>
          <button class="header__button" @click="logout">
            <router-link :to="{name: 'LoginPage', params: {}}" tag="p">Выйти</router-link>
          </button>
        </div>
        <nav class="header__nav nav">
          <ul class="nav__list">
            <router-link class="nav__item" :to="{name: 'UserPage', params: {}}" tag="li">Профиль</router-link>
            <router-link class="nav__item" :to="{name: 'TrackList', params: {}}" tag="li">Треки</router-link>
            <router-link class="nav__item" :to="{name: 'ArtistList', params: {}}" tag="li">Исполнители</router-link>
            <router-link class="nav__item" :to="{name: 'GenreList', params: {}}" tag="li">Жанры</router-link>
            <router-link class="nav__item" :to="{name: 'PlaylistList', params: {}}" tag="li">Плейлисты</router-link>
          </ul>
        </nav>
        <button class="header__burger">
          <img src="../assets/burger.svg" alt="Меню">
        </button>
      </div>
    </header>
</template>

<script>
export default {
  name: 'HeaderMain',
  props: ['user'],
  methods: {
    logout: function() {
      this.$emit('logout', null);
    }
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
    gap: 30px;
    align-items: center;
  }
  &__text {
    font-weight: 600;
    font-size: 1.1rem;
    line-height: 1.3;

  }
  &__button {
    border: none;
    border-radius: 10px;
    box-shadow: 0 0 5px rgba(0,0,0,0.5);
    background: none;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 1rem;
    transition: 0.2s ease;
    &:hover {
      transform: scale(1.05);
      transition: 0.2s ease;
    }
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
.nav {
  align-self: center;
  &__list {
    display: flex;
    gap: 20px;
  }
  &__item {
    cursor: pointer;
    &:hover {
      color: purple;
    }
  }
}
</style>
