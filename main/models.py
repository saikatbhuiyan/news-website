from django.db import models


class Main(models.Model):
  """Create main object"""
  name = models.CharField(max_length=255, default='-')
  about = models.CharField(max_length=255, default='-')
  fb = models.CharField(max_length=255, default='-')
  yt = models.CharField(max_length=255, default='-')
  tw = models.CharField(max_length=255, default='-')
  set_name = models.CharField(max_length=255, default='-')
  tell = models.CharField(max_length=255, default='-')
  link = models.CharField(max_length=255, default='-')

  def __str__(self):
    return self.set_name + " | " + str(self.pk)