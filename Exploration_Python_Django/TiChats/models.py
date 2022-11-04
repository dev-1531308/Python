from asyncio.windows_events import NULL
from email.policy import default
from logging import PlaceHolder
from operator import truediv
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Couleur(models.Model):
    nomCouleur = models.CharField(max_length=50)

    def __str__(self):
        return self.nomCouleur

class Chat(models.Model):
  nom = models.CharField(max_length=50)
  age = models.IntegerField()
  ageString = models.CharField(max_length=50,default='Ans')
  activitePref = models.CharField(max_length=50)
  couleur = models.ForeignKey(Couleur,on_delete=models.CASCADE,null= True)
  photo = models.ImageField(upload_to='TiChats/', blank= False,default='placeholder.jpg')
  #https://www.javatpoint.com/django-image-upload regarder pour image upload

  def __str__(self):
    return self.nom + ' ' + self.nom

