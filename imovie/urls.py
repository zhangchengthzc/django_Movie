#coding = utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
    #/  views.index
    url("^$",views.index)
]