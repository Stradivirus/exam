from django.db import models

class BaseTable(models.Model):
    col1 = models.IntegerField()

    class Meta:
        abstract = True

class PDF1(BaseTable):
    col2 = models.IntegerField()

class PDF2(BaseTable):
    col3 = models.IntegerField()

class PDF3(BaseTable):
    col4 = models.IntegerField()

class PDF4(BaseTable):
    col5 = models.IntegerField()
