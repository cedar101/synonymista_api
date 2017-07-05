export default [
  // {
  //   name: '__handle',
  //   titleClass: 'text-center',
  //   dataClass: 'text-center'
  // },
  // {
  //   name: '__sequence',
  //   title: '#',
  //   titleClass: 'text-center',
  //   dataClass: 'text-right'
  // },
  // {
  //   name: '__checkbox',
  //   titleClass: 'text-center',
  //   dataClass: 'text-center'
  // },
  {
    name: 'id',
    sortField: 'id',
  },
  {
    name: 'subject_word.value',
    title: 'subject word',
    sortField: 'subject_word'
  },
  {
    name: 'subject_word.id',
    title: '(edit)',
    callback: 'linkWordEditor'
  },
  {
    name: 'similar_word.value',
    title: 'similar word',
    sortField: 'similar_word'
  },
  {
    name: 'similar_word.id',
    title: '(edit)',
    callback: 'linkWordEditor'
  },
  {
    name: 'value',
    title: 'similarity value',
    sortField: 'similarity'
  },
  {
    name: 'create_at',
    sortField: 'create_at',
    titleClass: 'text-center',
    dataClass: 'text-center',
    callback: 'formatDate|YYYY-MM-DD'
  },
  {
    name: 'update_at',
    sortField: 'update_at',
    titleClass: 'text-center',
    dataClass: 'text-center',
    callback: 'formatDate|YYYY-MM-DD'
  },
  // {
  //   name: 'nickname',
  //   sortField: 'nickname',
  //   callback: 'allcap'
  // },
  // {
  //   name: 'gender',
  //   sortField: 'gender',
  //   titleClass: 'text-center',
  //   dataClass: 'text-center',
  //   callback: 'genderLabel'
  // },
  // {
  //   name: 'salary',
  //   sortField: 'salary',
  //   titleClass: 'text-center',
  //   dataClass: 'text-right',
  //   callback: 'formatNumber'
  // },
  // {
  //   name: '__component:custom-actions',
  //   title: 'Actions',
  //   titleClass: 'text-center',
  //   dataClass: 'text-center',
  // },
  {
    name: '__slot:actions',
    title: 'Slot Actions',
    titleClass: 'text-center',
    dataClass: 'text-center',
  }
]
