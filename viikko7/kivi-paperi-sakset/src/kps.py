from tuomari import Tuomari

class KPS:
    def tulosta_vastapelaajan_siirto(self, siirto):
        pass

    def _anna_siirrot(self, vastapelaaja):
        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = vastapelaaja.anna_siirto()
        vastapelaaja.aseta_siirto(ekan_siirto)

        self.tulosta_vastapelaajan_siirto(tokan_siirto)

        return ekan_siirto, tokan_siirto

    def pelaa(self):
        tuomari = Tuomari()

        vastapelaaja = self.luo_vastapelaaja()
        siirrot = self._anna_siirrot(vastapelaaja)

        while set(siirrot).issubset("kps"):
            tuomari.kirjaa_siirto(*siirrot)
            print(tuomari)

            siirrot = self._anna_siirrot(vastapelaaja)

        print("Kiitos!")
        print(tuomari)
