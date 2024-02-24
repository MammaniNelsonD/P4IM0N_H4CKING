# 👹 INFORMACION WEB CON  WHOIS              P4InfoWebWhois.py

````python
// Some code

```python
#!programa para conseguir informacion de  un dominio usando el servicio de who.is - P4InfoWebWhois.py - By P4IM0N

#!/usr/bin/env python
#_*_coding: utf8_*_


#-----------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from tqdm import tqdm

#-----------------------------------------------------------------------------------------
banner = '''

__________  _____ .___        _____      __      __      ___.   __      __.__           .__         
\______   \/  |  ||   | _____/ ____\____/  \    /  \ ____\_ |__/  \    /  \  |__   ____ |__| ______ 
 |     ___/   |  ||   |/    \   __\/  _ \   \/\/   // __ \| __ \   \/\/   /  |  \ /  _ \|  |/  ___/ 
 |    |  /    ^   /   |   |  \  | (  <_> )        /\  ___/| \_\ \        /|   Y  (  <_> )  |\___ \  
 |____|  \____   ||___|___|  /__|  \____/ \__/\  /  \___  >___  /\__/\  / |___|  /\____/|__/____  > 
              |__|         \/                  \/       \/    \/      \/       \/               \/  
By P4IM0N'''
print(banner)

#-----------------------------------------------------------------------------------------
def main():
    dominio_objetivo = input('Manito porfavor dame el Dominio del que quieres que te de informacion con WHOIS: ')    #?obtenemos el dominio objetivo del susuario
    dominio_objetivo = requests.get(f'https://who.is/whois/{dominio_objetivo}')                                      #?al dominiioo lo agregamos al final de la url de la paginawho.is que es donde se realizara la busqueda de info, con request y su metodo get.   
    dominio_objetivo_parseado = BeautifulSoup(dominio_objetivo.text, 'html5lib')                                     #?parseamos el html donde esta la info suministrada por who.is, usando beatifulsoup y le damos formato html5lib
   
    lista_info_WHOIS = []                                                                                            #?creamos una lista donde se guardara cada info en forma de lista en lista, para mostrarla en un atabla luego   
    barra_de_progreso = tqdm(total=len(dominio_objetivo_parseado.find_all("div", class_="queryResponseBodyRow")))    #?creamos un objeto de barra de progreso, con el rango deacuerdo a la cantidad de etiquetas div con class "queryResponseBodyRow" encontradas con .find_all
    for info in dominio_objetivo_parseado.find_all("div", class_="queryResponseBodyRow"):                            #?iteramos por cada una de las class "queryResponseBodyRow"
        for llave in info.find_all("div", class_="queryResponseBodyKey"):                                            #?y dentro de ellaas iteramos con find_all por cada  "div", class_="queryResponseBodyKey" encontrada 
            llave = llave.text                                                                                       #?y la guarmos las llaves en una variabl con .text   
            
            for infollave in info.find_all("div", class_="queryResponseBodyValue"):                                  #?luego iteramos por todas las  "div", class_="queryResponseBodyValue"  con un loop terciario digamos 
                infollave = infollave.text                                                                           #?y la guarmos las informaciones e las llaves en una variabl con .text   
                
        cada_infor = f'{llave} = {infollave}'                                                                        #?luego de este loop de key guardamos una cadena de string formateadas con el estilo en que mostraremos nuestra informacion   
        lista_info_WHOIS.append([cada_infor])                                                                        #?y esta variable la guardamos en forma de lista dentro de nuestra lista_info:_whois con .append
        
        for resto_titulos in dominio_objetivo_parseado.find_all("span", class_="lead", text="Registrar Data"):       #?luego buscamos el resto de informacion que se dejo de encontrar dado que ya no existian classes "queryResponseBodyKey", por lo que vuelvo a iterar sobre el dominio principal ya parseado en busqueda nuevamente con find_all del contenido de etiquetas "span", class_="lead", text="Registrar Data" 
            titulo_resto_info = resto_titulos.text                                                                   #?las cuales al obtenerlas las guardo en variablñe por cada iteracion con el metodo.text   
            
            for resto_info in info.find_all("div", class_="queryResponseBodyValue"):                                 #?luego segida de esa informacion busco la informacion de estas span, las cuales se guardan, buscando con find_all en etiquetas "div", class_="queryResponseBodyValue" con un loop terciario digamos
                resto_info = resto_info.text                                                                         #?igual que anteriormemnte las guardo en variable con .text
                
        cada_resto_info = f'{titulo_resto_info} = {resto_info}'                                                      #?y nuevamente al final de este segundo loop secundario guardo con el formato y estilo que quiero la informacion
        lista_info_WHOIS.append([cada_resto_info])                                                                   #?al igual que anteriormente la guardamos toda con .append
        barra_de_progreso.update(1)                                                                                  #?actualizamos la barra de progreso en uno con cada iteracion
    barra_de_progreso.close()                                                                                        #?cerramos la barra de progreso
        
       
    tabla_info_whois = tabulate(lista_info_WHOIS,['INFORMACION WHOIS'], tablefmt='grid')                             #?terminando al final del loop principal creamos la tabla con sus parametros, de informacion con la lista info WHOIS, el encabezado y formato de tabla grid
    print(tabla_info_whois)    

#-----------------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Manito se esta cerrando el programita')
        exit()

#-----------------------------------------------------------------------------------------

```
````
