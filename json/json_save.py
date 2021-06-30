import json


#Crear diccionario
list_data = []
data = {
    "nombre":"Carlos",
    "asignatura":"Fisica",
    "notas":[4,4.5]
}

#Crear el archivo donde se va a guardar la informacion
fileName="estudiante.json"
with open(fileName,'w') as json_file:
    # Guardar la informacion
    json.dump(data,json_file)
    print("Archivo "+fileName+" guardado")


