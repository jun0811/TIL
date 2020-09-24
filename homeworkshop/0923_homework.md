# 0923_homework

### 1. 

1) T 

2) F

3) T

4) F



### 2.

articles_question

articles_comment

answer_id(FK)



### 3.

- question.comment_set.all()



### 4.

>로그인을 안한 상황

1. 로그인 페이지로 이동
2. 로그인 폼 작성 후 다시 요청(?next='-')
3. @require_POST 데코레이터 때문에 에러 발상
   - 405 Method Not Allowed



### 5. 해결방법

1. @ require_POST 데코레이터 제거 
2. 함수안에서 if문으로 해결 



