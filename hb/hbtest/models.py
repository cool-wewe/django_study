from django.db import models


# Create your models here.

class BookInfo(models.Model):
    b_title = models.CharField(max_length=50)
    b_pub_date = models.DateTimeField()

    def __str__(self):
        return self.b_title


class HeroInfo(models.Model):
    h_name = models.CharField(max_length=30)
    h_gender = models.BooleanField()
    h_content = models.CharField(max_length=1000)
    h_book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.h_name
