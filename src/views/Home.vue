<template>
  <div class="home-root">
    <vue-headful
      title="Title from vue-headful"
      description="Description from vue-headful"
    />
    <div id="home-start">
      <img src="@/assets/images/path5445.png" id="home-start-img" v-bind:class="{'img-blur' : hovered}" />
      <p class="hover-text text-center" v-html="hoverText" v-if="hovered"></p>
      <div id="home-buttons" class="flex-column float-left">
        <div class="btn-wrapper">
          <b-button squared class="home-btn" to="/want-help" @mouseover="butHover()" @mouseleave="butNoHover">Хочу помочь</b-button>
        </div>
        <div class="btn-wrapper">
          <b-button squared class="home-btn" to="/need-help" @mouseover="butHover()" @mouseleave="butNoHover">Нужна помощь</b-button>
        </div>
      </div>
    </div>
    <Header />
    <div class="home-main container justify-content-center">
      <div class="text-center mt-5" id="home-main-title">ПЛАТФОРМА ДОБРОЕ ДЕЛО В ОДЕССЕ</div>
      <div class="text-center mt-5">
        Уже много лет одесситы с помощью платформы "Доброе дело"  озеленяют и благоустраивают свой город!
        Помогают продуктами, одеждой, техникой, лекарствами, реанимационным оборудованием... Помогают жить и спасают жизни!
        Все они не политики, а обычные жители своего города, которые верят, что для того, чтобы что-то изменилось, надо не говорить, а делать.
      </div>
    </div>
  </div>
</template>

<script>

import Header from '@/components/Header.vue'

export default {
  name: 'home',
  data() {
    return {
      hoverText:`
          Уже много лет одесситы с помощью платформы «Доброе Дело» озеленяют и благоустраивают город! 
          Помогают продуктами, одеждой, техникой, лекарствами, реанимационным оборудованием… 
          Помогают жить и спасают жизни! Все они не политики, а обычные жители своего города, которые верят, что для того, чтобы вокруг что-то изменилось, надо не говорить, а делать, не разрушать, а созидать!
        `,
      hovered: false,
    }
  },
  methods:{
    butHover(){
      this.hovered=true
    },
    butNoHover(){
      this.hovered=false
    }
  },
  components: {
    Header,
  }
}
</script>
