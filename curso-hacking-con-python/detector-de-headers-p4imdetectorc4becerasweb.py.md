# 👹 DETECTOR DE HEADERS   P4IMdetectorC4becerasWEB.py

````python
// Some code

```python
#!/usr/bin/env python
#_*_ coding: utf8 _*_
#! INTERACCION WEB DETECTANDO SUS HEADERS - By P4IM0N



import requests
import argparse
from tabulate import tabulate
import socket
from bs4 import BeautifulSoup, Comment

parser = argparse.ArgumentParser(description='P4IM_DET3C4BECERASWEB: ')
parser.add_argument('-t', '--target', help='Antes del objetivo debes poner el parametro "-t"')
parser.add_argument('-u', '--usuario', help='tu usuario')
parser.add_argument('-o', '--output', help='Nombre del archivo para guardar los resultados')
parser = parser.parse_args()


#Banner
banner = ('''
      
  _____  _  _ _____ __  __   _____  ______ _______ ____   _____ _  _   ____  ______ _____ ______ _____             _______          ________ ____  
 |  __ \| || |_   _|  \/  | |  __ \|  ____|__   __|___ \ / ____| || | |  _ \|  ____/ ____|  ____|  __ \     /\    / ____\ \        / /  ____|  _ \ 
 | |__) | || |_| | | \  / | | |  | | |__     | |    __) | |    | || |_| |_) | |__ | |    | |__  | |__) |   /  \  | (___  \ \  /\  / /| |__  | |_) |
 |  ___/|__   _| | | |\/| | | |  | |  __|    | |   |__ <| |    |__   _|  _ <|  __|| |    |  __| |  _  /   / /\ \  \___ \  \ \/  \/ / |  __| |  _ < 
 | |       | |_| |_| |  | | | |__| | |____   | |   ___) | |____   | | | |_) | |___| |____| |____| | \ \  / ____ \ ____) |  \  /\  /  | |____| |_) |
 |_|       |_|_____|_|  |_| |_____/|______|  |_|  |____/ \_____|  |_| |____/|______\_____|______|_|  \_\/_/    \_\_____/    \/  \/   |______|____/ 
                        ______                                                                                                                     
                       |______|                                                                                           by P4IM0N                         

      ''')

print(banner)


#funcion para obtener los comentarios del HTML
def get_comments_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            comments = soup.find_all(string=lambda text: isinstance(text, Comment))
            return comments
        else:
            print(f"Error en la solicitud. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
    except Exception as ex:
        print(f"Error inesperado: {ex}")

    return None

def main():
    if parser.target:
        try:
            url = parser.target
            cabeceras = dict(requests.get(url).headers)
            
            #obtenemos los comentarios de la pagina web HTML
            comentarios = get_comments_from_url(url)                #?ejecutamos la fiuncion que nos devuelve los comentarios encontrados en el html de la pagina objetivo usando BeautifulSoup
            print('<----------------------->  INFORME DEL SITIO WEB OBJETIVO  <----------------------->\n')
            if comentarios:
                print("Comentarios encontrados:")
                tabla_comentarios = [] 
                for comentario in comentarios:
                    tabla_comentarios.append([comentario])  # Aquí añadimos el comentario en una lista dentro de otra lista
                print(tabulate(tabla_comentarios, headers=['COMENTARIOS EN EL HTML'], tablefmt='grid'))
            else:
                print("No se encontraron comentarios.")
                
            #vemos si ingreso el nombre de usuario
            if parser.usuario:    
                print(f'Mira {parser.usuario}, esta es la cabecera de la pagina OBJETIVO:')
            else:
                print('Debe ingresar su usuario luego del parametro "-u"')

            # Agregar información adicional
            print(f'Código de estado de la respuesta: {requests.get(url).status_code}')
            print(f'Longitud del contenido: {len(requests.get(url).content)} bytes')
            print(f'Información de dominio: {url}')
            print('El sitio utiliza HTTPS.\n' if url.startswith('https') else 'El sitio no utiliza HTTPS.\n')
        
            #creo la tabla e iteramos ingresando los datos obtenidos para mostrar en la consola 
            table = []                               
            for c in cabeceras:
                table.append([c, cabeceras[c]])
            print(tabulate(table, headers=['CABECERAS', 'INFORMACION'], tablefmt='grid'))

            # Guardar resultados en un archivo
            if parser.output:
                with open(parser.output, 'w') as file:
                    file.write(banner)
                    file.write('<----------------------->  INFORME DEL SITIO WEB OBJETIVO  <----------------------->\n')
                    file.write(f'Mira {parser.usuario}, esta es la cabecera de la pagina OBJETIVO:\n' if parser.usuario else 'Debe ingresar su usuario luego del parametro "-u"\n')
                    file.write(f'Código de estado de la respuesta: {requests.get(url).status_code}\n')
                    file.write(f'Longitud del contenido: {len(requests.get(url).content)} bytes\n')
                    file.write(f'Información de dominio: {url}\n')
                    file.write('El sitio utiliza HTTPS.\n' if url.startswith('https') else 'El sitio no utiliza HTTPS.\n')
                    file.write(tabulate(table, headers=['CABECERAS', 'INFORMACION'], tablefmt='grid'))
                    file.write('\n')
                    file.write('/'*150)
                    file.write(tabulate(tabla_comentarios, headers=['COMENTARIOS EN EL HTML'], tablefmt='grid'))

        except requests.exceptions.RequestException as e:
            print(f'Error en la solicitud: {e}')
        except socket.gaierror:
            print(f"No se pudo resolver el dominio '{parser.target}' para obtener la dirección IP.")
        except Exception as ex:
            print(f'Error inesperado: {ex}')
    else:
        print('No se dio un objetivo')

if __name__ == '__main__':
    main()


```

````
