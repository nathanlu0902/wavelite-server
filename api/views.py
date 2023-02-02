from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests

#该方法禁用csrf
@csrf_exempt
def login(request):
  if request.method!="POST":
    return JsonResponse({"code":"1001","msg":"请求方法错误"})
  if not request.POST.get("code"):
    return JsonResponse({"code":"1002","msg":"code为空"})
  else:
    code=request.POST.get("code")
    url="https://api.weixin.qq.com/sns/jscode2session?appid=wx63fd2a9f576da51b&secret=dfe88a92d09fa838f1f59864b5dc9969&js_code="+code+"&grant_type=authorization_code"
    response=requests.get(url)
    print(response.text)
    if not response.text.get('openid'):
      return JsonResponse({"code":"1003","msg":"openid请求错误"})
    else:
      openid=response.get('openid')
    return JsonResponse({"openid",openid}),openid
    
    

  
