import VueRouter from 'vue-router'
import MainPage from '../views/MainPage'
import TrackList from '../views/TrackList'
import ArtistList from '../views/ArtistList'

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
        },
        {
            path: '/artists',
            component: ArtistList,
            name: 'ArtistList',
            props: true,

        }
    ]
  })