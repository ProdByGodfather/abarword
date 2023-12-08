from django.urls import path
from main import views

urlpatterns = [
    path('',views.home,name='home'),
    path('posts/<slug:slug>/',views.detail,name='detail'),
    path('search/',views.search,name='search'),
    path('posts/',views.all,name='all'),
    path('posts/category/<slug:slug>/',views.category,name='category'),
    path('about/',views.about,name='about')
]