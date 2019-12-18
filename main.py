"""
TO DO:
    1) Macierz.__str__

FIXES:


UPGRADES:
    1) Upiekszyc kod funkcji sprawdz_wymiary()
    2) Macierz.__mul__ polepszyc sprawdzanie czy czynnik jest liczba

MAYBE:
    1) Stworzyc klase Sprawdz

"""



import sys
def wejscie(argument):
    wiersze = [x for x in argument.split(';')]

    macierz = [[float(x) for x in wiersz.split()]for wiersz in wiersze]

    if(sprawdz_wymiary(macierz)):
        raise Exception("Prosze podac macierz z poprawnymi wymiarami!")

    return macierz

def sprawdz_wymiary(tablica): # UP
    for index, item in enumerate(tablica):
        if index == 0:
            ostatnia = len(item)
            continue

        if len(item) != ostatnia:
            return True

        ostatnia = len(item)
    return False

class Macierz:
    def __init__ (self, tablica):
        """ 
            wartosc - zwraca tablice wartosci macierzy
            wiersze - zwraca ilosc wierszy macierzy
            kolumny - zwraca ilosc kolumn macierzy
        """
        self.wartosc = tablica
        self.wiersze = len(tablica)
        self.kolumny = len(tablica[0])

    def __str__(self):
        #return ''.join([str(j) for j in i ]for i in self.wartosc]) # FX
        pass

    def __add__ (self, other):
        """ Mozna wykonwyac operacje (+) na obiektach klasy Macierz """
        if not isinstance(other, Macierz):
            raise Exception('Operacje (+) mozna wykonywac tylko na innych obiektach klasy Macierz')
        elif (self.wiersze != other.wiersze) or (self.kolumny != other.kolumny):
            raise Exception('Macierze musza byc tych samych wymiarow!')

        return [[self.wartosc[i][j]+other.wartosc[i][j] for j in range(self.kolumny)] for i in range(self.wiersze)]

    def __mul__(self, other):
        if not isinstance(other, int): # UP
            raise Exception('Operacje (*) mozna wykonywac tylko za pomoca liczby typu int')

        iloczyn = [[self.wartosc[i][j]*other for j in range(self.kolumny)] for i in range(self.wiersze)]
        return iloczyn



if __name__ == "__main__":
    x1 = wejscie("1 2 3; 4 5 6; 1 1 1")
    x2 = wejscie("1 1 1; 1 1 1; 1 1 1")
    a = Macierz(x1)
    b = Macierz(x2)


    #print(c.wartosc)

    # [ 1 2 3; 4 5 6; 7 8 9 ]
