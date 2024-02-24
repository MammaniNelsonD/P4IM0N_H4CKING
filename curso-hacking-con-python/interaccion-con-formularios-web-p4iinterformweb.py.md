# 👹 INTERACCION CON FORMULARIOS WEB     P4IInterFormWeb.py

````python
// Some code

```python
#!practica interactuando con formiularios web - P4IInterFormWeb.py - By P4IM0N

#!/usr/bin/env python
#_*_coding: utf8_*_


import mechanize
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-b','--buscar',help='opcion que vamos que vamos a buscar mano')
parser = parser.parse_args()

banner = '''__________  _____ .___.___        __              ___________                  __      __      ___.    
\______   \/  |  ||   |   | _____/  |_  __________\_   _____/__________  _____/  \    /  \ ____\_ |__  
 |     ___/   |  ||   |   |/    \   __\/ __ \_  __ \    __)/  _ \_  __ \/     \   \/\/   // __ \| __ \ 
 |    |  /    ^   /   |   |   |  \  | \  ___/|  | \/     \(  <_> )  | \/  Y Y  \        /\  ___/| \_\ 
 |____|  \____   ||___|___|___|  /__|  \___  >__|  \___  / \____/|__|  |__|_|  /\__/\  /  \___  >___  /
              |__|             \/          \/          \/                    \/      \/       \/    \/ 
                                                                                     by P4IM0n     

'''


print(banner)


def main():
    if parser.buscar:
        bus = mechanize.Browser()           #?creamos un objeto del navegador para poder trabajar sobre el luego
        bus.set_handle_robots(False)        #?definimos configuraciones del misoen False (definimos en false para que no hagaa seguimiento de de estos) aca ignoramos las reglas que establesen los mismos, pero se puede estar incumpliendo normas legales que klimitan los mismos, a los que se estan puenteando definiendolo en False
        bus.set_handle_equiv(False)         #?definimos configuraciones del misoen False (definimos en false para que no hagaa seguimiento de de estos) aca ignoramos las reglas que establesen los mismos, pero se puede estar incumpliendo normas legales que klimitan los mismos, a los que se estan puenteando definiendolo en False
        #bus.add_header = [('User-Agent','Firefox')]
        bus.addheaders = [('User-Agent','Firefox')]   #?definimos la cabecera del navegador
        bus.open('https://google.com')                #?le definimos la url con las que trabajeromos con su envio de formulario
        #for n in bus.forms():                        #?con el metodo .form trabajamos denro de la url google solo buscando cada formulario dentroi de ella por que estamo iterando en la busqueda de cad una (luego de encontrada la variable q dentro de Textcontrol donde se guarda la busqueda, la comente paran no usarla)
            #print(n)
        bus.select_form(nr=0)                         #?seleccionamos el formulario donde trabajaremos enviando nuestra busqueda
        bus['q'] = parser.buscar                      #? y definimos que dentro de la variable ['q'] le mandamos la busqueda que seleccciono el usuario con -b 
        bus.submit()                                  #? con submit enviamos la busqueda ingresada por el usuario con -b
        #print(bus.response().read())
        p = BeautifulSoup(bus.response().read(),'html5lib')    #?parseamos el html obtenido para poder obtener mas en limpio la informacion despues
        for link in p.find_all('a'):                           #? iteramos  dentro del html optenido buscando dentro de cada etiqueta a cada link 
            u = link.get('href')                               #? luego dentro de cada linkbuscamos ua subetiqueta href lo que contiene dentro de ella
            u = u.replace('/url?q=', '')
            print(u)                                           #? y mostramos el resultado :D
        
    else:
        print('no se pudo realizart la busqueda mano')
       
    
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Se detuvo el programa manito')
        exit()    
        
```
````
