from django.contrib import admin
from .models import BookInfo, HeroInfo


# Register your models here.
# 实现关联注册类，由于BookInfo被HeroInfo类关联使用
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3


class BookInfoAdmin(admin.ModelAdmin):
    # 设置列表显示项
    list_display = ["id", "b_title", "b_pub_date"]
    # 设置过滤器的过滤项
    list_filter = ["b_title"]
    # 设置搜索首选项
    search_fields = ["b_title"]
    # 设置一页显示项的数量
    list_per_page = 10
    # 设置修改和添加页分组
    fieldsets = [
        ("basic", {"fields": ["b_title"]}),
        ("more", {"fields": ["b_pub_date"]})
    ]
    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "h_name", "h_gender", "h_content", "h_book"]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
