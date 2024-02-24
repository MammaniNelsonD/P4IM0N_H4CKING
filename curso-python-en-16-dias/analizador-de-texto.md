# 😀 ANALIZADOR DE TEXTO

````python
// Some code

```python
print("BIENVENIDO AL ANALIZADOR DE TEXTO")

#ingresa el texto
text_usuario = input("ingrese por favor cualquier texto por lo menos de un parrafo: ")

#ingresa las tres letras
consulta_usuario1 = input("Elija por favor una primer letra a su eleccion: ")
consulta_usuario2 = input("Elija por favor una primer letra a su eleccion: ")
consulta_usuario3 = input("Elija por favor una primer letra a su eleccion: ")


#transformar todo el texto a minuscula
text_usuario = (text_usuario.lower())


#transformar todas las letras ingresadas a minuscula
letra1 = (consulta_usuario1.lower())
letra2 = (consulta_usuario2.lower())
letra3 = (consulta_usuario3.lower())


#cuantas veces aparece cada letra elegida

print("CANTIDAD DE VECES QUE SE REPITEN EN EL TEXTO SUS LETRAS ELEGIDAS: ")

total_de_letras1 = (text_usuario.count(letra1))
total_de_letras2 = (text_usuario.count(letra2))
total_de_letras3 = (text_usuario.count(letra3))


print(f"En el texto la letra (({letra1})) se encuentra esta cantidad de veces: (({total_de_letras1}))")
print(f"En el texto la letra (({letra2})) se encuentra esta cantidad de veces: (({total_de_letras2}))")
print(f"En el texto la letra (({letra3})) se encuentra esta cantidad de veces: (({total_de_letras3}))")


#cuantas palabras ahi en el texto en total


print("CANTIDAD DE PALABRAS QUE CONTIENE SU TEXTO: ")

list_text_user = text_usuario.split()
total_palabras = len(list_text_user)

print(f"Su texto contiene un total de (({total_palabras})) palabras")



#cual es la primera letra del texto y la ultima

print("CON QUE LETRA EMPIEZA Y TERMINA SU TEXTO: ")

primer_letra = text_usuario[0]
ulti_letra = text_usuario[-1] 

print(f"Su texto comienza con la letra (({primer_letra})) y termina con la letra (({ulti_letra}))")



#como quedaria el texto si invirtieramos las palabras

print("PROCESANDO EL TEXTO AL REVES: ")

list_text_user.reverse()

print("Su texto escrito alreves quedaria de la siguiente manera: ")
print(" ".join(list_text_user))



#la palabra python se encuentra en el texto ??

print("BUSCANDO LA PALABRA PYTHON: ")

python_etara = "python" in list_text_user
respuesta_python = {True:"La palabra ((python)) esta en el texto",False:"La palabra ((python)) no esta en el texto"}

print(f"{respuesta_python[python_etara]}")
print("MUCHAS GRACIAS POR UTILIZAR NUESTRO ANALIZADOR DE TEXTO, HASTA LA PROXIMA :)")


#BY PAIMON

```
````

CODEO APRENDIENDO LOS CONCEPTOS DEL DIA 3

````python
// Some code

