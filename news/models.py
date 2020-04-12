from django.db import models


class News(models.Model):

  name = models.CharField(max_length=50)
  short_txt = models.TextField()
  body_txt = models.TextField()
  date = models.CharField(max_length=12)
  pic = models.TextField()
  writer = models.CharField(max_length=50)


  def __str__(self):
    return self.name