from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    hero = HeroInfo.objects.get(pk=1)
    context={'hero': hero}
    # list=HeroInfo.objects.filter(isDelete=True)
    list=HeroInfo.objects.all()
    context={'list':list}
    return render(request,'booktest/index.html',context)
def show(request,id):
    context={'id':id}
    return render(request,'booktest/show.html',context)
#練習模板繼承
def index2(request):
    return render(request,'booktest/index2.html')
def user1(request):
    context={'uname':'馬英九'}
    return render(request,'booktest/user1.html',context)
def user2(request):
    return render(request,'booktest/user2.html')

#html轉義
def htmlTest(request):
    context={'t1':'<h1>123</h1>'}
    return render(request,'booktest/htmlTest.html',context)

#csrf
def csrf1(request):
    return render(request,'booktest/csrf1.html')
def csrf2(request):
    uname = request.POST['uname']
    context={'uname':uname}
    return render(request,'booktest/csrf2.html',context)

#驗證碼
def verifyCode(request):
    from PIL import Image,ImageDraw,ImageFont
    import random
    #創建背景色
    bgColor=(random.randrange(50,100),random.randrange(50,100),0)
    #寬高
    width =100
    height=25
    image = Image.new('RGB',(width,height),bgColor)
    #構造字體
    # font = ImageFont.truetype('',24)
    #創建畫筆
    draw = ImageDraw.Draw(image)
    #創建文本內容
    text = '0123ABCF'
    verifyTemp=''
    for i in range(4):
        verifyTemp1=text[random.randrange(0, len(text))]
        verifyTemp+=verifyTemp1
        draw.text((i*25,0), verifyTemp1
        )
    request.session['code'] = verifyTemp
    #逐個繪製字
    # draw.text((0,0),text,(255,255,255))

    #保存到內存中
    from io import StringIO,BytesIO
    buf=BytesIO()
    image.save(buf,'png')
    #將內存留中的內容輸出到客戶端
    return HttpResponse(buf.getvalue(),'image/png')
def verifyTest1(request):
    message = ''
    return render(request,'booktest/verifyTest1.html',locals())
def verifyTest2(request):
    code1 = request.POST['code1']
    code2 = request.session['code']
    if code1==code2:
        return HttpResponse('OK')
    else:
        message = '驗證碼錯誤!!'
        return render(request,'booktest/verifyTest1.html',locals())
