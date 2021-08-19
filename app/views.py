from django.shortcuts import render

# Create your views here.

def fun_app(request):
    d={'name':'MANIKANNDAN'}
    return render(request,'first.html',context=d)