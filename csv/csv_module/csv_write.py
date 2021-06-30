import csv

fields = ['Nombre','Edad']



rows = [['Andres','28'],
        ['Diana','18']]

fileName="personas.csv"

#Guardar informacion en archivo
with open(fileName,'w') as csv_file:
    #Crear un objeto de tipo writer
    csv_writer = csv.writer(csv_file)
    #Añadir encabezado al archivo
    csv_writer.writerow(fields)
    #Añadir datos al archivo
    csv_writer.writerows(rows)

    print("Archivo creado exitosamente")
