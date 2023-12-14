class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta(self):
        print(f"{self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta(self):
        super().tulosta()
        print(f" Julkaisun kirjoittaja:{self.kirjoittaja} ja sivumäärä: {self.sivumäärä}")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta(self):
        super().tulosta()
        print(f" Julkaisun päätoimittaja:{self.päätoimittaja}")


julkaisut = []

julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for j in julkaisut:
    j.tulosta()