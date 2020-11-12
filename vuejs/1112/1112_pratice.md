# 1112_pratice

### App.vue

```html
<template>
  <div id="app">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>Cat Image</h1>
    <img :src="cat" alt="">
    <br>
    
    <button @click="putBtn">Get Cat</button>
  </div>
```

```vue
<script>
import axios from 'axios'
// axios 설치 후 import
    
export default {
  name: 'App',
  updated(){ // life cycle -> updated
    console.log(this.cat)
  },
  created(){ // life cycle -> created
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
```

