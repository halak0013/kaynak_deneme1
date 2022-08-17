from django.shortcuts import render,redirect

from .models import Author, Book
from .forms import  KitapFormSet


def kitap_olustur(request,pk):
    yazar=Author.objects.get(pk=pk)
    formset=KitapFormSet(request.POST or None)

    if request.method=='POST':
        if formset.is_valid():
            formset.instance=yazar
            formset.save()
            return redirect("kitap_olustur",pk=yazar.id)

    context={
        "formset":formset,
        "yazar":yazar,
    }

    return render(request,"kitap_olustur.html",context)