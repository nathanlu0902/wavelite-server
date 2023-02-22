from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import User,Goods,GoodsCategory
from .serializers import GoodsCategorySerializer,GoodsSerializer
from rest_framework import viewsets

#该方法禁用csrf
@csrf_exempt
def login(request):
  openid=getOpenId(request)
  try:
    user=User.objects.get(openid=openid)
  except User.DoesNotExist:
    return JsonResponse({
      "code":"1004",
      "msg":"User is not existed",
      "openid":openid
      })
  else:
    return JsonResponse({
      "code":"1005",
      "nickname":user.nickname,
      "phone":user.phone,
      "birth":user.birth,
      "openid":user.openid
      })


@csrf_exempt
def registerUser(request):
  if request.method!="POST":
    return JsonResponse({"code":"1001","msg":"wrong request method"})
  # nickname=request.POST.get("nickname")
  phone=request.POST.get("phone")
  # gender=request.POST.get("gender")
  openid=request.POST.get("openid")
  user=User(phone=phone,openid=openid)
  user.save()
  print("user is created with userid:",openid)
  return JsonResponse({"code":"1006","msg":"user is created"})

@csrf_exempt
def updateUser(request):
  if request.method!="POST":
    return JsonResponse({"code":"1001","msg":"wrong request method"})
  openid=request.POST.get("openid")
  print("server to lookup openid:"+openid)
  try:
    user=User.objects.get(openid=openid)
  except user.DoesNotExist:
    return JsonResponse({"code":"1004","msg":"User is not existed"})
  else:
    print("found user with openid:"+user.openid)
    #查找并更新数据库个人信息
    try:
      user.nickname=request.POST.get("nickname")
      user.phone=request.POST.get("phone")
      user.gender=request.POST.get("gender")
      user.birth=request.POST.get("birth")
      print("received",request.POST.get("birth"))
      # user=User(phone=phone,nickname=nickname,gender=gender)
      user.save()
      return JsonResponse({"code":"1007","msg":"User info updated"})
    except Exception as e:
      return JsonResponse({"code":"1008","msg":e})
  
    

def getOpenId(request):
  if request.method!="POST":
    return JsonResponse({"code":"1001","msg":"wrong request method"})
  else:
    code=request.POST.get("code","0")
    print("server received code:"+code)
    if code=="0":
      return JsonResponse({"code":"1002","msg":"code is empty"})

    url="https://api.weixin.qq.com/sns/jscode2session?appid=wx63fd2a9f576da51b&secret=dfe88a92d09fa838f1f59864b5dc9969&js_code="+code+"&grant_type=authorization_code"
   
    try:
      response=requests.get(url).json()
    except requests.exceptions.JSONDecodeError:
      return JsonResponse({"code":"1003","msg":"openid request error"})
    else:
      openid=response['openid']
      print("server received openid"+openid)
      return openid

class GoodsCategoryViewSet(viewsets.ModelViewSet):
  queryset=GoodsCategory.objects.all()
  serializer_class=GoodsCategorySerializer

class GoodsViewSet(viewsets.ModelViewSet):
  queryset=Goods.objects.all()
  serializer_class=GoodsSerializer

    