# 0915_workshop



### 1.

- settings.py

```python
# Media files
MEDIA_ROOT = BASE_DIR / 'media'
# http://localhost:8000/xxx.jpg -> ~~/media/xx.jpg
MEDIA_URL = '/media/'
```



- models.py

```python 
image = models.ImageField(blank = True, upload_to = '%Y/%m/%d/') 
# 추가
```

