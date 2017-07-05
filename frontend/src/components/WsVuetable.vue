<script>
import accounting from 'accounting'
import moment from 'moment'
import Vue from 'vue'
import VueEvents from 'vue-events'
import Vuetable from 'vuetable-2/src/components/Vuetable'
// import VuetablePagination from 'vuetable-2/src/components/VuetablePagination'
import VuetablePaginationInfo from 'vuetable-2/src/components/VuetablePaginationInfo'
import CustomActions from './CustomActions'
import FilterBar from './FilterBar'
import CssConfig from './VuetableCssConfig.js'
import VuetablePaginationBootstrap from './VuetablePaginationBootstrap'

Vue.use(VueEvents)
Vue.component('custom-actions', CustomActions)
Vue.component('filter-bar', FilterBar)

export default {
  components: {
    Vuetable,
    // VuetablePagination,
    VuetablePaginationInfo,
    VuetablePaginationBootstrap
  },
  props: {
    apiUrl: {
      type: String,
      required: true
    },
    fields: {
      type: Array,
      required: true
    },
    sortOrder: {
      type: Array,
      default() {
        return []
      }
    },
    appendParams: {
      type: Object,
      default() {
        return {}
      }
    },
    detailRowComponent: {
      type: String
    }
  },
  data () {
    return {
      css: CssConfig,
    }
  },
  mounted () {
    this.$events.$on('filter-set', eventData => this.onFilterSet(eventData))
    this.$events.$on('filter-reset', e => this.onFilterReset())
  },
  render(h) {
    return h(
      'div',
      {
        class: { container: true }
      },
      [
        h('filter-bar'),
        this.renderVuetable(h),
        this.renderPagination(h)
      ]
    )
  },
  methods: {
    // render related functions
    renderVuetable(h) {
      return h(
        'vuetable',
        {
          ref: 'vuetable',
          props: {
            apiUrl: this.apiUrl,
            fields: this.fields,
            paginationPath: "links.pagination",
            perPage: 10,
            multiSort: false,
            sortOrder: this.sortOrder,
            appendParams: this.appendParams,
            detailRowComponent: this.detailRowComponent,
            css: this.css.table,
          },
          on: {
            'vuetable:cell-clicked': this.onCellClicked,
            'vuetable:pagination-data': this.onPaginationData,
          },
          scopedSlots: this.$vnode.data.scopedSlots
        }
      )
    },
    renderPagination(h) {
      return h(
        'div',
        { class: {'vuetable-pagination': true} },
        [
          h('vuetable-pagination-info',
            { ref: 'paginationInfo', props: { css: this.css.paginationInfo } }),
          h('vuetable-pagination-bootstrap', {
            ref: 'pagination',
            class: { 'pull-right': true },
            props: {
            },
            on: {
              'vuetable-pagination:change-page': this.onChangePage
            }
          })
        ]
      )
    },
    // ------------------
    linkWordEditor (value) {
      return `<span><a href="http://127.0.0.1:5000/adn/word/edit/?id=${value}&url=%2Fadn%2Fword%2F">(edit)</a></span>`
    },
    formatDate (value, fmt = 'YYYY-MM-DD') {
      return (value == null)
        ? ''
        : moment(value, 'YYYY-MM-DD').format(fmt)
    },
    onPaginationData (paginationData) {
      this.$refs.pagination.setPaginationData(paginationData)
      this.$refs.paginationInfo.setPaginationData(paginationData)
    },
    onChangePage (page) {
      this.$refs.vuetable.changePage(page)
    },
    onCellClicked (data, field, event) {
      console.log('cellClicked: ', field.name)
      this.$refs.vuetable.toggleDetailRow(data.id)
    },
    onFilterSet (filterText) {
      this.appendParams.filter = filterText
      Vue.nextTick( () => this.$refs.vuetable.refresh() )
    },
    onFilterReset () {
      delete this.appendParams.filter
      Vue.nextTick( () => this.$refs.vuetable.refresh() )
    }
  }
}
</script>
