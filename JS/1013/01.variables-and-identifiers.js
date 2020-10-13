// 변수와 식별자
/*
  1. 식별자
  - 반드시 !! 문자, $, 또는 밑줄로 시작해야한다. 그 이후에는 숫자가 가능
  - 대소문자 구분하며, 클래스명 외에는 모두 대문자로 시작하지 않는다.
*/

// 1-1. 식별자 작성 스탕리(camelCase)
// 숫자, 문자, 불린
let dog
let variableName 

// 배열(array)
const cats = []

// 정규표현식 (변수명이 r로 시작해야한다)
// const rDesc  = /.*/

// 함수 
const func = function(params) {
  return params
}

// 이벤트 핸들러
function onClick() { }
function onKeyDown() { }

// boolean
let isReady = false

// 1-2. 식별자 작성 스타일(PascalCase)
// 클래스 작성
class User{
  constructor(options){
    this.name = options.name
  }
}

const person = new User({
  name: "홍길동"
})

// 1-3. 스네이크 케이스
const API_KEY = 'SOME....'

/*
  2. 변수, 키워드, 그리고 스코프
  - let
  - const
  - 전역 , 블록 스코프 
*/

// 2-1. let : 값을 재할당 가능한 변수
let x = 1
x =3 

let x = 3 // Error! 재선언은 불가능,.... (단, 크롬환경에서는 가능)
// 2-2. const : 상수 선언
const seven = 7
seven = 10 // Error!

const constNums = [1,2]
constNums.push(5)

// 2-3. 블록 스코프 
// - 조건문 또는 반복문 에서 사용되는 중괄호({}) 내부를 가리킨다. 
// - let 과 const는 블록 스코프다! 블록 스코프! 블록 스코프!
let scopedX = 1

if (scopeX == 1){
  let scopedX = 5
  console.log(scopedX) // 5
}

console.log(scopedX) // 1

// 2-4. var : ES6 이전 키워드
//  - 예기치 않은 문제를 발생시키므로 절대 사용하지 않는다.
var num = 1
var num = 2 // 재선언, 재할당이 가능

// - 블록 스코프 아닌 전역 또는 함수 스코프를 가진다. 중괄호({})에 갇혀있지 않다.
var functionScopeX = 1
let blcokScopedX = 1

if (functionScopeX == 1) {
  var functionScopeX = 100
  let blcokScopedX = 200
  
  console.log(functionScopeX) //100
  console.log(blcokScopedX) // 200
}
 
console.log(functionScopeX) // 100 
console.log(blcokScopedX) // 1

// 2-5. Hoistiong
// - var로 선언된 변수는 "선언 이전"에 참조 될 수 있다.
// - 마치 변수가 위로 끌어올려지는(hoisted)것처럼 보여서 호이스팅이라고 부른더
console.log(Myname)
var Myname = 'eric'

// - let도 호스팅이 일어나지만 에러가 발생

//  2-6. var vs. let/const (선언 및 할당과정)
// var
// 1. 선언 + 초기화 (undefined) 동시 진행

// let & const
// 1. 선언
// 2. TDZ (Temporal Dead Zone) - 변수에 접근하는 시점
// 3. 초기화
// 4. 할당

// 결론
// - 무조건 let, const 쓰되, var 동작 방식도 이해해두자.
// - var 특성과 hoistiong의 개념을 알아둘 것

// - 각 키워드의 특성과 스코프의 차이를 명확히 알아두자.

// window 객체 == 글로벌 객체
// - 브라우저 상에서 JS를 사용할 때 전역 변수 (or 객체들)을 관장하는 객체.
window.myGlobalVar = "어디서든 사용 가능하지"

function greedyFunc(){
  console.log(myGlobalVar)
}

console.log(myGlobalVar)