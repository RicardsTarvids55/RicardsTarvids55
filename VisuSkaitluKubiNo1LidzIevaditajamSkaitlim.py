import math
while True:
    user_input = input("Ievadiet skaitli") 
    if user_input == "exit":
        break
    y = int(user_input)
    x = pow(y, 3)
    print(x)