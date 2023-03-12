## Rozszerzenie programu do zarządzania plikami csv

    Napisz program oparty na klasach i dziedziczeniu, który odczyta wejściowy plik,
    następnie zmodyfikuje go i wyświetli w terminalu jego zawartość, 
    a na końcu zapisze w wybranej lokalizacji.

### Uruchomienie programu przez terminal:
    python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ... <zmiana_n>
    gdzie:
     <plik_wejsciowy> - nazwa pliku, który ma zostać odczytany, np. in.csv, in.json lub in.txt
     <plik_wyjsciowy> - nazwa pliku, do którego ma zostać zapisana zawartość, 
        np. out.csv, out.json, out.txt lub out.pickle
     <zmiana_x> - Zmiana w postaci "x,y,wartosc" - x (kolumna) oraz y (wiersz) są współrzędnymi liczonymi od 0,
        natomiast "wartosc" zmianą która ma trafić na podane miejsce.


#### Przykład działania:
        python reader.py in.json out.csv 0,0,gitara 3,1,kubek 1,2,17 3,3,0
        Z pliku in.json ma wyjść plik out.csv:
        gitara,3,7,0
        kanapka,12,5,kubek
        pedzel,17,34,5
        plakat,czerwony,8,0
        Wymagane formaty:
    
        .csv
        .json
        .txt
        .pickle