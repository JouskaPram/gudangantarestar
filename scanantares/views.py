from django.shortcuts import render
from scanantares.models import *


def home(req):

    scanner = Scanner.objects.all()
    sortir = Sortir.objects.all()
    total_sortir = Sortir.objects.count()

    
    context = {
        'scanner':scanner,
        'sortir':sortir,
        'total_sort':total_sortir,
    }


    return render(req,'main.html',context)