# 😀 WEB SCRAPING

````python
// Some code

```python
#!P4ISCRAPING - buscador de Libros con determinado rating de estrellas, de varias url a la ves. - By P4IM0N
#?Deberian estar las librerias, pero si no estan, instalar con el siguiente comando: pip install requests beautifulsoup4

import requests
import bs4
from tabulate import tabulate


print('''
__________  _____ .___  ____________________________    _____ __________.___ _______    ________ 
\______   \/  |  ||   |/   _____/\_   ___ \______   \  /  _  \\______   \   |\      \  /  _____/ 
 |     ___/   |  ||   |\_____  \ /    \  \/|       _/ /  /_\  \|     ___/   |/   |   \/   \  ___ 
 |    |  /    ^   /   |/        \\     \___|    |   \/    |    \    |   |   /    |    \    \_\  \
 
 |____|  \____   ||___/_______  / \______  /____|_  /\____|__  /____|   |___\____|__  /\______  /
              |__|            \/         \/       \/         \/                     \/        \/ 
------------------------------------------------------------------------------By P4IM0N
                          ░░┌┘     ░░░░░     └┐░░
                           ░│  ||  ▌░░░   ||  │░▐
                           ░│      ░░ ░░      │░
                           ─┘░░░░░░░   ░░░░░░░└─▀
                           ░░░   ▓░░   ░░▓   ░░░
                            ▄─┘   ░░░░░░░   └─▄
                             ░░  ─┬┬┬┬┬┬┬─  ░░
                             ░░░▀┬┼┼┼┼┼┼┼┬▀░░░
                              ░░░└┴┴┴┴┴┴┴┘░░░
                                ░░░░░░░░░░░      
---------------------------------------------------------------------------------
''')


def url_todas():
    todas_las_url = []
    for hojas in range(1, 51):
        pagina_de_libros2 = 'https://books.toscrape.com/catalogue/page-{}.html'
        url_base = pagina_de_libros2.format(hojas)
        todas_las_url.append(url_base)
    return todas_las_url

def mostrar(lista):
    estrellass = int(input('Del 1 al 5, ingrese el numero de estrellas de libros que desea ver: '))
    if estrellass == 1:
        estrellas = 'One'
    elif estrellass == 2:
        estrellas = 'Two'
    elif estrellass == 3:
        estrellas = 'Three'
    elif estrellass == 4:
        estrellas = 'Four'
    elif estrellass == 5:
        estrellas = 'Five'
    else:
        print('ingresa un numero valido')
        return mostrar(lista)
            

    todos_los_libros_seleccionados = []
    
    for url in lista:
        url_pagina = requests.get(url)
        url_pagina_lista = bs4.BeautifulSoup(url_pagina.text, 'lxml')
        libros_seleccionados = url_pagina_lista.select('.product_pod')
        
        for libro in libros_seleccionados:
            if libro.select(f'.star-rating.{estrellas}'):
                titulo = libro.select('h3 a[title]')
                titulo_del_libro = titulo[0]['title']
                todos_los_libros_seleccionados.append(titulo_del_libro)
    
    # Convierto cada título en una lista de un solo elemento titulo
    libros_formateados = [[titulo] for titulo in todos_los_libros_seleccionados]
    
    print(f'---------Los LIBROS con ({estrellass}) ESTRELLAS son un total de ({len(todos_los_libros_seleccionados)}) ------------------')
    print(tabulate(libros_formateados, headers=['TITULOS DE LIBROS SELECCIONADOS'], tablefmt='grid'))             

mostrar(url_todas())


#! By P4IM0N
```
````

CODEO DEL DIA 11:



````python
// Some code

