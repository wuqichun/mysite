from django.shortcuts import render,render_to_response
from django.shortcuts import HttpResponse
# Create your views here.
from .models import t_goods
from dwebsocket import require_websocket,accept_websocket
import dwebsocket
from dwebsocket import websocket
a = set()
def index(request):
    goods_1 = t_goods.objects.get(goods_id=1)
    print(goods_1)
    return render_to_response( "app1/index.html",{"good":goods_1})

def get_form(request):
    request.encoding = "utf-8"

    goods = t_goods.objects.create(goods_name=request.GET.get("name"),
                                   goods_price=request.GET.get("age"))
    return render_to_response("app1/index.html")

def uploadfile(request):
    if request.method == 'POST':  # 获取对象
        obj = request.FILES.get('fafafa')
        import os
        # 上传文件的文件名
        print(obj.name)
    # f = open(os.path.join(BASE_DIR, 'static', 'pic', obj.name), 'wb')
    # for chunk in obj.chunks():
    #     f.write(chunk)
    # f.close()
        return HttpResponse('OK')


    return render_to_response( 'app1/uploadfile.html')

@accept_websocket #既能接受http也能接受websocket请求
def echo(request):

    if not request.is_websocket():
        message = request.GET['message']
        return HttpResponse(message)
    else:
        if request.websocket not in a:
            a.add(request.websocket)
        for message in request.websocket:
            print(request.websocket)
            print(message)
            for t in a:
                t.send(message + '这是你发来的。。。'.encode('utf-8'))
