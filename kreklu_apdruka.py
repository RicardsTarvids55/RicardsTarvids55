import math
def pasuti_tkreklus():
    a = int(input("Cik kreklus vēlies pasūtīt?"))
    procenti = 15
    cena_par_kreklu = 5
    b = a * cena_par_kreklu
    c = 0
    d = 0
    e = 0
    print ("Izvēlies apdruku:")
    print ("1. TEKSTS")
    print ("2. ZIME")
    print ("3. FOTO")
    choice = int(input("Ieraksties ciparu, kuru opciju izvēlējāties (1/2/3):"))
    if choice == 1:
        c = 10*a
        print ("Jūs izvēlējies TEKSTS apdurku, par pasūtījumu Jums jāmaksā", c)
    elif choice == 2:
        d = 12*a
        print ("Jūs izvēlējāties ZIME apdruku, par pasūtījumu Jums jāmaksā", d)
    elif choice == 3:
        e = 25*a
        print ("Jūs izvēlējāties FOTO opciju, par pasūtījumu Jums jāmaksā", e)
    else:
        print("Šāda opcija Jums netika dota")
    delivery_fee = 0
    if c < 50 or d < 50 or e < 50:
        delivery_fee = 15
    total_price = b+ delivery_fee
    if total_price > 100:
        atlaide = total_price * procenti/100
        cena_ar_atlaidi = total_price - atlaide
        print ("Jūsu pirkums pārsniedz 100 eiro, Jūs esat saņēmuši 5% atlaidi no Jūsu pirkuma! Cena, kas Jums ir jāmaksā ir", cena_ar_atlaidi)
    else:
        print ("Gala cena nepārsniedz 50, par piegādi ir jāmaksā, Jūsu gala rēķins ir ", c + delivery_fee)
pasuti_tkreklus()
#gala rēķins d un e nav pareizs vēl