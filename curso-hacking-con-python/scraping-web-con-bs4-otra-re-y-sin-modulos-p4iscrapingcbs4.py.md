# 👹 SCRAPING WEB CON "BS4", otra"RE" Y SIN MODULOS                    P4IscrapingCbs4.py

CON BS4:

````python
// Some code

```python
#?MI PROGRAMA PRINCIPAL PARA BUSCAR; 
#!programa de raspado web o scrapinmg usando Beutifulsoup para tal fin - P4IscrapingCbs4.py - By P4IM0N

#----------------------------------------------------------------------------------------------
from tabulate import tabulate
import requests
from bs4 import BeautifulSoup

#----------------------------------------------------------------------------------------------
COLOR_ROJO = "\033[91m"
COLOR_AZUL = '\033[94m'
COLOR_RESET = "\033[0m"

#----------------------------------------------------------------------------------------------
banner = f'''

__________  _____ .___                                  .__               ____________.             _____  
\______   \/  |  ||   | ______ ________________  ______ |__| ____    ____ \_   ___ \_ |__   ______ /  |  | 
 |     ___/   |  ||   |/  ___// ___\_  __ \__  \ \____ \|  |/    \  / ___\/    \  \/| __ \ /  ___//   |  |_
 |    |  /    ^   /   |\___ |\  \___|  | \// __ \|  |_> >  |   |  \/ /_/  >     \___| \_\ |\___ \/    ^   /
 |____|  \____   ||___/____  >\___  >__|  (____  /   __/|__|___|  /\___  / \______  /___  /____  >____   | 
              |__|         \/     \/           \/|__|           \//_____/         \/    \/     \/     |__| 
{COLOR_ROJO}By P4IM0N{COLOR_RESET}'''
print(banner)

#----------------------------------------------------------------------------------------------
def consultas():
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    paginaWEB_para_scraping = input('Manito dame el sitio web para realizar el scraping: ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    primera_etiqueta_inicio = input('Manito ahora dime la etiqueta principal de inicio que quieres buscar solo el nombre si (<,>): ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    argumento = input('Manito ahora dame el argumento de la etiqueta principal que me diste antes: ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    return paginaWEB_para_scraping, primera_etiqueta_inicio, argumento
#----------------------------------------------------------------------------------------------
lista_informacion = []
lista_links = []

def main(paginaWEB_para_scraping, primera_etiqueta_inicio, argumento ):
    try:
        if paginaWEB_para_scraping:
            user_agent_navegador = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}
            objetivo = requests.get(url=paginaWEB_para_scraping, headers=user_agent_navegador)
            
            if objetivo.status_code == 200:
                informacion_html = BeautifulSoup(objetivo.text, 'html.parser')
                solicitud = informacion_html.find_all(primera_etiqueta_inicio, class_=argumento)
                
                for objetivos in solicitud:
                    lista_informacion.append([objetivos.text])
                    segunda_etiqueta= objetivos.find('a')
                    lista_links.append([segunda_etiqueta.get('href')])
                    tabla_info = tabulate(lista_informacion, ['TEXTO ENCONTRADO'], tablefmt='grid')
                    tabla_link = tabulate(lista_links, ['LINKS ENCONTRADOS'], tablefmt='grid')
                print(COLOR_AZUL+tabla_info+COLOR_RESET)
                print(COLOR_ROJO+tabla_link+COLOR_RESET)
                    
            
    except NameError as error:
        print(f'Manito ocurrio el siguiente erro: {error}')    
        

#----------------------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        respuestas = consultas()
        main(*respuestas)
    except KeyboardInterrupt:
        print('Manito se cerro bien el programa :D')
        exit()    

#----------------------------------------------------------------------------------------------


```
````

CON MODULO RE:

````python
// Some code

