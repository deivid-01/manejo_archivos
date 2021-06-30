import csv

fields = []
rows = []
fileName="personas.csv"

with open(fileName,'r') as csv_file:
    #Crear objeto reader
    csv_reader=  csv.reader(csv_file)

    #Obtener encabezado
    fields = next(csv_reader)

    #Extrar cada una de las filas
    for row in csv_reader:
        rows.append(row)
print(fields)
print(rows)
