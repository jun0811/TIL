/*
 1. 배열
*/

// 1-1. 기본 사용

const arrayNumbers = [1,2,3,4]
arrayNumbers[0]
console.log(arrayNumbers.length) // 길이

// 1-2. reverse
arrayNumbers.reverse() 

// 1-3 push & pop
arrayNumbers.push('a')
arrayNumbers.pop()

// 1-4. unshift & shift -> 앞에
arrayNumbers.unshift('a')
arrayNumbers.shift()

// 1-5. includes
// 배열에 특정 요소를 검사 -> boolean으로 반환.

arrayNumbers.includes(1)
arrayNumbers.includes(100)

// 1-6. indexof
// 특정인덱스 자리에 값을 출력. 없으면 -1 반환
arrayNumbers.indexOf(1)
arrayNumbers.indexOf(1000)

// 1-7.join 
// 인자를 기준으로 쭉 이어서 문자열로 반환
// 인자가 없다면 콤마를 기준으로 이어준다
arrayNumbers.join()

/**
 * 2. 오프젝트 (객체)
 * key와 value로 구성된 자바스크립트 자료형 중 하나
 * key는 문자열 타입이고 value는 모든 타입이 가능
 */

 const person = { }
 person.name = 'lee'
 const person = {
   name : 'lee',
   samsung : {
    tab : 's7'
   }
 }

 console.log(person.samsung.tab) // 값 불러오기 방법 

// 2-1. Object 축약 문법(ES6+)
const books = ['Eloquent' , 'JS Ninja']

const comics = {
  DC : ['Aquaman', 'Batman'],
  Marvel : ['Avengers', 'IronMan']
}

const bookShop = {
  books,  // books : books,
  comics, // comics : comics
}

// 2-2. 객체 내부의 함수 == 메서드 
const baby = {
  name : 'K',
  // cook : function() {
  //   console.log('HI i K')
  // }, 밑에와 동일
  cook () {
    console.log('HI i K')
  }
}

baby.cook()

// 2-3. Oject Destructing
// - ES6+에서만 사용 가능한 문법
// - 객체에서 일부만 사용하고 싶을 때 유용하다.

const userInformation = {
  name : '연주',
  userId : 'ssafy1234',
  phoneNumber : '010-1234-1234',
  emanil : 'sj@ssafy.com'
}
// - ES5까지
const name = userInformation.name

// - ES6
const {name} = userInformation
const {name, userId, email} = userInformation

// 기존 사용 방식
function getUserInfo(userInformation) {
  console.log(`${userInformation.name}`)
} 

// 실제 사용 방식
const {name, userId, email} = userInformation
function getUserInfo(name, email) {
  console.log(`${name} ${email}`)
}

