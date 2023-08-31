from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect("reserva_listar")

def reserva_listar(request):
    reservas = Reserva.objects.all()
    context ={
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


# Create your views here.
