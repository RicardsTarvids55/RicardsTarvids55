import csv
import random
with open('Numbers.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Random number"])
    for i in range (50):
        number = random.randint(0, 1000)
        writer.writerow([number])
f.close()