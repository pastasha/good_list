<template>
    <div>
        
        <Title title="Нужна помощь" />
        <div class="container">
            <div class="row" id="messages">
                <div class="col-4" v-for="item in helpTypes" :key="item.id">
                    <HelpType :message="item.message" :id="item.id" type="need-help" :category="item.category"/>
                </div>
            </div>
            <div class="row justify-content-center mt-5 mb-5">
                <b-button class="col-md-auto" id="need-help-btn">Оформить заявку</b-button>
            </div>
        </div>
    </div>
</template>

<script>

import HelpType from '@/components/HelpType.vue'
import Title from '@/components/Title.vue'

export default {
    components:{
        HelpType,
        Title
    },
    data() {
        return {
            helpTypes: []
        }
    },
    mounted(){
        this.helpTypes=[
            {id:0, message: 'Социальные службы, телефоны доверия, горячие линии',category:'tels'}, 
            {id:1, message: 'Помощь бездомным животным',category:'animals'}, 
            {id:2, message: 'Социальные столовые и раздача еды',category:'food'}, 
            {id:3, message: 'Благотворительные фонды',category:'fonds'},
            {id:4, message: 'Помощь временно перемещенным лицам',category:'moved'}, 
            {id:5 ,message: 'Размещение информации на ресурсе',category:'post-info'}
            
        ]
    }
}
</script>