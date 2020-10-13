# 10/13 practice

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .done{
      text-decoration: line-through;
    }
  </style>
</head>
<body>
  <input type="text" id = "user-input">
  <button id ='submit-button'>Add</button>
  <ul id ="todo-list">

  </ul>

  <script>
    /*
      1. 할일추가
        - 값을 입력하고 버튼을 누르면 li로 추가
        - 버튼을 만들고, 버튼에 이벤트를 달아주자!
        - 어떤 이벤트? 클릭 이벤트
      2. 할 일 삭제 기능
      3. 취소선 추가 및 제거 
      
    */ 
function addTodoItem() {
  // console.log('here')
  // 1-3. 입력값을 가져온다.
  const userInput = document.querySelector('#user-input')
  const userInputValue = userInput.value
  // console.log(userInputValue) 
  
  // 1-4. 사용자가 입력한 값을 화면에 넣어준다.
  const newli = document.createElement('li')
  // console.log(newli)

  // 개별 선택을 위한 코드
  const newTodoText =document.createElement('span')
  newTodoText.innerText = userInputValue
  
  // 이벤트 발생 취소선
  newTodoText.addEventListener('click', function(event){
    event.target.classList.toggle('done')
  })
  newli.appendChild(newTodoText)

  // 2. 삭제기능
  // 2-1. 삭제 버튼을 만든다.
  const deleteBtn = document.createElement('button') 
  deleteBtn.innerText = 'X'
  // 2-2. 이벤트 발생시 결과
  deleteBtn.addEventListener('click', () => newli.remove())
 

  //////////////////////////////////////////////////////////
  const todoList = document.querySelector('#todo-list')
  todoList.appendChild(newli)
  newli.appendChild(updateBtn)
  newli.appendChild(deleteBtn)

}

    // 1-1. 이벤트를 달아줄 버튼
    const submitButton = document.querySelector('#submit-button')
    // 1-2. 이벤트를 달아주고 이후 실행할 함수 정의
    submitButton.addEventListener('click', addTodoItem)
  </script>
</body>
</html>
```

