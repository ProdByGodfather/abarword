from main.models import Category, Posts, News, Emails

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


"""
    دریافت تعداد افرادی که در خبرنامه ثبت نام کرده اند بر اساس ایمیل هایشان
    تعداد ایمیل های مدل ایمیل را دریافت کرده در پارامتر ایمیل کانت باز میگردانیم
"""
def email_count(request):
    email_count = Emails.objects.all().count()
    return {"email_count":email_count}