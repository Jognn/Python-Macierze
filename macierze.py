"""
TO DO:
    1) Macierz.__str__
    2) Overload "=="

FIXES:


UPGRADES:
    1) Upiekszyc kod funkcji sprawdz_wymiary()
    2) Upiekszyc kod wymnazania macierzy

MAYBE:
    1) Stworzyc klase Sprawdz

"""

def sprawdz_wymiary(tablica): # UP
    if len(tablica) == 1: 
        return False

    for index, item in enumerate(tablica):
        if index == 0:
            ostatnia = len(item)
            continue

        if len(item) != ostatnia:
            return True

        ostatnia = len(item)
    return False

class Macierz:

    def __init__ (self, tablica = ''):
        """ 
            wartosc - zwraca tablice wartosci macierzy
            wiersze - zwraca wiersze macierzy
            kolumny - zwraca kolumny macierzy
            wiersze_ilosc - zwraca ilosc wierszy macierzy
            kolumny_ilosc - zwraca ilosc kolumn macierzy
        """

        if isinstance(tablica, str):
            self.convert(tablica)
        elif isinstance(tablica, (list, tuple, int, float)):
            self.wartosc = tablica
        else:
            raise Exception("Prosze podac odpowiedni typ (list, tuple, int, float, string)")

        if(sprawdz_wymiary(self.wartosc)):
            raise Exception("Prosze podac macierz z poprawnymi wymiarami!")

        self.wiersze = self.wartosc
        self.kolumny = [[self.wartosc[i][j] for i in range(len(self.wiersze))]for j in range(len(self.wiersze[0]))]
        self.wiersze_ilosc = len(self.wiersze)
        self.kolumny_ilosc = len(self.kolumny)

    def __str__(self):
        tmp = [[str(j) for j in i]for i in self.wartosc]
        tekst = ''
        for i in range(len(tmp)):
            tekst += '  '.join(tmp[i]) + "\n"
        return tekst

    def __add__ (self, other):
        """ Mozna wykonywac operacje (+) za pomoca liczb typu int lub obiektu klasy Macierz """

        wynik = None
        if isinstance(other, int):
            wynik = [[self.wartosc[i][j] + other for j in range(self.kolumny_ilosc)] for i in range(self.wiersze_ilosc)]

        elif isinstance(other, Macierz):
            if(self.wiersze_ilosc != other.wiersze_ilosc) or (self.kolumny_ilosc != other.kolumny_ilosc):
                raise Exception('Macierze musza byc tych samych wymiarow!')

            wynik = [[self.wartosc[i][j]+ other.wartosc[i][j] for j in range(self.kolumny_ilosc)] for i in range(self.wiersze_ilosc)]
        else:
            raise Exception('Operacje (+) mozna wykonywac tylko za pomoca liczby typu int lub obiektu klasy Macierz')

        return Macierz(wynik)

    def __mul__(self, other):
        """ Mozna wykonywac operacje (*) za pomoca liczb typu int lub obiektu klasy Macierz """

        wynik = []
        if(isinstance(other, int)):
            wynik = [[self.wartosc[i][j]*other for j in range(self.kolumny_ilosc)] for i in range(self.wiersze_ilosc)]

        elif(isinstance(other, Macierz)): # UP
            if self.kolumny_ilosc != other.wiersze_ilosc:
                raise Exception('Aby zaszla operacja (*) ilosc kolumn pierwszej macierzy musi sie rownac ilosci wierszy drugiej macierzy')

            for m in range(self.wiersze_ilosc):
                tmp = []
                for n in range(other.kolumny_ilosc):
                    #self.wiersze[m] * other.kolumny[n]
                    helper = 0
                    for x in range(len(self.wiersze[m])):
                        helper += self.wiersze[m][x] * other.kolumny[n][x]
                    tmp.append(helper)
                wynik.append(tmp)
        else:
            raise Exception('Operacje (*) mozna wykonywac tylko za pomoca liczby typu int lub obiektu klasy Macierz')

        return Macierz(wynik)

    def convert(self, wejscie):
        wiersze_ilosc = [x for x in wejscie.split(';')]
        self.wartosc = [[float(x) for x in wiersz.split()]for wiersz in wiersze_ilosc]



if __name__ == "__main__":
    a = Macierz("4 3 2; 1 3 2; 4 1 2; 5 2 3")
    b = Macierz("1; 2; 3")
    c = Macierz()
    
    
    c = a*b
    print(c)
    

    # [ 1 2 3; 4 5 6; 7 8 9 ]
