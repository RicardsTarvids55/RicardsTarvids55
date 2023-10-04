manavardnica = {
     'vards': 'Kitija',
     'vecums': 25,
     'alga': 1500,
     'pilseta': 'Tukums'
 }
manavardnica.pop('vards')
manavardnica.pop('alga')
print(manavardnica)
manavardnica = {
     'vards': 'Kitija',
     'vecums': 25,
     'alga': 1500,
     'pilseta': 'Tukums'
  }
keys = ['vards','alga']
for i in keys:
    manavardnica.pop(i)
print(manavardnica)
darbinieki={
    'vards': 'Ketllina',
    'vecums': 25,
    'telefons': "+3172196341",
    'ciemats': 'Dobele'
}
darbinieki.pop('ciemats')
darbinieki.update({'pilseta': 'Dobele'})
print(darbinieki)