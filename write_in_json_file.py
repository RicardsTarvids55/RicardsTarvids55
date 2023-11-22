arhivs = open("dati.json", "w")
json.dump(dati, arhivs, indent=4)
arhivs.close()