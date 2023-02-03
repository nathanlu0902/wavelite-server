from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

#该方法禁用csrf
@csrf_exempt
def login(request):
  if request.method!="POST":
    return JsonResponse({"code":"1001","msg":"请求方法错误"})
  else:
    print(request.POST)
    code=request.POST.get("code","0")
    if code=="0":
      return JsonResponse({"code":"1002","msg":"code is empty"})
    url="https://api.weixin.qq.com/sns/jscode2session?appid=wx63fd2a9f576da51b&secret=dfe88a92d09fa838f1f59864b5dc9969&js_code="+code+"&grant_type=authorization_code"
    try:
      response=requests.get(url).json()
      print(response)
    except requests.exceptions.JSONDecodeError:
      return JsonResponse({"code":"1003","msg":"openid request error"})
    else:
      openid=response['openid']
    return openid
    
    

  
