import json


def saveJSON(data,fileName):
    try:
        with open(fileName,'w') as json_file:
        # Guardar la informacion
            json.dump(data,json_file)
            print("Archivo "+fileName+" guardado")
    except :
        print("Archivo no fue creado exitosamente")



def readJSON(fileName):
    with open(fileName,'r') as json_file:
        data = json.load(json_file)
        print("Archivo leido correctamente")
        return data
