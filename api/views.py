from django.http import Http404
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import User,Goods,GoodsCategory
from .serializers import GoodsCategorySerializer,GoodsSerializer,UserSerializer
from rest_framework import viewsets,permissions,generics
from rest_framework.views import APIView
from rest_framework import status


class UserView(APIView):
  #不设置qs会导致错误？
  queryset=User.objects.all()

  def get_object(self,openid):
    try:
      return User.objects.get(openid=openid)
    except User.DoesNotExist:
      raise Http404
  
  # def get_object(self,openid):
  #   try:
  #     return User.objects.get(pk=openid)
  #   except User.DoesNotExist:
  #     raise Http404

  # def get(self,openid,format=None):
  #   user=self.get_user(openid)
  #   serializer=UserSerializer(user)
  #   return Response(serializer.data)

  def post(self,request,openid):
    serializer=UserSerializer(data=openid)
    # if self.get_object(openid):
    #   Response(serializer.data,status=status.HTTP_409_CONFLICT)
    if serializer.is_valid(): 
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self,request,openid,format=None):
    user=self.get_object(openid)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  

class UserDetailView(APIView):
  def get_object(self,openid):
    try:
      return User.objects.get(pk=openid)
    except User.DoesNotExist:
      raise Http404

  def get(self,openid,format=None):
    user=self.get_object(openid)
    serializer=UserSerializer(user)
    return Response(serializer.data)
  
  def put(self,request,openid,format=None):
    user=self.get_object(openid)
    serializer=UserSerializer(user,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  



#该方法禁用csrf
# @csrf_exempt
# def login(request):
#   openid=getOpenId(request)
#   try:
#     user=User.objects.get(openid=openid)
#   except User.DoesNotExist:
#     return JsonResponse({
#       "code":"1004",
#       "msg":"User is not existed",
#       "openid":openid
#       })
#   else:
#     return JsonResponse({
#       "code":"1005",
#       "nickname":user.nickname,
#       "phone":user.phone,
#       "birth":user.birth,
#       "openid":user.openid
#       })


# @csrf_exempt
# def registerUser(request):
#   if request.method!="POST":
#     return JsonResponse({"code":"1001","msg":"wrong request method"})
#   # nickname=request.POST.get("nickname")
#   phone=request.POST.get("phone")
#   # gender=request.POST.get("gender")
#   openid=request.POST.get("openid")
#   user=User(phone=phone,openid=openid)
#   user.save()
#   print("user is created with userid:",openid)
#   return JsonResponse({"code":"1006","msg":"user is created"})


# @csrf_exempt
# def updateUser(request):
#   if request.method!="POST":
#     return JsonResponse({"code":"1001","msg":"wrong request method"})
#   openid=request.POST.get("openid")
#   print("server to lookup openid:"+openid)
#   try:
#     user=User.objects.get(openid=openid)
#   except user.DoesNotExist:
#     return JsonResponse({"code":"1004","msg":"User is not existed"})
#   else:
#     print("found user with openid:"+user.openid)
#     #查找并更新数据库个人信息
#     try:
#       user.nickname=request.POST.get("nickname")
#       user.phone=request.POST.get("phone")
#       user.gender=request.POST.get("gender")
#       user.birth=request.POST.get("birth")
#       print("received",request.POST.get("birth"))
#       # user=User(phone=phone,nickname=nickname,gender=gender)
#       user.save()
#       return JsonResponse({"code":"1007","msg":"User info updated"})
#     except Exception as e:
#       return JsonResponse({"code":"1008","msg":e})
  
    

# def getOpenId(request):
#   if request.method!="POST":
#     return JsonResponse({"code":"1001","msg":"wrong request method"})
#   else:
#     code=request.POST.get("code","0")
#     print("server received code:"+code)
#     if code=="0":
#       return JsonResponse({"code":"1002","msg":"code is empty"})

#     url="https://api.weixin.qq.com/sns/jscode2session?appid=wx63fd2a9f576da51b&secret=dfe88a92d09fa838f1f59864b5dc9969&js_code="+code+"&grant_type=authorization_code"
   
#     try:
#       response=requests.get(url).json()
#     except requests.exceptions.JSONDecodeError:
#       return JsonResponse({"code":"1003","msg":"openid request error"})
#     else:
#       openid=response['openid']
#       print("server received openid"+openid)
#       return openid

class GoodsCategoryViewSet(viewsets.ModelViewSet):
  queryset=GoodsCategory.objects.all()
  serializer_class=GoodsCategorySerializer
  # permission_classes=[permissions.IsAuthenticated]

class GoodsViewSet(viewsets.ModelViewSet):
  queryset=Goods.objects.all()
  serializer_class=GoodsSerializer
  # permission_classes=[permissions.IsAuthenticated]

# class UserViewSet(viewsets.ModelViewSet):
#   def lookupUser(openid):
#     queryset=GoodsCategory.objects.filter(openid=openid)
#   serializer_class=UserSerializer
  # permission_classes=[permissions.IsAuthenticated]

# class UserCreateAPIView(generics.CreateAPIView):
#   queryset=User.objects.all()
#   serializer_class=UserSerializer

# create_user_view=UserCreateAPIView.as_view()

# class UserUpdateAPIView(generics.UpdateAPIView):
#   serializer_class=UserSerializer
#   lookup_field="openid"

#   def perform_update(self, instance):
#     if not instance.
#     return super().perform_update(serializer) 

# update_user_view=UserUpdateAPIView.as_view()