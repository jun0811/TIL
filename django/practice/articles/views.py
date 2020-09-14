from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    # READ
    # 1. 사용할 모델을 불러온다
    # 2. ORM을 이용해서 DB를 모든 게시글에 가져온다.
    # 3. context에 담아서 템플릿에 넘겨준다
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     # 게시글 작성 폼이 담신 페이지를 보여준다
#     return render(request, 'articles/new.html')


def create(request):
    # 1. POST 요청이면 폼 데이터를 처리한다.
    if request.method == 'POST':
        # 2. 폼의 인스턴스를 생성하고 사용자가 보낸 데이터로 폼을 채운다.
        form = ArticleForm(request.POST)
        # 3. 폼에 담긴 데이터가 유효한지 검사한다.
        if form.is_valid(): # 유효성 검사
            form.save()
            # article = Article(title=title, content=content) 
            # article.save()
            return redirect('articles:index')
        # # 1. form에 담긴 데이터를 꺼낸다
        # title = request.POST.get('title')
        # content = request.POST.get('content')

        # # 2. 데이터를 저장한다
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()
        
    
    else: # GET 요청일경우
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/new.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk =article_pk)
    # article2 = Article.objects.filter(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    # if request.method =='POST' # get요청일 떄는 삭제 x 
    # ->from django.views.decorators.http import require_POST : get으로 작동할 떄 ERRO 405
    article = Article.objects.get(pk=article_pk)
    # article2 = Article.objects.filter(pk=article_pk)
    article.delete()
    return redirect('articles:index')


def update(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.method =="POST":
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance = article)
    context = {
        'form' : form,
        # 'title': title,

    }
    return render(request,'articles/update.html',context)