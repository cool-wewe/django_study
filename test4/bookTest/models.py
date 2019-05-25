# coding=utf-8
from django.db import models


# Create your models here.
class BookInfo(models.Model):
    btittle = models.CharField(max_length=30)  # 设置书名字段，设置该字段的最长为30
    bpub_date = models.DateTimeField(db_column="pub_date")  # 设置出版日期字>    段，设置该字段在数据库中的字段名
    bread = models.IntegerField(default=0)  # 设置阅读量字段，设置初值为0
    bcommet = models.IntegerField(null=False)  # 设置点击量字段，设置不允许为空
    isDelete = models.BooleanField(default=False)  # 设置逻辑删除字段，设置初始值为False

    class Meta:
        db_table = "bookinfo"  # 设置表名
        ordering = ["-id"]  # 设置以id逆序排序

    def __str__(self):
        return self.btittle


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def show_name(self):
        return self.hname

    def __str__(self):
        return self.hname
