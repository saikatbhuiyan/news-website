from django.db import models


class Main(models.Model):
  """Create main object"""
  name = models.TextField()
  about = models.TextField()
  fb = models.TextField()
  yt = models.TextField()
  tw = models.TextField()

  def __str__(self):
    return self.name