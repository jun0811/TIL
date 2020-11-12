<template>
  <div id="app">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>Cat Image</h1>
    <img :src="cat" alt="cat Img">
    <br>
    
    <button @click="putBtn">Get Cat</button>
  </div>
</template>
<script>
// import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'
export default {
  name: 'App',
  updated(){
    console.log(this.cat)
  },
  created(){
    axios.get('https://api.thecatapi.com/v1/images/search')
      .then(res=>{
        const b = res.data[0].url
        // console.log(b)
        this.cat = b
      })
  }
  ,
  components: {
    // HelloWorld
  },
  data () {
    return { 
      cat : ''
    }
  },
  methods :{
    putBtn: function(){
      axios.get('https://api.thecatapi.com/v1/images/search')
      .then(res=>{
        const b = res.data[0].url
        // console.log(b)
        this.cat = b
      })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
img{
  width: 500px;
  height: auto;
}
</style>
