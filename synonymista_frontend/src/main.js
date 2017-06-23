// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import {ServerTable, ClientTable, Event} from 'vue-tables-2';

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})

Vue.use(VueTables.client, {
  perPage: 10
})

new Vue({
  el: "#vue-tables-options",
  data: {
    columns: ['id', 'value', 'similar_to', 'similar_from', 'link'],
    data: [
        {
        }
    ]
    },
  options: {
      sortable: ['value']
  }
})
