
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):    
    context = { 
        'title':'E-commerce FIT',
        'paragrafo1':'Primeiro parágrafo',
        'paragrafo2':'Segundo parágrafo',

    }
    return render  (request,"index.html", context)   

def login(request):
    if request.method =="GET":
        print("Aceso via GET")
    else:
        print("\nAcesso via POST/n")
        print("Acesso via POST com usuário",
        request.POST.get("usuario"),
        "e senha", 
        request.POST.get("senha"))


    return render (request, "login.html")