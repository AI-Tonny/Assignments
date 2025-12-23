from django.shortcuts import render, get_object_or_404
from news.models import News

def home(request):
    return render(request, 'city/home.html')

def news(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'city/news.html', {'news': news_list})

def news_detail(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'city/news_detail.html', {'news_item': news_item})

def news_extra(request, slug=None):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'city/news.html', {'news': news_list})

def management(request):
    return render(request, 'city/management.html')

def history(request):
    return render(request, 'city/history.html')

def history_people(request):
    return render(request, 'city/history_people.html')

def history_photos(request):
    return render(request, 'city/history_photos.html')

def history_extra(request, slug=None):
    return render(request, 'city/history.html')

def facts(request):
    return render(request, 'city/facts.html')

def contacts(request):
    return render(request, 'city/contacts.html')