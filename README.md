# Poziomica laserowa z cyfrowym odczytem kąta pochylenia
## Autorzy:
* Bartosz Ławrynowicz
* Miłosz Ziemba
* Paweł Urbański 
## 1. Cel projektu
Celem projektu jest stworzenie przenośnej poziomicy laserowej zarządzanej bezprzewodowo. Kluczowym elementem projektu jest zapewnienie komunikacji pomiędzy czujnikiem położenia kątowego oraz urządzeniem kontrolującym jego pracę. System powinien odczytywać pomiary w czasie rzeczywistym, a wszystkie jego elementy muszą stanowić integralną część. Końcowym zadaniem jest zaprojektowanie obudowy, która zabezpieczy wszystkie elementy systemu. 
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
![image](photos/2.jpg "Schemat połączenia elementów")
## 7. Schemat układu 
![image](photos/1.bmp "Schemat elektryczny")
## Obudowa
![image](photos/3.bmp)
![image](photos/4.bmp)
![image](photos/5.bmp)


