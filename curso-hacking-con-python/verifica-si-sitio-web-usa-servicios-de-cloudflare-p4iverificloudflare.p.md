# 👹 VERIFICA SI SITIO WEB USA SERVICIOS DE CLOUDFLARE                            P4IVerifiCloudflare.p

````python
// Some code

```python
#!programa que va a verificar si un dominio o sitio web que esta en un servidor, esta utilizando servicios de seguridad de CLOUDFLARE - P4IVerifiCloudflare.py - By P4IM0N

#!/usr/bin/env pyhton
#_*_coding: utf8_*_

import requests
from tabulate import tabulate

#--------------------------------------------------------------------------------------
banner = '''

__________  _____ ._______   ____           .__  _____.___________ .__                   .___ _____.__                        
\______   \/  |  ||   \   \ /   /___________|__|/ ____\__\_   ___ \|  |   ____  __ __  __| _// ____\  | _____ _______   ____  
 |     ___/   |  ||   |\   Y   // __ \_  __ \  \   __\|  /    \  \/|  |  /  _ \|  |  \/ __ |\   __\|  | \__  \_  __ \_/ __ \ 
 |    |  /    ^   /   | \     /\  ___/|  | \/  ||  |  |  \     \___|  |_(  <_> )  |  / /_/ | |  |  |  |__/ __ \|  | \/\  ___/ 
 |____|  \____   ||___|  \___/  \___  >__|  |__||__|  |__|\______  /____/\____/|____/\____ | |__|  |____(____  /__|    \___  >
              |__|                  \/                           \/                       \/                 \/            \/ 
By P4IM0N'''
print(banner)
#--------------------------------------------------------------------------------------
def main():
    CLOUDFLARE = 'cloudflare'                                                                                       #?variable con string de cloudfalre para usarla de busqueda luego dentro de la cabecera
    url_objetivo = input('Manito dame la pagina de la quieres saber si esta usando el servicio de CLOUDFLARE: ')    #?ingreso del usuario del  sitio objetivo
    cabecera_a_comprobar = requests.get('https://'+url_objetivo)                                                    #?variable que contiene , la respuesta tras la comunicacion HTTPS con reques y su metodo de tipo get, dandole como parametro, el string de http:// y la variable del objetivo que eligio el usuario
    cabecera_a_comprobar = dict(cabecera_a_comprobar.headers)                                                       #?luego la misma variable la actualizamos y guardamos dentro de un diccionario lo que es la respuesta get que recibimos anteriormente y con .headers optenemos solo el encabezado para analizarlo a posterior si contiene cloudflare
    
    stop = False                                                                                                    #?stop esta en False para luego con ella verificar si se encontro cloudflare y pase a valer True
    lista_informacio_cloudflare = []                                                                                #?lista vacia para la informacion
    for clave, valor in cabecera_a_comprobar.items():                                                               #?iteramos con FOR por cada clave y valor del diccionario cabecera cabecera_a_comprobar y muestre sus items que nos devuelve una tupla con las claves y valores tambien para poder ser iteradas
        if CLOUDFLARE in valor.lower():                                                                             #?como condicional si CLOUDFLARE esta in cada valor iterado(ponindolo en minusculo con .lower) y si esto es verdadero pasara el condicional
            stop = True                                                                                             #?como paso el condicional hacemos que la variable stop pase a vale True para usarla luego y confirmar que esi usa cloudflare                                                                            
            lista_informacio_cloudflare.append([clave,' ::::: '+valor] )                                            #?luego guardamos dentro de la lista vacia , la informacion que encontro con cloudflare, y guarde en ella una lista de lista con su llave y valor para usarla en la tabla luego    
          
    if stop == True:                                                                                                #?ya fuera del loop for le decimos que si stop ahora si encontro cloudflare vale True pase la condicion y nos imprima la tabla, y un aviso
        tabla_informativa = tabulate(lista_informacio_cloudflare, ['INFORMACION CLOUDFLARE OBTENIDA EN LA CABECERA'], tablefmt='grid') #?tabla con tabulate y suis parametros de lista de informacio, mas la cabecera y el tipo de tabla que esta en grid
        print('!!!!!!!!!!!!!!!!!!!!!!!!!MANITO SI ESTA USANDO SERVICIOS DE CLOUDFLARE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')                #?aviso de que usa cloudflñare 
        print(tabla_informativa)              
    else:
        print('MANITO NO ESTA USANDO SERVICIOS DE CLOUDFLARE 8D ')


#--------------------------------------------------------------------------------------        
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('se esta cerrando el programa manito')
        exit()   
    
```
````
