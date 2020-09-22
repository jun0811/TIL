# 0922_workshop

1.

```sql
CREATE TABLE countries(
      room_num TEXT,
      check_in TEXT,
      check_out TEXT,
      grade TEXT,
      price INTEGER
   );
```

2.

```sql
   INSERT INTO countries 
   VALUES('B203','2019-12-31','2020-01-03', 'suite',900);
   INSERT INTO countries
   VALUES('1102','2020-01-04','2020-01-08', 'suite',850);
   INSERT INTO countries
   VALUES('303','2020-01-01','2020-01-03', 'deluxe',500);
   INSERT INTO countries
   VALUES('807','2020-01-04','2020-01-07', 'superior',300);
```

3.

```sql
ALTER TABLE countries RENAME to hotels
```

4.

```sql
   SELECT room_num, price FROM hotels
   ORDER BY price DESC
   LIMIT 2;
```

5.

```sql
SELECT grade ,count(*) from hotels
   GROUP BY grade
   ORDER BY count(*) DESC;
```

6.

```sql
   SELECT * from hotels
   where grade ='deluxe' or room_num LIKE 'B%';
```

7.

```sql
SELECT * FROM hotels
WHERE room_num not like 'B%' and check_in='2020-01-04';
```

