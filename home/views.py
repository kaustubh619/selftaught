from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    my_infor = {
        "phone": "405-933-8099",
        "address": "102 N. University Pl. Apt.3, Stillwater - OK"
    }
    return render(request, "about.html", my_infor)


def portfolio_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")

    return render(request, "portfolio.html", {})


def error_view(request, *args, **kwargs):
    return render(request, "404.html")
