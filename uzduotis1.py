# Turėtų klasę Automobilis
# Automobilis turėtų savybes: metai, modelis, kuro_tipas

class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas

# Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą.

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")

# Sukurti norimą Automobilio objektą
# Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu
masina1 = Automobilis(2019, "Bmw", "dyzelis")
print(masina1.metai, masina1.modelis, masina1.kuro_tipas)
masina1.vaziuoti()
masina1.stoveti()
masina1.pildyti_degalu()
print("--------------------")

# Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“
# Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        #super().pildyti_degalu()
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")

# Sukurti norimą Elektromobilio objektą
# Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai

masina2 = Elektromobilis(2021, "Kia", "elektra")
print(masina2.metai, masina2.modelis, masina2.kuro_tipas)
masina2.vaziuoti()
masina2.stoveti()
masina2.pildyti_degalu()
masina2.vaziuoti_autonomiskai()


