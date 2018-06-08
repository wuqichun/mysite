from django.db import models

# Create your models here.

class manage_ad(models.Model):
    """create a project list"""
    class Meta:
        db_table = 'manage_ad'

    id = models.AutoField(max_length=100, db_column="id", primary_key=True)
    image = models.CharField(max_length=500, db_column="image", blank=True)
    replacead = models.CharField(max_length=100, db_column="replacead", blank=True)
    removead = models.CharField(max_length=100, db_column="removead", blank=True)

