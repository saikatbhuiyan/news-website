from django.db import models


class SubCat(models.Model):
  name = models.CharField(max_length=100)
  catname = models.CharField(max_length=100)
  catid = models.IntegerField()

  def __str__(self):
    return self.name