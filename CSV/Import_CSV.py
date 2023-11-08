Import CSV 
#Opening the CSV file
with open ('Giants.CSV', mode = 'r') as file:
    #Reading the CSV file 
    csvFile = csv.reader(file)
    #Displaying the contents of the CSV file 
    for lines in csvFile:
        print(lines)