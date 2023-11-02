import random
f = open("saraksts.txt", "w")
for i in range (100):
    number = random.randint(0, 1000)
    #f.write(str(number + "/n"))
    f.write(f"{ number}/n")
    print(number)
f.close()