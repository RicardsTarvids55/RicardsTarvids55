class Transports:
    
    def __init__(self, Marka, Gads, Max_atrums, Nobraukums):
        self.marka = Marka
        self.gads = Gads
        self.max_atrums = Max_atrums
        self.nobraukums = Nobraukums


class Autobuss(Transports):
    pass

a = Autobuss("Audi", 2010, 200, 150000)
print("Autobus marka ir " + a.marka + ", tā izveides gads ir " + str(a.gads) + ", tā maksimālais ātrums ir " + str(a.max_atrums) + "km/h" + ", tā nobraukums ir " + str(a.nobraukums) + "km")