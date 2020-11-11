<template>
<div>
  <h1>Lotto</h1>
  <p>{{nums}}</p>
  <button @click="pickNums">행운이~</button>

</div>
</template>

<script>
import _ from 'lodash'
export default {
  name : 'Lotto',
  data(){
    return {
      numlist : _.range(1,46),
      nums : ''
    }
  },
  methods :{
    pickNums(){
      this.nums = _.sampleSize(this.numlist,6)
    }
  }
}
</script>

<style>

</style>