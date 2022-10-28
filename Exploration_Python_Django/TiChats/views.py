from django.shortcuts import render

# Create your views here.
def index_view(request): return render(request,'TiChats/index.html')
def list_view(request): return render(request,'TiChats/ListeChats.html')
def form_view(request): return render(request,'TiChats/AdoptionForm.html')