```python
#uso de index, para buscar una letra en particular o buscar atraves de un orden numerico

mi_texto = "perfecto"
resultado = mi_texto.index("e")
print(resultado)


mi_texto = "perfecto"
resultado = mi_texto[3]
print(resultado)


#conteo negativo arranca cero del principio y luego el conteo alreves desde la derecha
mi_texto = "perfecto"
resultado = mi_texto[-2]
print(resultado)


#nos busca tambien por palabra y nos da el numero de posicion desde donde comisenza
mi_texto = "perfecto nos estamos viendo el lunes"
resultado = mi_texto.index("estamos")
print(resultado)


#comienza buscando de izq a der desde la posicion que le dimos con el numero y respeta el conteo desde donde le dimos.
mi_texto = "perfecto nos estamos viendo el lunes"
resultado = mi_texto.index("e",15)
print(resultado)


#tambien podemos hacer que busque marcandole un sector ej: entre posicion 24 y 29
mi_texto = "perfecto nos estamos viendo el lunes"
resultado = mi_texto.index("e",24,29)
print(resultado)



#rindex busca de derecha a izquierda osea alreves, pero devuelve el numero de indice real osea de izquierda a derecha
mi_texto = "perfecto nos estamos viendo el lunes"
resultado = mi_texto.rindex("e")
print(resultado)


#practicas


frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado)



frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)



#slising seria como cortar y agregar en un avariable


texto = "ABCDEFGHIJKLM"
fragmento = texto[2]
print(fragmento)


#va a extraer los caracteres que esten desde position 2 hasta la 5 sin incluirlo
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)


#cuando pones un valos y luego  : sin otro valor despues python interpreta que queremos extraer desde 2 hasta el final 
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:]
print(fragmento)



#cuando no ponemos un valor, y ponemos : y luego un valor, va a extraer alreves, osea desde la posicion 0 hasta el valor  posicion que dimos
texto = "ABCDEFGHIJKLM"
fragmento = texto[:5]
print(fragmento)


#el tercer factor indica posiciones salteadas, osea nos devuelve desde position 2 saltea dos y nos da un valor y asi consecutivamente hasta llegar posicion 10
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2]
print(fragmento)


#como no especificamos los dos primeros valores y solo el que saltea de forma negativa, nos imprime alreves el conteo
texto = "ABCDEFGHIJKLM"
fragmento = texto[::-1]
print(fragmento)


#practicas


frase = "Controlar la complejidad es la esencia de la programación"
resultado = frase[0:9]
print(resultado)


frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resultado = frase[9::3]
print(resultado)


frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado = frase[::-1]
print(resultado)




#metodos string

#upper sin parametros dentro del parrentesis nos transforma todo el texto en mayuscula
texto = "este es un texto de prueba"
resultado = texto.upper()
print(resultado)


#nos imprime la solo la letra en la posicion que le dimos en mayuscula 
texto = "este es un texto de prueba"
resultado = texto[3].upper()
print(resultado)


#lower sin parametros dentro del parrentesis nos transforma todo el texto en minuscula
texto = "Este es un texto de prueba"
resultado = texto.lower()
print(resultado)

#igual dandole la posicion
texto = "Este es un texto de prueba"
resultado = texto[0].lower()
print(resultado)


#split este separa los elementos para guardarlos en una lista, toma por defecto los espacios como separadores
texto = "Este es un texto de prueba"
resultado = texto.split()
print(resultado)


#indicandole un parametro a split, definimos que va a tomar el como separador
texto = "Este es un texto de prueba"
resultado = texto.split("t")
print(resultado)


#join lo que hace es unir los elementos de una LISTA y le definimos el lemento separador para unirlos, en este caso " " (espacio), luego join y dentro del parentecis el parametro
q = "como"
a = "perro"
b = "y"
c = "gato"
unido = " ".join([q,a,b,c])
print(unido)



#find muy parecido a index, seria para buscar tambien.(a diferencia de index, cuando find no encuentra un caracter que buscamos, nos devuelve -1, no un error como index)
texto = "Este es un texto de prueba"
resultado = texto.find("z")
print(resultado)



#replace lo que hace es remplazar la palabra que decignemos, por la que querramos, buscando solo y cambiandola en la primera posicion donde la encuentre
texto = "Este es un texto de prueba"
resultado = texto.replace("prueba","verdad")
print(resultado)



texto = "Este es un texto de prueba"
resultado = texto.replace("e","i")
print(resultado)





#practicas


frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())


lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))




frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
cambio1 = frase.replace("difícil","fácil") 
cambio2 = cambio1.replace("mala","buena")
print(cambio2)




#propiedades de string (los cuales por si mismos son inmutables)

#nombre  = "paimon"
#nombre[2] = "y"
#print(nombre)



#a no ser que se la cargue en una variable y se le de formato o modifique desde ahi

nombre = "paimon"
nombre = "paymon"
print(nombre)

#aca concatenamos dos string que estan guardados dentro de dos variables
n1 = "pai"
n2 = "mon"
print(n1+n2)


#tambien el string estando dentro de una variable se lo puede multiplicar y editar de varias formas, pero por si solo como string No.
n1 = "pai"
n2 = "mon"
print(n1*10)


#puede contener varios saltos de lineas, sin requerir de \n, usando """ ej: para escribir un poema
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)


# haciendo usdo de in podemos preguntar si dentro del poema contiene la palabra agua, para que nos responda con true o false
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print("agua" in poema)


poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print("perro" in poema)


#en fin en la anterior con in preguntamos si la palabra esta en el texto, y en este caso preguntamos si NO esta en el texto, por ende nos responde verdadero TRUE
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print("perro" not in poema)


#con len podemos ver el largo de un elemento, en este caso de poema
poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(len(poema))



#practicas

repe = "Repetición"
print(repe*15)


haiku = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
print("agua" not in haiku)


largo = "electroencefalografista"
print(len(largo))




#listas pueden ser de distintos tipos de dato, pero ordenados. se puede tener listas dentro de listas, y son inmutables se pueden modificar


mi_lista = ["a","b","c"]
print(type(mi_lista))


#se le pueden mesclar distintos tipos de datos
mi_lista = ["a","b","c"]
otra_lista = ["perro","60.66","80"]
print(type(mi_lista))
print(type(otra_lista))



#tambien se puede usar len para saber la cantidad de elementos paalabras que componen la lista
otra_lista = ["perro","60.66","80"]
resultado = len(otra_lista)
print(resultado)




#podemos extraer lo que pongamos en la posicion q le pedimos
otra_lista = ["perro","60.66","80"]
resultado = otra_lista[2]
print(resultado)


#tambien se puede determinar de donde hast donde extraer
otra_lista = ["perro","60.66","80"]
resultado = otra_lista[0:2]
print(resultado)


#concatenamos dos listas en una en el print, sin perder las listas originales, a no ser que creemos una variable de tercer lista
otra_lista = ["perro","60.66","80"]
otra_lista2 = ["gato","50","30.5"]
resultado = otra_lista[0:]
print(otra_lista+otra_lista2)




otra_lista = ["perro","60.66","80"]
otra_lista2 = ["gato","50","30.5"]
mi_lista3 = otra_lista+otra_lista2
print(mi_lista3)


#podemos modificar un elemento d una lista por otro seleccionando su posicion
otra_lista = ["perro","60.66","80"]
otra_lista2 = ["gato","50","30.5"]
mi_lista3 = otra_lista+otra_lista2
mi_lista3[0] = "loro"
print(mi_lista3)



#con append podemos agregar un elemento a un a lista, y lo agrega al final
otra_lista = ["perro","60.66","80"]
otra_lista2 = ["gato","50","30.5"]
mi_lista3 = otra_lista+otra_lista2
mi_lista3[0] = "loro"
mi_lista3.append("toro")
print(mi_lista3)



#pop sirve para remover uno de los elementos de la lista, sin parametros te elimina el ultimo elememtos de una lista, a no ser que se le de una posicion especifica a eliminar
otra_lista = ["perro","60.66","80"]
otra_lista2 = ["gato","50","30.5"]
mi_lista3 = otra_lista+otra_lista2
mi_lista3.pop()
print(mi_lista3)




otra_lista = ["perro","60.66","80"]
otra_lista2 = ["gato","50","30.5"]
mi_lista3 = otra_lista+otra_lista2
mi_lista3.pop(0)
print(mi_lista3)


#tambien se puede guardar el elemento eliminido con pop, creando una variable antes.
otra_lista = ["perro","60.66","80"]
otra_lista2 = ["gato","50","30.5"]
mi_lista3 = otra_lista+otra_lista2
eliminado = mi_lista3.pop(0)
print(mi_lista3)
print("se elimino la palabra: "+eliminado)




# sort  permite ordenar una lista de forma alfabetica o numerica. (nos devuelve info que no puede ser guardada en una variable, por que no es un elemennto, es de tipo nonetype)
lista = ["m","l","a","z","h"]
lista.sort()
print(lista)



#nos da vuelta el orden de la lista 
lista =["m","l","a","z","h"]
lista.reverse()
print(lista)



#practicas


mi_lista = ["a","50",60.6,"pelota","b"]
print(mi_lista)


medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)



frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)




#diccionarios


#las claves no se pueden repetir, si los valores
diccionario = {"clave1":"valor1","clave2":"valor2","clave3":"valor3"}
print(diccionario)


#de esta forma podemos buscar un valos con su clave
diccionario = {"clave1":"valor1","clave2":"valor2","clave3":"valor3"}
resultado = diccionario["clave2"]
print(resultado)


#pueden contener varios tipos de datos, hasta listas dentro, o diccionarios dentro de el tambien
cliente = {"nombre":"juan","apellido":"gomez","edad":30,"nacionalidad":"argentino"}
consulta = (cliente["apellido"])
print(consulta)




#de esta forma al buscar por la clave, nos imprime la lista osea todo el valor que esta dentro de ella, salvo que le especifiquemos una posicion
cliente = {"nombre":"juan","apellido":"gomez","edad":30,"nacionalidad":{"arg":"argentino","br":"brasil","pr":"peru"}}
consulta = (cliente["nacionalidad"])
print(consulta)



#de esta forma podemos buscar por posicion dentro de un diccionario, cualquier elementos que este dentro de el sea una lista o otro diccionario
cliente = {"nombre":"juan","apellido":"gomez","edad":[30,40,50,60],"nacionalidad":{"arg":"argentino","br":"brasil","pr":"peru"}}
consulta = (cliente["edad"][1]),(cliente["nacionalidad"]["br"])
print(consulta)



#ejercicio lograr imprimir una letra e en mayuscula . la misma esta en unal lista dentro del diccionario
cliente = {"nombre":"juan","apellido":"gomez","edad":[30,40,50,60,"e"],"nacionalidad":{"arg":"argentino","br":"brasil","pr":"peru"}}
print(cliente["edad"][4].upper())



#para agregar elemento al diccionario
dic = {1:"a",2:"b"}
print(dic)



dic = {1:"a",2:"b"}
print(dic)
dic[3] = "c"
print(dic)
dic["nombre"] = "ruper"
print(dic)

#asi sobreescribimos y cambiamos un dato del diccionario
dic[2] = "B"
print(dic)


#nos trae todas las llaves que contiene el diciconario(sin sus valores)
print(dic.keys())



#nos trae todos los valores que contiene el diciconario(sin sus claves)
print(dic.values())


#nos imprime el contenido completo de un diccionario, con sus claves y sus valores
print(dic.items())




#practicas


mi_dic = {"nombre":"Karen","apellido":"Jurgens","edad": 35,"ocupacion":"Periodista"}
print(mi_dic)



mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])




mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["edad"] = 36
mi_dic["ocupacion"] = "Editora"
mi_dic["pais"] = "Colombia"
print(mi_dic)





#tupples son inmutables y van entre parentesis o sin tambien, casi iguales que la listas pero se procesann mas rapido y pesan menos


mi_tuple = (1,2,3,4,5,6,7)
print(mi_tuple[2])




mi_tuple = (1,2,3,4,5,6,7)
print(mi_tuple[-2])



#se lo selecciona para imprimir como en los diccionarios, marcando la ruta con [][] para ir indicando posiciones...
mi_tuple = (1,2,3,(10,30),5,6,7)
print(mi_tuple[3][0])




#a travez de un casting lo podemos transformar en lista
mi_tuple = (1,2,3,(10,30),5,6,7)
mi_tuple = list(mi_tuple)
print(type(mi_tuple))



#se le pueden asignar los valores de la primer variable, por separado respetando el orden y teniendo que tener la misma cantidad de elementos de valor para que se pueda
t = (1,2,3)
x,y,z = t
print(x,y,z)




#pedimos que nos de la cantidad de elementos que contiuenen la tupla
t = (1,2,3,1)
print(len(t))



#count te permite contar la cantidad de veces que esta el elemento que le especificamos dentro d tuplas
t = (1,2,3,1)
print(t.count(1))


#nos permite hacer que nos indique el indice de posicion del elemento que le especificamos dentro de la tupla
t = (1,2,3,1)
print(t.index(3))





#practicas


mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))



mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = (list(mi_tupla))
print(type(mi_lista))



mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a,b,c,d)




#los set puede ir entre parentesis y set primero, o bien entre llavesd sin la palabra set, no admite elemntos repetidos, y no esta ordenado por indices y son inmutables, (no admite listas ni diccionarios, pero si admite tuple)

mi_set = set([1,2,3,4,5,6])
print(type(mi_set))
print(mi_set)



otro_set = {1,2,3,4,5}
print(type(otro_set))
print(otro_set)


#aca vemos como no atmite repeticiones, y las elimina
mi_set = set([1,2,3,4,5,6,6,6,6,2,3,4,5])
print(type(mi_set))
print(mi_set)




#si acepta tuplas dentro de el, por que tambien es un elemnto inmutable.
mi_set = set([1,2,3,4,5,6,(6,6,6),2,3,4,5])
print(type(mi_set))
print(mi_set)



#nos muestra la cantidad de elementos dedntro
mi_set = set([1,2,3,4,5,6])
print(len(mi_set))


#tambien podemos consultar si un elemnto esta dentro de nuestro set dandonos respuesta true o false
mi_set = set([1,2,3,4,5,6])
print(2 in mi_set)



mi_set = set([1,2,3,4,5,6])
print(7 in mi_set)


#hacer union de set, y aca tambien vemos que como 3 se repite lo elimina

a1 = {1,2,3}
b2 = {3,4,5}
c3 = a1.union(b2)
print(c3)



#con add podemos agregar un elemento al set
s1 = {1,2,3}
s1.add(4)
print(s1)




#remove sirve para eliminar un elemento,(si le damos un elemento que no existe, nos da error)
s1 = {1,2,3}
s1.remove(3)
print(s1)



#discard nos permite descartar un elemento (no eliminar), por tanto si el mismo no esta, no nos devuelve error
s1 = {1,2,3}
s1.discard(6)
print(s1)



#pop nos elimina un elemento al asar si no se le especifica parametro (podria usarce para un sorteo)
s1 = {1,2,3}
s1.pop()
print(s1)



#clear sirve para borrar o limpiar todo el set, dejandonos sin nada
s1 = {1,2,3}
s1.clear()
print(s1)



#practicas


mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)



sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo.pop())


sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")
print(sorteo)






#booleanos, le podemos definir en variable true o falso, (o al hacer una comparativa, o si se cumple o no una condicion o calculo lo resuelve solo si es true o false)muy usado en inteligencia artificial


var1 = True
var2 = False
print(type(var1))
print(var1)


#aca sin declarar flase ni true, lo resuelve solo, por si cumple la condicion que le dimos, al no cumplirse nos da false
numero = 5 > 2+3
print(type(numero))
print(numero)


# == comparacion de igualdad, por tanto enb seste ej. dara true (esto es igual a esto?)
numero = 5 == 2+3
print(type(numero))
print(numero)



# >= mayor o igual a tal valor, en este caso es igual asi que dara true
numero = 5 == 2+3
print(type(numero))
print(numero)



#. != nos permite decir que si ambos valores son diferentes, por ende nos dara false 
numero = 5 != 2+3
print(type(numero))
print(numero)



#esta es otra forma con la que se lo puede expresar, es igual (si no ponemos valor dentro del parentesis, nos dara falso)
numero = bool(5 != 2+3)
print(type(numero))
print(numero)


#aca decimo en una lista, que 5 esta en ella, por ende nos devuelve false
lista = [1,2,3,4]
control = 5 in lista
print(type(control))
print(control)



#aca decimos que 5 no esta en lista, por tanto nos devuelve true por que no lo esta
lista = [1,2,3,4]
control = 5 not in lista
print(type(control))
print(control)



#practicas 



prueba = 5 == 6
print(type(prueba))
print(prueba)


prueba = 17834/34 > 87*56
print(prueba)


prueba = 25*25 == 5
print(prueba)
```
````
