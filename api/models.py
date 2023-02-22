from django.db import models
from datetime import datetime

GENDER_CHOICES=(
  ('m','male'),
  ('f','female'),
)

LEVEL_CHOICES=(
  ('stone','青铜'),
  ('silver','白银'),
  ('gold','黄金'),
  ('diamond','钻石'),
  ('king','王者')
)

class User(models.Model):

    openid=models.CharField(max_length=100,unique=True,primary_key=True)
    nickname=models.CharField(max_length=32,blank=True,null=True)
    phone=models.CharField(max_length=11,null=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True,null=True)
    birth=models.DateField(blank=True,null=True)
    level=models.CharField(max_length=16,choices=LEVEL_CHOICES,blank=True,null=True)
    created=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['created']

    def __str__(self):
        return self.openid


class Goods(models.Model):
    id=models.CharField(max_length=30,unique=True,primary_key=True)
    goodsName=models.CharField(max_length=30,unique=True)
    goodsRemark=models.TextField(null=True)
    goodsPrice=models.DecimalField(max_digits=7,decimal_places=2,default=0)
    goodsCategoryId=models.ForeignKey('GoodsCategory',on_delete=models.CASCADE) #分类删除则菜品也删除
    goodsSale=models.IntegerField(default=0)
    goodsPic=models.CharField(max_length=100,blank=True,null=True)

    class Meta:
       verbose_name="商品信息"
       verbose_name_plural=verbose_name
    
    def __str__(self):
      return self.goodsName

class GoodsCategory(models.Model):
    category=models.CharField(max_length=30,unique=True,help_text="类别名")
    id=models.AutoField(primary_key=True,unique=True,help_text="类别code")
    desc=models.TextField(help_text="类别描述",null=True)
    add_time=models.DateTimeField(default=datetime.now)

    class Meta:
       verbose_name="商品类别"
       verbose_name_plural=verbose_name

    def __str__(self):
      return self.category
