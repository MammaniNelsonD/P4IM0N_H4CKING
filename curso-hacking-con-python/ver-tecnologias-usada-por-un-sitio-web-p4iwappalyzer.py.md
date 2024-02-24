# 👹 VER TECNOLOGIAS USADA POR UN SITIO WEB                          P4IWappalyzer.py

````python
// Some code

```python
#!usr/bin/env python
#_*_coding: utf8_*_

#! practica de uso de wappalyzer - P4IWappalyzer - By P4IM0N

#IMPORTACION DE MODULOS
#--------------------------------------------------------------------------------------------
from Wappalyzer import WebPage, Wappalyzer   #?Importar la clase WebPage del módulo Wappalyzer (representa una página web para análisis), Importar la clase Wappalyzer del módulo Wappalyzer (permite realizar análisis de tecnologías)
from tabulate import tabulate                #? sirve para crear la tabla 

#BANNER
#--------------------------------------------------------------------------------------------
banner = '''
__________  _____ .___ __      __                            .__                              
\______   \/  |  ||   /  \    /  \_____  ______ ___________  |  | ___.__.________ ___________ 
 |     ___/   |  ||   \   \/\/   /\__  \ \____ \____ \__  \ |  |<   |  |\___   // __ \_  __ 
 |    |  /    ^   /   |\        /  / __ \|  |_> >  |_> > __ \|  |_\___  | /    /\  ___/|  | \/
 |____|  \____   ||___| \__/\  /  (____  /   __/|   __(____  /____/ ____|/_____ \___  >__|   
              |__|           \/        \/|__|   |__|       \/     \/           \/    \/       


'''
print(banner)

#FUNCION PRINCIPAL
#--------------------------------------------------------------------------------------------
def main():
    wappa = Wappalyzer.latest()               #? creamos un objeto de wappalyzer para luego usar metoso en el 
    try:
        pagina = input('ingresa la pagina  web a la que quiere analizar manito: ')   #? soliciatamo al usuario la pagina a analizar 
        urlweb = WebPage.new_from_url(pagina)                                        #?usamos el modulo Webpage con su metodo .new_from_url donde le daremos la pagina elegida por el usuario para darle un formato para luego ser analizada
        tecnologia =  wappa.analyze(urlweb)                                          #? al objeto creado en wappa le usamos el metodo de wappalyzer .analizer el cual nos dara la tecnologia que utiliza la pagina que le dimos de parametrto (urlweb = a la que eligio el usario)
        
        lista_de_tecnologias = []                                                    #?creo lista vacia para luego usarla para crear la tabla
        for tec in tecnologia:                                                       #?iteramos dentro de la lista de tecnologia para imprimir cada uno de los elementos
            lista_de_tecnologias.append([tec])                                       #?sobre la lista agregamos con el metodo .append cara elemento encontrado en tecnologia y los guarde en eta lista 
           
        encabezado_tabla = ['TECNOLOGIAS ENCONTRADAS MANITO']                        #?creamos el encabezado d la tabla
        tabla_informativa = tabulate(lista_de_tecnologias,  encabezado_tabla, tablefmt='grid')   #?con el modulo tabulate le definimos sus parametros: la lista obtenida de tecnologias, el encabezado de cada columna, mas el formato de la tabla
        print(tabla_informativa)    
    except:
        print('algo salio mal mano')

#EJECUCION DE FUNCION PRINCIPAL
#--------------------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('el programa se cerromanito')
        exit()
        
            
```
````
