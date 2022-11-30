from multiprocessing import context
from optparse import Values
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from .forms import RegisterForm
from TiChats.forms import ChatForm, CouleurForm
from . import models

# Create your views here.
def index_view(request): 
    chats = models.Chat.objects.all()
    context = {
        'chats': chats
    }    
    return render(request,'TiChats/index.html',context)

def list_view(request):
    chats = models.Chat.objects.all()
    context = {
        'list_chats': chats
    }
    return render(request,'TiChats/ListeChats.html', context)

def chat_view(request, id):
    chat = models.Chat.objects.get(id=id)
    context = {
        'chat': chat
    }
    return render(request,'TiChats/AfficherChat.html', context)

@login_required
def chat_adopted_view(request, id):
    chat = models.Chat.objects.get(id=id)
    context = {
        'chat': chat
    }
    if request.method == 'POST':
        chat.delete()
        return redirect('ListeChats')
    return render(request,'TiChats/ChatEstAdopted.html',context)

@login_required
def form_view(request):
    return render(request,'TiChats/AdoptionForm.html')  

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

def modifier_chat_view(request, id):
    chat = models.Chat.objects.get(id=id)
    if request.method == 'POST':
        AjouterChat = ChatForm(request.POST, instance=chat)
        if AjouterChat.is_valid():
            # update the existing `Band` in the database
            AjouterChat.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('ListeChats')
    else:
        AjouterChat = ChatForm(instance=chat)

    return render(request,'TiChats/ModifierChat.html', {'form': AjouterChat})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('Index')
    else:
        form = RegisterForm()
    
    return render(request, 'TiChats/Register.html', {'form': form})