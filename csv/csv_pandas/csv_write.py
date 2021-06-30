import pandas as pd

# Creacion de los datos ##############
fields = ['Nombre','Edad']


data = [['Andres',28],
        ['Diana',10]]

#Crear Dataframe con los datos (Tabla) #########
df = pd.DataFrame(data=data, columns=fields)


#Guardar Dataframe en archivo csv
fileName="personas.csv"

df.to_csv(fileName)

