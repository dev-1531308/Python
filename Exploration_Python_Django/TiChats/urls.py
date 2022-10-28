from django.urls import path
from .import views

urlpatterns = [   
    path('', views.index_view, name="index"),
    path('ListeChats/', views.list_view, name="ListeChats"),
    path('AdoptionForm/', views.form_view, name="AdoptionForm"),
]