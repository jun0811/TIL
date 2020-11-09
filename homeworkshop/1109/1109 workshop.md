# 1109 workshop

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lunch & Lotto</title>
</head>
<body>
  <div id = 'app'>
    <h2>점심 메뉴</h2>
    <button @click='onePick'> pick one</button>
    <p v-model="result1">{{result1[0]}}</p>
  </div>

  <hr>
  <div id ='lotto'>
    <h2>로또</h2>
    <button @click = 'onPick'>Get lucky</button>
    <p v-model="result2">{{result2}}</p>
  </div>

  <script src= "https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

  <script>
    const app = new Vue ({
      el : '#app',
      data: {
        menu : ['피자', '국밥', '라면', '만두'],
        result1 : "",
      },
      methods : {
        onPick : function(){
          this.result1 = _.sampleSize(this.menu,1)
          // console.log(result1)
        },
      }
    })

    const lotto = new Vue ({
      el : '#lotto',
      data :{
        numbers : _.range(1,46),
        result2 : " "
      },
      
    methods : {
      onePick: function(){
        this.result2 = _.sampleSize(this.numbers,6)
      } 
    }
    })
  </script>
</body>
</html>
```

