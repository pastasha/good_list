<template>
    <div>
        <Title :title="title" />
        <div class="container">
            <div id="request-form">
                <form class="p-3">
                    <b-form-group>
                        <div class="d-flex justify-content-around">
                            <b-form-radio v-model="requestType" name="request-radio" value="phys">физ лицо</b-form-radio>
                            <b-form-radio v-model="requestType" name="request-radio" value="urid">юр лицо</b-form-radio>
                        </div>
                    </b-form-group>
                </form>
                <form class="p-3" v-if="requestType=='phys'">
                    <b-form-group>
                        <div class="d-flex justify-content-center">                            
                            <span>Фио: </span>
                            <b-form-input v-model="phys.name" placeholder="Ваше фио"></b-form-input>
                        </div>
                    </b-form-group>
                    <b-form-group>
                        <div class="d-flex justify-content-center">                            
                            <span>email: </span>
                            <b-form-input v-model="phys.email" placeholder="Ваш email" type="email"></b-form-input>
                        </div>
                    </b-form-group>
                    <b-form-group>
                        <div class="d-flex justify-content-center">                            
                            <span>Дата рождения:</span>
                            <Datepicker v-model="phys.bdate"/>
                        </div>
                    </b-form-group>
                </form>
            </div>
        </div>
    </div>
</template>

<script>

import Title from '@/components/Title.vue'
import Datepicker from 'vuejs-datepicker'
export default {
    data() {
        return {
            title: 'Оформить заявку',
            requestType: "phys",
            phys:{
                name: '',
                email: '',
                bdate: null
            }
        }
    },
    components:{
        Title,
        Datepicker
    }
}
</script>