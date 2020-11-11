# 1111_Pratice

```vue
# App.vue  
  <div id="app">
    <div id="nav">
      <router-link to='/'>Lunch</router-link>|
      <router-link to='/lotto'>Lotto</router-link>
    </div>
    <router-view/>
  </div>
```



```js
// index.js
import Lunch from '@/components/Lunch.vue'
import Lotto from '@/components/Lotto'

Vue.use(VueRouter)

const routes = [
  {
    path:'/',
    name : 'lunch',
    component: Lunch
  },
  {
    path:'/lotto',
    name : 'lotto',
    component :Lotto
  }

]
```

```vue
// Lotto.vue
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
```

```vue
// Lunch
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
```

