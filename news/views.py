from django.shortcuts import render, get_object_or_404

from .models import News

def index(request):
    queryset = request.GET.get('tag')
    if queryset:
        news = News.objects.filter(tag=queryset)
    else:
        news = News.objects.all()

    return render(request, 'news/list.html', {'news':news})



def news_detail(request, year, month, day,slug):
    news_paper = get_object_or_404(News,slug=slug,
                                   created__year=year,
                                   created__month=month,
                                   created__day=day,
                                   )
    return render(request, 'news/news_detail.html', {'news_paper':news_paper})