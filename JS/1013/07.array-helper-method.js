// Array Helper Method 

/**
 * 배열에 대해 자주 사용하는 로직을 재활용할 수 있게 만든 일종의 메서드 집합.
 */
// 여기서 기술하는것은 오직 배열에만 ...
//  1. forEach 
// 
const colors = ['red', 'blue', 'green']
colors.forEach(function (element){
  console.log(element)
  // console.log(idx)
})

// 2. map
// - 배열 내의 모든 요소에 대해 주어진 callback 함수를 실행.
// - 함수의 반환값을 요소로 하는 '새로운 배열'을 만든다.

const numbers = [1,2,3]
const doubleNumbers = numbers.map(function (number) {
  return 2*number
})
console.log(doubleNumbers) //[2,4,6]

// 3. filter
// - 주어진 callback 함수의 "테스트"를 통과하는 모든 요소를 모아,
// "새로운 배열"을 만든다
// - 다시 말해, return 구문이 true인 경우만 반환

const products = [
  {name: 'cucumber' ,type : 'vegetable'},
  {name: 'banana' ,type : 'fruit'},
  {name: 'carrot' ,type : 'vegetable'},
]

const fruits = products.filter(element => element.type == 'fruit' )

console.log(fruits)

// 4. reduce 
// - arr.reduce(callback(acc, element) ,initialValue)
// - 배열의 각 요소에 대해 주어진 reduce 함수를 실행하고, "하나의 값"을 반환
// - 숫자의 총합, 평균 등을 계산하기 위해 사용
const numbers = [90,90,80,7]
const sum = numbers.reduce(function(acc, element) {
  return acc + element
}, 0) // acc =0  <= 첫번째 인자로 계속 들어간다.
// 0 + 90 = 90 
// 90 + 90 = 180 
// 180 + 80 =260  .... 축적..

// 5.find
// -주어진 반별함수를 만족하는 "첫번째 요소의 값" 반환
const avengers= [
  {name : 'Tony', age : 42},
  {name : 'Steve', age : 32},
  {name : 'Thor', age : 112}
]
const ironman = avengers.find( avenger => avenger.name =='Tony')
console.log(ironman)

// 6. some
// - 어떤 요소라도 주어진 판별함수를 통과한다면 t /f 를 반환
const arr = [1,2,3,4,5]
const odd = arr.some(element => element%2 == 0)
console.log(odd)

// 7. every 
// - 모든 요소가 판별함수 통과여부
const odd = arr.every(element => element%2 == 0)



// 연습 1) filter 
const numbers = [15, 25, 35, 45, 55, 65, 75, 85, 95]
// 배열에서 50보다 큰 값만 filteredNumbers를 만드세요
const filteredNumbers = numbers.filter(element => element > 50)
console.log(filteredNumbers)

// 연습 2) reduce
// 주어진 url 문자열 뒤에 필수 요청 변수인 api의 key - value
// 'key = value' 의 형태로 더하여 요청 url을 만들어 주세요
const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
const api = {
  key : 'API_KEY',
  targetDt : '20201013'
}
const newApi = []
// 오브젝트 순회
for (const key in api){
  newApi.push([key, api[key]])
}
console.log(newApi)

newApi.reduce(function(acc,element){
  return acc + `${element[0]}=${element[1]}&`
}, baseUrl)

// 연습 3) reduce
const names = ['김소정', '조현지', '곽온겸', '김동욱', '전국현', '조현지', '김동욱']
// 배열에 담긴 이름을 {'이름' : 출현수 } 형태의 Object로 반환하세요.
const count = names.reduce((acc, element) =>{
  acc[element] = (acc[element] || 0 ) + 1
  return acc
},{})

console.log(count)


// 연습 4) find
const people = [
  { id: 1, admin: false },
  { id: 2, admin: false },
  { id: 3, admin: true },
]
// 관리자인 사람을 찾아서 배열에 담기
const a = people.find(element => element.admin == true)
console.log(a)