import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv('./living.csv', encoding='latin1')
df = pd.DataFrame(datos)
#Los 10 paises con el costo de vida mas alto
top_10_paises_costo_vida_alto = df.nlargest(10, 'Cost of living, 2017')
plt.figure(figsize=(10, 6))
plt.bar(top_10_paises_costo_vida_alto['Countries'], top_10_paises_costo_vida_alto['Cost of living, 2017'], color='skyblue')
plt.xlabel('Paises')    
plt.ylabel('Costo de vida')
plt.title('Top 10 paises con el costo de vida mas alto')
plt.xticks(rotation=45)
plt.show()

#Los 10 paises con el costo de vida mas bajo
top_10_paises_costo_vida_bajo = df.nsmallest(10, 'Cost of living, 2017')
plt.figure(figsize=(10, 6))
plt.bar(top_10_paises_costo_vida_bajo['Countries'], top_10_paises_costo_vida_bajo['Cost of living, 2017'], color='skyblue')
plt.xlabel('Paises')
plt.ylabel('Costo de vida')
plt.title('Top 10 paises con el costo de vida mas bajo')
plt.xticks(rotation=45)
plt.show()

# El costo de vida de los paises de America
america = datos[datos['Continent'] == 'America']
plt.figure(figsize=(10, 8))
plt.bar(america['Countries'], america['Cost of living, 2017'], color='skyblue')
plt.xlabel('Paises')
plt.ylabel('Costo de vida en America')
plt.title('Costo de vida en los paises de America')
plt.xticks(rotation=45)
plt.show()