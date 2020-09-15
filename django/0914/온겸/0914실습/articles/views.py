from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    # READ
    # 1. 사용할 모델을 불러온다.
    # 2. ORM을 이용해서 DB에서 모든 게시글을 가져온다.
    # 3. context에 담아서 탬플릿에 넘겨준다.
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     # 게시글 작성 폼이 담긴 페이지를 보여줍니다.
#     return render(request, 'articles/new.html')


def create(request):
    # 1. POST 요청이면 폼 데이터를 처리한다.
    if request.method == 'POST':
        # 2. 폼의 인스턴스를 생성하고 사용자가 보낸 데이터로 폼을 채운다. (binding)
        form = ArticleForm(request.POST)
        # 3. 폼에 담긴 데이터가 유효한지 검사한다.
        if form.is_valid(): # 유효성검사
            form.save()
        # # 1. form에 담긴 데이터를 꺼낸다.
        # title = request.POST.get('title')
        # content = request.POST.get('content')

        # # 2. 데이터를 저장한다.
        # article = Article()
        # article.title = title
        # article.content = content
        # article.save()
            return redirect('articles:index')
    else: # GET 요청일 때
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/new.html', context)


def detail(request, article_pk):
    # 1. 사용자가 요청한 게시글을 가져온다.
    # 2. context에 담아서 탬플릿으로 넘겨준다.
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article':article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST  # POST요청만 허용!
# @require_http_methods('GET', 'POST')
def delete(request, article_pk):
    # 1. 사용자가 요청한 게시글을 가져온다.
    # 2. 지운다
    # 3. 지우고나서 다른 페이지를 보여준다.
    # if request.method == 'POST': @require_POST를 해서 필요없음.
    article = Article.objects.get(pk=article_pk) # get, filter 차이 
    # get은 하나만, filter는 쿼리셋 전체
    article.delete()
    return redirect('articles:index')


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article_pk)
    else:
        form = ArticleForm(instance=article) # 기존의 내용을 보여줌
    # 1. GET 요청인 경우
    # 2. POST 요청이지만 검증에 실패했을 때 => form = ArticleForm(request.POST, instance=article)
    context = {
        'form':form,
    }
    return render(request, 'articles/update.html', context)