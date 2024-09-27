import os
import json

location = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Datos Unificados'
file_name = 'datos.json'
file_path= os.path.join(location, file_name)
with open(file_path, 'r',encoding='utf-8') as file:
    data = json.load(file)

cursos = data['Cursos']

for curso in cursos:  #Contiene los objetos que estan dentro de CURSOS, es decir, los cursos
    print(f"Curso:  {curso['nombre']}")
    for unidad in curso['Unidades']:   #Contiene los objetos que estan dentro del objeto del curso
        print(f"  Unidad: {unidad['nombre']}")
        try:
            for leccion in unidad['Lecciones']:
                print(f"    Lección: {leccion['nombre']}")
        except:
            print("     No hay lecciones")
            continue
    break
    # for unidad in curso['Unidades']:
    #     print(f"  Unidad: {unidad['nombre']}")
    #     for leccion in unidad['Lecciones']:
    #         print(f"    Lección: {leccion['nombre']}")