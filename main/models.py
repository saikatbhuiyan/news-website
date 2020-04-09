from django.db import models


class Main(models.Model):
  """Create main object"""
  name = models.TextField()
  about = models.TextField()

  def __str__(self):
    return self.name