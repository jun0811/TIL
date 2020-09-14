# 0914 Homework



1) 

a) forms.ModelForm

b) Mate



2) 

이유: is_valid() 메서드에서 검사시에 조건을 만족하지 못했을 때 context에 담긴것이 없는 상태에서 return을 호출하여 문제가 발생한다.



해결 방법: 

```python
else:
        form = ReservationForm() # 기존의 내용을 보여줌
    context = {
        'form':form
    }
#으로 수정이 필요하다
```



3) 

form = ArticleForm(instance=article)



4) 

.errors / .label_tag / .id_for_label / .value / .html_name / .help_text / .errors / .is_hidden / .field