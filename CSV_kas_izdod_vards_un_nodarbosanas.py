import csv
arhivs = open("vards_un_nodarbosanas.csv", "r") 
reader = csv.reader(arhivs, delimiter=",")
for ieraksts in reader:
    vards = ieraksts[0]
    nodarbosanas = ieraksts[3]
    print(f"{vards} - {nodarbosanas}")
arhivs.close()
