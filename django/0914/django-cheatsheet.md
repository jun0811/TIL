# Django Cheat Sheet

>  마음의 여유를 가지고 3주간 Django와 우리의 어색해진 사이를 다시 되돌려봅시다 😎

[toc]

## 0. 가상환경 설정

- [x] 가상환경 생성하기

```bash
$ python -m venv venv
```

- [x] 가상환경 실행하기

```bash
$ source venv/Scripts/activate          
```

- [x] Django 설치하기

```bash
$ pip install django
```



## 1. 프로젝트 및 앱 생성

- [x] 프로젝트 만들기

  ```bash
  $ django-admin startproject recap .
  ```

- [x] 앱 만들기

  ```bash
  $ python manage.py startapp articles
  ```

- [x] **❓🤔❓**

  ```
  settings.py : 앱등록 
  ```

- [x] 언어 및 시간 설정

  ```
  settings.py
  LANGUAGE_CODE = 'ko-kr'
  
  TIME_ZONE = 'Asia/Seoul'
  ```

  

## 2. 모델 정의 및 DB 반영

> 게시글을 저장하기 위한 테이블을 만든다고 가정합니다.

- [ ] 모델 정의
- [ ] 마이그레이션 작업
  - [ ] 마이그레이션 파일 생성
  - [ ] 마이그레이션 DB 반영
  - [ ] 마이그레이션 DB 반영 확인



## 3. READ

> 장고 코드는 `U => V => T` 순서로 작성했었죠 :)
>
> 기억을 더듬어보며 하나씩 구현해봅니다.

- [ ] 프로젝트 url 작성
- [ ] 앱 url 작성
  - [ ] path 함수
  - [ ] view 함수 설정 
  - [ ] name 속성 설정
  - [ ] ❓🤔❓
- [ ] view 함수 작성
  - [ ] 모든 게시글 가져오기
  - [ ] 가져온 모든 게시글 template에 넘겨주기
- [ ] template 작성
  - [ ] ❓🤔❓
  - [ ] base.html 작성
  - [ ] index.html 작성
  - [ ] 모든 게시글 보여주기 (ORM 활용)
    - [ ] ❓🤔❓
- [ ] (challenge) 디테일 페이지 만들기
  - [ ] ❓🤔❓



## 4. CREATE

> 게시글 작성 기능은 아래의 순서로 구현했었죠.
>
> 1. 사용자에게 `게시글 작성 페이지를 보여준다`.
> 2. 사용자가 보낸 데이터를 `꺼낸다`.
> 3. 데이터를 `DB에 저장`한다.

- [ ] url 작성
- [ ] view & template 작성
  - [ ] 게시글 작성 페이지 보여주는 함수 (new)
  - [ ] new.html
  - [ ] 사용자가 보낸 폼을 처리하는 함수 (create)
  - [ ] 게시글 작성 이후 사용자에게 메인페이지 보여주기
- [ ] view 함수 합치기 (new와 create 합치기 => create)
  - [ ] ❓🤔❓



## 5. DELETE

> 게시글 삭제 기능은 비교적 간단했습니다.
>
> 1. 사용자가 요청한 게시글을 DB에서 불러온다.
> 2. 지운다.
> 3. 메인 페이지를 보여준다.

- [ ] url 작성
- [ ] view 함수 작성
  - [ ] 특정 게시글 불러오기 (ORM)
  - [ ] 삭제 후 사용자에게 메인 페이지 보여주기



## 6. UPDATE

> 게시글 수정 기능은 기존의 데이터를 불러와서 수정 후 다시 저장하는 것이 핵심이었습니다.
>
> 1. 사용자가 요청한 게시글을 불러온다.
> 2. 수정 페이지에 기존의 게시글 정보를 담아서 보여준다.
> 3. 사용자가 보낸 데이터를 꺼낸다.
> 4. 기존의 데이터를 변경하고 DB에 저장한다.

- [ ] url 작성
- [ ] view & template 작성
  - [ ] 수정 페이지를 보여주는 함수 (edit)
  - [ ] 수정된 데이터를 처리하는 함수 (update)
- [ ] view 함수 합치기 (edit & update => update)
  - [ ] ❓🤔❓



