const nickName = 'LEE'

switch (nickName) {
  case 'LEE': {
    console.log('Hi')
    break // 필수 
  }
  case 'KIM': {
    console.log('Nope')
    break
  }
  default: {
    console.log('어떤 조건도 아닐때')
  }
}



/*
 2. 반복문
 - while
 - for
 - for of (주로 배열 또는 문자열에 사용 )
 - for in
*/

let whileIdx = 0

while (whileIdx <6){
  console.log(whileIdx)
  whileIdx ++ 
}

// 2-2 for
for (let i =0; i<6; i++) {
  console.log(i)
}

// 2-3. for of (주로 배열 또는 문자열에 사용 )
const arrayNums = [1,2,3,4,5]
for (const number of arrayNums) { 
  // 하나하나씩 출력.
  console.log(number)
}
// 2-4. for in 주로 오브젝트에 사용
const fruits = {
  apple : 'apple',
  banana : 'banana'
}
// 접근 방법
fruits.apple 
fruits['apple']

for (const key in fruits){
  console.log(key)
  console.log(fruits[key])
}
