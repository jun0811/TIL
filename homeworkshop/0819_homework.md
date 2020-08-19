# 0819_homework

### 1. Model 반영하기

migrate

명령어 : makemigrations/ migrate/  sqlmigrate/ showmigrations



### 2. Model 변경사항 저장하기

$ python manage.py sqlmigrate articles 0001

BEGIN;

Create model Article

CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL);
COMMIT;



### 3. Python Shell

python manage.py shell_plus



### 4. Django Model Field

Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지

CharField 

TextField

DateTimeField

TimeField

JsonField



