<template>
  <vuetable ref="vuetable"
    api-url="https://vuetable.ratiw.net/api/users"
    :fields="['name', 'email', 'birthdate']"
  ></vuetable>
</template>

<script>
import WordTable from '@/components/WordTable'

export default {
  components: {
    Vuetable
  }
}
</script>
