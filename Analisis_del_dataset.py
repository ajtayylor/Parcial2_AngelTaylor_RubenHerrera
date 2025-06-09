import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL RAW del archivo CSV en GitHub (reemplaza con el tuyo)
url = 'https://raw.githubusercontent.com/ajtayylor/Parcial2_AngelTaylor_RubenHerrera/refs/heads/main/Dataset_uso_ram.csv'

# Cargar el dataset desde GitHub
df = pd.read_csv(url)

# Convertir timestamp a datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Eliminar columnas que no aportan (columnas que son constantes)
df = df.loc[:, df.nunique() > 1]

# ESTADÍSTICAS BÁSICAS
print("----- ESTADÍSTICAS BÁSICAS -----")
print("Media:\n", df.mean(numeric_only=True))
print("\nMediana:\n", df.median(numeric_only=True))
print("\nModa:\n", df.mode(numeric_only=True).iloc[0])
print("\nDesviación estándar:\n", df.std(numeric_only=True))

# MATRIZ DE CORRELACIÓN
print("\n----- MATRIZ DE CORRELACIÓN -----")
correlacion = df.corr(numeric_only=True)
print(correlacion)


# VISUALIZACIÓN CON SEABORN
plt.figure(figsize=(10, 8))
sns.heatmap(correlacion, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Matriz de Correlación del Dataset')
plt.tight_layout()
plt.show()