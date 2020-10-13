// JSON 
/**
 * "key : value" 형태로 자바스크립트의 객체와 유사하게 생겼다.
 * JSON은 문자열 타입이다! 
 * 객체로 사용하기 위해서 구문 분석(파싱)이 필요하다.
 * JSON 형식의 파일을 다루기 위해 JS에서는 JSON 내장 객체를 제공
 */

//  Object -> json
const noJSON = {
  coffee : 'blue bottle',
  iceCream : 'mint choco'
}

typeof(noJSON) // object

const yJSON = JSON.stringify(noJSON)
console.log(yJSON)
console.log(typeof(yJSON)) // JSON(String)

// JSON (stirng) => Object
const parsedData = JSON.parse(yJSON)
console.log(parsedData)
console.log(typeof(parsedData))