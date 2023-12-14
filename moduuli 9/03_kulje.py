class auto:
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


#pääohjelma:

auto1 = auto("ABC-123", 142)

print(f"Auton rekkari on {auto1.rekisteritunnus}\n"
      f"Huippunopeus {auto1.huippunopeus:d} km/h\n"
      f"Nopeus tällä hetkellä {auto1.nopeus} km/h\n"
      f"Kuljettu matka {auto1.kuljettumatka} km\n")

auto1.kiihdytä(30)
print("Auto kiihdyttää 30km/h")
auto1.kiihdytä(70)
print("Auto kiihdyttää 70km/h lisää!")
auto1.kiihdytä(50)
print("Auto kiihdyttää vielä 50km/h!!")
print(f"Nopeus tällä hetkellä {auto1.nopeus} km/h")

auto1.kulje(2.0)
print(f"Auto kulki 2 tunnin aikana {auto1.kuljettumatka} km ")