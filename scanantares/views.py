from django.shortcuts import render
from scanantares.models import *
from .forms import FormSortir
from django.contrib import messages


def home(req):
    
    # if req.POST:
    #     form = FormSortir(req.POST)
    #     if form.is_valid():
    #         form.save()
    #         form=FormSortir()
    #         pesan="data sukses di simpan"
    #         context={
    #             'form':form,
    #             'pesan':pesan, 
    #         }

    # scanner = Scanner.objects.all()
    total = Sortir.objects.count()
    angle = Sortir.objects.filter(scanner='angle').count()
    latif = Sortir.objects.filter(scanner='latif').count()
    fazza = Sortir.objects.filter(scanner='fazza').count()
    antare = Sortir.objects.filter(scanner='antare').count()
    form = FormSortir()

    context = {
        # 'scanner':scanner, 
        'total':total,
        'form':form,
        'angle':angle,
        'latif':latif,
        'fazza':fazza,
        'antare':antare,
            
    }

    if req.POST:
        sortir = Sortir()

        barcode = req.POST.get('barcode')
        scanner = req.POST.get('scanner')

        sortir.barcode = barcode
        sortir.scanner = scanner

        sortir.save()

        messages.success(req, 'input sukses')
        return render(req,'main.html', context)

        
    
    return render(req,'main.html',context)