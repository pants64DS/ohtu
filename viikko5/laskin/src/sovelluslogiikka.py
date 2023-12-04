from enum import Enum

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvot = [arvo]

    def miinus(self, operandi):
        self.aseta_arvo(self._arvot[-1] - operandi)

    def plus(self, operandi):
        self.aseta_arvo(self._arvot[-1] + operandi)

    def nollaa(self, operandi):
        self.aseta_arvo(0)

    def kumoa(self, operandi):
        if len(self._arvot) > 1:
            self._arvot.pop()

    def aseta_arvo(self, arvo):
        if arvo != self._arvot[-1]:
            self._arvot.append(arvo)

    def arvo(self):
        return self._arvot[-1]

    def komennot(self):
        return Komento

    def suorita(self, komento, operandi):
        komennot = {
            Komento.SUMMA: self.plus,
            Komento.EROTUS: self.miinus,
            Komento.NOLLAUS: self.nollaa,
            Komento.KUMOA: self.kumoa
        }

        komennot[komento](operandi)
