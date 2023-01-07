from django.shortcuts import render, redirect
from scanantares.models import *
from django.contrib import messages
import datetime


def home(req):
    
    now = datetime.datetime.now()
    total = Sday.objects.count()
    double = Dday.objects.count()
    # scanner = Scanner.objects.all()
    angel = Sortir.objects.filter(scanner='angel').count()
    latif = Sortir.objects.filter(scanner='latif').count()
    fazza = Sortir.objects.filter(scanner='fazza').count()
    antare = Sortir.objects.filter(scanner='antarestar').count()

    context = {
        'total':total,
        'double':double,
        # 'scanner':scanner, 
        'angel':angel,
        'latif':latif,
        'fazza':fazza,
        'antare':antare,  
    }

    if now.hour == 0 and now.minute == 0:
        # Reset the model
        Sday.objects.all().delete()
        Dday.objects.all().delete()
        return redirect('/')


    if req.POST:
        sortir = Sortir()
        double = Double()
        sday = Sday()
        dday = Dday()

        barcode = req.POST.get('barcode')
        scanner = req.POST.get('scanner')


        if Sortir.objects.filter(barcode=barcode).exists():
            messages.warning(req, 'Barcode ini sudah pernah digunakan')
            double.barcode = barcode
            dday.jumlah = barcode
            double.scanner = scanner

            dday.save()
            double.save() 

            return redirect('/')
        else:

            sortir.barcode = barcode
            sday.jumlah = barcode
            sortir.scanner = scanner

            sday.save()
            sortir.save()

            return redirect('/')

        
    
    return render(req,'main.html',context)
