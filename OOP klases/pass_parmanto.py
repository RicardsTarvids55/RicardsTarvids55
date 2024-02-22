class  Vienakalse:
    def __init__ (self, Mainigais):
        self.mainigais = Mainigais

class Otraklase(Vienakalse):
    pass

p = Otraklase(100)
print(p.mainigais)