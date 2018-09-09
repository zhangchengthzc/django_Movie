# Generated by Django 2.1.1 on 2018-09-09 07:51

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=255, verbose_name='地区')),
            ],
            options={
                'verbose_name_plural': '地区管理',
            },
        ),
        migrations.CreateModel(
            name='CatalogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255, verbose_name='类型名称')),
                ('cremark', models.TextField(verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '类型管理',
            },
        ),
        migrations.CreateModel(
            name='PlayerListInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=255, verbose_name='清晰程度')),
                ('purl', models.CharField(max_length=2000, verbose_name='播放地址')),
                ('pname', models.CharField(max_length=1000, verbose_name='分集名称')),
                ('restype', models.CharField(choices=[('XIGUA', '西瓜影音'), ('JIJI', '吉吉影音'), ('ONLINE', '在线播放')], max_length=100, verbose_name='播放方式')),
            ],
            options={
                'verbose_name_plural': '分集管理',
            },
        ),
        migrations.CreateModel(
            name='ResouceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rname', models.CharField(max_length=1000, verbose_name='电影名称')),
                ('director', models.CharField(max_length=1000, verbose_name='导演')),
                ('scriptwriter', models.CharField(max_length=1000, verbose_name='编剧')),
                ('actor', models.CharField(max_length=2000, verbose_name='演员')),
                ('lanuage', models.CharField(max_length=255, verbose_name='语言')),
                ('publishdate', models.DateField(verbose_name='上映时间')),
                ('length', models.IntegerField(verbose_name='片长')),
                ('othername', models.CharField(max_length=1000, verbose_name='其他名字')),
                ('score', models.FloatField(verbose_name='评分')),
                ('issupreme', models.BooleanField(default=False, verbose_name='是否精选')),
                ('restype', models.CharField(choices=[('M', '电影'), ('T', '电视剧')], max_length=10, verbose_name='资源类型')),
                ('pic', models.ImageField(blank=True, default='image/default.png', null=True, upload_to='use_image/%Y/%m/%d', verbose_name='海报')),
                ('context', tinymce.models.HTMLField(null=True, verbose_name='请输入资源的简介')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovie.AreaInfo', verbose_name='产地')),
                ('catalog', models.ManyToManyField(to='imovie.CatalogInfo', verbose_name='影片类型')),
            ],
            options={
                'verbose_name_plural': '资源管理',
            },
        ),
    ]
