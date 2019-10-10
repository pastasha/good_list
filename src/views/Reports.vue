<template>
    <div>
        <Title :title="title" />
        <div id="news-root">
            <div class="container" v-for="item in reports" :key="item.id">
                <Card :dataObj="item" />
            </div>
        </div>
    </div>
</template>

<script>
import Title from '@/components/Title.vue'
import Card from '@/components/Card.vue'
export default {
    components:{
        Title, Card
    },
    data() {
        return {
            reports: [],
            title: 'Отчетность'
        }
    },
    mounted(){
        this.reports=[
            {title:"В Раздельной открылось окно жизни",imageSrc:require(''), text: "", date: '09/12/2018',id:0},
            {title:"В Раздельной открылось окно жизни",imageSrc:require(''), text: "asdasasdsdadqweqweqwezxcscsxcscsdcscsdcsdcsdccsc", date: '09/12/2018',id:1},
        ]
    }
}
</script>