<template>
  <div>
    <h1>Child</h1>
    <input type="text" @input="onInputUser">
    <p>appData:{{appData}}</p>
    <p>parentData:{{parentData}}</p>
  </div>
</template>

<script>


export default {
  name: 'Child',
  props:{
    appData: String,
    parentData:String,
  },
  data(){
    return{
      childData:'',
    }
  },
  methods :{
    onInputUser(e){
      this.childData = e.target.value
      this.$emit('child-data',this.childData)
  }
  }
}
</script>

<style>

</style>