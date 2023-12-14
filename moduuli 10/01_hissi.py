class Hissi:
    def __init__(self, alin, ylin):
        self.kerros = alin
        self.alin = alin
        self.ylin = ylin

    def siirry_kerrokseen(self, tavoite):
        self.kerros = tavoite
        while self.kerros != tavoite:
            if self.kerros < tavoite:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros > self.ylin:
            self.kerros += 1
            print(f"Hissi siirtyy kerrokseen {self.kerros}")
        else:
            print(f"Olet jo kerroksessa {self.kerros}")

    def kerros_alas(self):
        if self.kerros < self.alin:
            self.alin -= 1
            print(f"Hissi siirtyy kerrokseen {self.kerros}")
        else:
            print(f"Olet jo kerroksessa {self.kerros}")

hissi1 = Hissi(1,5)

print(f"Hissi on kerroksessa {hissi1.kerros}")

hissi1.siirry_kerrokseen(4)
print(f"Hissi on kerroksessa {hissi1.kerros}")

hissi1.siirry_kerrokseen(5)
print(f"Hissi on kerroksessa {hissi1.kerros}")

hissi1.siirry_kerrokseen(1)
print(f"Hissi on kerroksessa {hissi1.kerros}")


