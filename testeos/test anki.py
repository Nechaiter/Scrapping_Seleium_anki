import genanki
import os
import json
# Define el mazo
id=1 #ID del mazo
deck_principal = genanki.Deck(
    id,  # Un ID único para tu mazo
    'Matemáticas'
)
#Matematicas::Aritmetica::Unit 1
#deckes=[]

location = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Datos Unificados'
file_name = 'datos.json'
file_path= os.path.join(location, file_name)
with open(file_path, 'r',encoding='utf-8') as file:
    data = json.load(file)
Asignatura=[]
Unidades=[]
Lecciones=[]
for curso in data['Cursos']:
    deck=genanki.Deck(id+1, 'Matemáticas::'+curso['nombre'])
    Asignatura.append(deck)
    print(' '+curso['nombre'])
    for unidad in curso['Unidades']:
        deck=genanki.Deck(id+2, 'Matemáticas::'+curso['nombre']+'::'+unidad['nombre'])
        Unidades.append(deck)
        print('     '+unidad['nombre'])
        try:
            for leccion in unidad['Lecciones']:
                deck=genanki.Deck(id+3, 'Matemáticas::'+curso['nombre']+'::'+unidad['nombre']+'::'+leccion['nombre'])
                Lecciones.append(deck)
                print('         '+leccion['nombre'])
        except:
            Unidades.pop()
            continue
    break
print(len(Asignatura))
print(len(Unidades))
print(len(Lecciones))