```python
#!programa de raspado web o scrapinmg web usando RE para tal fin - P4IscrapingCre.py - By P4IM0N

#----------------------------------------------------------------------------------------------
from tabulate import tabulate
import urllib.request
import re

#----------------------------------------------------------------------------------------------
COLOR_ROJO = "\033[91m"
COLOR_AZUL = '\033[94m'
COLOR_RESET = "\033[0m"

#----------------------------------------------------------------------------------------------
banner = f'''

__________  _____ .___                                  .__               _________                 
\______   \/  |  ||   | ______ ________________  ______ |__| ____    ____ \_   ___ \_______   ____  
 |     ___/   |  ||   |/  ___// ___\_  __ \__  \ \____ \|  |/    \  / ___\/    \  \/\_  __ \_/ __ \ 
 |    |  /    ^   /   |\___ |\  \___|  | \// __ \|  |_> >  |   |  \/ /_/  >     \____|  | \/\  ___/ 
 |____|  \____   ||___/____  >\___  >__|  (____  /   __/|__|___|  /\___  / \______  /|__|    \___  >
              |__|         \/     \/           \/|__|           \//_____/         \/             \/ 
{COLOR_ROJO}By P4IM0N{COLOR_RESET}'''
print(banner)

#----------------------------------------------------------------------------------------------
def consultas():
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    paginaWEB_para_scraping = input('Manito dame el sitio web para realizar el scraping: ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    primera_etiqueta_inicio = input('Manito ahora dime la etiqueta principal de inicio que quieres buscar: ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    primera_etiqueta_final = input('Manito ahora dame la etiqueta de cierre de la etiquet principal que me diste antes: ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    return paginaWEB_para_scraping, primera_etiqueta_inicio, primera_etiqueta_final
#----------------------------------------------------------------------------------------------
lista_informacion = []

def main(paginaWEB_para_scraping, primera_etiqueta_inicio, primera_etiqueta_final ):
    try:
        if paginaWEB_para_scraping:
            pagina = open('paginarraspada.html', 'w+')
            codigoHTML = urllib.request.urlopen(paginaWEB_para_scraping)
            codigoHTML = codigoHTML.read().decode('utf-8')
            pagina.write(codigoHTML)
            pagina.close()
            
            paginaHTML = open('paginarraspada.html', 'r')
            
            tabla = None
            for linea in paginaHTML.readlines():
                if primera_etiqueta_inicio and primera_etiqueta_final:
                    
                    linea_limpia = re.findall(f'^{primera_etiqueta_inicio}', linea)
                    if linea_limpia:
                        print(f'{COLOR_ROJO}********************************************************************************{COLOR_RESET}')
                        print(linea_limpia)
                    
                    linea_limpia = re.findall(f'{primera_etiqueta_final}$', linea)
                    if linea_limpia:
                        print(f'{COLOR_AZUL}···············································································{COLOR_RESET}')
                        print(linea_limpia)
                    
                    linea_limpia =  re.findall(f'{primera_etiqueta_inicio}(.+?){primera_etiqueta_final}', linea)
                    for linea_re in linea_limpia:
                        print(f'{COLOR_ROJO}////////////////////////////////////////////////////////////////////////////////{COLOR_RESET}')
                        print(linea_re)
                        
                    linea_limpia1 = re.findall(f'{primera_etiqueta_inicio}.*{primera_etiqueta_final}', linea)          
                    if linea_limpia1:
                        linea_limpia = linea.replace(primera_etiqueta_inicio, '')
                        linea_limpia = linea_limpia.replace(primera_etiqueta_final, '')
                        lista_informacion.append([linea_limpia])
                        tabla = tabulate(lista_informacion, ['TEXTO ENCONTRADO'], tablefmt='grid')
                
                else:
                    print('-----------------------------------------------------------------------------------')
                    print('Manito debes darme si o si las etiquetas de inicio y de final para porder trabajar ')
                    respuestas = consultas()
                    main(*respuestas)
            
            print(COLOR_AZUL+tabla+COLOR_RESET)                
    except NameError as error:
        print(f'Manito ocurrio el siguiente erro: {error}')    
        

#----------------------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        respuestas = consultas()
        main(*respuestas)
    except KeyboardInterrupt:
        print('Manito se cerro bien el programa :D')
        exit()    

#----------------------------------------------------------------------------------------------

```
````

