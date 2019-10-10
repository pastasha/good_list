<template>
    <div>
        <Title :title="title" />
        <div class="container">
            <div class="row" id="messages">
                <div class="col-4" v-for="item in helpTypes" :key="item.id">
                    <HelpType :message="item.message" :id="item.id" type="want-help" :category="item.category"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Title from '@/components/Title.vue'
import HelpType from '@/components/HelpType.vue'

export default {
    components: {
        Title,
        HelpType
    },
    data() {
        return {
            title: 'Хочу помочь',
            helpTypes: []
        }
    },
    mounted(){
        this.helpTypes=[
            {id:0, message: 'Посадить деревья',category:'tree'}, 
            {id:1, message: 'Купить инвалидную коляску',category:'buy-disabled-carriage'}, 
            {id:2, message: 'Передать детям книги  интернаты',category:'give-books'}, 
            {id:3, message: 'Помоць домам престалрелым',category:'old-houses'},
            {id:4, message: 'ПОмочь с лечением',category:'help-with-therapy'}, 
            {id:5 ,message: 'Стать донором',category:'become-donor'}
        ]
    }
}
</script>