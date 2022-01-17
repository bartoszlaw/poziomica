from math import degrees
from django.shortcuts import redirect, render
from .forms import PomiaryForm
from django.contrib import messages
from .functions import generate_id, random_degrees
from .models import Pomiary
from django.http import JsonResponse
import json
from .functions import random_degrees
from .i2c import i2cConnector
def home(request): #pomiary
    pomiary = Pomiary.objects.all()
    print(random_degrees())
    return render(request, 'poziomica_app/index.html', {'pomiary': pomiary})


def robPomiar(request):
    if request.method == 'GET':
        return render(request, 'poziomica_app/zrob_pomiar.html')
    else:
        if request.POST.get('wyslij'):
            nazwa = request.POST['nazwa']
            pomiar = str(random_degrees())
            if request.POST.get('zapisz') == "tak":
                try:
                    form = PomiaryForm()
                    nowy_pomiar = form.save(commit=False)
                    nowy_pomiar.nazwa = nazwa
                    nowy_pomiar.wynik = pomiar
                    nowy_pomiar.save()
                    messages.info(request, "zapisano")
                    koduj_wynik = generate_id(4) + pomiar
                    return redirect('wynikpomiaru', pomiar_wynik = koduj_wynik)
                except:
                    return render(request, 'poziomica_app/zrob_pomiar.html', {'error':'Coś poszło źle'})
            else:
                koduj_wynik = generate_id(4) + pomiar
                return redirect('wynikpomiaru', pomiar_wynik = koduj_wynik)

        else:
            return render(request, 'poziomica_app/zrob_pomiar.html')


def wynikPomiaru(request, pomiar_wynik):
    if request.method == 'GET':
        decode = [pomiar_wynik[x] for x in range(len(list(pomiar_wynik))) if x >= 4]
        decode_str="".join(str(element) for element in decode)
        return render(request, 'poziomica_app/wynik_pomiaru.html', {'wynik':decode_str})
    else:
        pass

def liveView(request):
    if request.method == 'GET':
        return render(request, 'poziomica_app/liveview.html')
    
def liveViewUpdate(request):
    stopnie = random_degrees()
        
        # return response
    return JsonResponse({"value":stopnie})