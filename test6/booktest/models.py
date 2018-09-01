from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class AreaInfo(models.Model):
    aid = models.IntegerField(primary_key=True)
    atitle = models.CharField(max_length=20)
    aPArea = models.ForeignKey('AreaInfo',null=True,blank=True)

class Test1(models.Model):
    content=HTMLField()
