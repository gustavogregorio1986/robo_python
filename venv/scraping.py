import requests

url = "https://ultimosegundo.ig.com.br/"

html = requests.get(url).text

print(html)

endpoint = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(endpoint)

print(response)
