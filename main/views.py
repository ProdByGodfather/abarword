# import modules
from django.shortcuts import render



# home function returned home page of abarword
def home(request):


    # context send datas to homt.html file
    context = {
        
    }
    # return render html file and then send context and request to this
    return render(request, 'main/home.html',context)