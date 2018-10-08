from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Olá, mundo")
    #return render(request, "index.html")
    if request.method == "GET":
        print("Acesso via GET")
    else:
        print("Acesso via POST com usuário",
        request.POST.get("usuario"), "e senha",
        request.POST.get("senha"))

    return render(request, "login.html")
