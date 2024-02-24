# 👹 BUSCA ADMINISTRADORES DE SITIOS CON WORDPRESS  P4IUsuserWpress.py

````python
// Some code

```python
#! nos da los usuarios que administran una sitio web con wordpress - P4IUsuserWpress.py - By P4IM0N

#!/usr/bin/env python 
#_*_coding: utf8_*_

#------------------------------------------------------------------
import json
import urllib.request
from tabulate import tabulate

#------------------------------------------------------------------
banner = '''

__________  _____ .___ ____ ___                                 __      __                                     
\______   \/  |  ||   |    |   \________ __  ______ ___________/  \    /  \_____________   ____   ______ ______
 |     ___/   |  ||   |    |   /  ___/  |  \/  ___// __ \_  __ \   \/\/   /\____ \_  __ \_/ __ \ /  ___//  ___/
 |    |  /    ^   /   |    |  /\___ \|  |  /\___ \  ___/|  | \/\        / |  |_> >  | \/\  ___/ \___ \ \___ \ 
 |____|  \____   ||___|______//____  >____//____  >\___  >__|    \__/\  /  |   __/|__|    \___  >____  >____  >
              |__|                 \/           \/     \/             \/   |__|               \/     \/     \/ 
By P4IM0N'''

print(banner)

#------------------------------------------------------------------
def main():
    url_objetivo = input('Manito ingresa la pagina WP donde queres que encuentre los usuarios que administran: ')   #?solicitamos al usuario la url objetivo de la que quiere sabe r los usuarios que la administran
    url_objetivo = urllib.request.urlopen(url_objetivo)                                                             #?con urllib.request abrimos la url objetivo tomando una informacion en json
    url_objetivo = url_objetivo.read().decode()                                                                     #? luego leemos conn .read()
    lista_de_usuarios = json.loads(url_objetivo)                                                                    #?con .json.load cargamos solo la informacion json que se encuentra en la url objetivo, para lugo iterar en ella entre los usuarios dentrpo de lm a etiqueta 'slug'
    usuarios = []                                                                                                   #?creo la lsuta de lista de usuarioos para la tabala informativa
    encabezado = ['USUARIOS ADMINISTRADORES']                                                                       #?encabezado de tabla
    for usuario in lista_de_usuarios:                                                                               #?iteramois en cada usuario de la lista de usuarios en formato json carda anteriorment con load() 
        usuarios.append([usuario["slug"]])                                                                          #?con append agregamos cada elelmenteo como una lista dentro de lal lista para poder ser mostrada en la tabla, y cada uno de ellos es un usuario iterado en la lista de usuarios buscando solo los quie contienen la etiqueta ['slug']
    tabla_informativa_de_usuarios = tabulate(usuarios,encabezado,tablefmt='grid')                                   #?creamos la tabla con su respectivos parametros de informacion
    print(tabla_informativa_de_usuarios)    
        
#------------------------------------------------------------------    
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Se cerro el programa manito ')
        exit()
        
            





```
````
