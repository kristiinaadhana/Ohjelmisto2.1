import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeus):
        muutos = random.randint(-10, 15)
        uusnopeus = self.nopeus + muutos
        if uusnopeus < 0:
            self.nopeus = 0
        elif uusnopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = uusnopeus
        self.nopeus += nopeus
        return self.nopeus

    def kulje(self, tuntimäärä):
        matka = self.nopeus * tuntimäärä
        self.kuljettumatka += matka


#pääohjelma alkaa

autot = []

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100,201))
    autot.append(auto)

while True:
    for auto in autot:
        auto.kiihdytä(0)
        auto.kulje(1)

    if any(auto.kuljettumatka >= 10000 for auto in autot):
        break

print(f"{'Rekkari':<15}{'Huippunopeus':<15}{'Nopeus':<15}{'Kuljettu matka':<15}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<15}{auto.nopeus:<15}{auto.kuljettumatka:<15}")


