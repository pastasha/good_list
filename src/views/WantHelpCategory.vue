<template>
    <div>
        <Title :title="title"/>
        <div class="container">
            <Card :dataObj="data"/>
        </div>
    </div>
</template>

<script>
import Title from '@/components/Title.vue'
import Card from '@/components/Card.vue'

export default {
    data() {
        return {
            data:{
                title:'',
                text:'',
                imageSrc:''
            },
            title: ''
        }
    },
    components:{
        Title, Card
    },
    mounted(){
        this.title = 'Посадить деревья'
        this.data.imageSrc = require('@/assets/images/tree.png')
        // this.data.imageSrc = require(this.data.imageSrc);

        //пример получения данных с API
        fetch('https://baconipsum.com/api/?type=all-meat&paras=2&start-with-lorem=1',{
            method:'get'
        })
        .then((response)=>{
            return response.json();
        })
        .then((jsonData)=>{
            this.data.text=jsonData[0];
        })
    }
}
</script>