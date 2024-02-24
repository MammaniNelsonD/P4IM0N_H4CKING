# 👹 BUSCADOR DE PLUGINS DE WORDPRESS                       P4IPluginsWpress.py

````python
// Some code

```python
#! Buscador de plugins wordpress - P4IPluginsWpress.py - By P4IM0N

#-------------------------------------------------------------------------------------
#!/usr/bin/env pyhton
#_*_coding: utf8_*_

#-------------------------------------------------------------------------------------
#instalar libreria progress: pip install progress  


#-------------------------------------------------------------------------------------
import requests
from os import path
from progress.bar import Bar                                                      #?inportamos libbreria para mostras un abarra de progreso 
from tabulate import tabulate


#-------------------------------------------------------------------------------------
banner = '''
__________  _____ ._____________.__               .__                __      __                                     
\______   \/  |  ||   \______   \  |  __ __  ____ |__| ____   ______/  \    /  \_____________   ____   ______ ______
 |     ___/   |  ||   ||     ___/  | |  |  \/ ___\|  |/    \ /  ___/\   \/\/   /\____ \_  __ \_/ __ \ /  ___//  ___/
 |    |  /    ^   /   ||    |   |  |_|  |  / /_/  >  |   |  \\___ \  \        / |  |_> >  | \/\  ___/ \___ \ \___ \ 
 |____|  \____   ||___||____|   |____/____/\___  /|__|___|  /____  >  \__/\  /  |   __/|__|    \___  >____  >____  >
              |__|                        /_____/         \/     \/        \/   |__|               \/     \/     \/ 

By P4IM0N'''
print(banner)


#-------------------------------------------------------------------------------------
def main():
    if path.exists('wp_plugins.txt'):                                                      #?si en la ruta donde estamos .exists existe el archivo wp_plugins.txt pasa el condicional
        print('---SE CARGO EL DICCIONARIO DE PLUGINS DE WORDPRESS---')                     #?indico visualmente que se encontro el diccionario del .txt
        lista_plugins = open('wp_plugins.txt','r')                                         #?con el modulo os usamos el metodo open para abrir el archivo .txt en modo 'r' de read osea lectura
        lista_plugins = lista_plugins.read().split('\n')                                   #?sobre l archivo abierto usamos el metodo read leemos el archivo txt obviando con .split los saltos de linea y guardamos nuestro txt con cada elemento de plugins uno al lado del otro
        lista_plugins_ok = []                                                              #?creo una lista vacia donde se guardaran los plugins ya encontrados como ok con codigo de estado 200
        encabezado = ['PLUGINS DE WORDPRESS ENCONTRADOS EN EL OBJETIVO']                   #?creo el encabezado de la tabla
        url_objetivo = input('Manito porfavor dame la pagina WP para ver sus plugins: ')   #?solicito al usuario qu ingrese la url objetivo
        barra = Bar('Espera manito...', max=len(lista_plugins))                            #?creamos el objeto de la barra con una descripcion primero de  parametro osea un sttring, y le indicamos el la proporcion del largo del progreso va a ser igual  al maximo largo, calculado con len, de la cantidad de elementos que tendra nuestro diccionario .txt 
        
        for plugins in lista_plugins:                                                      #?con for comensamos a iterar por cada plugins encontrado en lista_plugins
            barra.next()                                                                   #?al comienzpo del loop inicio el objeto de la barra con .next()
            try: 
                plugins_a_probar = requests.get(url=url_objetivo+'/'+plugins)              #?nos conectamos con requests con su metodo .get a la url objetivo, sumandole '/' mas cada plugins iterado de la lista _plugins
                if plugins_a_probar.status_code == 200:                                    #?damos como condicional si el plugins probado con .get antenriormente , ahora con el metodo .status_code nos dio ok osea 200 pasara el condicional 
                    plugins_encontrado_ok = url_objetivo+'/'+plugins                       #?guardamos la url_obejtivo mas '/ y mas el plugins encontrado ok'
                    lista_plugins_ok.append([plugins_encontrado_ok.split('/')[-2]])        #? y a la lista creada anteriormente vacia, le guardamos cada elemento como una lista en lista, para ser usadad para la tabla a posterior, y este contendra el plugins_encontrado_ok, sacandole con .split las '/', y solo seleccionando dentro de cada una de las listas el ultimo elelmneto con el indice [-2]
            except:
                pass        
        barra.finish()                                                                               #?fianlizamos el objeto de la barra con .finish()
        tabla_plugins_encontrados = tabulate(lista_plugins_ok, headers=encabezado, tablefmt='grid')  #?creop la tabal y le paso todos los parametros
        print(tabla_plugins_encontrados)           
            
    else:
        print('No esta el diccionario de plugins loquito :( ')


#-------------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Se esta cerrando el programa manito ')
        exit()    


```
````
