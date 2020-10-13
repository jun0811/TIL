// 함수 

/* 
  1. 함수 선언식, 표현식
  - 선언식 (statement, declaration)
  - 표현식 (expression)
*/

// 1-1 함수 선언식
//  - 함수를 별도의 변수에 저장하지 않는다
//  - 반드시 이름이 필요

function add(num1,num2){
  return num1 + num2
}

add(2,3)

// 1-2. 함수 표현식
// - 함수를 변수에 저장하여 사용
// - 함수 이름이 있어도 되고 없어도 된다 (하지만, 이름은 지워주자)
// - 이름이 있으면 콜스텍에 쌓이므로 디버깅시 유용
// - 이름이 없는 함수는 콜스택에 익명함수라고 뜬다!
const sub = function sub(num1, num2) {
  return num1- num2
}

sub(7,2) // 5

// 1-3. 기본인자 설정
const greeting = function greetPolitely(name) {
  return `hello, ${name}`
}

greeting('승준')

// 1-4. IIFE(Immediately Invoked Function Expression)
// - 정말 참고만 할 것
(function callRightAway(){
  return '나는 바로 실행되지!'
}()) // 바로 실행  -> 바깥에 소괄호 필수

// 선언식은 hosting이 발생하고 정상적으로 동작
// 표현식은 hoisting시 에러가 발생

newAdd(2,7)
function newAdd(num1,num2){
  // 쌉가능
}

//  1-6 Arrow Func
//  키워드와 중괄호를 줄이기 위한 문법
//  매개변수가 단 하나라면 소괄호 생략가능
//  화살표 함수는 바디에 표현식이 딱 한 줄이라면 중괄호와 리턴도 생략가능

const arrowFunc = function arrowFunc(name) {
  return `hello ${name}`
}

// 1-6-1. func 키워드 삭제
const arrowFunc = (name) => {
  return `hello! ${name}`
}

// 1-6-2 소괄호 생략  ( 매개변수가 한개일 때만 )
const arrowFunc = name => {
  return `hello! ${name}`
}

// 1-6-3 중괄호와 return 생략 가능 (단, 바디에 표현식이 하나일 경우)
const arrowFunc =name => `hello! ${name}`


const myArrowFunc = (name,age) => `hello ${name} ${age}`

