import datetime

class Persona:

    def __init__(self, Name, Surname, Country, Birthdate):
        self.name = Name
        self.surname = Surname
        self.country = Country
        self.birthdate = Birthdate
    
    def introduce_self(self):
        today = datetime.datetime.now()
        age = today.year - self.birthdate.year
        print ("Mani sauc " + self.name + " " + self.surname + ", mana dzimtā valsts ir " + self.country + ", es esmu " + str(age) + " gadus vecs.") 



person = Persona("Antons", "Pakalns", "Latvija", datetime.datetime(1982, 6, 1))

person.introduce_self()
