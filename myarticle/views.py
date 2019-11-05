from django.shortcuts import render, HttpResponse
from myarticle.models import Article

def list_article(request):
    articles = Article.objects.all()
    return render(request, 'article/list.html', {'articles': articles})