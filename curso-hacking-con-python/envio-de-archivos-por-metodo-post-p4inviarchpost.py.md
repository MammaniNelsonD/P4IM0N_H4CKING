# 👹 ENVIO DE ARCHIVOS POR METODO POST                        P4InviarchPOST.py

````python
// Some code

```python
#!envio de archivos por POST - By P4IM0N

#!/usr/bin/env pyhton
#_*_ coding: utf8 _*_

import requests
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--archivo', help='dame un archivo para subir')
parser.add_argument('-k', '--captcha', help='dame el captcha hermano')
parser = parser.parse_args()

banner= '''

__________  _____ .___   _________   ____.___   _____ ___________________   ___ _____________________    ____________________
\______   \/  |  ||   | /     \   \ /   /|   | /  _  \\______   \_   ___ \ /   |   \______   \_____  \  /   _____/\__    ___/
 |     ___/   |  ||   |/  \ /  \   Y   / |   |/  /_\  \|       _/    \  \//    ~    \     ___//   |   \ \_____  \   |    |   
 |    |  /    ^   /   /    Y    \     /  |   /    |    \    |   \     \___\    Y    /    |   /    |    \/        \  |    |   
 |____|  \____   ||___\____|__  /\___/   |___\____|__  /____|_  /\______  /\___|_  /|____|   \_______  /_______  /  |____|   
              |__|            \/                     \/       \/        \/       \/                  \/        \/            

'''
print(banner)


def main():
    if parser.archivo:                                 #?comprobamops si el usuario nos indico el archivo
        
        if path.exists(parser.archivo):                #? comprobamos si realmente elk archivo indoicado existe
            print('perfecto tengo el archivo hermano')
            archivo = open(parser.archivo, 'rb')       #?abrimos el archivo seleccionado con -f
            headers = {'User_Agente':'Fierfox'}
            kaptcha = {'captcha': parser.captcha}      #?tomamos en una variable el captcha inreassado por el usuario
            comunicacion = requests.post(url='http://127.0.0.1:5000/upload',files={'archivossubidos[]':archivo}, headers=headers, data=kaptcha)
            if comunicacion.status_code == 200:        #?vemos el codigo de estado de la comunicacion POST
                print(comunicacion.text)
                print('el archivo se subio con exito hermanito')
            else:
                print('mal ingresado el captcha')
                print('elarchivo no se subio hermano')    
    else:
        print('dame el nombre del archivo hermano')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('El programa se cerro correctamente')    
```
````
