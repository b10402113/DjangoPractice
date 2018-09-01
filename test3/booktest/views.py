from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    return HttpResponse(request.path)
def detail(request,p1,p2,p3):#因為有加上括號所以需再傳一個參數
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))
#展示鍵接的頁面
def getTest1(request):
    return render(request,'booktest/getTest1.html')

#接收一鍵一值的情況
def getTest2(request):
    #根據鍵接收值
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    # 構造上下文
    context={'a':a1,'b':b1,'c':c1}
    # 向模板傳遞上下文並進行渲染
    return render(request,'booktest/getTest2.html',context)

#接收一鍵多值的情況
def getTest3(request):
    #根據鍵接收值
    a1 = request.GET.getlist('a')
    # 構造上下文
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context)
def postTest1(request):
    return render(request,'booktest/postTest1.html')
def postTest2(request):
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    ugender=request.POST['ugender']
    uhobby=request.POST.getlist('uhobby')#因為多個值採用post.getlist
    # context = {
    #     'uname':uname,
    #     'upwd':upwd,
    #     'ugender':ugender,
    #     'uhobby':uhobby
    # }
    return render(request,'booktest/postTest2.html',locals())
def cookieTest(request):
    response = HttpResponse()
    cookie=request.COOKIES
    if ('t1') in cookie:
        response.write(cookie['t1'])
    # response.set_cookie('t1','abc')
    return response
def redTest1(request):
    return HttpResponseRedirect('/booktest/redTest2/')
def redTest2(request):
    return HttpResponse('這是轉向的頁面')
#通過用戶登入練習session
def session1(request):
    uname = request.session.get('myname','未登入')#會變成none如果沒有的話
    context={'uname':uname}
    return render(request,'booktest/session1.html',context)
def session2(request):
    return render(request,'booktest/session2.html')
def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname
    request.session.set_expiry(0) #關閉瀏覽器就過期
    #登入處理玩了
    return redirect('/booktest/session1/')
def session3(request):
    #刪除session
    if ('myname') in request.session:
        del request.session['myname']
    else:
        return redirect('/booktest/session1/')
    return redirect('/booktest/session1/')