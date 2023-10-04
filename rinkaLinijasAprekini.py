import math
def laukums (r):
    S = math.pi*r**2
    return S
print ("Ievadies rādiusus 1")
r1 = int(input())
print ("Ievadies rādiusus 2")
r2 = int(input())
S1 = laukums(r1)
S2 = laukums(r2)
print ("Riņķa ar radiusu", r1, "laukums ir", laukums(r1)/laukums(r2),"reizes lielāks par riņķi ar rādiusu", r2)