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
def second(req):
    current_time = timezone.now()

    # if req.session.get('current_day') != current_time.date():
    #     req.session['count'] = 0
    # req.session['current_day'] = current_time.date()
    

    # scanner = Scanner.objects.all()
    total = Sortir.objects.count()
    double = Double.objects.count()
    angle = Sortir.objects.filter(scanner='angle').count()
    latif = Sortir.objects.filter(scanner='latif').count()
    fazza = Sortir.objects.filter(scanner='fazza').count()
    antare = Sortir.objects.filter(scanner='antarestar').count()

    context = {
        # 'scanner':scanner, 
        'total':total,
        'double':double,
        'angle':angle,
        'latif':latif,
        'fazza':fazza,
        'antare':antare,
            
    }

    if req.POST:
        sortir = Sortir()
        double = Double()

        barcode = req.POST.get('barcode')
        scanner = req.POST.get('scanner')


        if Sortir.objects.filter(barcode=barcode).exists():
            messages.warning(req, 'Barcode ini sudah pernah digunakan')
            # if Double.objects.filter(barcode=barcode).exists():
            #     return redirect('/')

            double.barcode = barcode
            double.scanner = scanner
            double.save() 

            return redirect('/')
        else:

            sortir.barcode = barcode
            sortir.scanner = scanner
            sortir.save() 
            return redirect('/')

        
    
    return render(req,'second.html',context)