from django.http import Http404
from rest_framework.response import Response
import requests
from .models import User,Goods,GoodsCategory
from .serializers import GoodsCategorySerializer,GoodsSerializer,UserSerializer
from rest_framework import viewsets,status,permissions,generics
from rest_framework.views import APIView


class UserView(APIView):

  def get_object(self,openid):
    try:
      return User.objects.get(openid=openid)
    except User.DoesNotExist:
      raise Http404

  #request不能不写
  def get(self,request,wx_code,format=None):
    openid=get_openid(wx_code)
    if not openid:
      return Response("Error when getting openid")
    user=self.get_object(openid)
    serializer=UserSerializer(user)
    return Response(serializer.data)

  def put(self,request,openid,format=None):
    user=self.get_object(openid)
    serializer=UserSerializer(user,data=request.data)
    #打印错误
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def post(self,request):
    #wx_code换成openid写入数据库
    wx_code=request.data.wx_code
    openid=get_openid(wx_code)
    request.data.openid=openid
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): 
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,openid,format=None):
    user=self.get_object(openid)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  
def get_openid(wx_code):
  url="https://api.weixin.qq.com/sns/jscode2session?appid=wx63fd2a9f576da51b&secret=dfe88a92d09fa838f1f59864b5dc9969&js_code="+wx_code+"&grant_type=authorization_code"
  try:
    response=requests.get(url).json()
  except requests.exceptions.JSONDecodeError:
    return
  else:
    openid=response['openid']
    return openid

class GoodsCategory(APIView):
  def get():
    queryset=GoodsCategory.objects.all()
    serializer=GoodsCategorySerializer(queryset)
    Response(serializer)

class GoodsCategoryViewSet(viewsets.ModelViewSet):
  queryset=GoodsCategory.objects.all()
  serializer_class=GoodsCategorySerializer
  # permission_classes=[permissions.IsAuthenticated]

class GoodsViewSet(viewsets.ModelViewSet):
  queryset=Goods.objects.all()
  serializer_class=GoodsSerializer
  # permission_classes=[permissions.IsAuthenticated]
