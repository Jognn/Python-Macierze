"""
TO DO:
    1) Wyliczanie wyznacznika
    2) Zrobic self.kolumny virtual

FIXES:


UPGRADES:
    1) Upiekszyc kod wymnazania macierzy
    2) Upiekszyc kod wykreslania

MAYBE:
    1) Overload "=="

"""

class Macierz:
    def __init__ (self, skladowe = ''):
        """
            wartosc - Zwraca tablice wartosci macierzy
            wiersze - Zwraca wiersze macierzy
            kolumny - Zwraca kolumny macierzy
            wiersze_ilosc - Zwraca ilosc wierszy macierzy
            kolumny_ilosc - Zwraca ilosc kolumn macierzy
        """
        if isinstance(skladowe, str):
            self.convert(skladowe)
        elif isinstance(skladowe, (list, tuple)):
            self.wartosc = skladowe
        else:
            raise Exception("Prosze podac odpowiedni typ (list, tuple, string)")

        if self.zle_wymiary():
            raise Exception("Prosze podac macierz z poprawnymi wymiarami!")

        self.wiersze = self.wartosc
        self.kolumny = [[self.wartosc[i][j] for i in range(len(self.wiersze))]for j in range(len(self.wiersze[0]))] # TO DO: make virtual
        self.wiersze_ilosc = len(self.wiersze)
        self.kolumny_ilosc = len(self.kolumny)

        self.kwadratowa = True if self.wiersze_ilosc == self.kolumny_ilosc else False

    def __str__(self):
        """ Wyswietla macierz """
        tmp = [[str(j) for j in i]for i in self.wartosc]
        tekst = ' '
        for i in range(len(tmp)):
            tekst += "| " + '  '.join(tmp[i]) + " | \n "
        return tekst

    def __add__ (self, other):
        """ Mozna wykonywac operacje (+) za pomoca liczb typu (int, float) lub obiektu klasy Macierz o tych samych wymiarach """
        wynik = None
        if isinstance(other, (int, float)):
            wynik = [[self.wartosc[i][j] + other for j in range(self.kolumny_ilosc)] for i in range(self.wiersze_ilosc)]
        elif isinstance(other, Macierz):
            if self.wiersze_ilosc != other.wiersze_ilosc or self.kolumny_ilosc != other.kolumny_ilosc:
                raise Exception('Macierze musza byc tych samych wymiarow!')

            wynik = [[self.wartosc[i][j]+ other.wartosc[i][j] for j in range(self.kolumny_ilosc)] for i in range(self.wiersze_ilosc)]
        else:
            raise TypeError('Operacje (+) mozna wykonywac tylko za pomoca liczby typu int lub obiektu klasy Macierz')
        return Macierz(wynik)

    def __mul__(self, other):
        """ Mozna wykonywac operacje (*) za pomoca liczb typu (int, float) lub obiektu klasy Macierz """
        wynik = []
        if isinstance(other, (int, float)):
            wynik = [[self.wartosc[i][j]*other for j in range(self.kolumny_ilosc)] for i in range(self.wiersze_ilosc)]
        elif isinstance(other, Macierz): # UP
            if self.kolumny_ilosc != other.wiersze_ilosc:
                raise Exception('Aby zaszla operacja (*) ilosc kolumn pierwszej macierzy musi sie rownac ilosci wierszy drugiej macierzy')

            for m in range(self.wiersze_ilosc):
                tmp = []
                for n in range(other.kolumny_ilosc):
                    x = 0
                    for i in range(len(self.wiersze[m])):
                        x += self.wiersze[m][i] * other.kolumny[n][i]
                    tmp.append(x)
                wynik.append(tmp)
        else:
            raise TypeError('Operacje (*) mozna wykonywac tylko za pomoca liczby typu int lub obiektu klasy Macierz')
        return Macierz(wynik)

    def wykresl(self, i, j): # UP: upiekszyc
        skladowe = []
        for m, wiersz in enumerate(self.wartosc):
            if m+1 == i:
                continue
            tmp = list()
            for n in range(len(wiersz)):
                if n+1 == j:
                    continue
                tmp.append(wiersz[n])
            skladowe.append(tmp)
        return Macierz(skladowe)

    def det(self):
        """ Wylicza wyznacznik macierzy """
        if not self.kwadratowa:
            raise Exception("Obliczenie wyznacznika jest mozliwe tylko dla macierzy kwadratowej!")

        i = 1
        j = 1







    def convert(self, wejscie):
        wiersze_ilosc = [x for x in wejscie.split(';')]
        self.wartosc = [[float(x) for x in wiersz.split()]for wiersz in wiersze_ilosc]

    def zle_wymiary(self):
        if isinstance(self.wartosc, (int, float)):
            return False

        if len(self.wartosc) == 1:
            return False

        for index, item in enumerate(self.wartosc):
            if not index == 0:
                if len(item) != ostatnia:
                    return True
            ostatnia = len(item)
        return False



if __name__ == "__main__":
    a = Macierz("4 3 2; 1 3 7; 4 3 8")
    #b = Macierz([[1]])
    #c = Macierz()

    print(a)
    print(a.wykresl(2,3))


    # [ 1 2 3; 4 5 6; 7 8 9 ]
