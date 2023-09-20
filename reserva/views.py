from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect("reserva_listar")

def reserva_listar(request):
    reservas = Reserva.objects.all()

    nome_empresa = request.GET.get('nome_empresa')
    quitado = request.GET.get('quitado')
    valor_stand = request.GET.get('valor')
    data_reserva = request.GET.get('date')

    if nome_empresa:
        reservas = Reserva.objects.filter(nome_empresa__icontains=nome_empresa)
    elif quitado is not None:
        try:
            quitado_boolean = bool(str(quitado))
            reservas = Reserva.objects.filter(quitado=quitado_boolean)
        except ValueError:
        
            reservas = Reserva.objects.none()

    elif valor_stand:
        reservas = Reserva.objects.filter(valor_stand=valor_stand)
    elif data_reserva:
        reservas = Reserva.objects.filter(date=data_reserva)

    context = {
        'reservas':reservas
    }

    return render(request, "reserva/lista_reserva.html",context)

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