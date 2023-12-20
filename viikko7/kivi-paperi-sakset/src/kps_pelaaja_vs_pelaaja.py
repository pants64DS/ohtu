from kps import KPS

class KPSPelaajaVsPelaaja(KPS):
    def luo_vastapelaaja(self):
        return Vastapelaaja()

class Vastapelaaja:
    def anna_siirto(self):
        return input("Toisen pelaajan siirto: ")

    def aseta_siirto(self, ekan_siirto):
        pass
