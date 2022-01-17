<h1 align="center">Projektowanie Urządzeń Optoelektronicznych</h1>
<h1 align="center">Projekt Poziomicy Laserowej z cyfrowym odczytem kąta pochylenia</h1>

## Autorzy:
* Bartosz Ławrynowicz 243197
* Miłosz Ziemba 236280
* Paweł Urbański 243232
## 1. Cel projektu

<p align="justify">
Celem projektu jest stworzenie przenośnej poziomicy laserowej zarządzanej bezprzewodowo. Kluczowym elementem projektu jest zapewnienie komunikacji pomiędzy czujnikiem położenia kątowego oraz urządzeniem kontrolującym jego pracę. System powinien odczytywać pomiary w czasie rzeczywistym, a wszystkie jego elementy muszą stanowić integralną część. Końcowym zadaniem jest zaprojektowanie obudowy, która zabezpieczy wszystkie elementy systemu.
</p>

## 2. Założenia projektowe
* Czujnik położenia kątowego umożliwia preceyzyjne ustawienie kątowe lasera.
* Czujnik powinien umożliwiać odczytanie wartości względnej i bezwględnej.
* System powinien umożliwić przesył danych pomiędzy czujnikiem a mikrokontrolerem lub dowolnej platformy komputerowej.
* Użytkownik systemu otrzymuje informację o aktualnej wartości przechyłu w czasie rzeczywistym. 
* Użytkownik ma możliwość zapisu oraz usunięcia dokonanych pomiarów.
* System umożliwia zdalną obsługę czujnika w tym jego konfigurację.
* Wyświetlanie i edycja pomiarów możliwa jest przy użyciu urządzeń mobilnych lub komputerów osobistych.


## 3. Wykorzystywane urządzenia 
* Laser krzyżowy LINELASER 50mW.
* Moduł sterujący systemem: Rasberry Pi 3 model B.
* Czujnik położenia kątowego: IMU 10DoF ( żyroskop, akcelerometr, magnetometr, barometr).
* Akumulator Li-Ion Titan 6000mAh 16C 6S.
* Wyświetlacz CUQI (5-calowy).
* Karta pamięci microSD 32 GB. 

## 4. Specyfikacja urządzeń 

* <h3>Laser</h3>
<p align="justify">Dobrano laser krzyżowy LINELASER 50mW czerwony (650 nm) [Rys. 1]. Dobrany laser spełnia założenie dotyczące zasięgu 50 m, jednak szerokość linii krzyżyka na tej odległości będzie miała około 1 do 2 cm. Dobrany laser zasilany jest napięciem 5V DC, więc może zostać podłączony bezpośrednio do mikrokontrolera.</p>

* <h3>Akumulator</h3>
<p align="justify">Dobrano Akumulator Li-Ion Titan 6000mAh [Rys. 2]. Posiada on napięcie wyjściowe 11.1 V co skutkuje koniecznością zastosowania przetwornicy zapewniającej napięcie na poziomie wymaganym przez wybrany mikrokontroler. Dobrany akumulator można ładować za pomocą dedykowanej do niego ładowarki Li-Pol/Li-HV/Li-Ion/Li-Fe/Ni-Cd/Ni-MH z balanserem SkyRC IMAX B6AC v2 USB z wbudowanym zasilaczem.</p>

* <h3>Czujnik przechyłu</h3>
<p align="justify">Dobrano czujnik przechyłu IMU 10DoF [Rys. 3], jest on połączeniem 3-osiowego żyroskopu, akcelerometru i magnetometru, co zapewnia zniwelowanie zakłóceń pomiarowych. Wymaga on zasilania 3,3 do 5,5 V oraz obsługiwany jest przez interfejs I2C.</p>

* <h3>Przetwornica</h3>
<p align="justify">W celu dostosowania napięcia zasilania do wymagań mikrokontrolera zastosowano przetworznicę Step-Down - 9-24V - na 5V [Rys. 4]. Posiada ona złacze USB, co ułatwia podłączenie jej do dobranego mikrokontrolera</p>

* <h3>Wyświetlacz</h3>
<p align="justify">Dobrano 5-calowy ekran dotykowy marki Jun-Saxifragelec [Rys. 5]. Posiada on rozdzielczość 800 x 480. Jest on zasilany napięciem 5V przez przewód USB. Komunikacja z mikrokontrolerem realizowana jest przez interfejs HDMI.</p>

* <h3>Mikrokontroler</h3>
<p align="justify">Dobrano mikrokontroler Raspberry pi 3b [Rys. 6]. Posiada on interfejsy HDMI, USB oraz i2c potrzebne do podłączenia dobranych komponentów: czujnika, przetwornicy i ekranu. Dobrany mikrokontroler wymaga zasilania 5V.</p>

* <h3>Przełącznik MRS-101A</h3>

* <h3>Śruby</h3>

