from luo_peli import luo_peli

__ohje = """Valitse pelataanko
 (a) Ihmistä vastaan
 (b) Tekoälyä vastaan
 (c) Parannettua tekoälyä vastaan
Muilla valinnoilla lopetetaan"""

def main():
    while True:
        print(__ohje)
        vastaus = input()

        peli = luo_peli(vastaus)
        if not peli: break

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        peli.pelaa()

if __name__ == "__main__":
    main()
