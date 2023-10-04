def linoleja_funkcija():
    p = float(input("Cik metrus plata ir istaba"))
    g = float(input("Cik metrus gara ir istaba"))
    w = float(input("Cik strādnieks prasa algu par kvadrātmetru linoleja?"))
    y = float(input("Cik maksā 1 kvadrātmetrs linoleja?"))
    room = (p*g)
    total = (room*y)+(w*room)
    print ("Istaba ir", room, "kvadrātmetrus plaša") 
    return total   
z = linoleja_funkcija()
print (z,"€")