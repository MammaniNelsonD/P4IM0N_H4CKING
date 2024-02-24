# 👹 FUERZA BRUTA A SUBDOMINIOS O DIRECTORIOS                          P4IForceBruteSubdom.py

````python
// Some code

```python
#!programa para hacer fuerza bruta sobre subdominios de un sitio web - P4IForceBruteSubdom.py - By P4IM0N

#!/usr/bin/env python
#_*_coding: utf8_*_

#-------------------------------------------------------------------------------
import dns.resolver
from os import path
from tqdm import tqdm
from tabulate import tabulate

#-------------------------------------------------------------------------------
banner = '''

__________  _____ .______________                       __________                __           _________    ___.        .___              
\______   \/  |  ||   \_   _____/__________   ____  ____\______   \_______ __ ___/  |_  ____  /   _____/__ _\_ |__    __| _/____   _____  
 |     ___/   |  ||   ||    __)/  _ \_  __ \_/ ___\/ __ \|    |  _/\_  __ \  |  \   __\/ __ \ \_____  \|  |  \ __ \  / __ |/  _ \ /     \ 
 |    |  /    ^   /   ||     \(  <_> )  | \/\  \__\  ___/|    |   \ |  | \/  |  /|  | \  ___/ /        \  |  / \_\ \/ /_/ (  <_> )  Y Y  !
 |____|  \____   ||___|\___  / \____/|__|    \___  >___  >______  / |__|  |____/ |__|  \___  >_______  /____/|___  /\____ |\____/|__|_|  /
              |__|         \/                    \/    \/       \/                         \/        \/          \/      \/            \/ 
'''
print(banner)

#-------------------------------------------------------------------------------
def main():
    if path.exists('subdominios.txt'):                                                                         #?verificamos con path que el archivo de subdominiios.txt este en el directorio donde ejecutamos
        diccionario_subdominios = open('subdominios.txt','r')                                                  #?con open abrimos el archivo de sudominios.txt en el metodo listo para leer 'r' 
        diccionario_subdominios = diccionario_subdominios.read().split('\n')                                   #?preparamos con el metodo read y sacando los saltos de linea de la lista de subdominiois para iterar sin problema en el luego...
        lista_subdom_encontrados = []                                                                          #?creamos una lista vacia donde estaran los subdominiis encontrados 
        url_dominio_objetivo = input('manito dame el dominio objetivo asi encuentro sus subdomios: ')          #?infgreso del dominiioo objetivo por el usuario 
        
        barra_de_progreso = tqdm(range(len(diccionario_subdominios)))                                          #?creamos el objeto de la barra de progreso usando tqdm, el cual debe recibir un rango , range de parametro ej:1,2,,3,4,5,6,7,8...y el numero de rango que lñe pasamos lo definimos con len y que cuente el numero d elementos dentro de nuestra lista de subdominiois             
        for subd in diccionario_subdominios:                                                                   #?iteramos dentro de cadad subdominio en txt, para que en el bloque try: al usar el tipo de consulta dns.resolver del tipo 'A' si este da Ok 200 el mismo no devuelva una exepcion y si es asi guarde esta url con subdominio encontrada dedntro de la lista   
            try:
                url_objetivo_probandoSB = dns.resolver.resolve(f'{subd}.{url_dominio_objetivo}','A')
                lista_subdom_encontrados.append([f'{subd}.{url_dominio_objetivo}'])
            except:                                                                                            #?si en la consulta 'A' se devolvio un exept el bloque try no se ejecutara por ende tampoco se guardara ese subdominio en la lista, y al tener pass en este exept se continuara con el bucle for para comprobar el siguiente subdominioio
                pass
            barra_de_progreso.update(1)                                                                        #?al objeto bara de progreso le aplicamos su metodo update con el parmetro en 1 para que actualice en cada bucle en mas uno el tamaño de la barra 
        barra_de_progreso.close()                                                                              #?con .close cerramos ya fuera del loop terminado la barra de progreso, para luego mpasar a mostrar el resultado 
            
        if len(lista_subdom_encontrados) > 0:                                                                  #?comprobamos con if y vemos si la cantidad de elementos devueltods por len encotrados en la lista, es superior a 0, nos pasara el condicional y mostrara los datos encontrados  
            print('Se encontraron subdominios para el dominio que me dis manito: ')
            print(f'Manito se encontraron: {len(lista_subdom_encontrados)} subdominios')
            tabla_de_subdominios_encontrados = tabulate(lista_subdom_encontrados,['SUBDOMINIOS ENCONTRADOS'], tablefmt='grid') #?creamos la tabla con sus parametros, informacion, cabecera y tipo de tabla
            print(tabla_de_subdominios_encontrados)     
        else:
            print('No se encontraron subdominiois manito')    

#-------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:print('manito se esta cerando el programa')
    exit()    
        

#-------------------------------------------------------------------------------

```
````
