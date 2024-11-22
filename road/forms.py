from django import forms
from .models import Calculator, CustomUser
import json
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class ContactForm(forms.Form): # asta oricum se pune in absolut orice
    CHOICES=[
        ('REC', 'Reclamatie'),
        ('QUE', 'Intrebare'),
        ('RV', 'Review'),
        ('RQS', 'Cerere'),
        ('APP', 'Programare'),
    ]
    nume = forms.CharField(max_length=10, label='Nume', required=True)
    prenume=forms.CharField(max_length=20, label='Prenume', required=True)
    #data_nasterii=forms.DateField(label='Data nasterii')
    subiect=forms.CharField(label='Subiect', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    confirm_email=forms.EmailField(label='Confirma Email', required=True)
    timp_asteptare=forms.IntegerField(min_value=1, label='Timp Asteptare')
    tip = forms.ChoiceField(choices=CHOICES)
    mesaj=forms.CharField(label="Mesaj", required=True,
                          widget=forms.Textarea(attrs={'rows': 14, 'cols': 60}))
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@domeniu.com'):
            raise forms.ValidationError("Adresa de email trebuie să fie de la domeniu.com")
        return email
    #def clean_birth(self):
    #    dob=self.cleaned_data.get('data_nasterii')
    #    if(dob): #poate ca nu a dat-o nimeni
    #        today=date.today()
    #        age=today.year-dob.year+((today.month, today.day)<(dob.month, dob.day))
    #        if(age<18):
    #            raise forms.ValidationError("Nu puteti fi client, sunteti minor")
    def clean_message(self):
        mesaj=self.cleaned_data.get('mesaj')
        cuvinte=mesaj.split(' ')
        if(len(cuvinte)<5 or len(cuvinte)>100):
            raise forms.ValidationError("Mesajul are lungime nepotrivita")
        if(re.match('^(.*http).*', mesaj)): # TODO make better regex for checking a link
            raise forms.ValidationError("Mesajul are un link, e spam")
    def test_mailuri(self):
        mail1=self.cleaned_data.get('email')
        mail2=self.cleaned_data.get('confirm_email')
        if(mail1 != mail2):
            raise form.ValidationError("Nu se potrivesc emailurile")

    def export_to_json(self, cale="form_data.json"):
        if not self.is_valid():
            raise ValueError("Form data is not valid. Cannot export.")
        form_data = self.cleaned_data
        with open(cale, "w") as json_file:
            json.dump(form_data, json_file, indent=4)
        return cale
class ComputerForm(forms.ModelForm): 
    class Meta:
        model=Calculator
        fields=['id', 'dataLansare', 'pret', 'RAM']
class CustomUserCreationForm(UserCreationForm):
    telefon = forms.CharField(required=True)
    class Meta:
        model = CustomUser
        fields = ("username","email", "telefon", "password1", "password2", "telefon", "oras"
        ,"strada", "zipcode","nr", "stay_logged_in")
    def save(self, commit=True):
        user = super().save(commit=False)
        user.telefon = self.cleaned_data["telefon"]
        if commit:
            user.save()
        return user
    def clean_telefon(self):
        tel=self.cleaned_data.get("telefon")
        if(len(tel)<10):
            raise form.ValidationError("Numar de telefon nepotrivit")
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model=CustomUser 
        fields=("username", "password1", "stay_logged_in")