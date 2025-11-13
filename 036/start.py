class Car:
    def __init__(self, brand, model, year, fuel=100):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel = fuel
        self.blinker = None  # None, 'left', 'right'

    def drive(self):
        if self.fuel > 0:
            self.fuel -= 10
            if self.blinker:
                signal = f" mit eingeschaltetem Blinker {self.blinker}"
            else: 
                signal = ""
            print(f"{self.brand} {self.model} fährt{signal}! Tankstand: {self.fuel}%")
        else:
            print(f"{self.brand} {self.model} kann nicht fahren – Tank ist leer")

    def refuel(self):
        self.fuel = 100
        print(f"{self.brand} {self.model} wurde vollgetankt. Als Bonus gibt's einen Döner aufs Haus!")

    def blinker_setzen(self, direction):
        if self.bmw_check():
            print("BMW-Fahrer benutzen keine Blinker!")
            return
        if direction in ['left', 'right']:
            self.blinker = direction
            print(f"{self.brand} {self.model} setzt den Blinker: {direction}")
        else:
            self.blinker = None
            print(f"{self.brand} {self.model} hat den Blinker ausgeschaltet")

    def bmw_check(self):
        if self.brand.lower() == "bmw":
            print("Blinker? Was ist das? Ich fahre BMW – wir kommunizieren mit Geschwindigkeit")
            return True
        return False


auto1 = Car("BMW", "M3", 2022)
auto2 = Car("Volkswagen", "Golf", 2018)

auto1.drive()
auto1.blinker_setzen('left')
auto1.drive()
auto1.blinker_setzen(None)
auto1.drive()
auto1.drive()
auto1.refuel()
auto1.drive()


auto = Car("Mercedes", "C-Klasse", 2020)
auto.refuel()

auto2.blinker_setzen("rechts")
auto2.drive()
auto2.blinker_setzen(None)