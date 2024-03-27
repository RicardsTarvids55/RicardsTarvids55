import requests
URL = str(input("Ievadiet programmas URL:"))
r = requests.get(URL)
answer = print(r)
if r.status_code == 200:
    print("URL pastāv")
else:
    print ("Šādas mājaslapas neksistē")