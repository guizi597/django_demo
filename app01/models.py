from django.db import models

# Create your models here.

class Department(models.Model):
    """部门表"""

    title = models.CharField(verbose_name='标题',max_length=32)

class UserInfo(models.Model):
    """员工表"""
    name = models.CharField(verbose_name='姓名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    account = models.DecimalField(verbose_name='账户余额',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name='入职时间')

    city = models.CharField(verbose_name='城市',max_length=64)
    country = models.CharField(verbose_name='国家',max_length=64)
    girlfriend = models.CharField(verbose_name='女朋友',max_length=64)
    boyfriend = models.CharField(verbose_name='男朋友', max_length=64)
