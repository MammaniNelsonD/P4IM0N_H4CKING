# 👹 GEOLOCALIZAR UN SERVIDOR CON SU IP      P4IpGeolocation.py

````python
// Some code

```python
#! programa para geolacalizar un servidor a traves de su IP - P4IpGeolocation.py - By P4IM0N

#!/usr/bin/env python
#_*_coding: utf8_*_


#---------------------------------------------------
import urllib.request
import json
from tabulate import tabulate
from deep_translator import GoogleTranslator

#---------------------------------------------------
banner='''

__________  _____ .___         ________             .__                        __  .__               
\______   \/  |  ||   |_____  /  _____/  ____  ____ |  |   ____   ____ _____ _/  |_|__| ____   ____  
 |     ___/   |  ||   \____ \/   \  ____/ __ \/  _ \|  |  /  _ \_/ ___\{\__  !\   __\  |/  _ \ /    \ 
 |    |  /    ^   /   |  |_> >    \_\  \  ___(  <_> )  |_(  <_> )  \___ / __ \|  | |  (  <_> )   |  !
 |____|  \____   ||___|   __/ \______  /\___  >____/|____/\____/ \___  >____  /__| |__|\____/|___|  /
              |__|    |__|           \/     \/                       \/     \/                    \/ 
by P4IM0N'''
print(banner)

#---------------------------------------------------
def main():
    ip_servirdor_objetivo = input('Manito danos la IP del servidor que quieres GEOLOCALIZAR: ')            #?solicitamois la IP del servidor al usuario para geolocalizarla
    web_ipinfo = f'https://ipinfo.io/{ip_servirdor_objetivo}/json'                                         #?trabajamos subre la url d la pagina ipinfo.com y dentro de la misma url introducimos la busqueda de la IP dada por el usuario, pero la terminamos a la misma con /json para obtenerla en ese formato 
    ip_servirdor_objetivo = urllib.request.urlopen(web_ipinfo)                                             #?en la misma variable objetivo, similar a con get, usamos urllib. con request y su metodo urlopen para abrir la url con la busqueda en formato json, y sacar luego su inform acion     
    info_geolocation_json = json.loads(ip_servirdor_objetivo.read())                                       #?con json y su metodo loads, dandole el resultado de urllib hacos que carge elñ mismo en formato json y lo lea con read()
    
    lista_info_geolocalizacion = []                                                                        #?creamos una lista basia para luego guardar listas de listas dentro de ella para usarse lpara la tabla con tabulate 
    for info in info_geolocation_json:                                                                     #?iteramois con for por cada info dentro de info_geolocatio_json, que en este caso seria como un diccionario, y cada info nos mostrar la llave solamente no su valor 
        #print(info+'='+info_geolocation_json[info])
        info_traducida = GoogleTranslator(source='en',target='es').translate(info)                         #?con cada llave que esta en eingles , vamos a usar la libreria  deep_translator, con googleTranslator y le damos primero de parametro de entrada el idima en el que esta, con source='en' ingles, y salida target='es' español, luego de los pametros le aplicamos el metodo translatey le damos como parametro cada info (llave) iterada para ser traducida a moodo que quede mejor visualmente nomas
        lista_info_geolocalizacion.append([info_traducida+':  '+info_geolocation_json[info]])              #?guardamos en cada iteracion con append dentro de la lista vacia, dandole comoo in formacion, primero la info traducida, (que va a ser la llave que se va a mostrar a l lado de cada informacion), lueego : y luego como es un diccionario y no podemos buscar por iundice su valor que contiene cada llave, tenemos que pasar al diccionario, cada llave en INGLES para que en cad iteracion guarde el valor da cada llave, asi:  info_geolocation_json[info]  == diccionario[llave] y nos dara el valor dentro 
    tabla_geolocalizacion_informativa = tabulate(lista_info_geolocalizacion,['DATOS GEOLOCALIZACION DEL SERVIDOR'],tablefmt='grid') #?creamos la tabla con tabulate y sus parametros, primero la lista de lista de informacion obtenida en toda la iteracion, luego el encabezado tambien dentrto de una lista en string y luego el formato d tabla en este caso grid
    print(tabla_geolocalizacion_informativa)    
    

#---------------------------------------------------
if __name__=='__main__':
    try: 
        main()
    except KeyboardInterrupt:
        print('manito cerraste el programa, gracias')
        exit()
            

```
````
