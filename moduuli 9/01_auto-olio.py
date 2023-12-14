class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0


#pääohjelma:

Auto1 = Auto("ABC-123", 142)

print(f"Auton rekkari on {Auto1.rekisteritunnus}\n"
      f"Huippunopeus {Auto1.huippunopeus:d} km/h\n"
      f"Nopeus tällä hetkellä {Auto1.nopeus} km/h\n"
      f"Kuljettu matka {Auto1.kuljettumatka} km")

