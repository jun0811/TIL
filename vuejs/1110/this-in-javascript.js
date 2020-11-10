// this 1. this가 아닌것

const sayhello = function sayhello(){
    console.log(this)
}
sayhello()

const sayBye = () => console.log(this)

sayBye() // 윈도우


/* 
    2. 'this'가 with Functions & Objects
*/



const me = {
    name :'lee', 
    // this는 자신이 속한 객체를 가리킨다.
    sayThis : function() {
        console.log(this)
    },
}

/*
    3. 'This' with Arrow Functions
    - 화살표 함수는 'this'가 없다
*/
const me = {
    name :'lee'
    , sayThis : () => console.log(this)
} // 화살표 함수는 this의 의미 x

const sayBye2 = () => console.log(this)

const you = {
    name : "kim"
}

you.sayBye2 = sayBye2
