# 1111_Workshop



### 1.  App.vue

```vue
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
```



### 2. Child.vue

```vue
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
```



### 3. Parent.vue

```vue
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
```

