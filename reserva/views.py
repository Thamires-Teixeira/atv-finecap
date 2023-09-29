from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.core.paginator import Paginator

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect("reserva_listar")

def reserva_listar(request):
    itens_por_pagina = 5

    
    reservas = Reserva.objects.all().order_by('date')

    
    nome_empresa = request.GET.get('nome_empresa')
    quitado = request.GET.get('quitado')
    valor_stand = request.GET.get('valor')
    data_reserva = request.GET.get('date')

    if nome_empresa:
        reservas = reservas.filter(nome_empresa__icontains=nome_empresa)
    elif quitado is not None:
        try:
            quitado_boolean = bool(str(quitado))
            reservas = reservas.filter(quitado=quitado_boolean)
        except ValueError:
            reservas = Reserva.objects.none()
    elif valor_stand:
        reservas = reservas.filter(valor_stand=valor_stand)
    elif data_reserva:
        reservas = reservas.filter(date=data_reserva)

    
    paginator = Paginator(reservas, itens_por_pagina)

    
    numero_pagina = request.GET.get('page')

   
    reservas_pagina = paginator.get_page(numero_pagina)

    context = {
        'reservas': reservas_pagina
    }

    return render(request, "reserva/lista_reserva.html", context)

def detalhe(request, id):
    detalhes=get_object_or_404(Reserva,id=id)
    context={
        'detalhes':detalhes
    }
    return render(request, 'reserva/detalhes.html', context)

def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ReservaForm()
    else:
        form = ReservaForm()

    return render(request, "reserva/form.html", {'form': form})