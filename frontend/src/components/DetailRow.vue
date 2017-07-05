<template>
  <div @click="onClick">
    <div class="inline field">
      <label>subject word id: </label>
      <span>{{rowData.subject_word.id}}</span>&nbsp;
      <!-- <span><a href="http://127.0.0.1:5000/adn/word/edit/?id={{rowData.subject_word.id}}&url=%2Fadn%2Fword%2F">(edit)</a><span> -->
    </div>
    <div class="inline field">
      <label>subject word value: </label>
      <span>{{rowData.subject_word.value}}</span>
    </div>
    <div class="inline field">
      <label>similar word id: </label>
      <span>{{rowData.similar_word.id}}</span>&nbsp;
      <!-- <span><a href="http://127.0.0.1:5000/adn/word/edit/?id={{rowData.subject_word.id}}&url=%2Fadn%2Fword%2F">(edit)</a><span> -->
    </div>
    <div class="inline field">
      <label>similar word value: </label>
      <span>{{rowData.similar_word.value}}</span>
    </div>
    <div class="inline field">
      <label>similarity value: </label>
      <span>{{rowData.value}}</span>
    </div>
  </div>
</template>

<script>
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
    onClick (event) {
      console.log('my-detail-row: on-click', event.target)
    }
  },
}
</script>
