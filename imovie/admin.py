from django.contrib import admin
from .models import *

# Register your models here.
class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ['aname']
    search_fields = ['aname']
admin.site.register(AreaInfo, AreaInfoAdmin)

class CatalogInfoAdmin(admin.ModelAdmin):
    list_display = ['cname']
    search_fields = ['cname']
admin.site.register(CatalogInfo, CatalogInfoAdmin)


class ResouceInfoAdmin(admin.ModelAdmin):
    list_display = ['rname']
    search_fields = ['rname']
admin.site.register(ResouceInfo, ResouceInfoAdmin)

class PlayerListInfoAdmin(admin.ModelAdmin):
    list_display = ['pname']
    search_fields = ['pname']
admin.site.register(PlayerListInfo, PlayerListInfoAdmin)

