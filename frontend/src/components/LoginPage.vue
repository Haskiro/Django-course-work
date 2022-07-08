<template>
  <div class="login">
    <h1 class="login__heading">Вход</h1>
    <form action="login__form" method="POST">
      <label for="email" style="display: none">Почта</label>
      <input v-model.lazy="email" class="login__input" type="email" id="email" name="email" aria-label="Почта" placeholder="Почта">
      <label for="password" style="display: none">Пароль</label>
      <input v-model.lazy="password" class="login__input" type="password" id="password" name="password" aria-label="Пароль" placeholder="Пароль">
      <button class="login__button" type="submit" @click.prevent="login"><router-link :to="{name: 'UserPage', params: {}}" tag="span">Отправить</router-link></button>
    </form>
  </div>
</template>

<script>


export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  components: {
    
  },
  methods: {
    login: function() {
      this.$emit('login', {'email': this.email, 'password': this.password});
    }
    // login: async function() {
    //   const response = await fetch(`http://django-course-work.std-1723.ist.mospolytech.ru/api/auth/login/`, {
    //     method: 'GET',
    //     body: JSON.stringify({email: this.email, password: this.password})
    //   });
    //   return response.json();
    // }
    
  },
  mounted: function() {

  },
  created() {

  }
}
</script>

<style lang='scss' scoped>
.login {
  max-width: 350px;
  margin: 0px auto;
  margin-top: 50px;
  display: flex;
  flex-direction: column;
  &__heading {
    text-align: center;
    font-size: 1.4rem;
    line-height: 1.2;
    font-weight: 700;
    margin-bottom: 30px;
  }
  &__input {
    width: 100%;
    border: none;
    height: 50px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    border-radius: 10px;
    padding: 5px 20px;
    text-align: center;
    font-size: 1rem;
    margin-bottom: 20px;
    transition: 0.2s ease;
    &:focus {
      transform: scale(1.05);
      transition: 0.2s ease;
    }
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
    max-width: 200px;
    margin: 0px auto;
    display: block;
    &:hover {
      transform: scale(1.05);
      transition: 0.2s ease;
    }
  }
}
</style>