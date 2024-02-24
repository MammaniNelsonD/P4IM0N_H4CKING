# 😀 BUSCADOR DE NUMERO DE SERIE EN ARCHIVOS DE DIRECTORIOS

````python
// Some code

```python
#!P4IbuscadorNserie   -  by P4IM0N

import os
import time
import re
from datetime import datetime
import timeit

#recorrer todo el arbol de carpetas y sus archivos buscando un patron de numero de serie 
#patron formato del nmero de serie : N+abc+12345 = Nabc12345
#resultado y presentacion en estilo tabla (fecha actual"d/m/a")+(archivo y numero serie encontrado)+(cantidad encontrada)+(duracion de la busqueda)

#?banner
print('''___  ____ _______  __  ______________      _  __    ___________  ________
  / _ \/ / //  _/ _ )/ / / / __/ ___/ _ |____/ |/ /___/ __/ __/ _ \/  _/ __/
 / ___/_  _// // _  / /_/ /\ \/ /__/ __ /___/    /___/\ \/ _// , _// // _/  
/_/    /_//___/____/\____/___/\___/_/ |_|  /_/|_/   /___/___/_/|_/___/___/  
                                                                        By P4IM0N
------------------------------------------------------------------------------------
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
---------------------------------------------------------------------------------''')

#?ruta del directorio a escanear
ruta = "/home/paimon/cursopython/dia9-buscadordenumerosdeserie/extraidoProyecto+Dia+9/Mi_Gran_Directorio"


#?funcionunica que busca las rutas de los archivos con terminacion .txt usando os.walk() y luego usando re.findall() buscamos el match (coincidencia del patron) dentro de los archivos en modo lectura, imprimiendo una tabla al final con dicha informacion
def P4IbuscadorNserie():
    tiempo_inicio = timeit.default_timer()                                                                          #?medir el tiempo, de inicio
    saludo = input("Buenas como estas, deseas buscar numeros de serie en este directorio completo(s/n): ")
    nombre = input("Dime tu nombre manito: ")
    if saludo == "s":                                                                                               #?si la respuesta del usuario es "s" entrara
        print(f"Bien manito {nombre}, estamos buscando los numeros de serie: ")
        lista_archivo_serie_tabla = []                                                                              #?lista para extraer datos para el formato de tabla
        for dir_princ, sub_dir, archivos in os.walk(ruta):                                                          #?con for itineramos en la exploracion con os.walk(ruta) de la ruta de directorio buscando "directorio principal, subdiorectorio y archivos dentro de todos ellos"
            for archivo in archivos:                                                                                #?luego con for itineramos buscando archivo dentro de los archivos encontrados y guardados en el con el uso de walk() anteriormente
                if archivo.endswith(".txt"):                                                                        #?y le decimos que de todos los encontrados con el uso de .endswitch deje entrar a los que solo tienen la extencion .txt                
                    ruta_de_archivos_txt = os.path.join(dir_princ, archivo)                                         #?dentro de la variable ruta_de_archivos_txt con os.path.join le decimos que cree la ruta completa de cada uno de los txt encontrados usando como referencia el directorio principal y el nombre del archivo, y las guarde dentro de esta variable
                    ruta_pura_tabla = os.path.basename(ruta_de_archivos_txt)                                        #?guardo solo el nombre del archivo extraido de la ruta completa con .basename
                    with open(ruta_de_archivos_txt,"r") as archivo_abierto:                                         #?con la ruta de cada archivo txt los pongo en ejecucion con with y en modo lectura guardandolo con as en una variable archivo abierto
                        patron_N_serie = re.findall("N+\w{3}-\d{5}", archivo_abierto.read())                        #?con findall busco el match coinsidencia, con el patron aportado y buscando el mismo dentro de los archivos abiertos ya en bodo lectura con read()            
                        if patron_N_serie:                                                                          #?si ahi un paron de serie encontrado True va a entrar la condicion     
                            lista_archivo_serie_tabla.append((ruta_pura_tabla, patron_N_serie))                     #?con append voy agregando a una lista creada anteriormente, todos los nombres de archivos con basenamed y los numeros de serie para ser utilizados en el modo tabla visual
                            print(f"El archivo esta en: {ruta_de_archivos_txt} ")
                            for numero_de_serie in patron_N_serie:                                                  #?itinero para que me encuantre e inprima luego cada uno de los numeros de serie match encontrados en patron_n_series
                                print(f"Y contiene el NUMERO DE SERIE:{numero_de_serie}")
        ver_tabla = input("Desea verlo en formato de tabla: (s/n) ")
        if ver_tabla == "s":
            def tabla_informatica(lista_archivo_serie):                                                             #?funcion2 interna que va a recibir los datos de la lista_serie _tabla que guardamos antes para ser utilizada y extraer los datos para el modo tabla
                print("-"*50)
                print(datetime.now())
                print("-"*50)
                print("ARCHIVO\t\t\t\tNºSERIE")
                print("-"*50)
                contador = 0
                for a,n in lista_archivo_serie:                                                                     #?itinero entre los a y n osea archivos y numeros serie que guarde previamente en la lista serie tabla
                    print(f"{a}\t\t\t{n}")
                    contador += 1
                print("-"*50)    
                print(f"Mira {nombre} el total de archivos encontrados es: [{contador}]")
                tiempo_final = timeit.default_timer()                                                               #?bandera para marcar el tiempo final de la ejecusion del programa            
                print(f"El sistema demoro en encontrar los numeros de serie: [{tiempo_final-tiempo_inicio:.2f}] segundos")   #?con .2f definimos que queremos dos decimales luego de la coma
                print("SALUDOS Y ESPERO TE ALLA SIDO DE AYUDA :D")
            tabla_informatica(lista_archivo_serie_tabla)                                                            #?ejecucion de la funcion2 internamente ingresandole dicho parametro que dijimos para que extraiga los datos lista_archivo_serie_tabla.                          
    else:
        print(f"muchas gracias manito {nombre}, sera la proxima :)")   
                





P4IbuscadorNserie()       

```
````

