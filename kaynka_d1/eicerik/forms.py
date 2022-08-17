from django import forms
from django.forms.models import inlineformset_factory
from .models import Author, Book

class KitapForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['baslık', 'sayfa_sayısı']

KitapFormSet=inlineformset_factory(
    Author,
    Book,
    KitapForm,
    can_delete=False,
    min_num=2,
    extra=0,

)