

# 1110_workshop



### 1. computed를 통해 상태별로 todo list를 계산하고 표시

![](1110_workshop.assets/1.PNG)

![](1110_workshop.assets/2.PNG)



```html
...
<div id='app'>
    <select v-model='apt'>
      <!-- on event -->
      <option value="all">전체</option>
      <option value="ing">진행중</option>
      <option value="completed">완료</option>
    </select>
    <input type="text" v-model="userInput" @keydown.enter="addTodo">
    <button @click='addBtn'>+</button>
    <br>
    ....
</div>
....
      const app = new Vue({
        el: '#app',
        data: {
          userInput: "",
          apt :'all', 
          list: [], //
        },
        computed : {
          aptlist() {
            if (this.apt==='completed'){
              return this.list.filter( todo => {
                return todo.isCompleted
              })
            } else if(this.apt ==='ing'){
              return this.list.filter(todo=>{
                return !todo.isCompleted
              })
            } else {
              return this.list
            }
          },
        },
....
```





### 2. Local Stroage

![](1110_workshop.assets/3.PNG)

```js
const TODO_STORAGE_KEY = 'TODO_STORAGE_KEY'
      const todoStorage = {
        fetch(){
          const listJson = localStorage.getItem(TODO_STORAGE_KEY)
          return JSON.parse(listJson)
        },
        save(list){
          const listJson = JSON.stringify(list)
          localStorage.setItem(TODO_STORAGE_KEY,listJson)
        },
      }
      
      ...
       methods: {
           ......
           
      watch : {
          list: {
            handler(newV,oldV){
              todoStorage.save(newV)
            },
            deep : true,
          },
        },
        created(){
          this.list = todoStorage.fetch() || []
        },
      })
      
```

