# 10/12 pratice

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Health Survey</title>
  <style>
    /* body background color */
    #main {
      background-color: rgba(197, 255, 251)
    }

    /* 중앙 정렬 */
    .box-container {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    /* 박스 별 테두리 */
    .box-item {
      margin: 20px;
      padding: 30px;
      border-radius: 10px;
      width: 600px;
      background-color: white;
    }

    /* 버튼 텍스트 변경 및 스타일링 */
    .button {
      background-color: rgba(45, 166, 153);
      border-radius: 4px;
      color: white;
      padding: 10px 20px;
      margin: 20px;
      cursor: pointer;
      font-size: 15px;
    }

    /* footer */
    .footer {
      margin-top: 3vh;
      margin-bottom: 3vh;
    }
  </style>
</head>
<body>
  <nav>
    <a href="https://www.ssafy.com">
      <img id = "ssafy-image" src="ssafy.png" alt="싸피 이미지" width="300px">
    </a>
  </nav>

  <header>
    <h1>SSAFY 4기 학생 건강설문</h1>
  </header>

  <section>
    <form action="#" method="GET">
      <div id = "input__name">
        <label for="name">이름을 기재해주세요.</label><br>
        <input type="text" id="name" placeholder="실명을 작성해주세요." >
      </div>

      <div id = "input__region">
        <label for="region">지역을 선택해주세요.</label>
        <select name="region" id="region" required>
          <option value="">선택</option>
          <option value="서울" disabled>서울</option>
          <option value="대전">대전</option>
          <option value="광주">광주</option>
          <option value="구미">구미</option>
        </select>
      </div>

      <div id ="input__temperature">
        <p>오늘의 체온을 선택해주세요.</p>
        <input type="radio" name="body-heat" id="normal" value="normal" checked>
        <label for="normal">37도 미만</label>
        <input type="radio" name="body-heat" id="warning" value="warning">
        <label for="warning">37도 이상</label>
      </div>

      <input type="submit" value="제출하기">
      <!-- 타입 이용 가능 -->
    </form>
  </section>

  <script>
    // 1. 백그라운 색 변경 -> 클래스 붙이기 
    // 선택해서 가져온다
    const body = document.querySelector('body') 
    // console.log(body) // console에 출력
    body.id = "main"
    
    
    // 2. img 바꾸기 -> 복합 선택자 
    const ssafyImg = document.querySelector('nav > a > img') // 명시적이고 구체적으로 지정
    // or  const ssafyImg = document.querySelector('#ssafy-image')
    ssafyImg.src = "https://zzu.li/ssafy-image"
    // 이미지 크기 변경

    
    // 3. 각 섹션을 박스형태로 바꿔주기 -> 같은tag
    // const sections = document.querySelectorAll('form > div')
    // console.log(sections)
    const nameInput = document.querySelector('#input__name')
    const regionInput = document.querySelector('#input__region')
    const tempInput = document.querySelector('#input__temperature')

    nameInput.classList.add('box-item')
    regionInput.classList.add('box-item')
    tempInput.classList.add('box-item')

    // 4. 각 섹션별로 중앙 정렬
    const nav = document.querySelector('nav')
    const haeder = document.querySelector('header')
    const section = document.querySelector('section')

    nav.classList.add('box-container')
    haeder.classList.add('box-container')
    section.classList.add('box-container')

    // 5. 버튼 색깔 바꾸기 
    const submitBtn = document.querySelector('form>input[type=submit]')
    // console.log(submitBtn)
    submitBtn.classList.add('button')


    // 6. footer tag 만들기
    const footer = document.createElement('footer')
    // console.log(footer)
    // 스타일링
    footer.classList.add('footer', 'box-container')
    footer.innerText = 'Google 설문지'

    // footer 태크 DOM에 부착시키기
    body.appendChild(footer)


    // 이벤트 추가
    const userName = document.querySelector('#name')
    // console.log(userName) 
    userName.addEventListener('focus', function () {
      alert('안녕!')
    })
  </script>
</body>
</html>

```

