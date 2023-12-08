from django.urls import path
from main import views

urlpatterns = [
    path('',views.home,name='home'),
    path('posts/<slug:slug>/',views.detail,name='detail')
]