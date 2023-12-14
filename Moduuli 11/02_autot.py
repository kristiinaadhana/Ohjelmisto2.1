class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if muutos < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else: self.nopeus = self.nopeus
        return self.nopeus

    def kulje(self, tuntimäärä):
        matka = self.nopeus * tuntimäärä
        self.kuljettumatka += matka

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        self.bensatankki = bensatankki
        super().__init__(rekisteritunnus, huippunopeus)


#pääohjelma:

autot = []

autot.append(Sähköauto("ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

autot[0].kiihdytä(50)
autot[1].kiihdytä(100)

autot[0].kulje(3)
autot[1].kulje(3)

print(f"1. Auto kulki 3 tunnin aikana nopeudella {autot[0].nopeus} km/h: {autot[0].kuljettumatka} km")
print(f"2. Auto kulki 3 tunnin aikana nopeudella {autot[1].nopeus} km/h:{autot[1].kuljettumatka} km")