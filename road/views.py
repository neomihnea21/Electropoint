from django.shortcuts import render
from django.http import HttpResponse
import re
def afisare_statica(request):
    return HttpResponse("Pagina de cale fixa")
def afisare_dinamica(request, no, address, road):
    return HttpResponse(f"Suntem la numarul {no}, adresa{address} si calea{road}")
def index(request):
    return HttpResponse("Arda")
sumInput=0
num_cereri=0
def aduna_numere(request, cod):
    global sumInput
    global num_cereri
    if(re.match("^[a-z0-9]+$", cod)):
        num_cereri+=1
        ans=""
        index=-1
        while(cod[index] in '0123456789' and index>-len(cod)):
            ans+=cod[index]
            index-=1
        if(index==-len(cod)):
            ans+=cod[0]
        ans=ans[::-1]
        sumInput+=int(ans)
    return HttpResponse("numar cereri: " + str(num_cereri)+ "<br> suma cereri bune: "+str(sumInput))
def afiseaza_liste(request): #FINITE INCANTATEM 2
    a=request.GET.getlist("a")
    b=request.GET.getlist("b")
    html="a: <ul>"
    for x in a:     
        html+="<li>"+x+"</li>"
    html+="</ul>b:<ul>"
    for y in b:
        html+="<li>"+y+"</li>"
    html+="</ul>"
    return HttpResponse(html)
nume_citite=0
def numeCorecte(request, nume):
    global nume_citite
    tokens=nume.split("+")
    valid=True
    if(len(tokens)!=2):
        valid=False
    if(valid==True):
        regexFirstName="^[A-Z][a-z]*-?[a-z]*$"
        regexLastName="^[A-Z][a-z]+$"
        prenume=re.compile(regexFirstName)
        nume=re.compile(regexLastName)
        if(re.match(prenume, tokens[0])==False):
            valid=False
        if(re.match(nume, tokens[1])==False):
            valid=False
    if(valid):
        nume_citite+=1
    return HttpResponse(str(nume_citite))
def cauta_subsir(request, tokeni):
    valid=re.match("^\d*[ab]*\d*$", tokeni)
    if(valid):
        sirRedus=tokeni.strip('0123456789')
        return HttpResponse(len(str(sirRedus)))
    else:
        return HttpResponse("String necorespunzator")
def black_ops(request):
    return HttpResponse("e")
def scriePiese(request):
    return HttpResponse("e") #TODO scrie o pagina HTML cum se cuvine aici