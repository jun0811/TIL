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