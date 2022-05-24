class Bruch():
    def __init__(self, zaehler, nenner=1):
        self.zaehler = zaehler
        if (nenner == 0):
            self.nenner = 1
            print("Nenner darf nicht 0 sein")
        else :
            self.nenner = nenner
        if self.nenner < 0:
            self.nenner  *= -1
            self.zaehler *= -1

    def dezimalwert(self):
        return self.zaehler / self.nenner

    def erweitern(self,faktor):
        self.zaehler *= faktor
        self.nenner  *= faktor

    def kuerzen(self):
        teiler = self.ggt(self.zaehler, self.nenner)
        self.zaehler //= teiler
        self.nenner  //= teiler
    
    def multipliziere(self, bm):
        z = self.zaehler * bm.zaehler
        n = self.nenner * bm.nenner
        temp = Bruch(z, n)
        temp.kuerzen()
        return temp

    def dividiere(self, bd):
        z = self.zaehler * bd.nenner
        n = self.nenner  * bd.zaehler
        temp = Bruch(z, n)
        temp.kuerzen()
        return temp

    def addiere(self, ba):
        z = self.zaehler*ba.nenner + ba.zaehler*self.nenner
        n = self.nenner * ba.nenner
        temp = Bruch(z, n)
        temp.kuerzen()
        return temp
        
    def subtrahiere(self, bs):
        z = self.zaehler*bs.nenner - bs.zaehler*self.nenner
        n = self.nenner * bs.nenner
        temp = Bruch(z, n)
        temp.kuerzen()
        return temp
        
    # größte gemeinsame Teiler von a und b
    def ggt(self, a, b):
        a = abs(a)
        b = abs(b)
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a
            
    def ausgabe(self):
        print(f'{self.zaehler:d} / {self.nenner:d}')

        
        

# Hauptprogramm
b1 = Bruch(4,6)
b1.ausgabe()
print("Dezimalwert = ",b1.dezimalwert())

b1.erweitern(2)
b1.ausgabe()
print("Dezimalwert = ",b1.dezimalwert())

b1.kuerzen()
b1.ausgabe()
b2 = Bruch(1,3)

b1.ausgabe()
b2.ausgabe()
print("b2 * b1")
b3 = b2.multipliziere(b1)
b3.ausgabe()

# 4/5 div 4/3 --> 12/20
print("dividieren")
b4 = Bruch(4,5)
b5 = Bruch(4,3)
b6 = b4.dividiere(b5)
b6.ausgabe()

# 2/3 + 1/4 = 11/12
print("addieren")
b7 = Bruch(2,3)
b8 = Bruch(1,4)
b9 = b7.addiere(b8)
b9.ausgabe()

# 9/10 - 2/5 = 1/2
print("subtrahieren")
b10 = Bruch(9,10)
b11 = Bruch(2,5)
b12 = b10.subtrahiere(b11)
b12.ausgabe()

#  Test
print("--Test--")
Bruch(1,-3).addiere(Bruch(5,6)).ausgabe()
Bruch(8,25).addiere(Bruch(2,15)).ausgabe()


