# 👹 VER VERSION DE JOOMLA QUE USA UN SITIO WEB              P4IVersionJoomla.py

````python
// Some code

```python
#! ver la version de joola que usa un sitio web - P4IVersionJoomla.py - By P4IM0N

#!/usr/bin/env python
#_*_codigng: utf8_*_

#-------------------------------------------------------------
import wget                                                                                         #?wget lo usamos para descargar la la url del joomla
from xml.etree.ElementTree import parse                                                             #?parse de xml lo usamos para parsear el archivo descargdo por wget de joomla.xml
from tabulate import tabulate

#-------------------------------------------------------------
banner = '''

__________  _____ ._______   ____                  .__                    ____.                     .__          
\______   \/  |  ||   \   \ /   /___________  _____|__| ____   ____      |    | ____   ____   _____ |  | _____   
 |     ___/   |  ||   |\   Y   // __ \_  __ \/  ___/  |/  _ \ /    \     |    |/  _ \ /  _ \ /     \|  | \__  \  
 |    |  /    ^   /   | \     /\  ___/|  | \/\___ \|  (  <_> )   |  \/\__|    (  <_> |  <_> )  Y Y  \  |__/ __ \_
 |____|  \____   ||___|  \___/  \___  >__|  /____  >__|\____/|___|  /\________|\____/ \____/|__|_|  /____(____  /
              |__|                  \/           \/               \/                              \/          \/ 
By P4IM0N'''
print(banner)

#-------------------------------------------------------------
def main():
    web_objetivo = input('Ingresa manito la url objetivo para saber su version de Joomla: ')      #?obtenemos la url objetivo del usuario
    web_objetivo = wget.download(url=web_objetivo+'administrator/manifests/files/joomla.xml')     #?con wget y su metodo download le damos la url objetivo mas la ruta donde se suele encontrar el joomla.xml y con esto lo descargara en el directorio donde estamos
    archivo_joomla = parse("joomla.xml")                                                          #? con parse y de parametro le pasamos el archivo que se descargo lalmado joomla.xml para que lo parsee para luego poder buscar en el a traves de metodos por sus etiquetas
    version_joomla_obtenida = []                                                                  #? lista vacia para la informacion de las versiones obtenidas
    encabezado_tabla = ['VERSION DE JOOMLA UTILIZADO']                                            #?encabezado de tabala
    for version in archivo_joomla.findall('version'):                                             #?iteramos con for a traves de la variable temporal version que busque o ietere dentro de el archivo xml descargado y ya parseado, y con el metodo .findall solo itere en la informacion encontrada solo dentro de las etiquetas 'version'
        version_joomla = version.text                                                             #? dentro de la variable guardamos cada version en texto plano con el metodo .text
        version_joomla_obtenida.append([version_joomla])                                          #?guardo con .append dentrod e la lista version_joomla_obtenida en forma de lista cada version_joomla apra lñuego se r usada en la tabla informativa
    #print('\n'+'La version de Joomla que uiliza es: '+version_joomla)
    tabla_de_version_joomla = tabulate(version_joomla_obtenida, encabezado_tabla, tablefmt='grid')#?creamos la tabla informativa con sus parametros, informacion (version_joomla_obtenida) + encabezado + tipo de tabla
    print(tabla_de_version_joomla)    
        
    
#-------------------------------------------------------------
if __name__== '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('se cierra el programa manito')
        exit()    
        




```
````
