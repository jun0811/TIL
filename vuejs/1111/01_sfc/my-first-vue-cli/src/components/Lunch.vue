<template>
  <div>
    <!-- template는 최상의 태그가 하나 잇어야한다. 같은 레벨의 tag 생성 x -->
    <!-- 
1. 컴포넌트 이름부터 지어줄 것
2. data는 반드시 retrun이 있는 함수로 작성할 것...
     -->
    <h1>Lunch!</h1>
    <p>{{menu}}</p>
    <button @click= "pick"> 추천</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name : 'Lunch',
  data (){ // data : function(){ }
    return {
      menuList : ['커피', '파스타', '국밥'],
      menu : ''
    }
  },
  methods:{
    pick(){
       {
        const randomIndex = _.random(0, this.menuList.length-1)
        this.menu = this.menuList[randomIndex]
      }
    }
  }
}
</script>

<style>

</style>