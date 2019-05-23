# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(request):
    return HttpResponse("hello word")


def detail(request, year, month, day):
    return HttpResponse(str(year) + "年" + str(month) + "月" + str(day) + "日")


# 展示连接页面
def get_test1(request):
    return render(request, "bookTest/getTest1.html")


# 接收一键一值
def get_test2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {"a": a1, "b": b1, "c": c1}
    return render(request, "bookTest/getTest2.html", context)


# 接收一键多值
def get_test3(request):
    a1 = request.GET.getlist("a")
    context = {'a': a1}
    return render(request, "bookTest/getTest3.html", context)


def post_test1(request):
    return render(request, "bookTest/postTest1.html")


def post_test2(request):
    name = request.POST["username"]
    pwd = request.POST["password"]
    gender = request.POST["gender"]
    like = request.POST.getlist("like")
    context = {"name": name,
               "pwd": pwd,
               "gender": gender,
               "like": like, }
    return render(request, "bookTest/postTest2.html", context)


def cookie_test(request):
    response = HttpResponse("cookie test")
    cookie = request.COOKIES
    if "t1" in cookie:
        print(cookie["t1"])
    else:
        response.set_cookie("t1", "1214ajoiwur0fi3y9qufh")
    return response


def redirect_test1(request):
    # return HttpResponseRedirect("/bookTest/redirectTest2")
    return redirect("/bookTest/redirectTest2")


def redirect_test2(request):
    return HttpResponse("这是转向来的页面")
