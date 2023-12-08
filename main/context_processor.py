from main.models import Category, Posts, News

def bests(request):
    post = Posts.objects.filter(best = True).order_by('-date')[:4]
    return {'best_posts':post}

def news_processor(request):
    news = News.objects.all()
    return {"news":news}

def category_processor(request):
    categoryes = Category.objects.all()
    return {"category": categoryes}

def new_posts(request):
    new_posts = Posts.objects.order_by("-date")[:2]
    return {"new_posts":new_posts}