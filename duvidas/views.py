from django.shortcuts import render, redirect
from duvidas.forms import DuvidaForm
from duvidas.models import Duvida


def list_duvida(request):
    duvida = Duvida.objects.all()
    return render(request, 'duvida.html', {'duvidas': duvida})


def create_duvida(request):
    form = DuvidaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_duvida')
    return render(request, 'duvida-form.html', {'form': form})


def update_duvida(request, id):
    duvida = Duvida.objects.get(id=id)
    form = DuvidaForm(request.POST or None, instance=duvida)

    if form.is_valid():
        form.save()
        return redirect('list_duvida')
    return render(request, 'duvida-form.html', {'form': form, 'duvida': duvida})


def delete_duvida(request, id):
    duvida = Duvida.objects.get(id=id)

    if request.method == 'POST':
        duvida.delete()
        return redirect('list_duvida')
    return render(request, 'duvida-delete-confirm.html', {'duvida': duvida})
