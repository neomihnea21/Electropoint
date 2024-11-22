from django.urls import path


from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("pag1", views.afisare_statica, name="f"),
    path("pag2", views.afisare_statica, name="g"),
    path("pag/<str:cod>", views.aduna_numere),
    path("liste", views.afiseaza_liste),
    path("nume_corect/<str:nume>", views.numeCorecte),
    path("subsir/<str:tokeni>", views.cauta_subsir),
    path("operatii", views.black_ops),
    path("contact", views.scriePiese, name='sent'),
    path("create-computer", views.showComputer),
    path("shop", views.computer_list),
]
