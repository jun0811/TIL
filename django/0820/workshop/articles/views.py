from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request,'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article.pk)


def detail(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    context ={
        'article' : article
    }
    return render(request, 'articles/detail.html', context)


def edit(request, article_pk):
    article = Article.objects.get(pk = article_pk)
    context ={
        'article' : article
    }
    return render(request, 'articles/edit.html', context)


def update(request, article_pk):
        #1. 
    title = request.POST.get('title')
    content = request.POST.get('content')
    #2.
    article = Article.objects.get(pk = article_pk)
    #3. 수정 및 저장
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article_pk)

def delete(request,article_pk):
    article = Article.objects.get(pk = article_pk)
    article.delete()
    return redirect('articles:index')
