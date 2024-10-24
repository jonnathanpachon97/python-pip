import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame
data = {
    'Nombre': ['Ana', 'Luis', 'Pedro', 'María', 'Javier'],
    'Edad': [23, 34, 45, 29, 37],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid', 'Barcelona']
}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)

# Filtrar filas
mayores_de_30 = df[df['Edad'] > 30]
print(mayores_de_30)

# Graficar
plt.figure(figsize=(8, 5))
plt.bar(mayores_de_30['Nombre'], mayores_de_30['Edad'], color='skyblue')
plt.title('Personas mayores de 30 años')
plt.xlabel('Nombre')
plt.ylabel('Edad')
plt.xticks(rotation=45)
plt.ylim(30, 50)  # Ajustar límites del eje y
plt.grid(axis='y')

# Mostrar la gráfica
plt.show()