import json
import os
# Lista para almacenar los datos combinados
combined_data = []

# Nombres de los archivos JSON
files = ['datos 1.json', 'datos 2.json', 'datos 3.json']

# Leer y combinar los datos de cada archivo
location = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Datos Json'

for file_name in files:
    file_path= os.path.join(location, file_name)
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
        combined_data.append(data)

# Ahora puedes trabajar con los datos combinados
Cursos = []
for data in combined_data:
    for curso in data['cursos']:
        Cursos.append(curso)
print(len(Cursos))
datos = {'Cursos': Cursos}
directorio = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Datos Unificados'
nombre_archivo = 'datos.json'
ruta_archivo = os.path.join(directorio, nombre_archivo)
with open(ruta_archivo, 'w', encoding='utf-8') as file:
    json.dump(datos, file, ensure_ascii=False, indent=4)
