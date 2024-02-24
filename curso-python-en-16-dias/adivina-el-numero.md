# 😀 ADIVINA EL NUMERO

````python
// Some code

```python
#programa adivina el numero
print("(((ADIVINA MI NUMERO)))")
#su nombre?
usuario = (input("Porfavor registrate solo con tu NOMBRE o APODO: "))


#progama dice e pensado un numero entre el 1 y el 100 y tienes solo 8 intentos para adivinar
print(f"Bienvenido {usuario}, muchas gracias por jugar con migo :)\nA continuacion pensare un NUMERO del ((1 al 100)) y trataras de adivinarlo, para lo cual tendras 8 INTENTOS!!!\n((tranquilo te ayudare un poco))")

from random import *
adivina_elnumero = [randint(1,100)]


#ingresa el numero elejido por el jugador:
#numero_usuario = int(input(f"DIME TU NUMERO {usuario} a ver aciertas: "))
#por cada intento el programa debe poder dar cuatro opciones de respuestas y hasta que no acierte seguira repitiendo el ciclo bucle, hasta que gane o se acaben los 8 intentos.
#opcion 1 : si el numero elegido por el usuario es imferior a 1 o superior a 100.(osea fuera de parametro dado)
#opcion 2 : has elegido un numero menor al que pense.
#opcion 3 : has elegido un numero mayor al que pense.
#opcion 4 : has !!!GANADO!!! acertaste al numero que pense. Te FELICITO lo lograste en 0 intentos!!!

veces = 8

while veces > 0:
    numero_usuario = int(input(f"DIME TU NUMERO {usuario} a ver aciertas: "))
    veces = veces - 1
    oportunidades = 8 - veces
    if veces == 0:
        print(f"Terminaste tus 8 oportunidades para adivinar mi numero..El numero era ({adivina_elnumero}), Lo siento {usuario}jaja 8P")
        break
    for num in adivina_elnumero:
        if num == numero_usuario:
            veces = veces - veces
            print(f"BIEN {usuario} has !!!GANADO!!! acertaste al numero que pense: (({adivina_elnumero})). Te FELICITO lo lograste en {oportunidades} intentos!!!")
            break
        elif numero_usuario<1 or numero_usuario>100:
            print("Su numero esta fuera del parametro..!!! recuerde que tiene que elejir opciones del 1 al 100..!!!")
        elif num < numero_usuario:
            print("Lo siento!!! 8D su numero es mayor al que pense ")
        elif num > numero_usuario:
            print("lo siento!!! 8D su numero es menor al numero que pense ")
        
                    
```
````

CODEO DEL DIA 4:

````python
// Some code

