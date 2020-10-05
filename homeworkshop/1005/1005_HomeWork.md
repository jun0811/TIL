# 1005_HomeWork



### 1. 

1. T
2. F
3. T
4. F



### 2. 

- 200 : 요청이 성공적으로 되었습니다.
- 400 : 요청을 이해할 수 없다.
- 401 : 권한이 없다 -> 인증이 필요
- 403 : 클라이언트는 콘텐츠에 접근 권리 x 
- 404 : Not Found
- 500 : 서버가 처리 방법을 모르는 상황



### 3. 

```python
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'age', 'address')
```



### 4.

> 시리얼라이져는 데이터를 쉽게 렌더링 할수있는 콘텐츠 형식으로 파이썬 데이터 유형에서 JSON, XML과 같은 형식으로 변환시켜준다. 역도 성립.

