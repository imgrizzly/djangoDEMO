from django.db import models
import django.utils.timezone as timezone

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Order(models.Model):
    orderID=models.AutoField(primary_key=True)
    orderName=models.CharField(max_length=50)
    orderPayee=models.CharField(max_length=50, null=True)
    orderPhone=models.IntegerField(null=True)
    orderAllPrice=models.CharField(max_length=50, null=True)
    orderPrice=models.CharField(max_length=50, null=True)
    orderStatus=models.CharField(max_length=50, null=True)
    orderPayStatus=models.CharField(max_length=50, null=True)
    orderPayType=models.CharField(max_length=50, null=True)
    orderDeliveryStatus=models.CharField(max_length=50, null=True)
    orderDistributionlogistics=models.CharField(max_length=50, null=True)

class  Member(models.Model):
    memberID=models.AutoField(primary_key=True)
    memberName=models.CharField(max_length=50)
    memberGender=models.CharField(max_length=5)
    memberPhone=models.IntegerField(null=True)
    memberEmail=models.CharField(max_length=20)
    memberAddr=models.CharField(max_length=20)
    memberJoinTime=models.DateTimeField(default = timezone.now)
    memberStatus=models.BooleanField(null=True,default=True)

# Create your models here.
