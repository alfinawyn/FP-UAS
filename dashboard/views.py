from django.shortcuts import render, redirect
from dashboard.forms import FormBarang
from dashboard.models import Barang
from dashboard.forms import FormAksesoris
from dashboard.models import Aksesoris
from django.contrib import messages

# Create your views here.


def produk(request):
    titelnya="Produk"
    konteks = {
        'titel':titelnya,
    }
    return render(request,'produk.html',konteks)

def Barang_View(request):
    barangs=Barang.objects.all()

    konteks={
        'barangs':barangs,
    }
    return render(request, 'tampil_brg.html', konteks)

def Aksesoris_View(request):
    aksesoriss=Aksesoris.objects.all()

    konteks={
        'aksesoriss':aksesoriss,
    }
    return render(request, 'aksesoris.html', konteks)

def tambah_barang(request):
    form= FormBarang(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Data Berhasil Ditambahkan")
        form =FormBarang()
        konteks = {
            'form' : form,
        }
        return render(request, 'tambah_barang.html', konteks)
    else:
        form=FormBarang()
        konteks ={
            'form':form,
        }
        return render(request, 'tambah_barang.html', konteks)

def tambah_aksesoris(request):
    form= FormAksesoris(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Data Berhasil Ditambahkan")
        form =FormAksesoris()
        konteks = {
            'form' : form,
        }
        return render(request, 'tambah_aksesoris.html', konteks)
    else:
        form=FormAksesoris()
        konteks ={
            'form':form,
        }
        return render(request, 'tambah_aksesoris.html', konteks)

def ubah_brg(request,id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diubah")
            return redirect('ubah_brg', id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form' : form,
            'barangs' : barangs
        }
    return render(request, 'ubah_brg.html', konteks)

def ubah_aksesoris(request,id_aksesoris):
    aksesoriss=Aksesoris.objects.get(id=id_aksesoris)
    if request.POST:
        form=FormAksesoris(request.POST, instance=aksesoriss)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diubah")
            return redirect('ubah_aksesoris', id_aksesoris=id_aksesoris)
    else:
        form=FormAksesoris(instance=aksesoriss)
        konteks = {
            'form' : form,
            'aksesoriss' : aksesoriss
        }
    return render(request, 'ubah_aksesoris.html', konteks)

def hapus_brg(request, id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")
    return redirect('Vbrg')

def hapus_aksesoris(request, id_aksesoris):
    aksesoriss=Aksesoris.objects.filter(id=id_aksesoris)
    aksesoriss.delete()
    messages.success(request,"Data Terhapus")
    return redirect('aksesoris')