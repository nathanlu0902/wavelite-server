from rest_framework import serializers
from api.models import User,GoodsCategory,Goods

class GoodsCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model=GoodsCategory
    fields='__all__'

class GoodsSerializer(serializers.ModelSerializer):
  class Meta:
    model=Goods
    fields='__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields='__all__'