from django.forms import ModelForm
from dashboard.models import Barang
from dashboard.models import Aksesoris
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.TextInput({'class':'form-control'}),
            'harga': forms.TextInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.TextInput({'class':'form-control'}),
        }

class FormAksesoris(ModelForm):
    class Meta :
        model=Aksesoris
        fields='__all__'

        widgets = {
            'kodeaks': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'stok': forms.TextInput({'class':'form-control'}),
            'harga': forms.TextInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.TextInput({'class':'form-control'}),
        }