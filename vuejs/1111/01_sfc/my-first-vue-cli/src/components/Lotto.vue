<template>
  <div>
    <h1>Lotto</h1>
    <p>{{result}}</p>
    <button @click="pick">돌려</button>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'Lotto',
  data(){
    return {
      numList : _.range(1,46),
      result : ''
    }
  },
  methods : {
    pick(){
      this.result = _.sampleSize(this.numList,6)
    }
  }
}
</script>

<style>

</style>