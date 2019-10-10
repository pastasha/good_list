<template>
  <div id="app">
    <Header v-if="!IsHome" />
    <router-view />
    <Footer/>
  </div>
</template>

<script>

import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import Title from '@/components/Title.vue'
export default {
  components: {
    Header,
    Footer,
  },
  computed:{
    PageTitle:function(){
      return this.titles[this.$route.name];
    },
    IsHome:function(){
      return this.$route.name=='home'
    },
    TitleDefined:function(){
      return this.titles[this.$route.name];
    }
  },
  mounted(){
  }
}
</script>

