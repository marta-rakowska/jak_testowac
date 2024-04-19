class Czlowiek():
    def __init__(self, imie, kolor_wlosow):
        self.imie = imie
        self.kolor_wlosow = kolor_wlosow
        self.wiek = 0

    def urodziny(self):
        self.wiek = self.wiek + 1

    def przedstaw_sie(self):
        print('Mam na imie', self.imie, 'i mam lat', self.wiek)

Ala = Czlowiek('Ala', 'czarne')
Ala.urodziny()

Adam = Czlowiek('Adam', 'blond')

Ala.urodziny()
Adam.urodziny()

Ala.urodziny()
Adam.urodziny()

Ala.przedstaw_sie()
Adam.przedstaw_sie()

print(Ala.wiek)