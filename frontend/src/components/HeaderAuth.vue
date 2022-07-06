<template>
  <header class="header">
      <div class="header__body container">
        <nav class="header__nav nav">
          <ul class="nav__list">
            <router-link class="nav__item" :to="{name: 'RegisterPage', params: {}}" tag="li">Регистрация</router-link>
            <router-link class="nav__item" to="/" tag="li">Вход</router-link>
          </ul>
        </nav>
      </div>
    </header>
</template>

<script>
export default {
  name: 'HeaderAuth',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang='scss'>
.header {
  &__body {
    display: flex;
    justify-content: right;
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
