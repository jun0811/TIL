<template>
  <div>
    <h1>Parent</h1>
    <input type="text" @input="onUserInput">
    <!-- {{appData}} -->
    <p>AppData: {{appData}}</p>
    <p>childData:{{childData}}</p>
    <Child :appData="appData" :parentData="parentData" @child-data="getChild"/>
  </div>
</template>

<script>
import Child from '@/components/Child'

export default {
  name: 'Parent',
  components:{
    Child,
  },
  props : {
    appData : String, // string, Object,Number....etc  
  },
  data(){
    return {
      parentData : '',
      childData : '',
    }
  },
  methods:{
    onUserInput(e){
      this.parentData = e.target.value
      this.$emit('parent-data',this.parentData)
    },
    getChild(childData){
      // 자식에서 emit 발동시, 자동으로 호출 
      // console.log('자식에서 먼가 있다...!')
      this.childData = childData
      this.$emit('child-data',this.childData)
    },
  }
}
</script>

<style>

</style>