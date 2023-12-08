# import modules
from django.shortcuts import render
from main import models


# home function returned home page of abarword
def home(request):
    # get objects from models
    lasts = models.Posts.objects.all().order_by("-date")[:6]

    # context send datas to homt.html file
    context = {
        'last_posts':lasts,
    }
    # return render html file and then send context and request to this
    return render(request, 'main/home.html',context)


def detail(request,slug):
    post = models.Posts.objects.get(slug = slug)
    context = {
        'post':post
    }
    return render(request,'main/detail.html',context)

def search(request):
    s = request.GET.get("q")
    search = models.Posts.objects.filter(description__icontains=s)
    context = {
        'search':search,
        'q':s
    }
    return render(request,'main/search.html',context)