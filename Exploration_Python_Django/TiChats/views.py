from multiprocessing import context
from optparse import Values
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models

# Create your views here.
def index_view(request): return render(request,'TiChats/index.html')
def list_view(request):
    chats = models.Chat.objects.all().values()
    context = {
        'list_chats': chats
    }
    return render(request,'TiChats/ListeChats.html', context)


def form_view(request): return render(request,'TiChats/AdoptionForm.html')
