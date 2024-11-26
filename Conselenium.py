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
    time.sleep(0.1)


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
CantidadCursos=0
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._yi0e9gr")))

CursosWeb=driver.find_elements(By.CSS_SELECTOR,"._yi0e9gr")
for curso in CursosWeb:
    texto=curso.find_element(By.TAG_NAME, value='h3').text
    link=curso.find_element(By.TAG_NAME, value='a').get_attribute('href')
    cursos.append(Curso(texto,link,[]).to_dict())
print('Cursos agregados')
for curso in cursos:
    url=curso['link']
    driver.get(url)
    EsperarCargadado(3)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._c53vsu1")))
    UnidadesWeb=driver.find_elements(By.CSS_SELECTOR,"[data-testid='unit-header']")
    Unidades=[]
    print('Progreso: '+str(CantidadCursos)+'/'+str(len(cursos)))
    CantidadCursos+=1
    print('Curso: '+curso['nombre'])
    for Uni in UnidadesWeb:
        texto=Uni.find_element(By.TAG_NAME, value='h2').text
        link=Uni.get_attribute('href')
        Unidades.append(Unidad(texto,link,[]).to_dict())
    for unidad in Unidades:
        url=unidad['link']
        driver.get(url)
        EsperarCargadado(3)
        try:
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='mastery-practice-content-item']")))
                LeccionesWeb = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-testid='mastery-practice-content-item']")))
                print('Lecciones tipo MASTERY')
            except:
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._168icmv")))
                    LeccionesWeb = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._168icmv")))
                    print('Lecciones tipo LAPIZ')
                except:
                    raise
            #LeccionesWeb=driver.find_elements(By.CSS_SELECTOR,"[data-testid='mastery-practice-content-item']")
            Lecciones=[]
            for Lecc in LeccionesWeb:
                WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "._pc9bder")))
                #texto=Lecc.find_element(By.CSS_SELECTOR,'._pc9bder').text
                texto = WebDriverWait(Lecc, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '._pc9bder'))).text
                link=Lecc.find_element(By.CSS_SELECTOR,'._dwmetq').get_attribute('href')  #_dwmetq
                Lecciones.append(Leccion(texto,link).to_dict())
        except:
            print("Error al encontrar lecciones")
            Lecciones='No hay lecciones'
        unidad['Lecciones']=Lecciones
    curso['Unidades']=Unidades
datos = {'cursos': cursos}
print('Datos obtenidos')

Iteraciones=1

directorio = os.getcwd()
nombre_archivo = 'datos '+str(Iteraciones)+'.json'
ruta_archivo = os.path.join(directorio, nombre_archivo)
with open(ruta_archivo, 'w', encoding='utf-8') as file:
    json.dump(datos, file, ensure_ascii=False, indent=4)







# Obtener el HTML completo de la página después de la ejecución de JavaScript
#page_source = driver.page_source


# Cerrar el navegador
#driver.quit()
