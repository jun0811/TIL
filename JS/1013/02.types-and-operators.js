// 타입과 연산자

/*
 1. 원시자료형
 - JS 전체 자료형은 7가지 (우리는 6가지...)
 - 원시 자료형은 이 중에서 객체와 심볼을 제외한 것들을 말한다.
*/

// 1-1 Number
const numberA = 13
const numberB = -5
const numberC = 3.14
const numberD = 2.998e6

const numberE = Infinity
const numberE = -Infinity
const numberE = NaN // Not a Number
typeof(NaN)

const sentenceOne = 'Hello!'
const sentencetwo = "hello!"
const sentenceThree = sentenceOne + sentencetwo 

const greeting = '안녕'
const yourName = 'ssafy'

const Message =`${greeting} + ${yourName}`

const isTrue =true 

// 1-4 undefined

let firstName 
console.log(firstName)

// 1-5. null
// 개발자의 의도가 있음
let lastName = null 

//  - 둘의 타입에는 함정이 존재
typeof(5) //number
typeof(null) // object(?)

// 연산자
let changeMe = 0
changeMe ++ // 가능

// 문자열은 소문자가 대문자보다 큰값, 알파벳은 오름차순으로 비교

// 논리 연산자
// && (and)
// || (or)
//  ! (not)

true ? 1: 2 // 1
true ? 1 : 2 // 2 
const result = Math.PI > 4 ? 'Yes' : 'Nope'

