from django.urls import path
from django.conf.urls import include
from .import views

urlpatterns = [   
    path('', views.index_view, name="index"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Register/', views.register_view, name="Register"),
    path('ListeChats/', views.list_view, name="ListeChats"),
    path('AfficherChat/<int:id>', views.chat_view, name="AfficherChat"),
    path('AdoptionForm/', views.form_view, name="AdoptionForm"),
    path('AjouterChat/', views.ajouter_chat_view, name="AjouterChat"),
    path('AjouterCouleur/', views.ajouter_couleur_view, name="AjouterCouleur"),
    path('ChatEstAdopted/<int:id>', views.chat_adopted_view, name="ChatEstAdopted"),
    path('ModifierChat/<int:id>', views.modifier_chat_view, name="ModifierChat"),
]