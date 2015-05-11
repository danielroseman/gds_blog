from django.shortcuts import render
from core.models import Article

def index(request):
  articles = Article.objects.all()
  return render(request, 'index.html', {'articles': articles})


def article(request, article_id):
  article = Article.objects.get(id=article_id)
  return render(request, 'article.html', {'article': article})
