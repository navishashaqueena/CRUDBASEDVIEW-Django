from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from . models import murid
from . forms import FormMurid


@login_required
def LihatMurid(request):
    model = murid.objects.all()
    return render(request, "CRUDApp/index.html", {"model": model})


@login_required
def BuatDaftarMurid(request):
    model = FormMurid()

    if request.method == 'POST':
        model = FormMurid(request.POST)
        if model.is_valid():
            model.save()
        return redirect('/')

    return render(request, "CRUDApp/tambah-murid.html", {"model": model})


@login_required
# (namaapp.fungsi delete_nama objects)
@permission_required("CRUDApp.delete_murid")
def HapusMurid(request, id):
    model = murid.objects.get(id=id)
    model.delete()
    return redirect('/')


@login_required
def PerbaruiDaftarMurid(request, id):
    model = murid.objects.get(id=id)
    form = FormMurid(instance=model)

    if request.method == "POST":
        model = FormMurid(request.POST, instance=model)
        if model.is_valid():
            model.save()
            return redirect('/')

    return render(request, "CRUDApp/update-murid.html", {"form": form})


def logout(request):
    return render(request, "CRUDApp/logout.html")
