from django.db import models
from django.db.models.functions import Now
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import uuid


#chestiile relevante la proiect
class Cooler(models.Model):
    id = models.AutoField(primary_key=True)  # Auto incrementing primary key
    pret = models.DecimalField(max_digits=10, decimal_places=2)  # Price with two decimal places
    frecventa = models.PositiveIntegerField()  # Frequency in Hz or RPM (Positive integer)

    def __str__(self):
        return f"Cooler {self.id}, Pret: {self.pret}, Frecventa: {self.frecventa}"

# Processor Model (CPU)
class CPU(models.Model):
    class Fabricant(models.TextChoices):
        INTEL = 'Intel', 'Intel'
        AMD = 'AMD', 'AMD'

    id = models.AutoField(primary_key=True)  # Auto incrementing primary key
    fabricant = models.CharField(max_length=10, choices=Fabricant.choices)  # Intel or AMD
    model = models.TextField()  # Model name/identifier
    generatie = models.IntegerField()  # Generation number
    pret = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the CPU

    def __str__(self):
        return f"CPU {self.id}, {self.fabricant} {self.model}, Generation: {self.generatie}"

# SSD Model
class SSD(models.Model):
    id = models.AutoField(primary_key=True)  # Auto incrementing primary key
    pret = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the SSD
    dimensiune = models.PositiveIntegerField()  # Size of SSD in GB
    fabricant = models.CharField(max_length=100)  # Manufacturer of the SSD

    def __str__(self):
        return f"SSD {self.id}, Pret: {self.pret}, Dimensiune: {self.dimensiune}GB"

# Calculator Model
class Calculator(models.Model):
    id = models.AutoField(primary_key=True)  # Auto incrementing primary key
    dataLansare = models.DateField()  # Launch date of the calculator
    pret = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the calculator
    descriere = models.TextField()  # Description of the calculator
    peStoc = models.BooleanField()  # Whether it's in stock
    RAM = models.IntegerField()  # RAM size in GB
    idSSD = models.ForeignKey(SSD, on_delete=models.CASCADE)  # Foreign key relation to SSD
    idProcesor = models.ForeignKey(CPU, on_delete=models.CASCADE)  # Foreign key relation to CPU

    def __str__(self):
        return f"Calculator {self.id}, Pret: {self.pret}, RAM: {self.RAM}GB, {self.descriere[:30]}..."

# Graphics Card Model (Placa Grafica)
class PlacaGrafica(models.Model):
    id = models.AutoField(primary_key=True)  # Auto incrementing primary key
    cores = models.IntegerField()  # Number of cores in the GPU
    fabricant = models.CharField(max_length=100)  # Manufacturer of the GPU
    frecventa = models.IntegerField()  # Frequency in MHz or GHz
    pret = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the graphics card

    def __str__(self):
        return f"Placa Grafica {self.id}, Cores: {self.cores}, Pret: {self.pret}"
# Create your models here.

class CustomUser(AbstractUser):
    telefon = models.CharField(max_length=15, blank=True)
    zipcode = models.CharField(max_length=6, blank=True)
    oras=models.CharField(max_length=30, blank=True)
    strada=models.CharField(max_length=50, blank=True)
    nr=models.PositiveIntegerField(default=1) #e un numar de casa, sau o cladire
    stay_logged_in = models.BooleanField(
        blank=True
    )