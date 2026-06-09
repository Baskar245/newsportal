from django.shortcuts import render
from .models import News

def home(request):
    articles = News.objects.all().order_by('-published_date')
    return render(request, 'home.html', {'articles': articles})