def burti_a(fails):
    with open (fails, 'r') as f: 
        saturs = f.read()
        skaits = saturs.count('a')
    return skaits
fails = "text.txt"
skaits = burti_a(fails)
print (f"Failā '{fails}' ir { skaits} burti 'a'.")