# 👹 INFORMACION DE TIPOS DE CONSULTAS DNS              P4InfoTipoConsDNS.py

````python
// Some code

```python
#!info de tipos de consyultas DNS - P4InfoTipoConsDNS.py - By P4IM0N

#!/usr/bin/env python
#_*_coding: utf8_*_

#------------------------------------------------
import dns.resolver
from tabulate import tabulate

#------------------------------------------------
banner = '''

__________  _____ .___        _____    ___________.__              _________                      ________    _______    _________
\______   \/  |  ||   | _____/ ____\___\__    ___/|__|_____   ____ \_   ___ \  ____   ____   _____\______ \   \      \  /   _____/
 |     ___/   |  ||   |/    \   __\/  _ \|    |   |  \____ \ /  _ \/    \  \/ /  _ \ /    \ /  ___/|    |  \  /   |   \ \_____  \ 
 |    |  /    ^   /   |   |  \  | (  <_> )    |   |  |  |_> >  <_> )     \___(  <_> )   |  \___ \ | !___!   \/    |    \/        }
 |____|  \____   ||___|___|  /__|  \____/|____|   |__|   __/ \____/ \______  /\____/|___|  /____  >_______  /\____|__  /_______  /
              |__|         \/                        |__|                  \/            \/     \/        \/         \/        \/ 
'''
print(banner)

#------------------------------------------------
def main():
    try:
        opciones = '''
        1 - nombre a dirección IP (A)
        2 - servidores de nombres autoritativos (NS)
        3 - Localiza servidores de correo (MX)
        4 - Almacena datos en registros DNS (TXT)
        5 - btiene dirección IPv6 (AAAA)
        6 - Detalles de servidor de autoridad (SOA)
        7 - Traduce dirección IP a nombre (PTR)
        8 - Identifica servicios en dominios (SRV)
        9 - Versión avanzada de consulta 1 (A6)
        10 - obterner todas las consultas (ANY)'''
        
        url_objetivo = input('Manito dame la URL de la que quieres obtener info del DNS: ')                        #?ingreso de la url obbjetivo
        informacion_DNS = []                                                                                       #?lista de informacion para la tabla informativa 
        continuar = True                                                                                           #?variable para controlar el loop while
        while continuar:                                                                                           #?como continuar es true se ejecuta el loop
            print(opciones)                                                                                        #?mostramos las opciones     
            opcion_elgida = int(input('Elige una opcion indicando el numero manito: '))                            #?forzamos la entrada del usuario para qeu sea un entero con int         
            
            if opcion_elgida == 1:                                                                                 #?condicional como los que continuan por cada opcion, si la opcion elegida por el usuario es igual a 1, pasara 
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo,'A')                               #?con la libreria dns de python , usando dns.resolver con su metodo .resolve (query esta obsoleto) de esta forma nos permite darle dos parametros , el primero la url_objetivo y segundo el tipo de consulta aportando el codigo de consulta DNS que eligio el usuario en el menu de opciones.
                for info in url_objetivo_para_tipos_DNS:                                                           #?iteramos por cada elemento que nos dio resolve con la consulta
                    informacion_DNS.append([info])                                                                 #?a cada elemento que tuvimos de la consulta lo guardamos con append, como una lista de lista dentro de informacion DNS la cual la mostraremos en la tabla 
                tabla_informativa = tabulate(informacion_DNS,['nombre a dirección IP'],tablefmt='grid')            #?creamos la tabla con sus patrametros
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')                       #?consulatamos al manito si continua para ver si paramos el loop while cambiando a False si elige n
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []                                                                           #?limpiamos la informacion de la tabla 
                else:
                    continuar = False                                                                              #?se cierra el loop while por que pasa a ser False la variable continuar
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')     
            
            elif opcion_elgida == 2:
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo,'NS')
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['servidores de nombres autoritativos'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')
            
            elif opcion_elgida == 3:
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo,'MX')
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['Localiza servidores de correo'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')
            
            elif opcion_elgida == 4:
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo,'TXT')
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['Almacena datos en registros DNS'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')
            
            elif opcion_elgida == 5:
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo,'AAAA')
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['dirección IPv6'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')
            
            elif opcion_elgida == 6:
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo,'SOA')
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['Detalles de servidor de autoridad'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')
            
            elif opcion_elgida == 7:
                ip_pagina_objetivo = input('Dame la IP de la pagina que quieres saber su nombre de dominio DNS manito: ')
                ip_pagina_objetivo = ip_pagina_objetivo+'.in-addr.arpa'
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(ip_pagina_objetivo,'PTR')
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['dirección IP a nombre'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')
            
            elif opcion_elgida == 8:
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo,'SRV')
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['servicios en dominios'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')
            
            elif opcion_elgida == 9:
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo, 38)
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['nombre a dirección IP AVANZADO'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')
            
            elif opcion_elgida == 10:
                url_objetivo_para_tipos_DNS = dns.resolver.resolve(url_objetivo, 255)
                for info in url_objetivo_para_tipos_DNS:
                    informacion_DNS.append([info])
                tabla_informativa = tabulate(informacion_DNS,['TODAS LA CONSULTAS DNS'],tablefmt='grid')
                print(tabla_informativa)
                decision = input('Manito queres continuar con las opciones de nuevo? (y/n)')
                if decision == 'y':
                    continuar = True
                    informacion_DNS = []
                else:
                    continuar = False
                    print('Gracias por usar mi sistema manito, saludos de P4IM0N')                        
                
        
           
    except:
        print('algo salio mal manito :(')    

#------------------------------------------------
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('El programa se esta cerranddo manito ')
        exit() 
           
```
````
