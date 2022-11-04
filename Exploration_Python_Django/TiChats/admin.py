from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = [ 'nom', 'age', 'ageString','activitePref', 'couleur' ,'photo',]
    #list_filter = ['prenom', 'nom', ]
    ordering = [ 'nom', ]
    #readonly_fields = ['nom']
    search_fields = ['nom', 'couleur']

@admin.register(models.Couleur)
class CouleurAdmin(admin.ModelAdmin):
    list_display = [ 'nomCouleur']
    #list_filter = ['prenom', 'nom', ]
    ordering = [ 'nomCouleur', ]
    #readonly_fields = ['nom']
    search_fields = ['nomCouleur']