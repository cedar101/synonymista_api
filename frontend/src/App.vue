<template>
  <div id="app">
    <!-- <img id="logo" src="./assets/logo.png"> -->
    <ws-vuetable
      api-url="http://localhost:5050/word-similarities"
      :fields="fields"
      :sort-order="sortOrder"
      :append-params="moreParams"
      detail-row-component="my-detail-row"
    >
    <!-- :pagination-path="links.pagination" -->
    <!-- detail-row-component="my-detail-row" -->

      <template slot="actions" scope="props">
        <div class="custom-actions">
          <button class="btn btn-default btn-sm"
            @click="onAction('view-item', props.rowData, props.rowIndex)">
            <span class="glyphicon glyphicon-zoom-in"></span>
          </button>
          <button class="btn btn-default btn-sm"
            @click="onAction('edit-item', props.rowData, props.rowIndex)">
            <i class="glyphicon glyphicon-pencil"></i>
          </button>
          <button class="btn btn-default btn-sm"
            @click="onAction('delete-item', props.rowData, props.rowIndex)">
            <i class="glyphicon glyphicon-trash"></i>
          </button>
        </div>
      </template>
    </ws-vuetable>
  </div>
</template>

<script>
import Vue from 'vue'
import WsFieldDefs from './components/WsFieldDefs.js'
import WsVuetable from './components/WsVuetable'
import DetailRow from './components/DetailRow'

Vue.component('my-detail-row', DetailRow)


export default {
  name: 'app',
  components: {
    WsVuetable
  },
  data () {
    return {
      fields: WsFieldDefs,
      sortOrder: [
        {
          field: 'id',
          sortField: 'value',
          direction: 'asc'
        }
      ],
      moreParams: {}
    }
  },
  methods: {
    onAction (action, data, index) {
      console.log('slot action: ' + action, data.name, index)
    },
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
img#logo {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.filter-bar {
  padding: 8px;
}
.pagination {
  margin-top: 0px;
}
</style>
