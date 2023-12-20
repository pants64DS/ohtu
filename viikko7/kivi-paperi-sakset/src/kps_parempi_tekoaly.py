from tekoaly_parannettu import TekoalyParannettu
from kps_tekoaly import KPSTekoaly

class KPSParempiTekoaly(KPSTekoaly):
    def luo_vastapelaaja(self):
        return TekoalyParannettu(10)
