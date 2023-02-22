from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import User,GoodsCategory,Goods

class GoodsCategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model=GoodsCategory
    fields=['category','id']

class GoodsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model=Goods
    fields=['id','goodsName','goodsRemark','goodsPrice','goodsCategoryId','goodsPic','goodsSale','goodsSale']
