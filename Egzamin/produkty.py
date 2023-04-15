class Produkty:
    def __init__(self, nazwa, cena):
        self.__nazwa = nazwa
        self.__cena = cena

    def get_nzawa(self):
        return self.__nazwa

    def get_cena(self):
        return self.__cena
