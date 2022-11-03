from multiprocessing import context
from optparse import Values
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from TiChats.forms import ChatForm, CouleurForm
from . import models

# Create your views here.
def index_view(request): return render(request,'TiChats/index.html')
def list_view(request):
    chats = models.Chat.objects.all()
    context = {
        'list_chats': chats
    }
    return render(request,'TiChats/ListeChats.html', context)


def form_view(request): return render(request,'TiChats/AdoptionForm.html')

def ajouter_chat_view(request):
    if request.method == "POST":
        AjouterChat = ChatForm(request.POST, request.FILES)

        if (AjouterChat.is_valid()):
            AjouterChat.save()
            return redirect('ListeChats')
        context = {
            'form': AjouterChat
        }
    else:
        context = {
            'form' : ChatForm()
        }
        
    return render(request,'TiChats/AjouterChat.html',context)

def ajouter_couleur_view(request):
    if request.method == "POST":
        AjouterChat = CouleurForm(request.POST, request.FILES)

        if (AjouterChat.is_valid()):
            AjouterChat.save()
            return redirect('AjouterChat')
        context = {
            'form': AjouterChat
        }
    else:
        context = {
            'form' : CouleurForm()
        }
        
    return render(request,'TiChats/AjouterCouleur.html',context)
