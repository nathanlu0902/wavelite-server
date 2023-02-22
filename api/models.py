from django.db import models

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
    
    def __str__(self):
      return self.id

class GoodsCategory(models.Model):
    category=models.CharField(max_length=30,unique=True)
    id=models.AutoField(primary_key=True,unique=True)

    def __str__(self):
      return self.category
