from django.db import models


class Category(models.Model):
  """Create Category object"""
  name = models.CharField(max_length=255, default='-')

  def __str__(self):
    return self.name + " | " + str(self.pk)