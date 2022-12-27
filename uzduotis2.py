# Turėtų klasę Darbuotojas
# Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
import datetime

class Darbuotojas():
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

# Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien
    # (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)

    def _kiek_dirbo(self):   #privatus metodas?po viena bruksneli?
        laikas = datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
        siandien = datetime.datetime.today()
        kiek_dienu_dirba = siandien - laikas
        print(f"Dirba: {kiek_dienu_dirba} ") #svarbus - rodo dirba kiek dienu
        return kiek_dienu_dirba.days * 8


# Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą
# (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
    def paskaiciuoti_atlyginima(self):
        alga = self.valandos_ikainis * self._kiek_dirbo()
        print(self.vardas + " užsidirbo: " + str(alga) + " eur")
        #return alga

# Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę

class NormalusDarbuotojas(Darbuotojas):
    def _kiek_dirbo(self):  # privatus metodas?po viena bruksneli?
        laikas = datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
        siandien = datetime.datetime.today()
        kiek_dienu_dirba = siandien - laikas
        print(f"Dirba: {kiek_dienu_dirba} ")
        return round(kiek_dienu_dirba.days * 8 / 7) * 5


# Sukurti norimą Darbuotojo objektą
# Sukurti norimą NormalusDarbuotojas objektą
# Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima

dirbantis = Darbuotojas("Antanas", 62, "2011-11-03")
dirbantis_maziau = NormalusDarbuotojas("Vincas", 12, "2014-08-08")


dirbantis.paskaiciuoti_atlyginima()
print("----------------------------------------")

dirbantis_maziau.paskaiciuoti_atlyginima()


