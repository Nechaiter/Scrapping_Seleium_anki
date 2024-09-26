import json
import os

class Curso:
    def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link

    def to_dict(self):
        return {'nombre': self.nombre, 'link': self.link}
class Unidad:
    def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link
    def to_dict(self):
        return {'nombre': self.nombre, 'link': self.link}

class Leccion:
    def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link
    def to_dict(self):
        return {'nombre': self.nombre, 'link': self.link}
class Dato:
    def __init__(self, curso, unidad, leccion):
        self.curso = curso
        self.unidad = unidad
        self.leccion = leccion

    def to_dict(self):
        return {
            'curso': self.curso.to_dict(),
            'unidad': self.unidad.to_dict(),
            'leccion': self.leccion.to_dict()
        }


def menu():
    print("Seleccione una opción:")
    print("1. Añadir Curso")
    print("2. Añadir Unidad")
    print("3. Añadir Lección")
    print("4. Guardar datos")
    print("5. Exportar datos")
    return input("Opción: ")

def obtener_datos_clase(clase):
    nombre = input(f"Introduce el nombre del {clase}: ")
    link = input(f"Introduce el link del {clase}: ")
    return nombre, link

datos = {}

directorio = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping'
nombre_archivo = 'datos.json'
ruta_archivo = os.path.join(directorio, nombre_archivo)


while True:
    opcion = menu()
    if opcion == '1':
        nombre, link = obtener_datos_clase("Curso")
        curso = Curso(nombre, link)
    elif opcion == '2':
        nombre, link = obtener_datos_clase("Unidad")
        unidad = Unidad(nombre, link)
    elif opcion == '3':
        nombre, link = obtener_datos_clase("Lección")
        leccion = Leccion(nombre, link)
    elif opcion == '4':
        datos.append(Dato(curso, unidad, leccion).to_dict())
    elif opcion == '5':
        with open('datos.json', 'w', encoding='utf-8') as file:
            json.dump(datos, file, ensure_ascii=False, indent=4)
    elif opcion == '6':
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
