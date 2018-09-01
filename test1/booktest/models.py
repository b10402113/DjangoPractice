from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)#映射數據庫的表結構
    bpub_date = models.DateTimeField()
    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook=models.ForeignKey('BookInfo')#引用bookinfo的
    def __str__(self):
        return self.hname
# class Person():
#     def __str__(self):
#         return 'abc'
# p=Person()
# p.age = 18
