from django.shortcuts import render
from .models import BookInfo


# from django.http import HttpResponse
# from django.template import RequestContext, loader


# Create your views here.


def index(request):
    # temp = loader.get_template(r"hbtest/index.html")
    # return HttpResponse(temp.render())
    book_list = BookInfo.objects.all()
    context = {"say": "我在做Django项目测试", "list": book_list}
    return render(request, r"hbtest/index.html", context)


def show(request, book_id):
    book = BookInfo.objects.get(pk=book_id)
    hero_list = book.heroinfo_set.all()
    context = {"hero_list": hero_list}
    return render(request, r"hbtest/showHero.html", context)
