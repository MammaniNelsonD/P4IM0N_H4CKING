# 👹 VER VERSION DE WORDPRESS DE UNA WEB                           P4IV3rsionWordpres.py

````python
// Some code

```python
#! Detectado la version de wordpress de un sitio web - P4IV3rsionWordpres.py - By P4IM0N 

#!/usr/bin/env python
#·_*_coding: utf8_*_


#--------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


#--------------------------------------------------------------------------------------------------------------
banner = '''
__________  _____ ._______   ____________              .__              __      __   .___                            
\______   \/  |  ||   \   \ /   /\_____  \______  _____|__| ____   ____/  \    /  \__| _/____________   ____   ______
 |     ___/   |  ||   |\   Y   /   _(__  <_  __ \/  ___/  |/  _ \ /    \   \/\/   / __ |\____ \_  __ \_/ __ \ /  ___/
 |    |  /    ^   /   | \     /   /       \  | \/\___ \|  (  <_> )   |  \        / /_/ ||  |_> >  | \/\  ___/ \___ \ 
 |____|  \____   ||___|  \___/   /______  /__|  /____  >__|\____/|___|  /\__/\  /\____ ||   __/|__|    \___  >____  >
              |__|                      \/           \/               \/      \/      \/|__|               \/     \/ 

'''
print(banner)

#--------------------------------------------------------------------------------------------------------------
def main():
    url = input('Ingresa mano la pagina para ver la version de wordpress: ')      #?pedimos la pagina a abalizar
    cabecera = {'User-Agent':'Firefox'}                          #?creamos la cabecera de la pagina
    pedido = requests.get(url=url,headers=cabecera)              #?mandamos una solicitud de tipo get con la cabecera y la url que se usara para recibir el html de respuesta 
    paginasoup = BeautifulSoup(pedido.text,'html5lib')           #?tratamos y damos formato al html del pedido usando beautifousoup y un formato de html5lib para luego usar los metodos de esta libreria y buscar etiquetas que nos sirvan para saber la version de wordpress
    
    version_wordpress = None                                     #?creao una variable None para luego usarla en un condicional si no se encontro version 
    for version in paginasoup.find_all('meta'):                  #?iteramos con for y el metodo de bs4 .find_all dentor de todas las etiquertas 'meta'
        if version.get('name')=='generator':                     #?un condicional que la llamar con get y dentro de cada etiqueta 'meta' que se encontro si esta contiene el valor generator pase el condicional
            version_wordpress = version.get('content')           #?como aca ya obtuvimos las etiquetas meta, con valor generator que son las que contienen la version e wordpress, sabemos que estamos ante esa informacion, por ende le pediomos que lea el valr quye contiene 'content' cpor que dentro de el esta la respectiva version de wordpress
            
    
    headers = [' VERSION DE WORDPRESS ']                         #?creo el encabezado de la tabla
    if version_wordpress:
        version_wordpress_tabla = [[version_wordpress]]          #?guardo la informacion de version en formato de lista para ser mostrada en la tabla 
        tabla_de_version_wordpress = tabulate(version_wordpress_tabla, headers, tablefmt="grid")   #?usamos tabulate con el parametro de primero la informacion version_wordpress_tabla, luego el headers y el tipo de tabla que usaremos 
        print(tabla_de_version_wordpress)
    else:
        print('aparentemente no usa wordpress manito')           
            
#--------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('saliendo del programa manito')
        exit()    

```
````
