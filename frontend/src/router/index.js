import VueRouter from 'vue-router'
import MainPage from '../views/MainPage'
import TrackList from '../views/TrackListPage'
import ArtistList from '../views/ArtistListPage'
import ArtistDetails from '../views/ArtistDetails'
import AlbumDetails from '../views/AlbumDetails'
import GenreDetails from '../views/GenreDetails'
import GenreList from '../views/GenreListPage'

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

        },
        {
            path: '/artists/:id',
            component: ArtistDetails,
            name: 'ArtistDetails',
            props: true,

        },
        {
            path: '/albums/:id',
            component: AlbumDetails,
            name: 'AlbumDetails',
            props: true,

        },
        {
            path: '/genres',
            component: GenreList,
            name: 'GenreList',
            props: true,

        },
        {
            path: '/genres/:id',
            component: GenreDetails,
            name: 'GenreDetails',
            props: true,

        }
    ],
    scrollBehavior() {
        return { x: 0, y: 0 };
    }
  })