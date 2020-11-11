<template>
  <div id="app">
    <div id="nav">
      <router-link to="/lunch">Lunch</router-link> |
      <router-link to="/lotto">Lotto</router-link>
    </div>
    <!-- router view 자체는 아무것도 화면에 보여지진 않지만 경로에 따라 보여줄 컴포넌트를 설정하겟다고
    설정 한것 -->
    <router-view/>
    <!-- workshop code -->
    <h1>App</h1>
    <input type="text" @input="onUserInput">
    {{appData}}
    <p>parentData:{{parentData}}</p>
    <p>childData:{{childData}}</p>
    <Parent :appData="appData" @parent-data='getParent' @child-data='getChild'/> 
    <!-- 자식 한테 보여줄 데이터  -->
  </div>
</template>

<script>
import Parent from '@/components/Parent.vue'

export default {
  name: 'App',
  created:function(){
    console.log('created!')
  },
  components:{
    Parent,
  },
  data(){
    return {
      appData: '',
      childData : '',
      parentData: '',
    }
  },
  methods: {
    onUserInput(e){
      this.appData = e.target.value
    },
    getChild(childData){
      this.childData = childData
    },
    getParent(parentData){
      this.parentData = parentData
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
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
