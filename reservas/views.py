from django.shortcuts import render, redirect
from .models import Reserva
from .forms import ReservaForm

def list_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'reservas.html', {'reservas': reservas})


def create_reserva(request):
    form = ReservaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_reservas')

    return render(request, 'reservas-form.html', {'form': form})


def update_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    form = ReservaForm(request.POST or None, instance=reserva)

    if form.is_valid():
        form.save()
        return redirect('list_reservas')

    return render(request, 'reservas-form.html', {'form': form, 'reserva': reserva})


def delete_reserva(request, id):
    reserva = Reserva.objects.get(id=id)

    if request.method == 'POST':
        reserva.delete()
        return redirect('list_reservas')

    return render(request, 'rese-delete-confirm.html', {'reserva': reserva})
