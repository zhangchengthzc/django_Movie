from django.db import models
from tinymce.models import HTMLField

# Create your models here.

#地区
class AreaInfo(models.Model):
     aname=models.CharField(max_length=255,verbose_name="地区")
     def __str__(self):
         return self.aname
     class Meta:
         verbose_name_plural="地区管理"

#类型
class CatalogInfo(models.Model):
    cname=models.CharField(max_length=255,verbose_name="类型名称")
    cremark=models.TextField(verbose_name="备注")
    def __str__(self):
        return self.cname
    class Meta:
        verbose_name_plural="类型管理"

#资源
class ResouceInfo(models.Model):
    RESTYPE_CHOICE = (
        (u'M', u'电影'),
        (u'T', u'电视剧'),
    )
    rname=models.CharField(max_length=1000,verbose_name="电影名称")
    director=models.CharField(max_length=1000,verbose_name="导演")
    scriptwriter=models.CharField(max_length=1000,verbose_name="编剧")
    actor=models.CharField(max_length=2000,verbose_name="演员")
    area=models.ForeignKey(AreaInfo,on_delete=models.CASCADE,verbose_name="产地")
    lanuage=models.CharField(max_length=255,verbose_name="语言")
    publishdate=models.DateField(verbose_name="上映时间")
    length=models.IntegerField(verbose_name="片长")
    othername=models.CharField(max_length=1000,verbose_name="其他名字")
    score=models.FloatField(verbose_name="评分")
    issupreme=models.BooleanField(default=False,verbose_name="是否精选")
    restype = models.CharField(choices=RESTYPE_CHOICE,max_length=10,verbose_name="资源类型")
    pic=models.ImageField(upload_to='use_image/%Y/%m/%d',default='image/default.png',
max_length=100,verbose_name='海报',blank=True,null=True)
    context=HTMLField("请输入资源的简介",null=True)
    catalog=models.ManyToManyField(CatalogInfo,verbose_name="影片类型")
    def __str__(self):
        return self.rname
    class Meta:
        verbose_name_plural="资源管理"


#分集 TC HD BD
class PlayerListInfo(models.Model):
    RESTYPE_CHOICE = (
        (u'XIGUA', u'西瓜影音'),
        (u'JIJI', u'吉吉影音'),
        (u'ONLINE', u'在线播放'),
    )
    ptype=models.CharField(max_length=255,verbose_name="清晰程度")
    purl=models.CharField(max_length=2000,verbose_name="播放地址")
    pname=models.CharField(max_length=1000,verbose_name="分集名称")
    restype = models.CharField(choices=RESTYPE_CHOICE,max_length=100,verbose_name="播放方式")
    def __str__(self):
        return self.pname
    class Meta:
        verbose_name_plural="分集管理"