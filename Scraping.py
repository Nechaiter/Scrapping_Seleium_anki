import requests
from bs4 import BeautifulSoup
import time
import json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

import json
import os

class Curso:
    def __init__(self, nombre, link,Unidades):
        self.nombre = nombre
        self.link = link
        self.Unidades = Unidades
    
    def to_dict(self):
        return {'nombre': self.nombre, 'link': self.link, 'Unidades': self.Unidades}
    
class Unidad:
    def __init__(self, nombre, link, Lecciones):
        self.nombre = nombre
        self.link = link
        self.Lecciones = Lecciones
    
    def to_dict(self):
        return {'nombre': self.nombre, 'link': self.link, 'Lecciones': self.Lecciones}

class Leccion:
    def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link
    
    def to_dict(self):
        return {'nombre': self.nombre, 'link': self.link}




datos = {}

directorio = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping'
nombre_archivo = 'datos.json'
ruta_archivo = os.path.join(directorio, nombre_archivo)





# URL de la página que quieres analizar

Unidades = []
Lecciones = []
cursos = []


while True:
    time.sleep(2)
    url = 'https://www.khanacademy.org/profile/me/courses'
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        print('Acceso exitoso')
        soup = BeautifulSoup(response.text, 'html.parser')
        for cursos in soup.find_all('div', class_='_yi0e9gr'):    
            nombre_curso=cursos.find('h3', class_='_jwc8z53').text
            link=cursos.find('a', class_='_1666bk1u')['href']
            cursos.append([nombre_curso,link])
        print(cursos)
        break
    else:
        print(f'Error al acceder a la página: {response.status_code}')
        break

