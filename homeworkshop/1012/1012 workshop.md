# 10/12 workshop

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TODO</title>
</head>
<body>
  <input type="text">     <!-- 입력을 받을 input -->
  <button>Add</button>    <!-- 클릭 시 todo item을 추가해주는 버튼 -->
  <ul>                    <!-- 순서 없는 list (Unordered List) -->
    <li>Item 1</li>       <!-- Todo Item 1 -->
    <li>Item 2</li>       <!-- Todo Item 2 -->
  </ul>

  <script>
    function addTodo () {
      // input 요소를 선택하고, value 값을 꺼낸다.
      const inputText = document.querySelector('input')
      text = inputText.value
      // 새로운 li 요소를 생성하고, input value를 innerText로 넣는다.
      const newli = document.createElement('li')
      newli.innerText = text
      // ul 요소를 선택하고, li 요소를 자식요소로 추가한다.
      const ul = document.querySelector('ul')
      ul.appendChild(newli)
      // input 요소의 value 값을 초기화한다.
      inputText.value = ''
    }

    // button 요소를 선택하고, 클릭되었을 때 addTodo 함수를 실행한다.
    const button = document.querySelector('button')
    button.addEventListener('click', addTodo)
  </script>
</body>
</html>

```

