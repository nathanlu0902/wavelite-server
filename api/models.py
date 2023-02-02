from django.db import models

class User(models.Model):

    userid=models.CharField(max_length=10,primary_key=True,unique=True)
    username=models.CharField(max_length=32,blank=True,null=True)
    phonenumber=models.CharField(max_length=11,blank=True,null=True)
    level=models.CharField(max_length=16,blank=True,null=True)
    account_status=models.CharField(max_length=10,blank=True,null=True)
    birth=models.DateField(blank=True,null=True)
    created_by=models.DateField(blank=False)

    GENDER=(
        ('m','male'),
        ('f','female'),
    )

    gender=models.CharField(max_length=1,choices=GENDER,blank=True,null=True)

    class Meta:
        ordering=['created_by']

    def __str__(self):
        return self.userid


class Level(models.Model):
    level=models.CharField(max_length=20)

    def __str__(self):
        return self.name