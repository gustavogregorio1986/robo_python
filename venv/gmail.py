from imbox import Imbox
import json

with open("credenciais_gmail.json","r") as file:
    credenciais = json.loads(file.read())