CODEO DEL DIA 9:



````python
// Some code

```python
#! dia 9


#modulo collections
#?Counter


from collections import Counter,defaultdict,namedtuple


list_numeros=[2,2,2,3,4,4,5,6,6,7,7,7,5,4,3,2,1,1,9]
print(Counter(list_numeros))               #?Counter nos va a crear digamos un diccionario, con claves de los numeros de nuestra lista y de valor la cantidad de veces que se repite cada uno, osea cada clave nombrada (tambien se puede contar cada caracteres de un string, o palabras)



palabras = "auque la mona se vista de seda mona se queda"
print(Counter(palabras.split()))           #?Counter aca lo usamos para que nos cuente por palabnraas, indicandole con split que cuente lo que hahi entrecada espacio vacio, para que detecte las palabras por separado



letras = "ydtygdsfyudsuiftasrtyasretwyuibasfs"
print(Counter(letras))                     #?Counter aca va a contar la cantidad de veces que se repite cada letra




counter=Counter([1,1,1,2,3,3,4,5,78,8,5,4,2,1,4,5,6,8,9,9,9,3,4,1])
print(counter.most_common())               #?most_common (es una de las propiedaddes de Counter, esta nos muestra los elemento mas comunes de nuestra lista, primero el que mas se repite y al final el que menos)



counter=Counter([1,1,1,2,3,3,4,5,78,8,5,4,2,1,4,5,6,8,9,9,9,3,4,1])
print(list(counter))                       #?de esta forma casteamos en una lista y con Counter los elementos unicos en ella




#?defaultdict


'''diccionario = {'s': 6, 'y': 5, 't': 4, 'd': 3, 'f': 3, 'u': 3, 'a': 3, 'i': 2, 'r': 2, 'g': 1, 'e': 1, 'w': 1, 'b': 1}
print(diccionario("z"))'''                 #? en este caso llamamos a imprimir un elemento clave que no esta en mi diccionario y nos dara error por ende, lo podemos hacer sin error usando el modulo Defaultdict




diccionario = defaultdict(lambda: 'no se encuentra')   #?con defaultdict nos permite dar una respuesta al llamar a una clave de diccionario que no este, usando lambda y su valor de respuesta.
diccionario["perro"] = "negro"       
print(diccionario["gato"])




tupla = (300,500,20,700)
print(tupla[1])                                        #?de la manera normal imprimimos el valor que esta en la posicion 1 dentro de nuestra tupla, pero si no recordaramos la posicion del valor que queremos buscar dentro de la tupla para impriomirlo, lo podemos solucionar con namedtuple (nombre de la tupla, en ves de su posicion)




Personaje = namedtuple("Persona",["nombre","apellido","altura","peso"])     #?como que creamos un objeto o clase Perspona que esta dentro de un atupla con nametuple y que tiene como parametros o claves de diccionario que lo deescribel y a los que vamos a llamar en su posiciones para agregarles su valores gracias al modulo nametuple
paimon = Personaje("paimon","makarov",1.90,80)                              #?creamos una instacia
print(paimon.apellido)                                                      #? y aca vemos como usando el modulo podemos llamar a imprimir el valor de la clave sin conocer su posicion, solo con su nombre de clave digamos
print(paimon.altura)
print(paimon.nombre)
print(paimon.peso)





#practicas



from collections import defaultdict

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)






from collections import defaultdict

mi_diccionario = defaultdict(lambda: "Valor no hallado")
mi_diccionario["edad"]= 44




'''import collections

lista_ciudades = collections.deque("Londres", "Berlin", "París", "Madrid", "Roma", "Moscú")
lista_ciudades.extendleft()
lista_ciudades.appendleft("Brasilia")
print(lista_ciudades)'''

#?asi resolvi yo
import collections

lista_ciudades = collections.deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.appendleft("Brasilia")
print(lista_ciudades)

#?asi lo aseptaba udemy
from collections import deque

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.extendleft(["Brasilia"])
print(lista_ciudades)




#modulo datatime (ya integrado a python) nos sirve para:-almacenar hora,fecha datos de tiempo en fin, -calciulos de tiempo -mostrar en diferente formato

import datetime


hora = datetime.time(19, 35, 50, 1000)               #?usando el modulo datetime + time (es el tiempo en horas) y vemos como nos exige el parametro de los minutos 
print("HORA:")
print(hora)                                          #?podemos hacer que nos muestre e imprima elementos dell dato tiempo a eleccion, osea solo los minutos o segundos,etc
print(hora.hour)
print(hora.minute)
print(hora.second)
print(hora.microsecond)





fecha = datetime.date(2023, 2, 13)                              #?usando datetime + date (le indicamos fechas)año , mes , dia . 
print("FECHA:")
print(fecha)                                                    #?al iguualque con time podemos acceder por separado a cada dato, por qiue nos lo avilita luego del . en la variable creada como un metodo
print(fecha.year)
print(fecha.month)
print(fecha.day)
print(fecha.ctime())                                              #?tambien con ctime podemos mostrar otro formato de fecha con el nombre de dia
print(fecha.today())                                              #? a today lo debemos trabajar sobre una variable date, pero nos mostrara el dia real en el que estamos



from datetime import datetime                                      #? para trabajar con ambos objetos a la ves debemos immportar datetime



mi_fecha_y_hora = datetime(2023, 2, 13, 20, 00, 20, 1000)          #?con datetime podemos trabajaar y configurar ambos datos 
print(mi_fecha_y_hora)
mi_fecha_y_hora = mi_fecha_y_hora.replace(year=2024)               #?con replace podemos remplasar y cambiar un dato a eleccion, en este caso el año year
print(mi_fecha_y_hora)




from datetime import date

#con date podemos tambien por ejemplo calcular margenes de tiempo entre un comienzo y un final como ejemplo= el tiempo que duro un auto, desde la fecha que lo compramos hasta el dia que no funciono mas, usando el modulo date


compra = date(2017, 2, 20)                                         #?simplemente creamos la fecha de comienzo
dejo_de_funcionar = date(2022, 2, 15)                              #? y la fecha que dejo de funcionar

duracion = dejo_de_funcionar - compra                              #?luego restamos a la fecha que dejo de funcionar la fecha de compra y vemos los dias que duro nuestro auto
print("EL AUTO DURO FUNCIONANDO: ")
print(duracion)








#practicas



import datetime 

mi_fecha = datetime.date(1999, 2, 3)





import datetime 

hoy = datetime.date(2023, 2, 12)
hoy = hoy.today()
print(hoy)





#?asi lo hice yo
import datetime 

hora = datetime.time(20, 23, 40)

minutos = hora.minute
print(minutos)



#?asi lo pedia udemy

from datetime import datetime

minutos = datetime.now().minute                      #? con now al igual que today nos da los datos del tiempo actual completos en este caso que travajamsos con datetime, pero luego con .miunte le solicitamos que guarde en la variable solo lols minutos de la hora actual
print(minutos)







#modulo time o timeit (ejemplo nos permite ver el tiempo que tarda en ejecutarse un codigo ya asi poder compararlo con otro, etc)



#?las dos funciones hacen lo mismo pero mediremos sun  tiempo apara comparar su eficicencia una con otra
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista 





   
def pruba_while(numero):
    lista = []
    contador = 1
    while contador <= numero: 
        lista.append(contador)
        contador+= 1
    return lista    




print(prueba_for(15))
print(pruba_while(15))




import time                             #?aca vamos a usar el modulo time q no es tan especifico pero nos va a apermitir medir el tiempo de ejecucion

#?las dos funciones hacen lo mismo pero mediremos sun  tiempo apara comparar su eficicencia una con otra
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista 





   
def pruba_while(numero):
    lista = []
    contador = 1
    while contador <= numero: 
        lista.append(contador)
        contador+= 1
    return lista    


 
inicio = time.time()                      #?digamos quqe ponemos una marca de tiempo comienzo justo antes que se ejecute la funcion
print(prueba_for(15))
final = time.time()                       #? y otra marca de tiempo justo apenas termina la funcion
print(final - inicio)                     #? luego restando el tiempo final menos el de iincio nos da el tiempo que tardo en terminar de ejecurtarse la funcion para asi poder compararla con la otra y ver cual fue mas eficiente




inicio = time.time()
print(pruba_while(15))
inicio = time.time()
print(final-inicio)





import timeit                              #? timeit si es especifica para medir el tiempode ejecucion y darnos algo mas especifico




def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista 





   
def pruba_while(numero):
    lista = []
    contador = 1
    while contador <= numero: 
        lista.append(contador)
        contador+= 1
    return lista   





ejecucion = '''                   #?para usar timeit es como que generamos nuestra funcuncion y ejecucion en un string, para luego ingresarcela a la funcion importada de timeit con estas variables.
prueba_for(15)
'''



funcion = '''                     #?igual hacemos lo mismo con nuestra funcion para luego ser ingresadas a timeit y pueda ser analizada para ver su tiempo de ejecucion
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista 
'''


duracion = timeit.timeit(ejecucion, funcion, number=1000)      #?dentro de la variable duracion le ponemos el modulo tiemit con su metodo timeit, y dentro del parentecisd le ingresamos nuestras variables de ejecucion , funcion y definimos un parametro mas numero= que es el numero de vesese que queremos que se ejecute nuestra funcion para medir su tiempo
print("la funcion FOR al ejecutarse 1000 veces demosra : ")
print(duracion)






ejecucion = '''
pruba_while(15)
'''


funcion = '''
def pruba_while(numero):
    lista = []
    contador = 1
    while contador <= numero: 
        lista.append(contador)
        contador+= 1
    return lista
'''


duracion = timeit.timeit(ejecucion, funcion, number=1000)
print("la funcion WHILE al ejecutarse 1000 veces demosra : ")
print(duracion)








#modulo math (kit completo para trabajar con numeros)









import math



redondeado = math.floor(66.888)             #?floor redondeo para abajo
print(redondeado)




redondeado = math.ceil(66.222)               #?ceil redondea para arriba
print(redondeado)




redondeado = math.pi                         #?pi es un valor ya definido (para calculo de radio,etc)
print(redondeado)





redondeado = math.log(25, 5)                 #?log nos permite saber a cuanto debemos exponenciar al segundo numero que le damos para que llegue al primer valor que le dimos dentro del parentesis
print(redondeado)




redondeado = math.tan(2500)                  #?tan nos devuelve la tangente del numero que le ingresemos
print(redondeado)




redondeado = math.cos(2500)                        #?cos nos devuelve el coseno del nuemero que le demos
print(redondeado)







#practicas



import math 

resultado = math.log10(25)






import math 

resultado = math.sqrt(math.pi)






import math 

resultado = math.factorial(7)











#!by P4IM0N

#modulo re (expresiones regulares, nos permite construir un patron para verbsi este sebrespeta o si se encuebtra en un lugar Ej: para filtrar y vetificar que datos de numerosbtelefonicos ingresados coinsidan con un patron solivitado valido)





import re

texto = "Comuniquece a nuestro numero telefonico las 24hs (351)5447123"

patron = "nada"   #?lobque se va a buscar

busqueda = re.search(patron, texto)   #? con re y el metodo search buscamos el patron que definimos para ver si lo encuentra en texto
print(busqueda)




texto1 = "Comuniquece a nuestro numero telefonico las 24hs y hable con nuestro operador (351)5447123"

patron1 = "nuestro"   #?lobque se va a buscar

busqueda1 = re.search(patron1, texto1)     #? con re y el metodo search buscamos el patron que definimos para ver si lo encuentra en texto, en este caso encontrara la primer palabra nosma qie encuentre de izq a der. y nos dara su spam posicion de comienzoby final, etc pero parav encontrar todas las repeticiones y no solo una se usa otro metodo a continuacion
print(busqueda1)





'''
texto2 = "Comuniquece a nuestro numero telefonico las 24hs para hablar con nuestro operador (351)5447123"

patron2 = "nada"   #?lobque se va a buscar

busqueda2 = re.search(patron2, texto2)   #? con re y el metodo search buscamos el patron que definimos para ver si lo encuentra en texto
print(busqueda2.span())     #?podemos encobtrar metodos en la variable busqueda ej. .span parabque nos de su ppsicion , etc
'''





texto3 = "Comuniquece a nuestro numero telefonico las 24hs para hablar con nuestro operador (351)5447123"

patron3 = "nuestro"   #?lobque se va a buscar

busqueda3 = re.findall(patron3, texto3)   #? con re y el metodo findall buscamos el patron que definimos para ver si lo encuentra en texto varias veces no como search 
print(busqueda3)     #?podemos encobtrar metodos en la variable busqueda ej. .span parabque nos de su ppsicion , etc







texto4 = "Comuniquece a nuestro numero telefonico las 24hs para hablar con nuestro operador (351)5447123"

patron4 = "nuestro"   #?lobque se va a buscar

for encontrado in re.finditer(patron4, texto4):            #? con re y finditer vemos la posicion de start comienzo de la palabra encobtrada y el final end de la misma, y como estamos iterando buscando el patron lo buscara tambien a todas las veces que se repita la palabra.
 print(encontrado.span())






texto5 = "comuniquese a nuestro numero telefonico 351-544-6234"

patron5 = r'\d\d\d-\d\d\d-\d\d\d\d'   #? aca generamos un patron de busqueda telefonico, usando la 'd' indicamos que van a ser digitos numerocos en el orden que le indicamos con las \ asibque cada ves que encuebtre este patron lo tomara y encobtrara como un objeto match indistintamentebque los numeros cambien.

telefono = re.search(patron5, texto5)   #?hacemos que busque nuestro patron indicado y luego lo imprima

print(telefono)







texto6 = "comuniquese a nuestro numero telefonico 351-544-6234 tambien 351-737-6384 o 351-948-1289"

patron6 = r'\d{3}-\d{3}-\d{4}'   #? aca generamos un patron de busqueda telefonico, usando la 'd' indicamos que van a ser digitos numerocos en el orden que le indicamos con las \ asibque cada ves que encuebtre este patron lo tomara y encobtrara como un objeto match indistintamentebque los numeros cambien.(en estev caso indicamos la cantidad de digitos usando el numero de repetocion que querenos dentro de las llaves {} funciona igual)

for telefono1 in re.finditer(patron6, texto6):   #?hacemos que busque nuestro patron indicado y luego lo imprima

 print(telefono1.group())







texto6 = "comuniquese a nuestro numero telefonico 351-544-6234 tambien 351-737-6384 o 351-948-1289"

patron6 = r'\d\d\d-\d\d\d-\d\d\d\d'   #? aca generamos un patron de busqueda telefonico, usando la 'd' indicamos que van a ser digitos numerocos en el orden que le indicamos con las \ asibque cada ves que encuebtre este patron lo tomara y encobtrara como un objeto match indistintamentebque los numeros cambien.
for telefono1 in re.finditer(patron6, texto6):   #?hacemos que busque nuestro patron indicado y luego lo imprima

 print(telefono1.span())  #?con span nos va a imprinir la posicion comienzo y final de cada elemento encobtrado con el patron ondicado 






texto6 = "comuniquese a nuestro numero telefonico 351-544-6234 tambien 351-737-6384 o 351-948-1289"

patron6 = r'\d\d\d-\d\d\d-\d\d\d\d'   #? aca generamos un patron de busqueda telefonico, usando la 'd' indicamos que van a ser digitos numerocos en el orden que le indicamos con las \ asibque cada ves que encuebtre este patron lo tomara y encobtrara como un objeto match indistintamentebque los numeros cambien.

for telefono1 in re.finditer(patron6, texto6):   #?hacemos que busque nuestro patron indicado y luego lo imprima

 print(telefono1.group())  #?con el metodo group nos imprime losnelementos encontrados con ese patron







texto6 = "comuniquese a nuestro numero telefonico 351-544-6234 tambien 351-737-6384 o 351-948-1289"

patron6 = re.compile(r'(\d{3})-(\d{3})-(\d{4})') #? aca generamos un patron de busqueda telefonico, usando la 'd' indicamos que van a ser digitos numerocos en el orden que le indicamos con las \ asibque cada ves que encuebtre este patron lo tomara y encobtrara como un objeto match indistintamentebque los numeros cambien.(en estev caso indicamos la cantidad de digitos usando el numero de repetocion que querenos dentro de las llaves {} funciona igual)(usando re y compile es como que compilamos el patron con posiciones separadas con parentesis () como los dispongamos, para luego poder sokicitarle que nos muewtre solo una parte determinada del patron indicado)

for telefono1 in re.finditer(patron6, texto6):   #?hacemos que busque nuestro patron indicado y luego lo imprima

 print(telefono1.group(3))   #?poniendo dentrobdel parentesis la posicion le ibdicamos cual parte del patron vompilado queremos que nos imprima en este caso 





contraseña7 = input("Porfavor ingrese su contraseña: ")

patron7 = r'\D{1}\w{8}'    #?como ejemplo vemos que podemos usarlo para gestionar formatos de contraseñas validas, en este caso con D indicamos que no comience con un digito numero, y a continuacion con w que puede ingresarse ocho digitos alfanumericos

controlar = re.search(patron7, contraseña7)

print(controlar)
print(controlar.group())






texto8 = "hola como estas tia, trabajo oos dias lunes martes viernes y sabados"

buscar8 = re.search(r'lunes|martes', texto8)     #? con or | podenos usarlo hacer que tenga otrabopcion de patron de busqueda

print(buscar8)







texto9 = "hola como estas tia, trabajo oos dias lunes martes viernes y sabados"

buscar9 = re.search(r'..tes', texto9)     #? con . lo podemosnusar de comodin, en estevcaso iva a buscar la coinsidencia si existe el patron "tes" y como le añadimos .. antes va a añadir dos letras antes de encontrar ese patron

print(buscar9)








#practicas



#?asi resolvi yo
import re

email = input("ingrese su email: ")


def verificar_email(email):
    patron = r'\w+@\w+.com...'
    aprobado =  re.search(patron, email)
    if aprobado:
        print("ok")
        print(aprobado.group()) 
    else:
        print("La dirección de email es incorrecta")    
     

verificar_email(email)







#?asi resolvio gpt, mejoro el patron
import re

email = input("ingrese su email: ")


def verificar_email(email):
    patron = r'\w+@\w+\.[a-zA-Z]{2,3}(?:\.[a-zA-Z]{2,3})?'     #?el signo de pregunta al final de la compilacion de patrones que pusimos dentro del parentesis, le indica que es un patron que puede o no estar respetandose para que sea aprobado, osea que no es obligatorio. si el otro resto del patron del principio
    aprobado =  re.search(patron, email)
    if aprobado:
        print("ok")
        print(aprobado.group()) 
    else:
        print("La dirección de email es incorrecta")    
     

verificar_email(email)






#?asi me lo aprobaba udemy
import re
 
def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")










#Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.'''


#?asi resolvi yo
import re

frase = "hola como estas juan carlos y hola paolaaaa"

def verificar_saludo(frase):
    patron = r'\bhola\b'
    aprobado = re.search(patron, frase)
    if aprobado:
        print("Ok")
    else:
        print("No has saludado")    


verificar_saludo(frase)





#?asi me lo mejoro gpt
import re

frase = "hola como estas juan carlos y Hola paolaaaa"

def verificar_saludo(frase):
    patron = r'\bhola\b'
    aprobado = re.search(patron, frase, re.IGNORECASE)     #?me explico que usar dentro de search, IGNORECASE simplifica que tambien detecte la presencia del patron palabra, ' hola ' aunque este en minuscula o mayuscula
    if aprobado:
        print("Ok")
    else:
        print("No has saludado")    


verificar_saludo(frase)




#?asi la aprobo udemy
import re
 
def verificar_saludo(frase):
    patron = r'^Hola'                     #?lo que hace ^ es indicar que la palabra hola deve comensar en el principio del string para que se de el patron, si esta en el medio de la frase no se aprobara el patron por ende
    verificar = re.search(patron,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")
        
        
        
        
        
        
        
        
        
#El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".        
        




#?asi resolvi yo
import re

cod_postal = input("ingrese su codigo postal: ")

def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    aprobado = re.search(patron, cod_postal)
    if aprobado:
        print("ok")
    else:
        print("El código postal ingresado no es correcto")    
        

verificar_cp(cod_postal)






#?asi mejoro solo el patron gpt
import re

cod_postal = input("ingrese su codigo postal: ")

def verificar_cp(cp):
    patron = r'^[A-Za-z0-9\-\s]{3,10}$'
    aprobado = re.search(patron, cod_postal)
    if aprobado:
        print("ok")
    else:
        print("El código postal ingresado no es correcto")    
        

verificar_cp(cod_postal)








#?asi la aprueba udemy 
import re
 
def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")






#comprimir y descomprimir archivos desde python (zipfile o shutil)

#?hacemos una practica en otro archivo para descomprimir el zip de las consignas del proyecto del dia 9


```
````
