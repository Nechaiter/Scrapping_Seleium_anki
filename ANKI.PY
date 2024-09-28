import genanki
import os
import json


def export_deck(deck,nombre_archivo,export_path='C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Mazos/'):
    export_path = export_path+nombre_archivo+'.apkg'
    genanki.Package(deck).write_to_file(export_path)


#Matematicas::Aritmetica::Unit 1
#deckes=[]

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

# Ruta del directorio que deseas crear
ruta_directorio = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Mazos/Mathematics'

def parsear_signos(nombre):
    return nombre.replace(':', '').replace('/', '').replace('\\', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '').replace('𝘶', 'u').replace('®︎','')

def CrearCarpeta(nombre_carpeta, ruta_directorio=ruta_directorio):
    try:
        ruta_creacion=ruta_directorio+'/'+nombre_carpeta
        os.makedirs(ruta_creacion, exist_ok=True)
        print(f"Directorio '{nombre_carpeta}' creada con éxito!")
    except OSError as error:
        print(f"Error al crear la carpeta '{nombre_carpeta}': {error}")



Criterio='''<div><div style="text-align: center;"><span style="color: rgb(0, 0, 0);"><b>again: (Fail once) I forgot, wrong answer (memory interference), lucky guess, or partial recall (I consider not enough to be a pass)</b></span></div><div style="text-align: center;"><span style="color: rgb(0, 0, 0);"><b>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; hard: successful but effortful recall</b></span></div><div style="text-align: center;"><span style="color: rgb(0, 0, 0);"><b>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; good: default pass grade</b></span></div><div style="text-align: center; "><span style="color: rgb(0, 0, 0);"><b>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; easy: quick and easy, feeling that the review was not needed, even a waste of time</b></span></div></div>'''

location = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping/Datos Unificados'
file_name = 'datos.json'
file_path= os.path.join(location, file_name)
with open(file_path, 'r',encoding='utf-8') as file:
    data = json.load(file)

id=21313123

for curso in data['Cursos']:
    CrearCarpeta(parsear_signos(curso['nombre']))
    for unidad in curso['Unidades']:
        id=id+1
        deck_unidad=genanki.Deck(id, 'Matemáticas::'+curso['nombre']+'::'+unidad['nombre'])
        try:
            Cartas_Unidad=[]
            for leccion in unidad['Lecciones']:
                Carta={'Nombre_Leccion':f'<div style="text-align: center;"><h1><a href="{leccion['link']}">{leccion['nombre']}</a></h1></div>','criterio': Criterio}
                Cartas_Unidad.append(Carta)
            for carta in Cartas_Unidad:
                deck_unidad.add_note(genanki.Note(
                    model=my_model,
                    fields=[carta['Nombre_Leccion'], carta['criterio']]
                ))
            export_deck(deck_unidad,parsear_signos(unidad['nombre']),ruta_directorio+'/'+parsear_signos(curso['nombre'])+'/')
        except Exception as e:
            print(f"Error al exportar la unidad {unidad['nombre']}: {e}")
            continue

print("Mazos creado con éxito!")
