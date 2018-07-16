from django.contrib import admin
from .models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','image','image_url','user','content','created','update']
    list_filter = ['created']

admin.site.register(News, NewsAdmin)
