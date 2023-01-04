from django.shortcuts import render
from scanantares.models import *
from .forms import FormSortir


def home(req):
    id_1 = Scanner.objects.get(id=1)
    id_2 = Scanner.objects.get(id=2)
    id_3 = Scanner.objects.get(id=3)
    id_4 = Scanner.objects.get(id=4)
    total1 = Sortir.objects.filter(scanner_id='1').count()
    total2 = Sortir.objects.filter(scanner_id='2').count()
    total3 = Sortir.objects.filter(scanner_id='3').count()
    total4 = Sortir.objects.filter(scanner_id='4').count()
    total_sortir = Sortir.objects.count()
    form = FormSortir()

    if req.POST:
        form = FormSortir(req.POST)
        if form.is_valid():
            form.save()
            form=FormSortir()
            pesan="data sukses di simpan"
            context={
                'form':form,
                'pesan':pesan, 
            }

    id_1 = Scanner.objects.get(id=1)
    id_2 = Scanner.objects.get(id=2)
    id_3 = Scanner.objects.get(id=3)
    id_4 = Scanner.objects.get(id=4)
    total1 = Sortir.objects.filter(scanner_id='1').count()
    total2 = Sortir.objects.filter(scanner_id='2').count()
    total3 = Sortir.objects.filter(scanner_id='3').count()
    total4 = Sortir.objects.filter(scanner_id='4').count()
    total_sortir = Sortir.objects.count()

    

    
    context = {
        'id_1':id_1,
        'id_2':id_2,
        'id_3':id_3,
        'id_4':id_4,
        'total1':total1,
        'total2':total2,
        'total3':total3,
        'total4':total4,
        'total_sort':total_sortir,
        'form':form,
    }
   

    return render(req,'main.html',context)