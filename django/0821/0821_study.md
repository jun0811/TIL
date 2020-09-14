# 0821_study



여러 프로젝트를 진행하게 되면 프로젝트 마다 다른 버전의 라이브러리가 필요할 수 있다. -> *python* 에서는 한 라이브러리에 대해 하나의 버전만 설치가 가능

-> **가상환경** 을 사용한다.



- 가상환경 만들기  : `python -m venv 가상환경이름(venv)
- git: `source venv/Scripts/activate`  -> `(venv)` 출력 확인 
-  vscode에서 interpreter 가상환경 만든 것으로 바꿔주기
  - `pip list`명령어를 통해 환경이 초기화된 리스트를 확인 가능
- 활성화 :
  - window : 가상환경이름\Scrips\activate





### vscode 

- 가상환경 설정 :  interpreter->venv 선택 -> terminal 켜기
- 가상환경 , DB , (.vscode)는 git에서 관리하지 않는다
  - https://www.toptal.com/developers/gitignore
  - ex) window , Django, python, venv  vscode 등등을 추가



	### 패키지 관리(환경)

- pip freeze   : requirements format으로 출력



- 패키지 요구사항 생성
  - pip freeze > requirements.txt (포멧 출력을 txt로 저장)
  - 패키지 목록
- pip 설치를 한다면 다시 `pip freeze > requirements.txt`



- 내가 그대로 받을 때.

  - 패키지

  1.  git clone
  2.  `python -m venv venv`
  3. `source venv/Scripts/activate`
  4. `pip install -r requirements.txt` # 설치



### DB관리

--- -

### fixtures

> Django가 데이터베이스로 import 할 수 있는 데이터 모음
>
> 앱을 처음 설정할 때 데이터베이스를 미리 채워야하는 상황이 존재하는데 이러한 초기 데이터를 제공하는 방법 중 하나 



필요한 과정 : 초기데이터 만들기 + 데이터 심기



##### 초기데이터 만들기

- dumpdata : 특정 앱의 관련된 데이터베이스의 모든 데이터를 출력
  - `python manage.py dumpdata app_name.Model`

- loaddata : 
  - dumpdata를 통해 만들어진 fixtures파일을 데이터 베이스에 import
  - fixtures 파일은 반드시 app디렉토리 안에 fixtures 디렉토리에 위치해야함



##### 명령어

- `python manage.py dumpdata app_name.ModelName [--options]`
  - ex) python manage.py dumpdata articles.Article --indent(4) > articles.json
- `python manage.py loaddata fixtures_path`
  - ex) python manage.py loaddata articles/articles.json
- 관리자 data : `auth.User` 



---

### 정리

버전관리에서 ignore를 패키지와 DB를 하게된다

패키지는 freeze / 데이터는 fixtures를 통해 한다.