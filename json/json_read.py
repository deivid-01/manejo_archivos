import json


#Abrir el archivo y leer los datos
fileName="estudiante.json"
data = {}
with open(fileName,'r') as json_file:
    data = json.load(json_file)
    print("Archivo leido correctamente")

print(type(data))
print(data["nombre"])
#Convertir a diccionario el resultado de la lectura