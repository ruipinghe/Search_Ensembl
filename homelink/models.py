from django.db import models

# Create your models here.


class HouseInfo(models.Model):
    dbname = models.CharField(max_length=256, verbose_name='dbname',default='human')
    dbtype = models.CharField(max_length=20, verbose_name='dbtype',default='core')

    def __str__(self):
        return "{}-{}".format(self.dbname,self.dbtype)

    class Meta:
        verbose_name = "datbase"



