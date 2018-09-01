from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^pro/$',views.pro),
    url(r'^city(\d+)/$',views.city),
    url(r'^htmlEditor/$',views.htmlEditer),
url(r'^htmlEditerHandle/$',views.htmlEditerHandle),
    url(r'^cache1/$',views.cache1)
]