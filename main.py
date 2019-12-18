import sys
def wejscie(argument):
    wiersze = [x for x in argument.split(';')]

    macierz = [[float(x) for x in wiersz.split()]for wiersz in wiersze]

    return macierz

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

    def __add__ (self, other):
        """ Mozna wykonwyac operacje (+) na obiektach klasy Macierz"""
        if not isinstance(other, Macierz):
            raise Exception('Operacje (+) mozna wykonywac tylko na innych obiektach klasy Macierz')
        elif (self.wiersze != other.wiersze) or (self.kolumny != other.kolumny):
            raise Exception('Macierze musza byc tych samych wymiarow!')

        return 



if __name__ == "__main__":
    x = wejscie("1 2 3; 4 5 6")
    a = Macierz(x)
    b = Macierz([[1, 2, 3]])
    print(a.wartosc[0][1])
    print(a.wiersze)
    print(a.kolumny)
    print(a + 2)

    # [ 1 2 3; 4 5 6; 7 8 9 ]