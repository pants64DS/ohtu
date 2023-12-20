from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def luo_vastapelaaja(self):
        return Tekoaly()

    def tulosta_vastapelaajan_siirto(self, siirto):
        print(f"Tietokone valitsi: {siirto}")
