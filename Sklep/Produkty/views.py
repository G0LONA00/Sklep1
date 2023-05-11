from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty, Kategoria


def index(request):
    wszystkie = Produkty.objects.all()
    jeden = Produkty.objects.get(pk=3)
    kat = Produkty.objects.filter(kategoria = 2)
    producent = Produkty.objects.filter(producent=2)
    kat_name = Kategoria.objects.get(id = 2)
    kategorie = Kategoria.objects.all
    null = Produkty.objects.filter(kategoria__isnull=True)
    zawiera = Produkty.obejcts.filter(opis__icontains='dysk')

    #return HttpResponse(wszystkie)
    context = { 'wszystkie' : wszystkie,
                'kategorie' : kategorie,}
    return render(request, 'szablon.html', context)