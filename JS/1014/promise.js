console.log('hello ssafy!')

setTimeout(()=> {
  console.log('LEE')
},1000)

console.log("4기")

// Promise

const promise = new Promise( (resolve, reject) => {
  setTimeout(()=> {
    resolve('1초 뒤~') // 1초뒤에 내가 하고 싶은 일!
  },1000)
  
  reject()
}) 

promise
  .then(value => {
    console.log('hello ssafy')
    console.log(value)
    console.log('bye ssafy')
  }) //resolve()가 실행됐을 때
  .catch() // reject()가 실행됐을 때 

console.log('jjj')


// fetch

const res = fetch('https://jsonplaceholder.typicode.com/') // requests.get()
  .then(res => {
    console.log(res)
  })
  .catch()
// axios  중요 !!!!!!!!!!!
axios.get('https://jsonplaceholder.typicode.com/')
.then(res => {
  console.log(res)
})
.catch(err => {
  console.error(err)
  // 대응책 코드
})
