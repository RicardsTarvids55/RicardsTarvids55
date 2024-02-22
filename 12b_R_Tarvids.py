#1. uzdevums are koeficentu 0,6
#definēju klasi
class Kalkulators:
#definēju metodes
    def __init__ (self, skaitlis1, skaitlis2):
        self.skaitlis1 = skaitlis1
        self.skaitlis2 = skaitlis2

    def skaitlu_summa(self):
        return self.skaitlis1 + self.skaitlis2
    
    def skatilu_starpiba(self):
        return  self.skaitlis1 - self.skaitlis2 
    
    def skaitlu_reizinajums(self):
        return  self.skaitlis1 * self.skaitlis2
    
    def skaitlu_dalijums(self):
        return  self.skaitlis1 / self.skaitlis2
    
#lieku ievadīt izvēlētos skaitļus
skaitlis1 = int(input("Ievadiet pirmo skaitli"))
skaitlis2 = int(input("Ievadiet otro skaitli"))

rezultati = Kalkulators(skaitlis1, skaitlis2)

#parādu rezultātus
print("Skaitļu summa:", rezultati.skaitlu_summa())
print("Skaitļu starpība:", rezultati.skatilu_starpiba())
print("Skaitļu reizinājums:", rezultati.skaitlu_reizinajums())
print("Skaitļu dalījums:", rezultati.skaitlu_dalijums())

#2. uzdevums ar koeficentu 1.0


#definēju klasi
class Taisnstūris:
    #definēju metodes
    def __init__(self, mala_garums, mala_platums):    
        self.m1 = mala_garums
        self.m2 = mala_platums

    def Perimetra_aprekinasana(self):
        return 2*(self.m1 + self.m2)
    
    def Laukuma_aprekinasana(self):
        return self.m1 * self.m2
    
#lieku ievadīt izvēlētos skaitļus

mala_garums = int(input("Ievadiet malas garumu"))
mala_platums = int(input("Ievadiet malas platumu"))
    
#parādu rezultātus

rezultati = Taisnstūris(mala_garums, mala_platums)
print("Malas garums:", mala_garums, "centimetri")
print("Malas platums:", mala_platums, "centimetri")
print("Taisnstūra perimetrs:", rezultati.Perimetra_aprekinasana(), "kvadrātcentimetri")
print("Taisnstūra laukums:", rezultati.Laukuma_aprekinasana(), "kvadrātcentimetri")    

#pārmantoju rezultātus uz otru klasi

class Paralelskaldnis(Taisnstūris):
    pass

#augstums = mala_garums
#platums un garums = mala_platums

#parādu rezultātus
Tilpums = Paralelskaldnis(mala_garums, mala_platums)
print("Paralelskalņa tilpums: ", mala_garums * mala_platums * mala_platums, ("kubikcentimetri"))