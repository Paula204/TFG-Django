from django.shortcuts import render, redirect
from .forms import NewsForm

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def crearPeticion(request):
    if request.method == 'POST':
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            print("ENTROOOOOOOOOOOO")
            news_form.save()
            print("VUELVO A ENTRAAAAAAAAR")
            return render(request, 'index.html')
    else:
        news_form = NewsForm()
    return render(request, 'tfg/crear_peticion.html',{'news_form':news_form})
