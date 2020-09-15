# 0915 Homework

### 1. 

```python
STARTICFILES_DIRS = [
    BASE_DIR / 'assets',  # 폴더 구조 만들어주기
]
```



### 2. 

```python
MEDIA_ROOT = BASE_DIR / 'media'
# http://localhost:8000/xxx.jpg -> ~~/media/xx.jpg
MEDIA_URL = '/media/'
```



### 3.

(a)  settings

(b) django.conf.urls.static

(c) static 

(d) settings.MEDIA_URL, document_root=settings.MEDIA_ROOT

