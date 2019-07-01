from django.shortcuts import render, redirect
from .forms import NewsForm
from .models import  News

# Create your views here.
def Home(request):
    return render(request, 'index.html')


def CrearPeticion(request):
    print("Estoy aquí 1")
    print("#######")
    print (request.method)
    if request.method == "POST":
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            print("ENTROOOOOOOOOOOO")
            news_form.save()
            print("VUELVO A ENTRAAAAAAAAR")
            return redirect('index')
    else:
        print("Ahora en el 3")
        news_form = NewsForm()
    return render(request, 'tfg/crear_peticion.html',{'news_form':news_form})


def ListarNoticias(request):
    noticias = News.objects.all()
    return render(request, 'tfg/listar_noticias.html',{'news':noticias})

