#Importar el modulo
import json

#1. Convertir JSON a Python
persona = '{"nombre":"Fabio", "apellido":"Cortez", "edad":20}'

#Convertir string a python

y = json.loads(persona)

#print(type(y))
#print(y["nombre"])

#2. Convertir Python a JSON

x = {
    "nombre":"John",
    "ciudad":"Medellin",
    "edad": 30
}

#Convertir a JSON 
y = json.dumps(x)

print(type(y))
print(y)