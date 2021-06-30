import pandas as pd

fileName="personas.csv"

df = pd.read_csv(fileName)


mean = sum(df.Edad.tolist())/2
print(mean)