## 5. Wykorzystywane technologie oraz protokoły
* Komunikacja czujnika z Rasberry Pi odbywa się przy użyciu protokołu **I2C**. 
* Skrypty obsługujące komunikację I2C napisane są w języku programowania **Python**.
* Interfejs użytkownika stworzony jest w formie aplikacji webowej.
* Rolę serwera WWW pełni Rasberry Pi.
* System wykorzystuje bazę danych **SQLite**.
* Aplikacja webowa stworzona została z wykorzystaniem frameworku **django**.
* Połączenie wyświetlacza z Rasberry Pi odbywa się za pomocą interfejsu **HDMI**.
* Rasberry Pi działa w formie acces point (punkt dostępu).
* Urządzenia mobilne łączą się z punktem dostępu za pomocą modułu **Wi-Fi**. 

## 6. Schemat połączenia elementów 
![image](photos/2.jpg "Schemat połączeń elektrycznych w projektowanej poziomicy.")

## 7. Schemat układu 

![image](photos/1.bmp "Schemat elektryczny")

Schemat połączeń elektrycznych w projektowanej poziomicy.

<p align="justify">Jednostką centralną układu elektrycznego jest mikrokontroler Raspberry Pi 3B. Mikrokontroler zasilany jest z akumulatora, którego napięcie wyjściowe 11,1 V przetwarzane jest przez przetwornicę na 5 V. Przetwornica podłączona jest do mikrokontrolera przez złącze USB. Pomiędzy akumulatorem, a przetwornicą znajduje się przełącznik, zapewniający możliwość włączania i wyłączania urządzenia. Czujnik przechyłu podłączony jest poprzez interfejs I2C oraz zasilany napięciem 3,3V z mikrokontrolera. Laser zasilany jest z mikrokontrolera napięciem 5V. Wyświetlacz podłączony jest do mikrokontrolera poprzez złącze USB oraz HDMI. Złącze USB służy do zasilania wyświetlacza, natomiast HDMI do przesyłania informacji.</p>

## 8. Obudowa
![image](budowa/1.png)
![image](photos/4.bmp)
![image](photos/5.bmp)


### Urlpatterns
Urlspatterns to mapowanie ścieżek adresów url do odpoweidnich funkcji. Wpisanie określonego adresu url w okno przeglądarki spowoduje wywaołanie konkretnej funkcji opisanej w pliku `views.py`. Funkcje te nazywane są widokami i definiują odpowiedzi serwera www na akcję użytkownika.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ='home'),
    path('go/', views.robPomiar, name="robPomiar"),
    path('go/<str:pomiar_wynik>', views.wynikPomiaru, name="wynikpomiaru"),
    path('liveview', views.liveView, name="liveview"),
    path('liveview/update', views.liveViewUpdate, name="liveviewUpdate")
]
```
Wpisanie adresu strony bez określonej ścieżki spowoduje wywołanie funkcji widoku `home`.

### Widok początkowy (home)

`render()` to popularny idiom do ładowania szablonu, wypełniania kontekstu i zwracania obiektu HttpResponse z wynikiem wyrenderowanego szablonu. W tym przypadku kontekstem jest przekazany do szablonu obiekt typu słownik (dictionary). Zawarte w nim dane to obiekty pobrane z modelu Pomiary, które odpowiadają rekordom w tabeli bazy danych. Obiektowe odniesienie do bazy danych jest możliwe dzięki ORM - mapowaniu obiektowo-relacyjnym. Jest to sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych. 
```
def home(request): #pomiary
    pomiary = Pomiary.objects.all()
    print(random_degrees())
    return render(request, 'poziomica_app/index.html', {'pomiary': pomiary})
```
Wygląd wyrenderowanego szablonu `index.html`. Szablonowy tag {% static %} generuje bezwzględny URL plików statycznych. Znacznik `<thead>` służy do grupowania treści nagłówka w tabeli HTML. W pętli for loop z każdego obiektu (nazywanym pomiarem) ze słownika pomiary odczytujemy jego atrybuty.


```html
{% extends 'poziomica_app/base.html' %}

{% block content %}
{% load static %}

<div class="d-flex justify-content-center mt-5 ">
    <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Nazwa</th>
            <th scope="col">Wynik</th>
            <th scope="col">Data</th>
          </tr>
        </thead>
        <tbody>
        {% for pomiar in pomiary %}
          <tr>
            <td>{{pomiar.id}}</td>
            <td>{{pomiar.nazwa}}</td>
            <td>{{pomiar.wynik}}</td>
            <td>{{pomiar.data}}</td>
          </tr>
        {% endfor %}
        </tbody>
      </table>
</div>
{% endblock %}
```
Klasa pomiary dziedziczy metody i atrybuty z klasy nadzrzędnej `models`. W związku z czym staje się modelem bazy danych. Klasa Pomiary posaiada cztery atrybuty (jeden uktyty - id), które są polami w tabeli bazy danych SQLite. 

```python
from django.db import models
class Pomiary(models.Model):
    nazwa = models.CharField(max_length=100)
    wynik = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
```
