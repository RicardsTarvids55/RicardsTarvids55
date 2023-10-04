import random
def nedelas_horoskopi():
    prognozes_zimei = {
        "AUNS": ["Šonedēl Jums nedēļa būs veiksmīga un priek pilna", "Jums ieteicams palikt mājās, jo ir iespēja negadījumiem ārpus dzīvesvietas", "Jūs sagaida lieliska dzīves iespēja"],
        "VĒRSIS": ["Jums sekos apkārt laba enerģija, kas uzlabos citu dienu", "Jums sekos apkārt slikt enerģija, kas izbojās citiem dienu", "Šī nedēļa padarīs jūs par labāku sevis versiju"],
        "DVĪŅI": ["Apmeklējiet draugus, jo Jūs ar nepacietību tiekat gaidīti", "Apmeklējiet ģimeni, jo Jūs ar nepacietību tiekat gaidīti", "Apmeklējiet veikalu, jo Jūs ar nepacietību tiekat gaidīti"],
        "VĒZIS": ["Šonedēļ komunikācija ir visa atslēga", "Šonedēļ komunikācija nav visa atslēga", "Šonedēļ komunikācija varbūt ir visa atslēga"],
        "LAUVA": ["Šonedēļ Jums būs enerģijas bez gala", "Šonedēļ Jums nebūs enerģijas bez gala", "Šonedēļ iespējams Jums būs enerģijas bez gala"],
        "JAUNAVA": ["Šodien Jūsu skaistums būs nepārspējams", "Šodien Jūsu skaistums nebūs nepārspējams", "Šodien Jūsu skaistums varbūt būs nepārspējams"],
        "SVARI": ["Šonedēļ Jums ir ieteicams investēt", "Šonedēļ Jums nav ieteicams investēt", "Šonedēļ Jums varbūt ir ieteicams investēt"],
        "SKORPIONS": ["Šonedēļ Jūs lieliski pavaditu laiku Ēģiptē", "šonedēļ Jūs lieliski nepavaditu laiku Ēģiptē", "Šonedēļ Jūs lieliski pavaditu laiku mājās"],
        "STRĒLNIEKS": ["Šonedēļ Jūs lieliski tēmēsiet", "Šonedēļ Jūs lieliski netēmēsiet", "Šonedēļ Jūs varbūt lieliski tēmēsiet"],
        "MEŽĀZIS": ["Šonedēļ Jums būtu jāgatavojas ziemas miegam", "Šonedēļ Jums nebūtu jāgatavojas ziemas miegam", "Šonedēļ Jums varbūt būtu jāgatavojas ziemas miegam"],
        "ŪDENSVĪRS": ["Šonedēļ Jums ir ieteicams peldēties", "Šonedēļ Jums nav ieteicams peldēties", "Šonedēļ Jums varbūt ir ieteicams peldēties"],
        "ZIVIS": ["Šonedēļ Jums jāuzmanās no dzīves āķiem", "Šonedēļ Jums nav jāuzmanās no dzīves āķiem", "Šonedēļ Jums varbūt jāuzmanās no dzīves āķiem"],
    }
    for zimei, prognozes in prognozes_zimei.items():
        random_prognozes = random.choice(prognozes_zimei[zimei])
        print(f"{zimei}: {random_prognozes}")
nedelas_horoskopi()