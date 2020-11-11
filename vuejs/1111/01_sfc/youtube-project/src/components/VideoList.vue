<template>
  <div>
    <ul>
      <li v-for="(video,idx) in videos" :key="idx">
          {{video.snippet.title}}

      </li>
    </ul>
  </div>
</template>

<script>


export default {
  name: 'VideoList', 
  components: {

  },
  props: {
    videos: Array,
  },
}
</script>