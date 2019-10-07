<template>
    <b-card class="news-item">
        <b-card-text class="news-item-title text-center mb-1">
            {{title}}
        </b-card-text>
        <b-card-text class="news-item-date text-center">
            {{date}}
        </b-card-text>
        <b-card-img :src="imageSrc" class="news-item-img" />     
        <b-card-text class="mt-3 text-center">
            {{text}}
        </b-card-text>
    </b-card>            
</template>

<script>

export default {
    props:{
        dataObj: Object
    },
    computed:{
        imageSrc(){
            return this.dataObj.imageSrc
        },
        title(){
            return this.dataObj.title
        },
        text(){
            return this.dataObj.text
        },
        date(){
            return this.dataObj.date
        }
    }
}
</script>