```python
'''
OPERADORES DE COMPARACION
-mayor           >
-menor           <
-mayor o igual   >=
-menor o igual   <=
-igual           ==
-diferente       !=
'''


# con las comparaciones se optienen valores booleanos

var_true = 10>=8
print(var_true)


var_igual = 10==25
print(var_igual)


# se pueden comparar la sumas de operaciones matematicas apartes
var_igual = 10*10==25*4
print(var_igual)



#tambien se puede comparar string y la misma es sencible a las mayusculas
var_igual = "gordo"=="flaco"
print(var_igual)



var_igual = "gordo"=="gordo"
print(var_igual)



var_igual = "gordo"=="Gordo"
print(var_igual)


#si usamos  el metodo .lower que sirve para transformar en minuscula, nos da true
var_igual = "gordo"=="Gordo".lower()
print(var_igual)


#identifica que no es lo mismo un string que un numero interger y da falso qe no es igual
var_igual = "100"==100
print(var_igual)


# da true aunque uno sea float y el otro inter , pero el valor del numero entero sigue siendo 100, no en el siguiente ejemplo
var_igual = 100.0==100
print(var_igual)


var_igual = 100.5==100
print(var_igual)



#no da false por que son iguales, no son diferentes como afirma la comparativa
var_diferente = 100!=100
print(var_diferente)


#aca por ende si son diferente, osea que la comparativa nos va a dar la razon devolviendonos true
var_diferente = 100!=99
print(var_diferente)



var_diferente = 100!=99
print(var_diferente)



var_mayoromenor = 100>99
print(var_mayoromenor)


var_mayoromenor = 100<99
print(var_mayoromenor)


var_mayoroigual = 100>=99
print(var_mayoroigual)



var_mayoroigual = 100>=100
print(var_mayoroigual)


#practicas


num1 = 36
num2 = 17
mi_bool = num1>=num2
print(mi_bool)



num1 = 25*25
num2 = 5 
mi_bool = num1==num2
print(mi_bool)



num1 = 64*3
num2 = 24*8 
mi_bool = num1!=num2
print(mi_bool)




#operadores logicos  ( Y-and   O-or   NO-not  )


#tratando de hacer dos comparativas juntas a la ves 
'''
4 < 5
5 < 6
'''


#se puede legar a ser asi pero no siempre va a funcioinar bien 
mi_bool = 4 < 5 <6
print(mi_bool)


#trabaja por valores booleanos y luego los compara, por ende aca da true y false = false por q no son iguales, y no se cumple que los dos valores bool sean iguales
mi_bool = 4 < 5 and 5 > 6
print(mi_bool)



#y en este caso da true y true por tanto es igual a true por que si son las dos iguales
mi_bool = 4 < 5 and 5 == 2+3
print(mi_bool)


# en este caso las dos son false y por ende nos devuelve false
mi_bool = 6 < 5 and 5 == 2+4
print(mi_bool)



#se pueden comparar distintos tipòs de datos, para los string da error con comillas dobles, por ende usar simples
mi_bool = (55 == 55) and 'perro' == 'perro'
print(mi_bool)


#            true     +         true         = true
mi_bool = (55 == 55) and 'perro' == 'perro'
print(mi_bool)



#           true     +      true       = true    
mi_bool = (55 == 55) and 3 == 3
print(mi_bool)



# or nos comppara ambos valores y con que uno de ellos se cumpla, nos da verdadero osea true
#           true    +     true    = true
mi_bool = (55 == 55) or 3 == 3
print(mi_bool)



#            true     +     false   =  true
mi_bool = (55 == 55) or 3 == 6
print(mi_bool)


#            false   +   false   =  false
mi_bool = (55 == 56) or 3 == 6
print(mi_bool)



#
texto = "hola mundo como estan"
mi_bool = "frase" in texto
print(mi_bool)



# usando AND tiene que cumplirse los dos valores, si solo se cumple uno, nos da false
#                 false       +     true          =  false
texto = "hola mundo como estan"
mi_bool = ("frase" in texto) and ("hola" in texto)
print(mi_bool)



# usando OR tiene que cumplirse solo alguno de los dos valores, y al cumplirse solo uno, nos daria true
#                 false       +     true          =  false
texto = "hola mundo como estan"
mi_bool = ("frase" in texto) or ("hola" in texto)
print(mi_bool)




# NOT aca negamos que la comparacion sea correcta. en este caso la comparacion es true y como dijimos q no lo era, nos devuelve que lo que dijimos con NOT es falso
#   no es igual!  true    =  false
mi_bool = not "a" == "a"
print(mi_bool)





# NOT aca negamos que la comparacion sea correcta. en este caso la comparacion es falso y como dijimos q no lo era, nos devuelve que lo que dijimos con NOT es true
#   no es igual!  false    =  true
mi_bool = not "a" != "a"
print(mi_bool)




#practicas 


num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 and num1 < num3
print(mi_bool)




num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3
print(mi_bool)





frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
mi_bool = not palabra1 in frase or palabra2 in frase 
print(mi_bool)



# control de flujos  (if = si ocurre tal cosa     elif=si no ocurre tal cosa que ocurra otra opcion   else= si no se cumple)

if 10 > 9:
    print("es correcto")
    


#no imprime nada si no se cumpre if, debemos darle otra opcion con elif o else
if 10 > 11:
    print("es correcto")
    
    
    
if 10 > 11:
    print("es correcto")    
else:
    print("no es correcto") 
    


#haciendo comparativas con string    
raza = "doverman"
if raza == "doverman":
    print("si es la misma raza de perro")
else:
    print("no es la misma raza")  
    
    
    
raza = "doverman"
if raza == "dogo":
    print("si es la misma raza de perro")
else:
    print("no es la misma raza")       
       



# en este caso usamos una opsion mas con elif, que si es correcta se mostrara el mensaje
raza = "doverman"
if raza == "dogo":
    print("si es la misma raza de perro")
elif raza == "rottwailer":
    print("si esa raza tambien esta en nuestra base de datos")
else:
    print("no es la misma raza") 
    
    
    

raza = "rottwailer"
if raza == "dogo":
    print("si es la misma raza de perro")
elif raza == "rottwailer":
    print("si esa raza tambien esta en nuestra base de datos")
else:
    print("no es la misma raza")    
    
    
    
raza = "pastor"
if raza == "dogo"or"galgo"or"pastor":
    print("si es la misma raza de perro")
elif raza == "rottwailer":
    print("si esa raza tambien esta en nuestra base de datos")
else:
    print("no es la misma raza")    
    


#vemos como podemos entrar y anidar dos if dentro de otro para que el arbol se ramifique para esas respuestas o no y siga a else y termine
edad = 16
calificacion = 9
if edad < 18:
    print("eres menor de edad")
    if calificacion >= 7:
        print("aprobado")
    else:
        print("no aprobaste")
else:
    print("eres adulto")  
    



#practicas


num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:    
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")     
    
       




edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia != tiene_licencia:
    print("Puedes conducir")
elif edad < 18 and tiene_licencia == tiene_licencia:    
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif edad >=18 and tiene_licencia == tiene_licencia:
    print("No puedes conducir. Necesitas contar con una licencia")
    
    
    



habla_ingles = True
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte")
elif habla_ingles == False and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif habla_ingles == False and sabe_python == True:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")








#loops (bucle) los hay que se repiten cantidsad de veses definidas (loop FOR) y los de manera infinita o no definida (while)



#LOOB FOR 

nombres = ["pedro","juan","jose","marcos"] 
for elementos in nombres:                   # le decimos FOR que por cada + ELEMENTOS (es una variable interna que le podriamos poner cualquier nombre, y significa los elementos de una lista,etc)+ que estan IN + el nombre de la lista NOMBRES
    print("hola como estas "+elementos)     # itinere entre cada elementos que le dijimos y los imprima + sumandole el string que le pusimos al principio






nombres = ["pedro","juan","jose","marcos"] 
for p in nombres:                   # le decimos FOR que por cada + ELEMENTOS (es una variable interna que le podriamos poner cualquier nombre, y significa los elementos de una lista,etc)+ que estan IN + el nombre de la lista NOMBRES
    print("hola como estas "+p)




lista = ["a","b","c","d","e","f","g"]
for element in lista:                      # le decimos FOR que por cada + ELEMENT (es una variable interna que le podriamos poner cualquier nombre, y significa los elementos de una lista,etc)+ que estan en IN + el nombre de la lista LISTA
    numero_letra = lista.index(element)+1  # que al momento de itinerar entre ellos, vea el INDEX osea indice + de cada elemento (ELEMENT) + y le sume 1 (en este caso para poder imprimir la primer letra, y no empiese contando desde posicion 0)
    print(f"En la pocision numero: {numero_letra} se encuentra la letra: {element}")   #le damos formato a la respuesta e incluimos las variables para que quede bien presentable y claro





lista = ["arbol","barco","coche","delfin","elefante","foca","gato"]
for element in lista:
    numero_letra = lista.index(element)+1
    print(f"En la pocision numero: {numero_letra} se encuentra la letra: {element}")





# aca le sumamos que itinere con una condicion de IF buscando entre los elementos palabras que empiesen con c, si la condicion se da la imprimira
lista = ["arbol","barco","coche","delfin","elefante","foca","gato"]
for element in lista:
    if element.startswith("c"):
        print(element)
    



#aca itineramos entre los numeros de la lista, pero vemos la importaancia de la tabulacionm, en este caso del print que esta dentro del for, pero en el siguiente ejemplo el mismo esta fuera sin tabulacion y vemos como cambia
numeros = [1,2,3,4,5,6]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
    
    
    
#como print esta fuera del for, en ves de darnos todos los pasos imprimidos, solo arroja el resultado final del FOR    
numeros = [1,2,3,4,5,6]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)    





#en un string tambien podemos itinerar entre cada una de la sletras que componen el string

palabra = "caballeros"
for letras in palabra:
    print(letras)




for letras in "caballeros del zodiaco":
    print(letras)




#podemos iterar con una lista que tenga listas dentro tambien

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)



#podemos imprimir por cada objeto en una lista por separados, asignandoles dos variables, e impimiendolas por separado
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)
    
    
    
    
    
    
    
#si usamos el FOR para itinerar en un diccionario, nos imprime solo las claves a no ser de hacerlo de otra forma    
dic = {"llave1":"a","llave2":"b","llave3":"c"}   
for item in dic:
    print(item) 
    




dic = {"llave1":"a","llave2":"b","llave3":"c"}   
for item in dic.items():
    print(item)    
    


dic = {"llave1":"a","llave2":"b","llave3":"c"}   
for a,b in dic.items():
    print(a,b)    
    
    
    




#practicas
 
 
 
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for alumnos in alumnos_clase:
    print(f"Hola {alumnos}") 
 
 
 
 
 
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numeros in lista_numeros:
    suma_numeros = suma_numeros + numeros 
    print(suma_numeros)   
    
    
    
      
    
    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for num in lista_numeros:                 #para FOR + los items NUM + en mi IN + LISTA_NUMEROS (itinerar entre cada uno de ellos con las siguientes reglas)
    if num % 2 == 0:                      # si IF + los items NUM divididos resto % por 2 es igual == a cero 0 de cada numero itinerado con resultado en cero de resto, por q seria par, hacer lo siguiente si se cumple esta condicion
        suma_pares = suma_pares + num     # en la variable SUMA_PARES meter el resultado de = SUMA_PARES que vale 0 + el items NUM que anteriormente fueron igual a cero 0 en la divivion de resto (por ende sumariamos todos los pares dentro de esa variable)
    else:
        suma_impares = suma_impares + num # con ELSE le decimos si no se cumple la anterior condicion, venir con esta y dejar el resto de los numeros que dio igaul a 1 osea impares, y realizar esta operacion itinerandolos 
print(f"La suma de todos los numeros pares es: {suma_pares} y la suma de todos los numeros impares es: {suma_impares}")        
    
    
    
    
    


# loop WHILE (mientras) osea el bucle se repite mientras cumpla una condicion que le demos
    
    
    
    
monedas = 5
while monedas > 0:                    #la condicion dice que se hara un bucle infinito hasta que no se de mas la condicion(de que monedas deje de ser mayor que 0)
    print(f"tengo {monedas} monedas")
    monedas = monedas - 1             #si no ponemos un freno o algo que corte con esa condicion, lo ejecutara infinitamente hasta agotar la memoria y habra que reiniciar, por tanto pusimos que por cada ves que se daba la condicion nos descuente una moneda asi hasta llegar a 0 parara 
else:print("No tengo mas monedas")    
    





respuesta = "s"
while respuesta == "s":
    respuesta = input("quieres seguir? s/n")
else:
    print("gracias")




nombre = input("su nombre: ")
for letra in nombre:
    if letra == "r":          # declaramos en break que si en input ingresan un nombre q contenga R el siclo o bucle parara
        break
    print(letra)






nombre = input("su nombre: ")
for letra in nombre:
    if letra == "r":          # declaramos en continue que si en input ingresan un nombre q contenga R el siclo o bucle volvera a iniciarce desde el FOR
        continue
    print(letra)



#practica



numero = 10
while numero > -1:
    print(numero)
    numero = numero - 1
    




numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(numero)
        numero = numero -1
    else:
        numero = numero -1




lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for num in lista_numeros:
    if num >= 0:
        print(num)
    else:
        break




# range (rango)


#forma vieja de hacerlo
lista = [1,2,3,4,5]
for num in lista:
    print(num)




#para NUMERO en el rango hasta el 5, imprimirlos(se frena y imprime hasta antes del numero que ele dimos de rango)
for numero in range(5):
    print(numero)




#podemos estableser en el parentesis desde y hasta que rango, y hasta un tercer oparametro para indicar cada cuanto saltear, y no recibe float
for numero in range(1,5):
    print(numero)




# de esta forma creamos una lista de forma mas rapida
lista = list(range(1,101))
print(lista)





#practicas


mi_lista = list(range(2500,2586))


mi_lista = list(range(3,303,3))


suma_cuadrados = 0
for num in range(1,16):
    suma_cuadrados = suma_cuadrados + num**2
    print(suma_cuadrados)





#enumerador


#enumerar de la forma rebucada, no con enumerador
lista = ["a","b","c"]
indice = 0 
for item in lista:
    print(indice,item)
    indice = indice + 1
    
    

#usando enumerador con una variable temporal ITEM
lista = ["a","b","c"]    
for item in enumerate(lista):      #como que transformamos la lista en una enumerada directamente
    print(item)






#usando enumerador con dos variables temporales INDICE,ITEM   
lista = ["a","b","c"]    
for indice,item in enumerate(lista):      #como que transformamos la lista en una enumerada directamente
    print(indice,item)
    
    
    


lista = ["a","b","c"]    
for indice,item in enumerate(lista):      #como que transformamos la lista en una enumerada directamente
    contenido_indice = indice,item
    print(contenido_indice)  
    
      
    
    
    
    
#podemos enumerar directamente en una lista creada con range.    
for indice,item in enumerate(range(50,55)):
    print(indice,item)
    
    




lista = ["a","b","c"]    
for indice,item in enumerate(lista):      #como que transformamos la lista en una enumerada directamente
    contenido_indice = indice,item
    print(contenido_indice)    




#podemos enumerar elementos dentro de una lista de tuplas, haciendo un casting con LIST
lista = ["a","b","c"]    
mis_tuples = list(enumerate(lista))
print(mis_tuples)




#de esta forma podemos extraer la tupla numero 1 [1] que seria (1,"b"), y le indicamos seguido que de ahi nos extraiga lo que tenga en el indice 0 por ende nos devuelve 1 
lista = ["a","b","c"]    
mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])





#practicas


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')



#otraopcion del primero
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indices,nombres in enumerate(lista_nombres):
    indice = indices
    nombre = nombres
    print(f'{nombre} se encuentra en el índice {indice}')






palabra = "Python"
lista_indices = list(enumerate(palabra)) 
print(lista_indices)   




lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice_m, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(indice_m)





# funcion ZIP (combina y une dos o mas listas entrelasando sus elementos en tuplas)





lista_nombres = ["Marcos", "Laura", "Mónica"]
edades = [23,45,65]
combinados = list(zip(lista_nombres,edades))  #si no le hacemos casting con LIST para ponerlos en una lista, nos dara error. (los une hasta combinar la cantidad de elementos mas corta que tenga uno o otra lista, a los demas que sobran y no los puede combinar , los ignora directamente.)
print(combinados)






#se pueden combinar mas de dos listas
lista_nombres = ["Marcos", "Laura", "Mónica"]
edades = [23,45,65]
paises = ["argentina","brasil","colombia"]
combinados = list(zip(lista_nombres,edades,paises))  #si no le hacemos casting con LIST para ponerlos en una lista, nos dara error. (los une hasta combinar la cantidad de elementos mas corta que tenga uno o otra lista, a los demas que sobran y no los puede combinar , los ignora directamente.)
print(combinados)




#podemos hacer cosas muy buenas combinandolo con loop como FOR en este caso 
lista_nombres = ["Marcos", "Laura", "Mónica"]
edades = [23,45,65]
paises = ["argentina","brasil","colombia"]
combinados = list(zip(lista_nombres,edades,paises))  #si no le hacemos casting con LIST para ponerlos en una lista, nos dara error. (los une hasta combinar la cantidad de elementos mas corta que tenga uno o otra lista, a los demas que sobran y no los puede combinar , los ignora directamente.)
for lista_nombre,edades,paises in combinados:
    print(f"{nombre} tiene {edad} de edad, y vive en {paises}")




#practicas


capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados = list(zip(capitales,paises))
for capitales,paises in combinados:
    print(f"La capital de {paises} es {capitales}")




marcas = ["fanta","pepsy","pritty","narampol"]
productos = ["gaceosa de naranja","gaseosa de cola","gaseosa de limon","gaseosa de pomelo"]
mi_zip = zip(marcas,productos)
print(mi_zip)



español = ["uno","dos","tres","cuatro","cinco"]
portugues = ["um","dois","três","quatro","cinco"]
ingles = ["one","two","three","four","five"]
numeros = list(zip(español,portugues,ingles))
print(numeros)







# MIN  y MAX (nos detecta el valor maximo o minimo de un numero int o de string texto)



menor = min(234,45,564,76,87,65,87)
mayor = max(323,43,45,656,456,54,435)
print(menor)
print(mayor)


#podemos llamar tambien a la funcioin en el print
lista = [234,45,564,76,87,65,87]
print(min(lista))


#podemos hacer varios llamados de min y max a la ves
lista = [234,45,564,76,87,65,87]
print(f"el menor de la lista es {min(lista)} y el mayor de la lista es {max(lista)}")






# busca alfabeticamente , pero tener en cuenta que primero busca en las letras mayusculas y luego minusculas
nombres = ["berlín", "tokio", "parís", "helsinki", "ottawa", "canberra"]
print(min(nombres))



nombres = ["berlín", "tokio", "parís", "helsinki", "ottawa", "Canberra"]
print(min(nombres))



nombre = "ruperta"
print(min(nombre))


nombre = "rupErta"
print(min(nombre))


#a no ser que la transformemos en minuscula usando .LOWER
nombre = "rupErta"
print(min(nombre.lower()))



  
#en este caso nos toma la llave y verifica eso del diccionario de forma alfabetica, a no ser que le definamos con .VALUES para que busque el minimo ded los valores  
dic = {"c1":50,"C2":60} 
print(min(dic)) 
  
  
  
dic = {"c1":50,"C2":60} 
print(min(dic.values()))  
  
  
#practicas 


lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
print(max(lista_numeros)) 
  
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)





lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
max_num = max(lista_numeros)
min_num = min(lista_numeros)
rango = max_num - min_num
print(rango)
  
  
  
  
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(edad_minima," ",ultimo_nombre)  






#randint (random) se deben importar los metodos de una libreria random ( otros mas: uniform,random,choise) (importante : el nombre del archivo nunca debe ser igual a la libreria que importamos)



#desde FROM + libreria RANDOM + llevar IMPORT + RANDINT (control + espace nos muestra opciones a importar)
from random import randint
aleatorio = randint(1,50)       #con RANDIN nos arroja numeros random
print(aleatorio)                #nos arroja cada ves un numero random, en el rango de numero que le dimos del 1 al 50 en este caso
  
  
  

from random import randint
aleatorio = randint(1,1000)
print(aleatorio)




# usando el * indicamos que de la libreria RANDOM nos importe TODO su contenido, para no llamarlo uno por uno
from random import *
aleatorio = uniform(1,10)   # con UNIFORM nos arroja numero random, con decimales largos, pero con ROUND se puede arreglar si se quiere   
print(aleatorio) 
  
  
  
  
from random import *
aleatorio = round(uniform(1,10),2)    #aca con ROUND redondeamos y al final con ,2 le decimos que solo muestre dos decimales
print(aleatorio)  
  
  




#RANDOM nos elige random sin ningun parametro entre 0 y 1 , hasta numeros con decimales
from random import *
aleatorio = random()   
print(aleatorio)





#CHOISE este nos permite trabajar con una seleccion aleatoria dentro de una lista (para sorteo va genial :))
from random import *
ganador = ["carlos","pedro","raul","demian"]
aleatorio = choice(ganador)   
print(aleatorio)




#SHUFFLE lo que hace es mesclarnos los elementos de una lista ya hecha, o creada como en este caso. (ideal par un juegom de cartas, y mesclar las cartas)
from random import *
numeros_ganadores = list(range(5,50,5))
print(numeros_ganadores)
shuffle(numeros_ganadores)    # genera una modificacion en el lugar, por ende no se la puede guardar en una variabble
print(numeros_ganadores)






#practica 



from random import *
aleatorio = randint(1,11)
print(aleatorio)




from random import *
aleatorio = random()
print(aleatorio)




from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)





#comprension de listas (seria para comprimir codigo, y mejor comprension del mismo)

#normal
palabra = "python"
lista = []              #que abajo .APPEND agrega las letras aca en LISTA 
for letra in palabra:   #para LETRAS + IN + PALABRA 
    lista.append(letra) #le agregamos a LISTA con .APPEND una LETRA 
print(lista)    


#comprimido
palabra = "python"
lista = [letra for letra in palabra] #indicamos q a variable LISTA = agregue + una LETRA + por FOR + cada LETRA + que esta en nuestra variable PALABRA (las variables temporales LETRAS se podrian llamar como siempre de cualquier forma)
print(lista)



palabra = "python"
lista = [xx for xx in palabra] #indicamos q a variable LISTA = agregue + una LETRA + por FOR + cada LETRA + que esta en nuestra variable PALABRA (las variables temporales LETRAS se podrian llamar como siempre de cualquier forma)
print(lista)




#todavia mas comprimido y mejor comprension
lista = [xx for xx in "python"] #indicamos q a variable LISTA = agregue + una XX + por FOR + cada XX + que esta en string "python" y en ves de cargarlo en variable lo ponemos ahi dentro directamente (las variables temporales LETRAS se podrian llamar como siempre de cualquier forma)
print(lista)



#tambien podemos crear una lista numerica con RANGE dentro del for para q itinere
lista = [n for n in range(1,100)]
print(lista)



#que por cada numero que alla en nuestra lista creada en ese rango, cada numero sea dividido por 2
lista = [n/2 for n in range(1,100)]
print(lista)



#aca tal cual al anterior, pero le ponemos una condicion con IF que solo hagregue a los numeros de la LISTA que al multiplicarlos por dos, sean mayor que 30
lista = [n for n in range(1,100) if n*2 >30]
print(lista)



#podemos agregar otro parametrto mas como ELSE pero ahi que agregarlo desde el IF antes del FOR, al comprimir mas el codigo, ganamos digamos alivianar las lineas de comando, pero empeoramos la comprension o legibilidad nuestra
lista = [n if n*2 >30 else "no" for n in range(1,100)]
print(lista)



#en este caso transformamos pies en metros con *3.281 (valor en mtrs) en un codigo comprimido en una sola linea, pero perdemos poco de legibilidad
pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]
print(metros)



#practicas


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n*n for n in valores]
print(valores_cuadrado)




valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores if n%2==0]
print(valores_pares)



temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grados-32)*(5/9) for grados in temperatura_fahrenheit]
print(grados_celsius)






#MATCH a partir de de python 3.10


#antes
serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("No existe en la base de datos")
    
                




#usando MATCH (coinsidencia) y en el caso CASE que coincida con ""
series = "N-03"

match series:
    case"N-01":
        print("Samsung")
    case"N-02":
        print("Nokia")
    case"N-03":
        print("Motorola")
    case _:
        print("No existe en la base de datos")

  





#otro ejemplo mas complejo usando MATCH (que nos permite detectar muchos patrones)

cliente = {"nombre":"Federico","edad":45,"ocupacion":"instructor"}
pelicula = {"titulo":"matrix","ficha_tecnica":{"protagonista":"keanu reeves","director":"lana y lilly wachowski"}}


elementos = [cliente, pelicula, "libro"]

for e in elementos:
    match e:
        case {"nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("Es un cliente registrado")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo,"ficha_tecnica": {"protagonista": protagonista,
                                                "director": director}}:    
            print("es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("no se encuentra elemento")    




#fin , vamos al proyecto



```
````
