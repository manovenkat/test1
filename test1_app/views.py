from django.shortcuts import render

# Create your views here.

def index(request):
    index_dict={'insert_me':'I am coming from views.py'}
    return render(request, 'test1_app/index.html', context=index_dict)

def help(request):
    return render(request,'test1_app/help.html')


