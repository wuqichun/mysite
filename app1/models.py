from django.db import models

# Create your models here.

class t_goods(models.Model):
    """create a project list"""
    class Meta:
        db_table = 't_goods'
    goods_id = models.AutoField(max_length=11, db_column="goods_id", primary_key=True)
    goods_name = models.CharField(max_length=255, db_column="goods_name", blank=True)
    goods_price = models.DecimalField(max_length=100, max_digits=3, decimal_places=1, db_column="goods_price", blank=True)

