import psutil
import pandas as pd
from datetime import datetime
from time import sleep

datos = []
intervalo_segundos = 1.5
repeticiones = 400  # Recolectar 400 registros

print(f"Iniciando recolección de {repeticiones} registros de RAM...")

for i in range(repeticiones):
    memoria = psutil.virtual_memory()
    total_MB = round(memoria.total / 1024 / 1024, 2)
    available_MB = round(memoria.available / 1024 / 1024, 2)
    used_MB = round(memoria.used / 1024 / 1024, 2)
    free_MB = round(memoria.free / 1024 / 1024, 2)
    percent_used = memoria.percent

    datos.append({
        'timestamp': datetime.now(),
        'total_MB': total_MB,
        'available_MB': available_MB,
        'used_MB': used_MB,
        'free_MB': free_MB,
        'percent_used': percent_used
    })

    print("[{", i+1, "repeticiones Uso de RAM: ", percent_used)
    sleep(intervalo_segundos)

# Guardar a CSV
df = pd.DataFrame(datos)
df.to_csv("uso_ram_windows.csv", index=False)
print("\n✅ Archivo guardado como uso_ram_windows.csv")

# Detección simple de uso anómalo de RAM
excesivos = df[(df['percent_used'] > 22) | (df['available_MB'] < df['total_MB'] * 0.10)]

if len(excesivos):
    print("\nUso de memoria sospechoso detectado:")
    print(excesivos[['timestamp', 'percent_used', 'available_MB']])
else:
    print("\nRAM en niveles normales durante el monitoreo.")
