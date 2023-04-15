class Produkty:
    def __init__(self,wiersz):
        dane = wiersz.split(",")
        self.__nazwa = dane [0]
        self.__ceny =[float(cena) for cena in dane[1:]]

    def get_nzawa(self):
        return self.__nazwa

    def get_cena(self):
        return self.__cena
