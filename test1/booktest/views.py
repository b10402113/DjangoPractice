from django.shortcuts import render
from django.http import *
from .models import *
from django.template import loader,RequestContext
# Create your views here.
def index(request):#接收參數
    # temp=loader.get_template('booktest/index.html')#加載一班不這麼做
    bookList = BookInfo.objects.all()
    context={'list':bookList}
    return render(request,'booktest/index.html',context)

def show(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    context={'list':herolist}
    return render(request,'booktest/show.html',context)