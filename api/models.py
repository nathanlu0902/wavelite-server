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

    userid=models.CharField(max_length=10,primary_key=True,unique=True)
    openid=models.CharField(max_length=100,null=True)
    username=models.CharField(max_length=32,blank=True,null=True)
    phonenumber=models.CharField(max_length=11,null=True)
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True,null=True)
    birth=models.DateField(blank=True,null=True)
    level=models.CharField(max_length=16,choices=LEVEL_CHOICES,blank=True,null=True)
    created=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=['created']

    def __str__(self):
        return self.userid

