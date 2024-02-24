# 👹 BUSCA TEMAS UTILIZADO POR SITIO WEB WORDPRESS         P4ItemasWordpress.py

````python
// Some code

```python
#! consiguiendo los temas que utilza un sitio web con wordpress - P4ItemasWordpress.py - By P4IM0N

#!/usr/bin/env python
#_*_coding: utf8_*_


#--------------------------------------------------------------------
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

#--------------------------------------------------------------------
banner='''
__________  _____ .___  __                                 __      __   .___                                   
\______   \/  |  ||   |/  |_  ____   _____ _____    ______/  \    /  \__| _/____________   ____   ______ ______
 |     ___/   |  ||   \   __\/ __ \ /     \\__  \  /  ___/\   \/\/   / __ |\____ \_  __ \_/ __ \ /  ___//  ___/
 |    |  /    ^   /   ||  | \  ___/|  Y Y  \/ __ \_\___ \  \        / /_/ ||  |_> >  | \/\  ___/ \___ \ \___ \ 
 |____|  \____   ||___||__|  \___  >__|_|  (____  /____  >  \__/\  /\____ ||   __/|__|    \___  >____  >____  >
              |__|               \/      \/     \/     \/        \/      \/|__|               \/     \/     \/ 

'''
print(banner)

#--------------------------------------------------------------------
def main():
    url_para_analizar = input('ingresa la pagiona manito para que sepas los temas que usa: ')   #? ingreso de la pagina a analizar
    cabecera = {'User-Agent':'Firefox'}                                                         #? definimos el uso del navegador que utilizamos con el encabezado  
    url_para_analizar_lista = requests.get(url=url_para_analizar,headers=cabecera)              #? hacemos un llamado de tipo get usando request para obtener la respuesta de el html del la pagina aportada en su parametro
    #print(url_para_analizar_lista.text)                                                        #? comprobamos que se recibio bien la llamada tipo post obteniendo el html perfectamente
    html_de_url_con_soup = BeautifulSoup(url_para_analizar_lista.text,'html5lib')               #? parseamos con Beautifusoup el html optenido por request.get y le damos un formato html5lib, para luego usar metodos sobre el en esta variable
    
    lista_de_temas_encontrados = []                                                             #?creo una lista vacia donde guardare la informacion de los temas encontrados para se r mostrados luego en la tabla
    cabecera_de_lista = ['TEMAS DE WORDPRESS ENCONTRADOS ' ]                                    #?creao la cabecera de la tabla
    for enlace in html_de_url_con_soup.find_all('link'):                                        #?iteramos sobre cada enlace encontrado dentro de la variable parseada con bs4 con su metodo find_al y el parametro de busqueda que encunetre solo las etiquetas 'link'
        if '/wp-content/themes/' in enlace.get('href'):                                         #?condicionamos que si se encuentra el string /wp-content/themes/ in cada enlace con 'link' encontrado y que en su 'href' contenga el string que le dimos de condicional, siga con el siguienrte paso en el caso de que sea True
            tema = enlace.get('href')                                                           #?guardamos el 'href' de cada una de estos enlaces
            tema = tema.split('/')                                                              #? a este 'href' link obtenido tras todo el filtro de condiciones, le aplicamos el metodo .split para que nos separe en una lista los elementos que esten separados con / que le definimos nosotros, para luego poder usar sus posiciones
            if 'themes' in tema:                                                                #?si se encuentra 'themes' en la lista de eleemntos guardados en tema
                posicion = tema.index('themes')                                                 #?creamos una posicion usando el metodo .index() sobre la lista que creamos con .split anteriormente, y le decimos que con index en donde encuentre el parametro o elemento que le dimos, que seria 'themes' nos de su posicion numerica en la lista
                temas_encontrados = tema[posicion+1]                                            #?aca jugamos con la posicion obtenida y le sumamos 1 por que el nombre del tema , se encuentra en la posicion que le sigue a 'theme'
                lista_de_temas_encontrados.append([temas_encontrados])                          #?acc con append voy guardando en la lista vacia, en cada iteracion cada tema encontrado cada uno como una lista o elemento separado y luego mostrarlos en la tabla
                #print(temas_encontrados)
    tabla_de_informacion = tabulate(lista_de_temas_encontrados,cabecera_de_lista, tablefmt='grid') #?creamos la tabla, con tabulate, le damos la informacion que contendra, la cabecera creada y el formato de la tabla
    print(tabla_de_informacion)            
            
        
#--------------------------------------------------------------------
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('el programa se esta cerrando manito')
        exit()
        
             

```
````
