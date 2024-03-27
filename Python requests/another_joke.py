import requests
res = requests.get("https://v2.jokeapi.dev/joke/Any?format=txt&type=single")

print(res.text)