from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
from django.views.decorators.cache import cache_page
# Create your views here.
def index(request):
    return render(request,'booktest/index.html')
def pro(request):
    prolist=AreaInfo.objects.filter(aPArea__isnull=True)
    list = []
    #[[1,'北京'],[2,'天津'],...]
    for item in prolist:
        list.append([item.aid,item.atitle])#[1,'北京']
    return JsonResponse({'data':list})
def city(request,id):
    citylist=AreaInfo.objects.filter(aPArea_id=id)
    list=[]
    #[{id:1,title:'北京'},]
    for item in citylist:
        list.append({'id':item.aid,'title':item.atitle})
    return JsonResponse({'data':list})
#自定義編輯器
def htmlEditer(request):
    return render(request,'booktest/htmlEditer.html')
def htmlEditerHandle(request):
    html=request.POST['hcontent']
    # test1=Test1.objects.get(pk=1)
    # test1.content=html
    # test1.save()
    test1=Test1()
    test1.content=html
    test1.save()
    context = {'content':html}
    return render(request,'booktest/htmlEditerHandle.html',context)
@cache_page(60*10)
def cache1(request):
    # return HttpResponse('Hello1')
    return HttpResponse('Hello2')