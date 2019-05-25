# -*- coding:utf-8 -*-
from django.shortcuts import render
from .models import BookInfo, HeroInfo


# Create your views here.

def index(request):
    book = BookInfo.objects.get(pk=1)
    hero_she = HeroInfo.objects.filter(book__btittle="射雕英雄传")
    hero_all = HeroInfo.objects.all()
    context = {"book": book,
               "hero_she": hero_she,
               "hero_all": hero_all,
               }

    return render(request, "bookTest/index.html", context)


def show(request):
    return render(request, "bookTest/show.html")


def index2(request):
    return render(request, "bookTest/index2.html")
