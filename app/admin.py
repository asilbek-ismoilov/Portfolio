from django.contrib import admin
from .models import ResumeCategory, Resume, WorkCategory, Work, Blog, Contact
from django.utils.html import format_html

admin.site.register((ResumeCategory, Resume, WorkCategory, Work, Contact)) 

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('img','title','category_name')
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))

    def category_name(self, obj):
        return obj.category.name