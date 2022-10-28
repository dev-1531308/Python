from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Chat(models.Model):
  nom = models.CharField(max_length=50)
  age = models.IntegerField()
  activitePref = models.CharField(max_length=50)
  couleur = models.CharField(max_length=50)
  photo = models.CharField(max_length=50)

  def __str__(self):
    return self.nom + ' ' + self.nom