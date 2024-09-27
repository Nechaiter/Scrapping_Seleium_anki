import os
import json
datos={}
Iteraciones=1

directorio = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Datos Json'
nombre_archivo = 'datos '+str(Iteraciones)+'.json'
ruta_archivo = os.path.join(directorio, nombre_archivo)
with open(ruta_archivo, 'w', encoding='utf-8') as file:
    json.dump(datos, file, ensure_ascii=False, indent=4)