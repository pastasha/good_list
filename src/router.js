import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import News from './views/News.vue'
import NeedHelp from './views/NeedHelp.vue'
import NeedHelpCategory from './views/NeedHelpCategory.vue'
import WantHelp from './views/WantHelp.vue'
import WantHelpCategory from './views/WantHelpCategory.vue'
import Reports from './views/Reports.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/news',
      name: 'news',
      component: News
    },
    {
      path: '/need-help',
      name: 'need-help',
      component: NeedHelp
    },
    {
      path: '/need-help/:category',
      name: 'need-help-:category',
      component: NeedHelpCategory
    },
    {
      path: '/want-help',
      name: 'want-help',
      component: WantHelp
    },
    {
      path: '/want-help/:category',
      name: 'want-help-:category',
      component: WantHelpCategory
    },
    {
      path: '/reports',
      name: 'reports',
      component: Reports
    }
  ]
})