```python
#!WebScraping   -  by P4IM0N
#?instalar con los siguientes comandos: "pip install beautifulsoup4", "pip install lxml", "pip install requests" 


import bs4
import requests
from bs4 import BeautifulSoup, Comment


#?para extraer contenidos de etiquetas

resultado_busqueda_titulo = requests.get("https://escueladirecta-blog.blogspot.com/2022/10/por-que-se-utiliza-python-en-ciencia-de.html")  #?con requests nos capturar todo el codigo de la web que le damos 

print("///////////////////////////////////////////////////////////////////////////////////")
#print(type(resultado_busqueda_titulo))
print(resultado_busqueda_titulo.text)                                                 #?con .text nos mostrara todo el codigo html de la pagina que le ingresamos      

print("///////////////////////////////////////////////////////////////////////////////////")
sopa_de_palabras = bs4.BeautifulSoup(resultado_busqueda_titulo.text, "lxml")          #?con bs4.beautifulsoup poniendo de parametro lo capturado en la primera variable por requests.get de la web, mas le definimos el tipo de motor que vamos a usar para convertir lo extraido de un modo distinto para poder navegar por dentro del codigo para las busquedas. 
print(sopa_de_palabras)


print("///////////////////////////////////////////////////////////////////////////////////")
print(sopa_de_palabras.select("title"))                                               #?con eñ metodo .select y el parametro de la etiqueta que queremos saber su informacion, nos va a devolver su contenido completo con etiqueta y todo


print("///////////////////////////////////////////////////////////////////////////////////")
print(sopa_de_palabras.select("title")[0].getText())                                  #?con el metodo .gettext nos va a devolver solo el contenido que esta dentro de la etiqueta que seleccionamos con .select antes


print("///////////////////////////////////////////////////////////////////////////////////")
parrafo = sopa_de_palabras.select("p")                                                #?seleccionando las etiquetas "p" nos devolvera los parrafos
print(parrafo)


print("///////////////////////////////////////////////////////////////////////////////////")
parrafo = sopa_de_palabras.select('p')[3]                                              #?agregandole el indice [3] en este caso solo nos devolvera solo el parrafo encontrado en el indice tres, osea el tersero    
print(parrafo)


print("///////////////////////////////////////////////////////////////////////////////////")
parrafo = sopa_de_palabras.select('p')[2].getText()                                    #?como anteriormente sumandole el metodo .gettext() nos devolvera solo el contenido dentro de la etiqueta seleccionada con select               #?agregandole el indice [3] en este caso solo nos devolvera solo el parrafo encontrado en el indice tres, osea el tersero    
print(parrafo)


print("///////////////////////////////////////////////////////////////////////////////////")
parrafo = sopa_de_palabras.select('.post-title-container h3')[1].getText()             #?dentro de select poniendo dos parametros (con un espacio entre medio), buscaremos dentro del primer parametro que le damos (en este caso le pasamos el primer parametro con el nombre de class añadiendo el .nombre , si fuese un id se pone #nombre), el siguiente elemento dentro h3                       #?como anteriormente sumandole el metodo .gettext() nos devolvera solo el contenido dentro de la etiqueta seleccionada con select               #?agregandole el indice [3] en este caso solo nos devolvera solo el parrafo encontrado en el indice tres, osea el tersero    
print(parrafo)

#podemos jugar un poco tambien con el contenido extraido
for e in parrafo:
    print(e)
    print(" ".join(parrafo))

print("///////////////////////////////////////////////////////////////////////////////////")
parrafo = sopa_de_palabras.select('.post-title-container h3')[1].getText()             #?dentro de select poniendo dos parametros (con un espacio entre medio), buscaremos dentro del primer parametro que le damos (en este caso le pasamos el primer parametro con el nombre de class añadiendo el .nombre , si fuese un id se pone #nombre), el siguiente elemento dentro h3                       #?como anteriormente sumandole el metodo .gettext() nos devolvera solo el contenido dentro de la etiqueta seleccionada con select               #?agregandole el indice [3] en este caso solo nos devolvera solo el parrafo encontrado en el indice tres, osea el tersero    
print(parrafo)


print("///////////////////////////////////////////////////////////////////////////////////")
#?para extraer imagenes
imagenes = requests.get("https://www.escueladirecta.com/courses")

sopa_imagen = bs4.BeautifulSoup(imagenes.text, "lxml")

imagenes_listas = sopa_imagen.select("img")                                #?mismo metodo que lo anterior pero buscamos "img" nos lo dara tdod junto de forma digamos, desordenada

print(imagenes_listas)

print("///////////////////////////////////////////////////////////////////////////////////")
#usanbdo un loop for haremos que nos lo de linea por linea imprimido uno debajo de otra img
for img in imagenes_listas:
    print(f"**{img}**")
    print("-"*90)


print("///////////////////////////////////////////////////////////////////////////////////")
#podemos seleccionar mas finamente que imagenes queremos que encuentre, analizando un npoco el codigo web y viendo los patrones que usa de nombre class para las imagenes que nos interesan extraer
imagenes_listas = sopa_imagen.select(".course-box-image")                  #?de esta forma nos va a extraer solo las imagenes con class  .course-box-image que en este caso son las que nos interesan
for img in imagenes_listas:
    print(f"**{img}**")
    print("-"*90)




print("///////////////////////////////////////////////////////////////////////////////////")
imagenes_listas = sopa_imagen.select(".course-box-image")[0]["src"]                  #?de esta forma nos va a extraer solo las imagenes con class  .course-box-image que en este caso son las que nos interesan, con [0] definimos que va a devolvernos la primera del indice 0 por que esto es una lista, y con [src] apuntamos a que solo nos devuelva la url que esta dentro de el como ruta donde esta la imagen.
print(imagenes_listas)

imagen_1 = requests.get(imagenes_listas)           #?metemos en una variable la imagen ya lista seleccionada anteriormente por su indice, para descargar solo la imagen de esa url
i = open("imagen1.jpg","wb")                       #?usamos wb (escribir binario)
i.write(imagen_1.content)                          #?dentro de la variable i, le indicamos que escriba, (en su archivo indicado recien "imagen1.jpg", que le escriba lo que este en la variable que contiene la url de la imagen seleccionada) y de esta forma nos va a escribir y crear descargado en el archivo, nuestra imagen, podriamos hacer un loop para extraer varias o desde determinados indices que le demos.
i.close()




print("///////////////////////////////////////////////////////////////////////////////////")
imagenes_listas_loop = sopa_imagen.select(".course-box-image")
contador = 0                                        #?contador para el loop
for im in imagenes_listas_loop[:3]:                 #?for, para im imagenes dentro de lo extraido con class .course-box-image, iterar solo hasta el indice  [:3] y extraer :
    img = requests.get(im["src"])                   #?extraer dentro de img, cada im imagenes tereradas, solo su url con src
    im = open(f"imagenes{contador}.jpg", "wb")      #?igual que arriba generamos el archivo..... le añadi un contador para que los enumere a los nombres de cada archivo creaodo mientras itera  (donde estael nombre del archivo podemos agregar antes la ruta  ose path donde se guardar)
    im.write(img.content)
    im.close()
    contador += 1
    
    
print("///////////////////////////////////////////////////////////////////////////////////")    
    
    
#?toscrape (pagina legal para practicar werscraping)

print("///////////////////////////////////////////////////////////////////////////////////")    

# Definiendo la función "buscar_comentarios" que toma un objeto "sopa" (BeautifulSoup) como argumento
def buscar_comentarios(sopa):
    # Creando una lista vacía llamada "comentarios" para almacenar todos los comentarios encontrados
    comentarios = []
    
    # Iterando a través de todos los elementos en el árbol del documento usando "recursiveChildGenerator()"
    for comentario in sopa.recursiveChildGenerator():
        # Verificando si el elemento actual es una instancia de la clase "Comment"
        if isinstance(comentario, Comment):
            # Si es un comentario, añadiéndolo a la lista "comentarios"
            comentarios.append(comentario)
    
    # Devolviendo la lista de comentarios al finalizar la iteración
    return comentarios

# Llamando a la función "buscar_comentarios" con el objeto BeautifulSoup "sopa_de_palabras" como argumento
comentarios = buscar_comentarios(sopa_de_palabras)

# Imprimiendo los comentarios encontrados en el documento HTML
print(comentarios)




print("///////////////////////////////////////////////////////////////////////////////////")    

#! probando scraping en web tospcrape en donde extraigo con la siguiente funcion todas las rutas de los libros

pagina_de_libros = requests.get('http://books.toscrape.com/')

buscar_libros = bs4.BeautifulSoup(pagina_de_libros.text, 'lxml')

libros_encontrados = buscar_libros.select('.image_container')

libros = []
contador = 0
for libro in libros_encontrados:
    libros = libro.find('img')['src']
    contador = contador + 1
    print(f'libro numero {contador} : {libros}')




print("///////////////////////////////////////////////////////////////////////////////////")

#!imprimimos varias paginas de la pagina principal para ver que podemos ver y buscar en varias url a la ves

pagina_de_libros1 =  'https://books.toscrape.com/catalogue/page-{}.html'
for hojas in range(1, 15):
    print(pagina_de_libros1.format(hojas))


print('o de esta forma')

for hojas in range(1, 15):
    pagina_de_libros1 = f'https://books.toscrape.com/catalogue/page-{hojas}.html'
    print((pagina_de_libros1))



print("///////////////////////////////////////////////////////////////////////////////////")



```
````
