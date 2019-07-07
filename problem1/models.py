from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LatestArrayModel(BaseModel):
    """ 对应题目的table1 """
    array = models.TextField()  # 存储json序列化的数组

    class Meta:
        db_table = 'problem1_table1'


class SaveArrayModel(BaseModel):
    array = models.TextField()  # 存储json序列化的数组

    class Meta:
        db_table = 'problem1_table2'
