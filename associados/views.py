from django.shortcuts import render, redirect
from .models import Associado
from .forms import AssociadoForm

def list_associados(request):
    associados = Associado.objects.all()
    return render(request, 'associados.html', {'associados': associados})


def create_associado(request):
    form = AssociadoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_associados')

    return render(request, 'associados-form.html', {'form': form})


def update_associado(request, id):
    associado = Associado.objects.get(id=id)
    form = AssociadoForm(request.POST or None, instance=associado)

    if form.is_valid():
        form.save()
        return redirect('list_associados')

    return render(request, 'associados-form.html', {'form': form, 'associado': associado})


def delete_associado(request, id):
    associado = Associado.objects.get(id=id)

    if request.method == 'POST':
        associado.delete()
        return redirect('list_associados')

    return render(request, 'asso-delete-confirm.html', {'associado': associado})