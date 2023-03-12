import csv
import json
import pickle
import os
import sys


class Odczyt:
    def __init__(self, typ_in, plik_in):
        self.typ_in = typ_in
        self.plik_in = plik_in
        self.lista = []

    def odczytaj_plik(self):
        if self.typ_in in ('csv', 'txt'):
            with open(self.plik_in, 'r') as f:
                reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
                for line in reader:
                    self.lista.append(line)
        elif self.typ_in == 'json':
            with open(self.plik_in, 'r') as f:
                self.lista = json.load(f)
        elif self.typ_in == 'pickle':
            with open(self.plik_in, 'rb') as f:
                self.lista = pickle.load(f)
        return self.lista


class Zapis:
    def __init__(self, typ_out, plik_out):
        self.typ_out = typ_out
        self.plik_out = plik_out
        self.lista = []

    def zapisz_plik(self):
        if self.typ_out in ('csv', 'txt'):
            with open(self.plik_out, 'w', newline='') as f:
                writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
                for line in self.lista:
                    writer.writerow(line)
        elif self.typ_out == 'json':
            with open(self.plik_out, 'w') as f:
                json.dump(self.lista, f)
        elif self.typ_out == 'pickle':
            with open(self.plik_out, 'wb') as f:
                pickle.dump(self.lista, f)


class OpracujPlik(Odczyt, Zapis):
    def __init__(self, plik_in, plik_out, typ_out, typ_in, zmiany, dlugosc):
        Odczyt.__init__(self, typ_in, plik_in)
        Zapis.__init__(self, typ_out, plik_out)
        self.plik_in = plik_in
        self.plik_out = plik_out
        self.typ_out = typ_out
        self.typ_in = typ_in
        self.dlugosc = dlugosc
        self.zmiany = zmiany
        self.lista = []

    def wprowadz_zmiany(self):
        i = 0
        while i < self.dlugosc - 3:
            wsad = self.zmiany[i].split(",")
            x = int(wsad[0])
            y = int(wsad[1])
            self.lista[x][y] = wsad[2]
            i += 1
        return self.lista


def start():
    obs_typy = ('csv', 'txt', 'json', 'pickle')
    if len(sys.argv) < 1:
        print('Nie podano zadnych argumentow')
    elif len(sys.argv) <= 3:
        print('Nie podano danych do zmiany')
    else:
        plik_in = sys.argv[1]
        plik_out = sys.argv[2]
        zmiany = sys.argv[3:]
        dlugosc = len(sys.argv)
        typ_in = plik_in.split(sep='.')[1]
        typ_out = plik_out.split(sep='.')[1]
        if not os.path.exists(plik_in):
            print('Plik zrodlowy nie istnieje !!')
            quit()
        elif typ_in not in obs_typy:
            print(f'Podano nieobslugiwany format pliku wejsciowego: {typ_in}')
            quit()
        elif typ_out not in obs_typy:
            print(f'Podano nieobslugiwany format pliku wyjsciowego: {typ_out}')
            quit()
        print(f'Podano: plik wejsciowy: {plik_in} , plik docelowy: {plik_out} oraz zakres zmian: {sys.argv[3:]}')

        x = OpracujPlik(plik_in, plik_out, typ_out, typ_in, zmiany, dlugosc)
        print(f'Prezentuje zawartosc pliku przed zmianami:\n{x.odczytaj_plik()}')
        print(f'Prezentuje zawartosc pliku po zmianach:\n{x.wprowadz_zmiany()}')
        x.zapisz_plik()


start()
