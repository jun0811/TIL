## 0921Homework

### 1. Look up

- __exact: 정확히 일치 <->  `exact` : 대소문자를 구분을 하지않는 exact 
- __contains: 조건 값을 포함하는지 , 대소문자 구분함. 
- __gt : 큼

### 2. 1:N 관계설정

- CASCADE : 부모객채(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
- PROTECT  : 참조가 되어 있는 경우 오류 발생
- SET_NULL : 부모 객체가 삭제 됐을 때 모든 값을 NULL로 치환.(NOT NULL 조건 시 불가능)

### 3. comment create

- commit=False

### 4. 1:N ORM

- comments