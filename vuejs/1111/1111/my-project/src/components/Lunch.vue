<template>
  <div>
    <h2>Lunch</h2>
    <p>{{menu}}</p>
    <button @click="onePick">메뉴@</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data(){
    return {
      menuList : ['커피','국밥','피자','치킨'],
      menu : ''
    }
  },
  methods: {
    onePick(){
      const randomIdx = _.random(0,this.menuList.length-1)
      this.menu = this.menuList[randomIdx]
    }
  }
}
</script>

<style>

</style>