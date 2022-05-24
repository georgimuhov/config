class Konto:
    """ Bank Kontoverwaltung """
    __geldbestand = 0 # Klassenvariable, existiert unabhängig von der Anzahl
                    # gebildeter Objekte nur einmal !!

    def __init__(self, kontonummer, kontostand=0):
        self.__kontonr = kontonummer
        self.__kontostand = kontostand

    def abheben(self, betrag):
        self.__kontostand -= betrag
        Konto.__geldbestand -= betrag

    def einzahlen(self, betrag):
        self.__kontostand += betrag
        Konto.__geldbestand += betrag

    def kontostand_anzeigen(self):
        print(self.__kontonr, "aktueller Kontostand: ", self.__kontostand)
        print("Geldbestand der Bank: ", Konto.__geldbestand)

# Hauptprogramm
kolbe = Konto("0012345")
kolbe.kontostand_anzeigen()

kolbe.abheben(150)
kolbe.kontostand_anzeigen()

kolbe.einzahlen(280)
kolbe.kontostand_anzeigen()

# kolbe.kontostand = 150000210 #sehr frech !!
# kolbe.kontostand_anzeigen()

huber = Konto("00471101")
huber.einzahlen(850)
huber.kontostand_anzeigen()
#kolbe.kontostand = 150000210 #sehr frech !!
kolbe.kontostand_anzeigen()

