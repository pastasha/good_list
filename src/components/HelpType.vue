<template>
    <router-link :to="link">
        <b-button class="help-type-root mt-3 text-center">
            {{message}}
        </b-button>
    </router-link>
</template>

<script>
export default {
    props:{
        'message': String, 'id': Number, 'category': String, 'type': String
    },
    computed:{
        link(){
            return '/' + this.type + '/' + this.category
        }
    }
}
</script>