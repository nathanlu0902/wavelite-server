from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import User

#该方法禁用csrf
@csrf_exempt
def login(request):
  openid=getOpenId(request)
  print(openid)
  try:
    user=User.objects.get(openid=openid)
  except User.DoesNotExist:
    return JsonResponse({"code":"1004","msg":"User does not exit"})
  else:
    return JsonResponse({"code":"1005",
                "nickname":user.nickname,
                "phone":user.phone,
                "birth":user.birth,
                "openid":user.openid
                })


@csrf_exempt
def registerUser(request):
  if request.method!="POST":
    return JsonResponse({"code":"1001","msg":"请求方法错误"})
  # nickname=request.POST.get("nickname")
  phone=request.POST.get("phone")
  # gender=request.POST.get("gender")
  openid=request.POST.get("openid")
  user=User(phone=phone,openid=openid)
  user.save()
  return JsonResponse({"code":"1006","msg":"user is created"})

@csrf_exempt
def updateUser(request):
  if request.method!="POST":
    return JsonResponse({"code":"1001","msg":"请求方法错误"})
  openid=request.POST.get("openid")
  user=User.objects.filter(openid=openid)
  #查找并更新数据库个人信息
  try:
    for (k,v) in request.POST:
      print(k,v)
      if user[k]!=v:
        user[k]=v
    user.save()
    return JsonResponse({"code":"1007","msg":"User info updated"})
  except:
    print("error when update user info")
  
    

def getOpenId(request):
  if request.method!="POST":
    return JsonResponse({"code":"1001","msg":"请求方法错误"})
  else:
    code=request.POST.get("code","0")
    if code=="0":
      return JsonResponse({"code":"1002","msg":"code is empty"})

    url="https://api.weixin.qq.com/sns/jscode2session?appid=wx63fd2a9f576da51b&secret=dfe88a92d09fa838f1f59864b5dc9969&js_code="+code+"&grant_type=authorization_code"
   
    try:
      response=requests.get(url).json()
    except requests.exceptions.JSONDecodeError:
      return JsonResponse({"code":"1003","msg":"openid request error"})
    else:
      openid=response['openid']
      return openid
