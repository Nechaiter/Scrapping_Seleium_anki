from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crear una instancia de Firefox con geckodriver gestionado automáticamente
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

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


Usuario='franciscoesteva2002@gmail.com'
Clave='kzd?Q42U>AGJryb'
def EsperarCargadado(x):
    time.sleep(x)
def EsperarAcciones():
    time.sleep(0.3)


def EncontrarElemento(css_selector,nombre):
    EsperarAcciones()
    Anidado="["+css_selector+"='"+nombre+"']"
    Elemento=driver.find_element(By.CSS_SELECTOR,Anidado)
    return Elemento


#_jwc8z53 cl;ase de los cursos
#

# Ir a la página que deseas analizar
url = 'https://www.khanacademy.org/login'
driver.get(url)

EsperarCargadado(1)
Boton=EncontrarElemento('id','onetrust-accept-btn-handler').click()
User=EncontrarElemento('data-testid','identifier-field').send_keys(Usuario)
Pass=EncontrarElemento('data-testid','password-field').send_keys(Clave)
IniciarSesion=EncontrarElemento('data-testid','log-in-submit-button').click()
EsperarCargadado(3)

cursos = []
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._yi0e9gr")))

CursosWeb=driver.find_elements(By.CSS_SELECTOR,"._yi0e9gr")
for curso in CursosWeb:
    texto=curso.find_element(By.TAG_NAME, value='h3').text
    link=curso.find_element(By.TAG_NAME, value='a').get_attribute('href')
    cursos.append(Curso(texto,link,[]))
for curso in cursos:
    print(curso.nombre + ' ' + curso.link)
'''
datos = {}

directorio = 'C:/Users/Francisco/Desktop/Google drive/Mini Proyecto/Scraping'
nombre_archivo = 'datos.json'
ruta_archivo = os.path.join(directorio, nombre_archivo)

Unidades = []
Lecciones = []
cursos = []
'''







# Obtener el HTML completo de la página después de la ejecución de JavaScript
#page_source = driver.page_source


# Cerrar el navegador
#driver.quit()
