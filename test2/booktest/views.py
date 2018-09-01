#coding=utf-8
from django.shortcuts import render
from django.db.models import Max,F,Q
from .models import *
# Create your views here.
def index(request):
    # list = BookInfo.books1.filter(heroinfo__hcontent__contains='六')#找到書裡包含八這個字的英雄的書籍
    # list = BookInfo.books1.filter(pk__lte=3) 找到書裡面id小於3的，pk代表primarykey
    # Max = BookInfo.books1.aggregate(Max('id'))
    # list = BookInfo.books1.filter(bread__gt=F("bcommet"))#查詢閱讀量大於評論量的 記得要import F
    #  list = BookInfo.books1.filter(pk__lt=4,btitle__contains='1')
    # list = BookInfo.books1.filter(pk__lt=4).filter(btitle__contains='1') #邏輯and與上句相同思。
    #如果要用邏輯或 要用Q 邏輯AND不需要用Q
    list = BookInfo.books1.filter(Q(pk__lt=4)|Q(btitle__contains='1'))

    context = {'list1':list
               # 'Max':Max
               }
    return render(request,'index.html',context)