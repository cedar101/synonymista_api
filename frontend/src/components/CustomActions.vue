<template>
  <div class="custom-actions">
    <button class="ui basic button" @click="itemAction('view-item', rowData, rowIndex)"><i class="zoom icon"></i></button>
    <button class="ui basic button" @click="itemAction('edit-item', rowData, rowIndex)"><i class="edit icon"></i></button>
    <button class="ui basic button" @click="itemAction('delete-item', rowData, rowIndex)"><i class="delete icon"></i></button>
  </div>
</template>

<script>
// import Vue from 'vue'
// import VueResource from 'vue-resource'
//
// Vue.use(VueResource)

export default {
  props: {
    rowData: {
      type: Object,
      required: true
    },
    rowIndex: {
      type: Number
    }
  },
  methods: {
    itemAction (action, data, index) {
      console.log('custom-actions: ' + action, data, index)
      const BaseURI = 'http://localhost:5050'
      // this.$http.remove(`${BaseURI}/word-similarities/${data.id}`) 
      if (action == 'delete-item') {
        this.$http.remove(`${BaseURI}/word-similarities/${data.id}`) //, {params:{id: data.id}});
      }
    }
  }
}
</script>

<style>
  .custom-actions button.ui.button {
    padding: 8px 8px;
  }
  .custom-actions button.ui.button > i.icon {
    margin: auto !important;
  }
</style>
