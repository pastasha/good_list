<template>
  <div class="home-root">
    <div :style="{'background':'url('+require('@/assets/images/main.png')+')','background-size':'cover'}" id="mainDiv" class="d-inline-flex align-items-center flex-column justify-content-center">
      <div id="title" class="m-4">{{title}}</div>
      <div id="text" class="container align-center m-4" >{{text}}</div>
      <div class="align-items-center m-4"><b-button id="make-request-btn" to="/">Подать заявку</b-button></div>  
    </div>
    <Header />
    <div id="rules">

    </div>
  </div>
</template>

<script>

import Header from '@/components/Header.vue'

export default {
  name: 'home',
  data() {
    return {
      title: 'дворики одессы',
      text: 'Ежегодный конкурсный проект среди одесских дворов, которые своими силами украшают их жители. Чтобы подать заявку на участие в конкурсе, присылается фото двора до благоустройства/реконструкции/ремонта, а затем после проделанной работы вместе с кратким описанием всех усовершенствований'
    }
  },
  components: {
    Header,
  }
}
</script>
