# 1110 pratice

```html
<!-- https://kr.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
  <style>
    .cat{
      height: 500px;
      width: auto;
    }
  </style>
<body>
  <h2>Cat Image</h2>
  <div id ='app'>
    <img class = "cat" v-bind:src="cat" alt="">
    <br>
    <button @click ='pushBut'>Get Cat</button>
  </div>

  <script src= "https://cdn.jsdelivr.net/npm/lodash@4.17.20/lodash.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

  <script>
    const app = new Vue({
      el : '#app',
      data: {
          cat : '',
      },
      methods : {

        pushBut : function(){
          // this.cat = 'giphy.gif'
          axios.get('https://api.thecatapi.com/v1/images/search')
          //메소드 함수안에서는 에로우 펑션을 써야한다. 
          .then(res =>{
            // console.log(res.data[0].url)
            const a = res.data[0].url
            this.cat = 'giphy.gif'
            setTimeout(() => {
                console.log(this.cat)
                this.cat = a
              }, 1);
              
            })
            
            .catch(function (err) {
              console.log(err)
          })
        }
      }
    })

  </script>
</body>
</html>
```

