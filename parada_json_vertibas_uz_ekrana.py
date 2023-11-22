import json
f = open("example_2.json")
data = json.load(f)
for i in data ["quiz"]:
    print(i)
f.close()