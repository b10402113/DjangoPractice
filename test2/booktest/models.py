from django.db import models
#管理器是用於跟數據庫做交互的
#自定義的管理器
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager,self).get_queryset().filter(isDelete=False)
    def create(self,btitle,bpub_date):
        b=BookInfo()
        b.btitle=btitle
        b.bpub_data=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)
    bcommet=models.IntegerField(null=False)
    isDelete=models.BooleanField(default=False)
    # class Meta:
    #     db_table='bookinfo'
    #一個應用當中可以定義多個管理器
    books1=models.Manager()#原本的管理器
    books2=BookInfoManager()#自己的管理器
    # def __init__(self): 這個會報錯
    #因為創建對象很麻煩，所以自己定義一個方法自己創造物件(對象)
    @classmethod
    def create(cls,btitle,bpub_date):
        b=BookInfo()
        b.btitle=btitle
        b.bpub_data=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b

    # books=models.Manager()
class HeroInfo(models.Model):#booktest_heroinfo
    hname = models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo)#book_id key=MUL
