from django.db import models
#管理器是用於跟數據庫做交互的
#自定義的管理器


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcommet=models.IntegerField(null=False)
    isDelete=models.BooleanField(default=False)
    #一個應用當中可以定義多個管理器


    # books=models.Manager()
class HeroInfo(models.Model):#booktest_heroinfo
    hname = models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo)#book_id key=MUL

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(max_length=10)
    upwd=models.CharField(max_length=40)
    isDelete=models.BooleanField()
class AreaInfo(models.Model):
    aid = models.IntegerField(primary_key=True)
    atitle = models.CharField(max_length=20)
    aPArea = models.ForeignKey('AreaInfo', null=True,blank=True)