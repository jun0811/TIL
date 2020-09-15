# 0915_pratice

- view.py

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    '''
    db에 있는 모든 게시글 가져오기 
    '''
    articles = Article.objects.all()
    context ={
        'articles' : articles, 
    }
    return render(request, 'articles/index.html', context)


def create(request): 
    if request.method == 'POST': 
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/articles')
    else: #먼저작성 -> 테스트 후 if문 작성
        form = ArticleForm()
    context = {'form' : form}
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    context={
        'article': article
    }
    return render(request, 'articles/detail.html',context)


@require_POST
def delete(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    article.delete()
    return redirect('/articles')


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detial', article_pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

- index.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>CRUD with ModelForm</h1>
  <br>
  <h1>Articles</h1>
  <a href="{% url 'articles:create' %}">NEW</a>
  <hr>
  {% for article in articles %}
    <h1>{{article.pk}}</h1>
    <h1>{{article.title}}</h1>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

- detail.html

```html
{% extends 'base.html' %}

{% block content %}

  <h1>DETAIL</h1>
  <hr>
  <h1>{{article.title}}</h1>
  <p>{{article.content}}</p>
  <p>{{article.created_at}}</p>
  <p>{{article.updated_at}}</p>
  <a href="{% url 'articles:update' article.pk%}">[UPDATE]</a>
  {% comment %} 삭제요청은 form tag {% endcomment %}
  <form action="{% url 'articles:delete' article.pk%}" method = "POST">
    {% csrf_token %}
  <input type="submit" value="DELETE">   
   {% comment %} <button>[DELETE]</button> {% endcomment %}
  </form>
{% endblock  %}
```

- update.html

```html
{% extends 'base.html' %}
{% block content %}
	<h2>Edit</h2>
<form action="" method="POST">
  {% csrf_token %}
  {{ form }}
  <button>submit</button>
  {% comment %} <a href="{% url 'articles:detail' article.pk %}">BACK</a>
{% endcomment %}
</form>
 <a href="{% url 'articles:detail' form.instance.pk %}">[back]</a>
{% endblock content %}
```

- create.html

```html
{% extends 'base.html' %}

{% block content %}
  <h1>New</h1>
  <form action="{% url 'articles:create'%}" method ="POST">
    {% csrf_token %}
    {{form}}
    <button>submit</button>
  </form>
{% endblock %}
```



