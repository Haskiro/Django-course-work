import VueRouter from 'vue-router'
import MainPage from '../views/MainPage'
import TrackList from '../views/TrackList'

export default new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: MainPage,
        },
        {
            path: '/tracks',
            component: TrackList,
            name: 'TrackList',
            props: true,
        }
    ]
  })