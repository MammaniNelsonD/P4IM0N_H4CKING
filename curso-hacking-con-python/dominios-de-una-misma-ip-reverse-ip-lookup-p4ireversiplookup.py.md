# 👹 DOMINIOS DE UNA MISMA IP - REVERSE IP LOOKUP P4IReversIPlookup.py

````python
// Some code

```python
#! programa que nos obtien todos los dominios que usan una mism a IP que estan dentro del mismo servidor - P4IReversIPlookup.py  -  By P4IM0N

#!/usr/bin/env python
#_*_coding: utf8_*_

#---------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

#---------------------------------------------------------------------------------------
banner = '''

__________  _____ ._____________                                ._____________.__                 __                 
\______   \/  |  ||   \______   \ _______  __ ___________  _____|   \______   \  |   ____   ____ |  | ____ ________  
 |     ___/   |  ||   ||       _// __ \  \/ // __ \_  __ \/  ___/   ||     ___/  |  /  _ \ /  _ \|  |/ /  |  \____ \ 
 |    |  /    ^   /   ||    |   \  ___/\   /\  ___/|  | \/\___ \|   ||    |   |  |_(  <_> |  <_> )    <|  |  /  |_> >
 |____|  \____   ||___||____|_  /\___  >\_/  \___  >__|  /____  >___||____|   |____/\____/ \____/|__|_ \____/|   __/ 
              |__|            \/     \/          \/           \/                                      \/     |__|    
By P4IM0N'''
print(banner)

#---------------------------------------------------------------------------------------
def main():
    ip_objetivo = input('Manito dame la IP o DOMINIO a la que quieres hacer un reverce IP lookup: ')                         #?ingreso de la IP o ODMINIO objetivo del usuario
    encabezado_web = {'User-Agent':'Firefox'}                                                                                #?creamos la cabecera para interactuar luego con requests   
    conexion_consulta_web = requests.get(f'https://viewdns.info/reverseip/?host={ip_objetivo}&t=1', headers=encabezado_web)  #?realizamos la coneccion con requests y sus metodo get, dandole como parametro la url de la pagina que analiza, y formateandoi con 'f' el string de la url, interactuamos dentro de ella ingresando la ip o dominio objetivo del usuario dentro de ella, para tener la informacion. luego le damos el encabezado
    conexion_consulta_web_SOUP = BeautifulSoup(conexion_consulta_web.text,'html5lib')                                        #?usamos Beatifulsoup con el parametro de la coneccion con la pagina donde tenemos la informacuon, y la parseamos o damos formato en 'html5lib' para luego buscar con find etiquetas dentro de ella
    informacion_reverce_ip = conexion_consulta_web_SOUP.find('font', face='Courier')                                         #?buscamos dentro de SOUP con el metodo find etiquetas 'font' con la descripcion face='coourier' y guardamos en variable.
    informacion_reverce_ip = informacion_reverce_ip.find(border="1")                                                         #?buscamos dentro de informacion_reverce_ip con el metodo find etiquetas border="1" y guardamos en variable.
    
    lista_informacion_reverce_ip = []                                                                                        #?creamos una lista vacia
    for informacion in informacion_reverce_ip.find_all('tr'):                                                                #?con for iteramos por cada informacion in informacion_reverce_ip solo las que tien n etiqueta 'tr' con find_all
        if informacion_reverce_ip.find_all('td'):                                                                            #?damos de condicional que cada elemento informacion dentro del informacion_reverce_ip con find_aall etiqueta 'td' pasen el condicional    
            informacion = informacion.td.string                                                                              #?dentro de la variable informacion guardamos esta informacion filtrada por etiquetas, y le decimos que nos de solo lo que contiene las etiquetas .td y de ellas solo su string contenido, con .string   
            lista_informacion_reverce_ip.append([informacion])                                                               #?guardamos con .append denro de la lista cada eleemnto como una lista apaarte, haciendo una lista de lista para usar con tabulate   
    tabla_informativa = tabulate(lista_informacion_reverce_ip,['RESULTADO REVERCE IP LOOKUP'],tablefmt='grid')               #?creamos la tabal con tabulate y sus parametros ya fuera del loop, dando primero la lista de lista con la inforrmacion optenida, mas el encabezado de tabla dentro de un alista, y el estilo de tabla 
    print(tabla_informativa)    
        
         
#---------------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()    
```
````