SIN USO DE MODULOS:

````python
// Some code

```python
#!programa de raspado web o scrapinmg web sin uso de librerias par tal fin - P4IscrapingSmod.py - By P4IM0N

#----------------------------------------------------------------------------------------------
from tabulate import tabulate
import urllib.request

#----------------------------------------------------------------------------------------------
COLOR_ROJO = "\033[91m"
COLOR_AZUL = '\033[94m'
COLOR_RESET = "\033[0m"

#----------------------------------------------------------------------------------------------
banner = f'''

__________  _____ .___                                  .__                _________                  .___
\______   \/  |  ||   | ______ ________________  ______ |__| ____    ____ /   _____/ _____   ____   __| _/
 |     ___/   |  ||   |/  ___// ___\_  __ \__  \ \____ \|  |/    \  / ___|\_____  \ /     \ /  _ \ / __ | 
 |    |  /    ^   /   |\___ |\  \___|  | \// __ \|  |_> >  |   |  \/ /_/  >        \  Y Y  (  <_> ) /_/ | 
 |____|  \____   ||___/____  >\___  >__|  (____  /   __/|__|___|  /\___  /_______  /__|_|  /\____/\____ | 
              |__|         \/     \/           \/|__|           \//_____/        \/      \/            \/ 
{COLOR_ROJO}By P4IM0N{COLOR_RESET}'''
print(banner)

#----------------------------------------------------------------------------------------------
def consultas():
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    paginaWEB_para_scraping = input('Manito dame el sitio web para realizar el scraping: ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    primera_etiqueta_inicio = input('Manito ahora dime la etiqueta principal de inicio que quieres buscar: ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    primera_etiqueta_final = input('Manito ahora dame la etiqueta de cierre de la etiquet principal que me diste antes: ')
    print(f'{COLOR_ROJO}-----------------------------------------------------------------------------------{COLOR_RESET}')
    return paginaWEB_para_scraping, primera_etiqueta_inicio, primera_etiqueta_final
#----------------------------------------------------------------------------------------------
lista_informacion = []

def main(paginaWEB_para_scraping, primera_etiqueta_inicio, primera_etiqueta_final ):
    try:
        if paginaWEB_para_scraping:
            pagina = open('paginarraspada.html', 'w+')
            codigoHTML = urllib.request.urlopen(paginaWEB_para_scraping)
            codigoHTML = codigoHTML.read().decode('utf-8')
            pagina.write(codigoHTML)
            pagina.close()
            
            paginaHTML = open('paginarraspada.html', 'r')
            
            for linea in paginaHTML.readlines():
                if primera_etiqueta_inicio and primera_etiqueta_final:
                    if primera_etiqueta_inicio in linea:
                        linea_limpia = linea.replace(primera_etiqueta_inicio, '')
                        linea_limpia = linea_limpia.replace(primera_etiqueta_final, '')
                        lista_informacion.append([linea_limpia])
                        tabla = tabulate(lista_informacion, ['TEXTO ENCONTRADO'], tablefmt='grid')
                
                else:
                    print(f'{COLOR_AZUL}-----------------------------------------------------------------------------------{COLOR_RESET}')
                    print('Manito debes darme si o si las etiquetas de inicio y de final para porder trabajar ')
                    respuestas = consultas()
                    main(*respuestas)
            tabla = tabulate(lista_informacion, ['TEXTO ENCONTRADO'], tablefmt='grid')
            print(COLOR_AZUL+tabla+COLOR_RESET)                
    except NameError as error:
        print(f'Manito ocurrio el siguiente erro: {error}')    
        

#----------------------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        respuestas = consultas()
        main(*respuestas)
    except KeyboardInterrupt:
        print('Manito se cerro bien el programa :D')
        exit()    

#----------------------------------------------------------------------------------------------


```
````
