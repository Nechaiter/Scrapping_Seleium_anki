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
# Define un modelo de carta
my_model = genanki.Model(
    1607392319,
    'Simple Model',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
    ],
    templates=[
        {
            'name': 'Tarjeta 1',
            'qfmt': '{{Front}}',  # Formato del anverso
            'afmt': '{{Back}}',   # Formato del reverso
        },
    ],
)

Criterio='''again: (Fail once) I forgot, wrong answer (memory interference), lucky guess, or partial recall (I consider not enough to be a pass)
            hard: successful but effortful recall
            good: default pass grade
            easy: quick and easy, feeling that the review was not needed, even a waste of time'''



    
Carta={'Nombre_Leccion':Asignatura, 'critero': Criterio}
unidades.append(curso['unidades'])

unidades = [
    {'link': 'https://www.khanacademy.org/math/1', 'criterio': 'Criterio para calificar unidad 1'},
    {'link': 'https://www.khanacademy.org/math/2', 'criterio': 'Criterio para calificar unidad 2'},
    # Agrega más unidades aquí...
]

# Crea las cartas
for unidad in unidades:
    deck_principal.add_note(genanki.Note(
        model=my_model,
        fields=[unidad['link'], unidad['criterio']]
    ))

# Exporta el mazo a un archivo .apkg
genanki.Package(deck_principal).write_to_file('mazo_matematicas.apkg')

print("Mazo creado con éxito!")
