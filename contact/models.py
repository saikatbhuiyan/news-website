from django.db import models

class Contact(models.Model):
  """Create contact object"""
  name = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  txt = models.TextField()
  # date = models.DateField()
  # time = models.TimeField()

  def __str__(self):
    return self.name