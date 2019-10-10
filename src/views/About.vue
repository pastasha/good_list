<template>
    <div>
        <Title :title="title" />
        <div class="container mt-3">
            <div id="about-content" class="text-center p-5">
                <div v-html="aboutUsText"></div>
                <div class="container">
                    <div class="row">
                        <div class="col-4 col-sm-5 col-xs-5 col-lg-4 col-md-4"  v-for="item in cards" :key="item.id">
                            <Card :dataObj="item" />
                        </div>
                </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import Title from '@/components/Title.vue'
import Card from '@/components/Card.vue'

export default {
    data() {
        return {
            title: 'О нас',
            aboutUsText: '',
            cards:[]
        }
    },
    components:{
        Title, Card
    },
    mounted(){
        this.aboutUsText = '<p><strong>ДРУЗЬЯ ПРОЕКТА</strong> - это десятки тысяч неравнодушных людей, благодаря любой поддержке которых или финансовому участию в наших акциях и проектах мы благоустраиваем мир вокруг нас и делаем его немного добрее - давая надежду, помогая жить и спасая жизни.</p>'
        this.cards=[
            {imageSrc: require('@/assets/images/about/93d865be67359f90d04a7997d58a1923.png'), text:'Описание челика',id:0},
            {imageSrc: require('@/assets/images/about/315bb1980dc199717fc5918fb449d26d.png'), text:'Описание челика',id:1},
            {imageSrc: require('@/assets/images/about/15690988157150s.jpg'), text:'Описание челика',id:2},
            {imageSrc: require('@/assets/images/about/s-l300.jpg'), text:'Описание челика',id:3},
            {imageSrc: require('@/assets/images/about/Shinji_instrumentality1.png'), text:'Описание челика',id:4},
            {imageSrc: require('@/assets/images/about/tumblr_nc8dnsq5Sc1sefquto1_500.jpg'), text:'Описание челика',id:5},
        ]
    }   
}

</script>