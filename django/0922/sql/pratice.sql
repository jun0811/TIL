sqlite> .headers on
sqlite> .mode column

 CREATE TABLE classmates(
   ...> name TEXT,
   ...> age INTEGER,    
   ...> address TEXT);

insert into classmates(name, age) values('홍길동', 24);
-- 모든 열의 데이터를 집어넣을 때 따로 명시 필요 x 
Select * from classmates
-- 데이터 조회
SELECT rowid, * FROM classmates;
-- 
DROP TABLE classmates;
CREATE TABLE classmates(
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL);
  -- row id 는 따로 안만들어주는 것이 좋다!!
  insert INTO classmates VALUES('김소정', 24, '화정');
  insert INTO classmates VALUES('이승준', 27, '인천');
  insert INTO classmates VALUES('곽온겸', 27, '영월');
  SELECT rowid, name FROM classmates
  LIMIT 1 OFFSET 2; 
  --  2칸 떨어진 곳에서 1개


  --  조건절 WHERE
  SELECT rowid, name from classmates WHERE address ='인천';
  
  
  -- 중복제거
  SELECT DISTINCT age
  FROM classmates;


  -- 데이터 삭제
  -- 1. select로 내가 지울 값을 가져와 본다.
  -- 2. 정확히 가져온지 확인 후 지운다.
  DELETE FROM classmates 
  WHERE rowid =3;


  -- table 만들기
  CREATE TABLE tests(
    id integer PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL);
  INSERT INTO tests(name)VALUES('곽온겸');
  INSERT INTO tests(name)VALUES('이승준');
  DELETE FROM tests WHERE id = 2; 
  -- 지우고 다시 만들어도 2 다음인 3으로 id가 주어진다.
  INSERT INTO tests(name)VALUES('김소정');

-- .shell clear  창 깨끗이
UPDATE classmates
SET name = '홍길동', address = '제주도'
WHERE rowid = 1;


-- 조건 조회
 SELECT first_name, last_name FROM users
 where age>=30;

SELECT last_name, age
from users
where age>=30 and last_name= '김';


-- count
SELECT count(*)
from users;

-- avg
SELECT avg(age) From users
WHERE age>=30;

-- max 계좌 잔액이 가장 높은 사람과 액수는?
SELECT first_name, max(balance) from users;

-- 20대인 사람들
SELECT * from users
where age Like '2_';

-- 
SELECT *
FROM users
WHERE first_name LIKE '%준';

-- 나이 오름차순 상위 10개
SELECT * FROM users
order by age
LIMIT 10; 

-- 
SELECT last_name, count(*) as name_count
from users
GROUP BY last_name;


-- alter
Create table articles(
title TEXT NOT NULL,
content TEXT NOT NULL);

insert INTO articles
values('1번','2번');

alter TABLE articles rename to news;

-- not null이면 디폴트 정해줄것 ~
alter table news 
add column created_at TEXT not NULL DEFAULT 1;

-- sql 연습 -> 프로그래머스 sql 고득점 kit

