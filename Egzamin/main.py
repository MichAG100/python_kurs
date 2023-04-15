from produkt import Produkt
from koszyk import Koszyk

def main():
    Produkt.wczytaj_produkty("ceny.csv")
   # print(Produkt.produkt("Chleb pszenno-żytni - za 0.5 kg").cena(1, 2021))
    koszyk = Koszyk()
    koszyk.dodaj(Produkt.produkt("Cebula - za 1 kg"))
    koszyk.dodaj(Produkt.produkt("Cebula - za 1 kg"))

    print(koszyk.roczna_stopa_inflacji(3,2015))

if __name__=="__main__":
    main()