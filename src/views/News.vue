<template>
    <div>        
        <Title title="Новостная лента" />
        <div id="news-root">
            <div class="container" v-for="item in news" :key="item.id">
                <Card :dataObj="item" />
            </div>
        </div>
    </div>
</template>

<script>
import Card from '@/components/Card'
import Title from '@/components/Title'

export default {
    name: 'news',
    components: {
        Card,
        Title
    },
    data() {
        return {
            news:[]
        }
    },
    mounted(){
        //Здесь будет получение данных через API, пока просто заполняю руками
        let newItem={
            id: 0,
            title: 'У нас появилось веб-приложение',
            text: 'Веб-приложение — клиент-серверное приложение, в котором клиент взаимодействует с веб-сервером при помощи браузера. Логика веб-приложения распределена между сервером и клиентом, хранение данных осуществляется, преимущественно, на сервере, обмен информацией происходит по сети.',
            imageSrc: require('@/assets/images/newsitem.png'),
            date: '04/10/2019'
        }
        this.news.push(newItem);
        newItem={
            id: 1,
            title: '2 У нас появилось веб-приложение',
            text: '4 Веб-приложение — клиент-серверное приложение, в котором клиент взаимодействует с веб-сервером при помощи браузера. Логика веб-приложения распределена между сервером и клиентом, хранение данных осуществляется, преимущественно, на сервере, обмен информацией происходит по сети.',
            imageSrc: require('@/assets/images/newsitem.png'),
            date: '04/10/2019'
        }
        this.news.push(newItem);
    }
}
</script>
