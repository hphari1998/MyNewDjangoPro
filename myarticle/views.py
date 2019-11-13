from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect
from myarticle.models import Article
from commenting.models import Comment
from myarticle.forms import ArticleModelForm, ArticleComment
from commenting.forms import CommitModelFrom


def list_article(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'article/list.html', {'articles': articles})


def view_article(request, id):
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=article).order_by('created_at')
    comit_form = CommitModelFrom(initial={'article': id})
    
    return render(request, 'article/detail.html', { 'comit': comit_form, 'article': article, 'comments': comments})


def create_article(request):
    if request.method == 'POST':
        article_form = ArticleModelForm(request.POST, request.FILES)
        if article_form.is_valid():
            article_obj = article_form.save(commit=False)
            article_obj.author = request.user
            article_obj.save()
            return HttpResponsePermanentRedirect('/articles/')
    else:
        article_form = ArticleModelForm()
    return render(request, 'article/form.html', {'form': article_form})