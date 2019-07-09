from django.shortcuts import render, redirect, reverse
from .forms import NewsForm
from .models import  News
import keras
import numpy
from bs4 import BeautifulSoup
from selenium import webdriver

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
    noticiasMalas = []
    noticiasBuenas = []
    noticias = News.objects.all()
    news_form = NewsForm()
    if request.method == 'GET':
        i = 0;
        j = 0;
        for noticia in noticias:
            if noticia.esFi == False:
                if(i < 5):
                    noticiasMalas.append(noticia)
                    i+=1
            else:
                if (j < 5):
                    noticiasBuenas.append(noticia)
                    j += 1
        print(noticiasMalas)
        print(noticiasBuenas)

    elif request.method == 'POST':
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news = news_form.save(commit = False)
            url = news_form.cleaned_data.get('url')
            bajar_noticia(url)
            news.esFi = neural_comprobation(bajar_noticia(url)[0], bajar_noticia(url)[1])
            news.save()
            return render(request, 'tfg/listar_noticias.html',
                          {
                              'news': noticias,
                              'buenas': noticiasBuenas,
                              'malas': noticiasMalas,
                              'news_form': news_form
                          })

    return render(request, 'tfg/listar_noticias.html',
                  {
                      'news': noticias,
                      'buenas': noticiasBuenas,
                      'malas': noticiasMalas,
                      'news_form': news_form
                  })

def bajar_noticia(url):
    options = webdriver.ChromeOptions()
    chrome_path = "web/apps/tfg/chromedriver.exe"
    options.add_argument('headless')
    options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    driver.get(url)
    nImagenes = 0
    nEnlaces = 0
    esFi = True

    driver.get(url)

    open_js = driver.execute_script("return document.documentElement.outerHTML")

    soup_js = BeautifulSoup(open_js, 'lxml')
    # soup_not = BeautifulSoup(open_not.text, 'lxml')

    notice_text = ""
    notice = soup_js.findAll("p")
    for noti in notice:
        if len(noti.text) >= 105:
            notice_text = notice_text + noti.text + '\n'
    head = soup_js.find("h1")
    head_text = head.text
    if (head_text in notice_text):
        str(notice_text).replace(head_text, '')

    periodico = ""
    periodico = str(url)
    periodico = periodico.split('.')
    if 'www.' in url:
        periodico = periodico[1]
    else:
        periodico = periodico[0][8:] if url[4] == 's' else periodico[0][7:]

    imagenes = soup_js.findAll("img", src=True)
    for img in imagenes:
        if periodico in str(img['src']) or not str(img['src']).startswith('http'):
            continue
        else:
            nImagenes = nImagenes + 1

    otrasImagenes = soup_js.findAll('iframe', src=True)
    for oImg in otrasImagenes:
        if periodico in str(oImg['src']) or not str(oImg['src']).startswith('http'):
            continue
        else:
            nImagenes = nImagenes + 1

    enlaces = soup_js.findAll("a", href=True)
    for enl in enlaces:
        if periodico in str(enl['href']) or str(enl['href']).startswith('http'):
            continue
        else:
            nEnlaces = nEnlaces + 1

    if nImagenes > 10 or nEnlaces > 50:
        esFi = False
    else:
        esFi = True

    comprobacion = [nImagenes, nEnlaces]
    print("Número de imágenes: " + str(nImagenes))
    print("Número de enlaces: " + str(nEnlaces))

    return comprobacion


def neural_comprobation(nImagenes, nEnlaces):
    x = numpy.array([[nImagenes, nEnlaces]])
    model = keras.models.load_model('web/apps/tfg/neural_network_news.model')
    prediction = model.predict(x)
    y = model.predict_classes(x)
    print("X=%s, Predicted=%s" % ([x][0], y[0]))

    esFi = True if y[0] == 1 else False

    print("¿Es una página fiable? Sí" if esFi == True else "¿Es una página fiable? No")

    return esFi
