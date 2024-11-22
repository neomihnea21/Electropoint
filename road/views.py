from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm, ComputerForm, CustomUserCreationForm
from .models import Calculator
import re
import time
import json
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
#FETCHING ALL RECORDS, FOR SHOPPING THEM
def computer_list(request):
   computers=Calculator.objects.all()
   return render(request, "forsale.html")#TODO populeaza nitel baza de date
#COMPLAINT FORM, extracted as .json to server
def scriePiese(request):
    if (request.method=='POST'):
       form=ContactForm(request.POST)
       if(form.is_valid()):
          nume=form.cleaned_data['nume']
          email=form.cleaned_data['email']
          mesaj=form.cleaned_data['mesaj']
          filtered_data=form.cleaned_data.pop()
          json_data = json.dumps(form.cleaned_data, indent=4) # e o lista
          nume_log="user"+str(int(time.time()))+".json"
          response = HttpResponse(json_data, content_type="application/json")
          response['Content-Disposition'] = 'attachment; filename='+nume_log
          return response
    else:
       form=ContactForm()
    return render(request, "contact.html", {'form': form})
#INSERT DATA
def showComputer(request):
    if(request.method=='POST'):
        form=ComputerForm(request.POST) # formul are metoda de POST
        if(form.is_valid()):
            form.save() # nu va fi intors ca JSON, ca n-are de ce, e un produs
            return redirect('sent')
    else:
        form=ComputerForm()
    return render(request, "computer.html", {'form': form}) #TODO creeaza inca un template
#STUFF RELATED TO LOGIN/SIGNUP
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
def custom_login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if not form.cleaned_data.get('stay_logged_in'):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(86400)  # 24h            
            return redirect('sent')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})
def sent(request):
    return HttpResponse("Sergio")