from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import User,GoodsCategory,Goods

class GoodsCategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model=GoodsCategory
    fields='__all__'

class GoodsSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model=Goods
    fields='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model=User
    fields='__all__'