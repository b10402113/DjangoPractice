from django.contrib import admin
from .models import *
class HeroInfoInline(admin.TabularInline):#給bookinfoadmin的inlines用的,這樣就能在新增書本的同時新增英雄
    model = HeroInfo  #要嵌入甚麼進去
    extra = 3



class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle'] #篩選
    search_fields = ['id'] #以id來搜索
    list_per_page = 5 #一頁顯示幾個
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline]

# Register your models here.
#註冊booktest模型
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)