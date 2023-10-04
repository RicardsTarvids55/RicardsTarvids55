num = 1234567
counter = 0 
while num != 0: 
    #izmanto floor dalīšanu 
    #Lai samazinātu ciparu skaitu skaitlī
    num = num // 10
    #palielinām skaitītāju par 1
    counter = counter + 1
print ("Ciparu skaits skaitlī ir", counter)