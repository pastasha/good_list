<template>
  <div id="app">
    <Header v-if="this.$route.name!='home'" />
    <router-view/>
    <Footer />
  </div>
</template>

<script>

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  components: {
    Header,
    Footer
  }
}
</script>

