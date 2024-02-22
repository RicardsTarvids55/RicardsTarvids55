#Objektu klase ir viena tipa objektu lielas kopas apkopotais apraksts. Objekti ir savas klases konkrētie pārstāvji, to ir pieņemts saukt par klases eksemplāriem.
#Peiemēram Klase ir SUNS, bet klases eksemprlārs ir DUKSIS
#Klases nosaukumus definējam ar lielo burtu

class Skolens:
    vecums = 18
    vards = "Visvaris"
    uzvards = "Krūmiņš"

    def skolena_vards(self):
        return self.vards

skolena_objekts = Skolens()

print(skolena_objekts.skolena_vards())

