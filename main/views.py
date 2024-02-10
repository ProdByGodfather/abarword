# import modules
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from main import models
from django.contrib import messages

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

def all(request):
    posts = models.Posts.objects.all().order_by('-date')

    context = {
        'post':posts,
        'c':"همه مقالات"
    }
    return render(request,'main/all.html',context)

def category(request,slug):
    cate = models.Category.objects.get(slug=slug)
    posts = models.Posts.objects.filter(category=cate)

    return render(request,'main/all.html',{'post':posts,'c':cate})


def about(request):
    return render(request,"main/about.html")

def contact(request):
    if request.method == "POST":
        try:
            email = request.POST.get('email')
            name = request.POST.get('name')
            message = request.POST.get('message')
            models.Contact.objects.create(email=email, name=name, message=message)
            messages.info(request,'پیغام شما با موفقیت ذخیره شد')
        except:
            messages.info(request, 'مشکلی در ذخیره پیغام شما رخ داد، لطفا مجددا تلاش کنید.')
    

    return render(request, 'main/contact.html')


"""
    این تابع مقدار خروجی خاصی ندارد و فقط ایمیل فرستاده شده توسط متد پست را ذخیره میکند.
    سپس صفحه خانه و اصلی را بر میگرداند.
"""
def save_mail(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            models.Emails.objects.create(email=email)
            messages.info(request,'ایمیل شما با موفقیت ذخیره شد')
        except:
            messages.info(request,"مشکلی در ذخیره ایمیل شما پیش آمد.")
    # redirect to home page ( redirect to home function )
    return HttpResponseRedirect(reverse_lazy('home'))