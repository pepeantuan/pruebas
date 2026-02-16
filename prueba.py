import os

# Nombre del archivo
#nombre_fichero = "datos.txt"
# RUTA ABSOLUTA a tu carpeta personal
ruta_fichero = r"D:\Files\datos.txt"

# Verificamos si el archivo existe para evitar errores en el Runner
if os.path.exists(nombre_fichero):
    with open(nombre_fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        
        total_registros = len(lineas)
        
        print("--- DEMOSTRACIÓN DE LECTURA ---")
        # Mostramos los 3 primeros (o menos si el archivo es corto)
        print("Primeros 3 registros:")
        for i, linea in enumerate(lineas[:3]):
            print(f"  {i+1}: {linea.strip()}")
            
        print("-------------------------------")
        print(f"CONTEO TOTAL: El fichero tiene {total_registros} registros.")
else:
    print(f"Error: No se encuentra el archivo {nombre_fichero} en la carpeta actual.")

