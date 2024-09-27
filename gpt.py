import genanki
import os
import json


def export_deck(deck, nombre_archivo, file):
    export_path = os.path.join('C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Mazos', file.replace(':', ''), nombre_archivo.replace(':', '') + '.apkg')
    genanki.Package(deck).write_to_file(export_path)


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

Criterio = '''again: (Fail once) I forgot, wrong answer (memory interference), lucky guess, or partial recall (I consider not enough to be a pass)
            hard: successful but effortful recall
            good: default pass grade
            easy: quick and easy, feeling that the review was not needed, even a waste of time'''

location = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Datos Unificados'
file_name = 'datos.json'
file_path = os.path.join(location, file_name)
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

id = 1123123  # ID del mazo principal
deck_principal = genanki.Deck(
    id,  # Un ID único para tu mazo
    'Matemáticas'
)

for curso in data['Cursos']:
    id += 1
    deck_curso = genanki.Deck(id, 'Matemáticas::' + curso['nombre'])

    for unidad in curso['Unidades']:
        id += 1
        deck_unidad = genanki.Deck(id, 'Matemáticas::' + curso['nombre'] + '::' + unidad['nombre'])

        try:
            Cartas_Unidad = []
            for leccion in unidad['Lecciones']:
                Carta = {
                    'Nombre_Leccion': f'<a href="{leccion["link"]}">{leccion["nombre"]}</a>',
                    'criterio': Criterio
                }
                Cartas_Unidad.append(Carta)

            for carta in Cartas_Unidad:
                deck_unidad.add_note(genanki.Note(
                    model=my_model,
                    fields=[carta['Nombre_Leccion'], carta['criterio']]
                ))

            # Exporta el mazo de la unidad solo después de agregar todas las notas
            export_deck(deck_unidad, unidad['nombre'], 'Principal/Cursos/Unidades')

        except Exception as e:
            print(f"Error al exportar la unidad {unidad['nombre']}: {e}")
            continue

    # Exporta el mazo del curso después de procesar todas las unidades
    export_deck(deck_curso, curso['nombre'], 'Principal/Cursos')

# Exporta el mazo principal al final
export_deck(deck_principal, 'MazoPrincipal', 'Principal')

print("Mazos creados con éxito!")