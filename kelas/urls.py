
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk
from dashboard.views import produk, tambah_barang, tambah_aksesoris, Barang_View, Aksesoris_View, ubah_brg, hapus_brg, ubah_aksesoris, hapus_aksesoris


def coba1(request): 
    return HttpResponse('Selamat Sore...')

def coba2(request):
    titelnya="Home"
    konteks = {
        'titel':titelnya,
    }
    return render(request, 'index.html',konteks)

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',coba2),
    path ('produk/',produk),
    path('addbrg/', tambah_barang),
    path('addaksesoris/', tambah_aksesoris),
    path('Vbrg/', Barang_View, name='Vbrg'),
    path('aksesoris/', Aksesoris_View, name='aksesoris_view'),
    path ('ubah/<int:id_barang>', ubah_brg, name='ubah_brg'),
    path ('ubahaks/<int:id_aksesoris>', ubah_aksesoris, name='ubah_aksesoris'),
    path ('hapus/<int:id_barang>', hapus_brg, name='hapus_brg'),
    path ('hapusaks/<int:id_aksesoris>', hapus_aksesoris, name='hapus_aksesoris'),

]