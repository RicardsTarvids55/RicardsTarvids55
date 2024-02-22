import math
class Riņķis:
    def __init__(self, radiuss):
        self.radiuss = radiuss

    def rinka_laukums(self):
        return math.pi * self.radiuss ** 2
    
    def rinka_linija(self):
        return 2 * math.pi * self.radiuss
    
riņķis1 = Riņķis(5)
print("Riņķa laukums:", riņķis1.rinka_laukums())
print("Riņķa līnija:", riņķis1.rinka_linija())