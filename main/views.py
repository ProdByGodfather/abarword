# import modules
from django.shortcuts import render
from main import models


# home function returned home page of abarword
def home(request):
    # get objects from models
    lasts = models.Posts.objects.all().order_by("-date")[:4]

    # context send datas to homt.html file
    context = {
        'last_posts':lasts,
    }
    # return render html file and then send context and request to this
    return render(request, 'main/home.html',context)


