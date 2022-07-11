<template>
  <div class="user">
    <div class="user__header">
      <img :src="user.photo" alt="Фотография" class="user__photo" height="250" width="250">
      <div class="user__block">
        <h1 class="user__title">Профиль</h1>
        <p class="user__text">{{ user.first_name }} {{ user.last_name }}</p>
      </div>
    </div>
    <div class="user__body">
      <p class="user__text">{{ user.bio }}</p>
    </div>
  </div>
</template>

<script>


export default {
  name: 'UserPage',
  props: [],
  data() {
    return {
      accessToken: '',
      user: {},
      cors: 'https://justcors.com/tl_034cbc1/http://'
    }
  },
  components: {
    
  },
  methods: {
    getUserInfo: async function() {
      const response = await fetch(`${this.cors}course-work-backend.std-1723.ist.mospolytech.ru/api/auth/me/`, {
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + this.accessToken,

        },
      });
      return response.json();
    },
  },
  mounted: function() {
    this.accessToken = localStorage.getItem('accessToken');
    this.getUserInfo().then(data => {
      this.user = data;
      this.user.photo = `http://course-work-backend.std-1723.ist.mospolytech.ru/${this.user.photo}`;
    });
  },
  created() {
    this.accessToken = localStorage.getItem('accessToken');
    this.cors = localStorage.getItem('cors');
    this.getUserInfo().then(data => {
      this.user = data;
      this.user.photo = `http://course-work-backend.std-1723.ist.mospolytech.ru/${this.user.photo}`;
    });
  }
}
</script>

<style lang='scss' scoped>
.user {
  &__header {
    display: flex;
    gap: 30px;
    @media (max-width: 480px) {
      flex-direction: column-reverse;
    }
  }
  &__photo {
    display: block;
    width: 250px;
    height: 250px;
    object-fit: cover;
    border-radius: 15px;
  }
  &__block {
    display: block;
  }
  &__title {
    font-size: 1.4rem;
    line-height: 1.2;
    font-weight: 600;
  }
  &__text {
    max-width: 85ch;
  }
  &__body {
    margin-top: 50px;
  }
}
</style>