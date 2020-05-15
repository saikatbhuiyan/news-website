from django.db import models


class Main(models.Model):
  """Create main object"""
  name = models.CharField(max_length=255, default='-')
  about = models.CharField(max_length=255, default='-')
  about = models.TextField(default='-')
  abouttxt = models.CharField(max_length=255, default='-')
  fb = models.CharField(max_length=255, default='-')
  yt = models.CharField(max_length=255, default='-')
  tw = models.CharField(max_length=255, default='-')
  set_name = models.CharField(max_length=255, default='-')
  tell = models.CharField(max_length=255, default='-')
  link = models.CharField(max_length=255, default='-')
  picurl = models.TextField(default="")
  picname = models.TextField(default="")
  picurl2 = models.TextField(default="")
  picname2 = models.TextField(default="")

  def __str__(self):
    return self.set_name + " | " + str(self.pk)