<template>
    <div class="container text-center" id="title-root">
        <div id="title-span">
            {{title}}
        </div>
    </div>
</template>

<script>
export default {
    props: {
        title:String
    }
}
</script>