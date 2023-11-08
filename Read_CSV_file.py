with open ("plankton.csv") as file: 
    for line in file: 
        row = line.rstrip().split(";")
        print(f"{row[1]} is in {row[2]}")