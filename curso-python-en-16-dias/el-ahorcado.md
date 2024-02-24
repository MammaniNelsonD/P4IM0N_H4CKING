# 😀 EL AHORCADO

````python
// Some code

```python
#! EL AHORCADO

#importamos la libreria para usar CHOISE para elegir una palabara random de nuestra lista
from random import choice                  

palabras = ["chocolatada", "laberinto", "estacionamiento", "ferrari", "preparador", "microprocesador", "computadora", "kickboxing", "ninjutzu", "beretta"]
letras_correctas = []                            #?lista vacia para las letras correctas
letras_incorrectas = []                          #?lista vacia par las letras incorrectas    
intentos = 7                                     #?vidas del jugaror
acertados = 0                                    #?conteo de aciertos
juego_terminado = False                          #?variable para luego terminar el juego




#funcion 1 para que el sistema elija una palabra al azar de nuestra lista
def elige_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)              #?con CHOICE nos saca una palabra al azar de nuestra lista que le pasamos
    letras_unicas = len(set(palabra_elegida))             #?le ponemos un SET para que de nuestra palabra elegida quede con sus letras unicas sin repetirse y con LEN contamos la cantidad de caracteres

    return palabra_elegida, letras_unicas                 #?nos retorna dos datos la palabra al azar + la cantidad de letras sin repetirse en la palabra





#funcion 2 para pedir una letra al usuario y que detecte si el usuario ingreso otro parametro no admitido
def ingresa_letra():
    letra_elegida = ''                                                  #?creamos una variable de tipo string vacia, para solo admitir string          
    valida = False                                                      #?variable para validar a posterior si la entrada del usuario esta admitida o no 
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'                          #?creamos un abecedario completo para comprobar si la letra ingresada por el usuario esta aca, si se la admite

    while not valida:                                                   #?creamos un loop (que mientras no se cumpla como verdadero se va a repetir), para que se repita hasta que el usuario ingrese una letra o caracter valido para el juego
        letra_elegida = input(f"{usuario} elige una letra: ").lower()              #?variable de input de ingreso de la letra elegida por el usuario y con lower hacemos que transforme en minuscula el ingreso, para que no se complique luego para buscar coincidencia
        if letra_elegida in abecedario and len(letra_elegida) == 1:     #?condicion si esa letra elegida se encuentra en nuestro abecedario, pero tambien si su extencion es igual a 1 un caracter ADMITIRLO para lo siguiente
            valida = True                                               #?darlo como ingreso valido al cumplir esas do condiciones
        else:                                                           #?si no
            print(f"No has elegido una letra correcta {usuario}")                  #?imprimir parametro invalido

    return letra_elegida                                                #?asi esta funcion nos entrega una letra osea un caracter valido para que no nos proboque error a posterio






#funcion 3 que mostrara la palabra que se va formando o no, comparandola con la elegida por el sistema CHOISE
def mostrar_palabra(palabra_elegida):                #?consume el resultado de la funcion 1

    lista_oculta = []                                #?lista vacia donde al itinerar por las letras de la palabra elegida las va a colocar dentro de esta lista

    for l in palabra_elegida:                        #?itinerar por cada letra in la palabra elegida
        if l in letras_correctas:                    #?quiero que te fijes si por cada letra de la palabra elejida encuentras añlguna coincidencia con las letras correctas ingresadas por el usuario y a posterior hacer lo siguiente si es asi
            lista_oculta.append(l)                   #?agrega la letra a la palabra oculta
        else:                                        #?si no hacer lo siguiente 
            lista_oculta.append(' _ ')               #?agrega el _ a la palabra oculta cifrada

    print(' '.join(lista_oculta))                    #?imprime la lista oculta donde guardamos los caracteres itinerados, usando JOIN lo hace con un espacio entre medio de cada caracter ingresado






#funcion 4 para controlar si la letra del usuario se coincide o no, y al hacer esto va a agregar a las listas variables las letras que fueron correctas y las incorrectas, tambien debe ver e ir descontando las vidas del jugador
def controlar_letra(letra_elegida, lista_oculta, vidas, acertados):           #?se alimenta con 4 cuatro parametros, el resultado de la funcion 2, + funcion 3 lista oculta + variable intentos + la variable acertados

    fin = False                                                               #?variable false para determinar a posterior cuando sea true

    if letra_elegida in lista_oculta:                                         #?damos la condicion si la letra elegida se encuentra dentro de la lista oculta hacer los siguiente  
        letras_correctas.append(letra_elegida)                                #?agregar a la variable letra correcta la letra que coincidio con lista oculta
        acertados += 1                                                        #?y a la variable acertados agregarle por cada acierto una suma de 1 acirto mas
    else:
        letras_incorrectas.append(letra_elegida)                              #?si no coincidio, agregar la letra ingresada a la lista de letras incorrectas y...
        vidas -= 1                                                            #?restar 1 a la variable vidas que arranca en 7

    if vidas == 0:                                                            #?luego vera la condicion de si las vidas del usuario llegaron a cero
        fin = perder()                                                        #?aqui el valo de la variable fin pasa a valer true, pero la invocamos con la funcion perder() que nos da mas propiedades para darle a posterior
    elif acertados == letras_unicas:                                          #?aqui vemos si el numero de aciertos es igual a la cantidad len de letras unicas de la funcion 1
        fin = ganar(lista_oculta)                                             #?aca la variable fin va a pasar a valer true, y le damos dentro un metodo llamado gana() para darle a posterior mas parametros

    return vidas, fin, acertados                                              #?nos va a devolver las vidas que le quedan a l usuario, la variable fin si sigue en false o paso a valer true si es que coincidio alguna condicion, y los aciertos  






#funcion 5 que devuelva al perder respuestas al usuario sobre que perdio todas sus vidas y cual era la palabra o lista oculta
def perder():
    print(f"Te quedaste sin vidas manito {usuario}")
    print("La palabra oculta era " + palabra)

    return True                                                                #?nos devuelve true para cambiar la variable fin a posterior






#funcion 6 que se activara si el jugador gana, con un parametro 
def ganar(palabra_descubierta):
    mostrar_palabra(palabra_descubierta)                                        #?invocamos en el la funcioin 3 de mostrar palabra
    print(f"Felicitaciones {usuario}, has encontrado la maldita palabra!!!:)")                       #?imprimimos un saludo al ganador

    return True                                                                 #?cambiamos el valor de la variable fin a true


palabra, letras_unicas = elige_palabra(palabras)                                #?ahora invoco a todas las funciones para que se alimenten entre si (primero la funcion 1 con la lista palabras y esta nos devolvia dos resultados, por lo que la almacenamos en dos variables palabra y letras unicas par usarlas a posterior)







#loop para que se reitere las funciones requeridas para solicitarle al jugador que ingrese la letra hasta perder o ganar
print("*********BIENVENIDO AL AHORCADO***********")
print("-------\n|     |\n|     O\n|    /|\\\n|     /\\\n|_________")
print("\n" + "=" * 30 + "\n")
usuario = input("Ingresa tu nombre para jugar: ")                           #?solicito un nombre para luego usarlo para ser mas personal el juego
while not juego_terminado:                                                  #?loop condicion que hasta que la variable juego terminado no pase a valer true no se detenga el loop y realize lo siguiente
    print("\n" + "=" * 30 + "\n")                                           #?detalle
    print("TU PALABRA DESCUBRIENDOCE: ")
    mostrar_palabra(palabra)                                                #?mostrara la lista oculta resultado de la funcion 3
    print("\n")
    print(f"{usuario} Tus letras incorrectas son: " + " / ".join(letras_incorrectas))  #?agrego con una barra entre medio, las letras incorrectas almacenadas en la variable
    print(f"{usuario} tus vidas restantes son: {intentos}")                           #?muestro los intentos o vidas que le quedan al jugador
    print("\n" + "=" * 30 + "\n")                                           #?detalle
    letra = ingresa_letra()                                                 #?llamamos al resultado de la funcion 2 y la meto dentro de la variable letra para luego usuarla

    intentos, terminado, acertados = controlar_letra(letra,palabra,intentos,acertados)   #?ahora hacemos uso de la funcion 4 controlar letras y le ingresamos la variable reciente letra, + seguido de la lista oculta + intentos + acertados y estos parametros dados sus resultados los guardamos en tres variables: intentos, terminado(almacenara si termina o no el juego, y aciertos para ver las vidas)

    juego_terminado = terminado                                             #?por ultimo a la variable juego terminado del principio, le damos que pase a valer lo que tien la variable terminado (que se alimenta de la variable fin, que es uno de los resultados de la funcion 4 )para definir si continua el loop o termina el juego

```
````

4 EJERCICIOS EXTRAS:

````python
// Some code

```python
#!ejercicio 1


#Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros
#Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
#Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
#Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio.



def devolver_distintos(num1,num2,num3):
    total = 0
    lista = list([num1,num2,num3])
    for num in num1,num2,num3:
        total = total + num1+num2+num3
        if total > 15:
            lista.sort()
            mayor = lista.pop(-1)
            return mayor
        elif total < 10:
            menor = lista.pop(0)
            return menor
        elif total == range(10,16):
            intermedio = lista.pop(1)
            return intermedio
        


print(devolver_distintos(4,5,3))






#!ejercicio 2


#Escribe una función (puedes ponerle cualquier nombre que
#quieras) que reciba cualquier palabra como parámetro, y que
#devuelva todas sus letras únicas (sin repetir) pero en orden alfabético.


def letra_unica_orden(palabra):
   
        ordenadas = sorted(palabra)
        unicas = set(ordenadas)
        return unicas
        
print(letra_unica_orden("caballo"))









#!ejercicio 3



#Escribe una función que requiera una cantidad indefinida de
#argumentos. Lo que hará esta función es devolver True si en
#algún momento se ha ingresado al numero cero repetido dos veces consecutivas



def doble_0(*args):
    for l in args:
        ceros = args.count(0)
        if ceros == 2:
            return True
        else:
            return False
        
    
    
print(doble_0(2,34,45,6,6,0,0,89,23))   








#!ejercicio 4




#Escribe una función llamada contar_primos() que requiera un solo argumento numérico
#Esta función va a mostrar en pantalla cuántos números
#primos hay en el rango que va desde cero hasta ese número
#incluido, y va a devolverla cantidad de números primos que encontró.



def contar_primos(numero):
   
    primos = [2]
    iteracion = 3
    
    if numero < 2:
        return 0
    
    while iteracion <= numero:
        
        for n in range(3,iteracion,2):
            
            if (iteracion % n) == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    
    print(primos)
    return len(primos)


print(contar_primos(150))     
            


```
````

CODEO DEL DIA 5:

````python
// Some code

```python
#documentacion y meetodos de como ver unformacion poniendo el mouse encima




#POPITEM nos saca el ultimo elemento agregado a un diccionario
dic = {"clave1":100,"clave2":500}
a = dic.popitem()
print(a)
print(dic)






#practicas




dic = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
a = dic.lstrip(",:_#")
print(a)
print(dic)





frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")
print(frutas)




marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)





#funciones (DEF)



#funcion DEF+nombre SALUDOS(el que querramos)+los parentesis () vacios o algun parametro que querramos, que podria servir para agregar despues.
def saludos():
     #esta funcion sirve para generar los saludos a las personas, imprimiendo el mismo cuando es invocada
    print("hola")



#de esta forma la llamamos o invocamos, dado que recien ahi va a funcionar la funcion y en este caso imprimira el saludo
saludos()





#cuando ponemos un parametro dentro de () es como que dejamos avierta una variable temporal, para luego al invocar la funcion, podamos agregar un elemento dentro del ()
def saludoss(nombre):
    print("hola "+nombre)
    
    
    
saludoss("paimon")    






def saludoss(nombre):
    print("hola "+nombre)
    
    
    
saludoss("pedro")



#practicas


def saludar():
    print("¡Hola mundo!")
    
    
    
    

nombre_persona = "Raul"
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
    
bienvenida(nombre_persona)    



un_numero = 5
def cuadrado(un_numero):
    print(un_numero*un_numero)
    
cuadrado(un_numero)    

    



#funciones con RETURN

def multiplicar(num1,num2):
    return num1*num2



#no nos devuelve nada, por que RETURN no es como el print, pero si nos permite guardarlo en una variable
multiplicar(5,5)



def multiplicar(num1,num2):    #esto seria declarar la funcion, nombre y sus parametros
    return num1*num2           #esto seria lo que hace la funcion MULTIPLICAR dos valores
resultado = multiplicar(5,5)   #aca se le ingresan dos valores que ocuparan los lugares de los parametros que le dimos y se guardan en la variable q le dimos ahora
print(resultado)               #y aca nos imprimira la variable nueva




#otra forma
def multiplicar(num1,num2):    #esto seria declarar la funcion, nombre y sus parametros
    total = num1*num2          #aca dentro de la funcion, creamos la variable que guarda dentro la MULTIPLICACION de los dos parametros de nuestra funcion
    return total               #aca le pedimos que nos retorne la variable de arriba
resultado = multiplicar(5,5)   #aca se le ingresan dos valores que ocuparan los lugares de los parametros que le dimos y se guardan en la variable q le dimos ahora
print(resultado)               #aca al final hacemos que imprima el resultado de la funcion





potencia = 3**4
print(potencia)



#practicas

def potencia(num1,num2):
    return num1**num2
resultado = potencia(3,4)
print(resultado)



def usd_a_eur(num1,num2):
    return num1*num2
dolares = usd_a_eur(5,0.90)
print(dolares)



def usd_a_eur(num1):
    num2 = 0.90
    return num1*num2
dolares = usd_a_eur(5)
print(dolares)





#revisar por que no invierte
palabra = "perro loco"
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    palabra = palabra.upper()
    return palabra
print(palabra)





#funciones dinamicas  (fucionadas con loops, if, elif, else)


#en este caso la funmcion sirve para controlar en el rango de numero especificado, si esta el numero que le ingresemos
def controlar3cifras(numero):
    return numero in range(100,1000)

resultado = controlar3cifras(740)
print(resultado)





#mismo caso, tambien le podemos ingresar el numero a buscar en una variable
def controlar3cifras(numero):
    return numero in range(100,1000)
suma = 300 + 400

resultado = controlar3cifras(suma)
print(resultado)






def controlar3cifras(lista):
    for n in lista:                  #para elementos N + en IN + lista. itinerar entre ellos
        if n in range(100,1000):     #y al itinerar entre los elementos, damos la condicion que si N (elementos) estan coincitentes dentro del RANGE de numeros de tres cifras del 100,1000... 
            return True              # nos retorne a continuacion TRUE si coincide
        else:
            pass                     # con PASS le decimos que pase y siga verificando la lista
lista = [55, 90, 1500]               # lista imput de ingreso a la funcion para ser anallizada con la misma

resultado = controlar3cifras(lista)  # aca llamamos a la funcion y le ingresamos el parametro LISTA creada para ser analizada
print(resultado)                     # no da como resultado NONE como en la lista no ahi ningun numero de tres cifras coincidente con la lista de rago de la funcion. (nos devuelve un elemento de class nonetype)









def controlar3cifras(lista):
    for n in lista:                  #para elementos N + en IN + lista. itinerar entre ellos
        if n in range(100,1000):     #y al itinerar entre los elementos, damos la condicion que si N (elementos) estan coincitentes dentro del RANGE de numeros de tres cifras del 100,1000... 
            return n              # nos retorne a continuacion el numero que coincidio en este caso
        else:
            pass                     # con PASS le decimos que pase y siga verificando la lista
lista = [555, 90, 1500]               # lista imput de ingreso a la funcion para ser anallizada con la misma

resultado = controlar3cifras(lista)  # aca llamamos a la funcion y le ingresamos el parametro LISTA creada para ser analizada
print(resultado) 









lista_vacia = []                     #creamos una variable para que nos almacene la lista de los numeros coincidentes

def controlar3cifras(lista):
    for n in lista:                  #para elementos N + en IN + lista. itinerar entre ellos
        if n in range(100,1000):     #y al itinerar entre los elementos, damos la condicion que si N (elementos) estan coincitentes dentro del RANGE de numeros de tres cifras del 100,1000... 
            lista_vacia.append(n)    # con .APPEND nos agrega los numeros coincidentes N dentros de la LISTA_VACIA
        else:
            pass                     # con PASS le decimos que pase y siga verificando la lista
    return lista_vacia               #el resultado de la funcion es que nos RETURN los que se guardo en LISTA_VACIA
lista = [555, 90, 500]               # lista imput de ingreso a la funcion para ser anallizada con la misma

resultado = controlar3cifras(lista)  # aca llamamos a la funcion y le ingresamos el parametro LISTA creada para ser analizada
print(resultado) 








# practicas



lista_numeros = [12, 34, 56, -45, 34, -7]
def todos_positivos(numeros):
    for num in numeros:
        if num < 0:
            return False
        else:
            pass
    return True        
            

resultado = todos_positivos(lista_numeros)
print(resultado)            





lista_numeros = [1, 50, 500, 5000, 750, -700]
def suma_menores(numeros):
    suma = 0
    for num in numeros:
        if num in range(1,1000):
             suma = suma + num
        else:
            pass
    return  suma    
resultado = suma_menores(lista_numeros)
print(resultado)    
    




lista_numeros = [23,56,67,89,54,78,60]         #lista de numeros pares e impares para q luego trabaje la funcion
def cantidad_pares(pares):                     #definimos la funcion, con su nombre y parametro
    cantidad=0                                 #creamos una variable Cantidad= 0, para luego ir sumandole las itineraciones o vueltas que pega el bucle sumandole a su valor +1
    for par in pares:                          #para FOR+elementos PAR itinerar entre ellos+en IN+parametro PARES
        if par%2==0:                           #damos la condicion, si IF+cada elemento dividido por dos para ver su resto y el mismo es igual a 0 PAR%2==0 realizar:
           cantidad = cantidad +1              #a la variable CANTIDAD+ guardarle cada ves que itinere o haga bucle por cada numero en la lista con la condicion que le dimos, nos sume CANTIDAD+1 y las  guarde en la variable (dandonos asi el conteo de los elementos con esas condiciones en cada vuelta de loop)
        else:                                  # y si no se da la condicion anterior ELSE
            pass                               # pasar de largo y salir de las condiciones
    return cantidad                            # para retornarnos al final de todo el loop, la variable CANTIDAD con el total de elementos pares sumados
resultado = cantidad_pares(lista_numeros)      #invocamos dentro de la variable RESULTADO a la funcion CANTIDAD_PARES, dandole en su parametro la lista LISTA_NUMEROS
print(resultado)                               #imprimimos el resultado guardado en la variable RESULTADO
        





#ejemplo de funcion  (para ver como podemos unificar muchas cosas dentro de una funcion)


#desempacamos las tuplas entreras que estan dentro de la lista 
precios_cafe = [("capuchino",1.5),("expreso",1.2),("moka",1.8)]
for elemento in precios_cafe:
    print(elemento)



#desempacamos solo el primer elemento, sin digamos el valor
precios_cafe = [("capuchino",1.5),("expreso",1.2),("moka",1.8)]
for elemento,valor in precios_cafe:
    print(elemento)



# aca por ejemplo del valor lo multiplicamos por el costo EJEMPLO 0.40 (%40) y nos da elcosto de cada tipo de cafe.
precios_cafe = [("capuchino",1.5),("expreso",1.2),("moka",1.8)]
for elemento,valor in precios_cafe:
    print(valor*0.40)
    




#una linda funcion
precios_cafe = [("capuchino",1.5),("expreso",1.2),("moka",1.8),("te",1.2),("te negro",2.8)]
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro =  ""
    for cafe,precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass    
    return (cafe_mas_caro,precio_mayor)
cafe,precio = cafe_mas_caro(precios_cafe)
print(f"El {cafe} es la bebida caliente mas cara que tenemos en el bar, su precio es de {precio}")


    




#una linda funcion (con la descripcion)
precios_cafe = [("capuchino",1.5),("expreso",1.2),("moka",1.8),("te",1.2),("te negro",2.8)]          #lista de cafes con sus precios que a posterior se la daremos a la funcion
def cafe_mas_caro(lista_precios):                                                                    #creamos la funcion DEF+llamada CAFE_MAS_CARO+parametro LISTA_PRECIOS
    precio_mayor = 0                                                                                 #creamos una variable PRECIO_MAYOR que valga cero 0 para poder ir itinerando en ella con los valores de cada cafe en la lista, para dar con el cafe mas caro
    cafe_mas_caro =  ""                                                                              #creamos una variable de tipo string pero vacia, llamada CAFE_MAS_CARO para que mientras se vallla tambien itinerando, ponga en ella el nombre string del cafe que se detecte con el precio mas caro
    for cafe,precio in precios_cafe:                                                                 #creamos el loop FOR + para itinerar por cada uno de los dos elementos por separados dentro de cada tupla, de la lista PRECIOS_CAFE, con las variables temporales CAFE, PRECIO
        if precio > precio_mayor:                                                                    #damos una condicion para detectar el cafe mas caro, le decimos: si IF + cada elemento con el valor PRECIO es mayor > a la variable PRECIO_MAYOR = 0 que arranca en 0 anteriormente definida, y en el caso de ser asi realizar lo siguiente:
            precio_mayor = precio                                                                    #a la variable PRECIO_MAYOR va a ser igual al elemento PRECIO (variable temporal) mas alto detectaco en cada itinerancia o loop que se haga de la lista sobre los precios(asi que pasara a valer ese precio)
            cafe_mas_caro = cafe                                                                     #tambien en la variable vacia de string llamada CAFE_MAS_CARO le decimos que le ingrese el texto de la variable temporal CAFE (para ir detectando tambien el nombre del cafe mas caro)
        else:                                                                                        # y si no se da esa condicion hacer lo siguiente:
            pass                                                                                     #con PASS le decimos, pasar de largo la vuelta del loop para seguir controlando todos los conjuntos de elementos de la lista y detectar si ahi otro mas caro, comparandoce a posterior con la variable PRECIO_MAYOR que va guardando cada PRECIO y viendo si es mayor al item PRCIO siguiente que sigue en la lista, (y asi terminar detectando al fin el mas caro con su nombre)
    return (cafe_mas_caro,precio_mayor)                                                              #le pedimos a la funcion que nos retorne las variables CAFE_MAS_CARO y PRECIO_MAYOR ya cargadas con el cafe mas caro al finalizar la funcion
cafe,precio = cafe_mas_caro(precios_cafe)                                                            #esos dos valores de variables anteriores, los metemos en dos variables juntas CAFE,PRECIO invocandole la FUNCION dentro de esta variable y guardando de esta forma los dos elementos por separados para a posterior trabajar con ellos de forma separada en un texto informativo
print(f"El {cafe} es la bebida caliente mas cara que tenemos en el bar, su precio es de {precio}")   #imprimimos con PRINT dandole formato con F y dentro de laas comillas coordinamos con un texto informativo, llamando a cada variable en donde corresponda





#interacciones entre funciones


#ejemplo de juego de palitos (quien saca el mas largo)
from random import shuffle


#lista inicial de palitos
palitos=["-","--","---","----"]

#mesclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#pedirle intento
def probar_suerte():
    intento = ""
    
    while intento not in ["1","2","3","4"]:
        intento = input("((Al que le toca el palito mas corto pierde)),Asi que elige un numero del 1 al 4: ")
    return int(intento)  


#comprobar intentos
def chequear_intento(lista,intento):
    if lista[intento -1] == "-":
        print("A lavar los platos, PERDISTE")
    else:
        print("te salvaste esta ves")
        
    print(f"Te ha tocado {lista[intento-1]}")         


#aca es donde invocamos a todas las tres funciones anteriores y las relacionamos entre si para que interaccionen en conjunto
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

 
 
 
 
 #practicas


#?juego arrojar DADOS (como yo lo resolvi)

#!importo librerias para random
from random import *


#!funcion que sirve para arrojar dos dados al azar y nos devuelve sus resultados valores entre 1 y 6 c/u, (sin argumentos o parametros, solo debe generar los valores aleatorios)
def lanzar_dados():
    dado1= randint(1,6)
    dado2= randint(1,6)
    return dado1,dado2
print(lanzar_dados())



#!funcion con dos parametros, que tome el resultado de la funcion LANZAR_DADOS y que la misma sirva para devolver distintas respuestas al usuario
#Si la suma es menor o igual a 6:
#"La suma de tus dados es {suma_dados}. Lamentable"
#Si la suma es mayor a 6 y menor a 10:
#"La suma de tus dados es {suma_dados}. Tienes buenas chances"
#Si la suma es mayor o igual a 10:
#"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"



def evaluar_jugadas(dados1,dados2):
    for num in dado1,dado2:
        suma_total=dado1+dado2
        if suma_total <= 6:
            print(f"La suma de tus dados es {suma_total}. Lamentable")
        elif suma_total > 6 and suma_total < 10:   
            print(f"La suma de tus dados es {suma_total}. Tienes buenas chances") 
        else:
            print(f"La suma de tus dados es {suma_total}. Parece una jugada ganadora") 
            
            
               
dado1,dado2 = lanzar_dados()
evaluar_jugadas(dado1,dado2)










#?juego arrojar DADOS (como me pedia el curso, sin encontrarle forma de que funcione)


import random
 
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)
print(lanzar_dados())
 
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"











#funciion llamada reducir_lista() con una lista como argumento, creando una variable de lista_numeros y la funcion devuelva esta lista, eliminando los numeros iguales y dejando solo uno de ellos, y eliminando el valor mas alto. 
lista_numeros = [22,34,45,21,1,2,2,60,34]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista
            
print(reducir_lista(lista_numeros))
#funcion llamada promedio() q reciba como argumento la lista devuelta por la anterior funcion y calcule el promedio de los elementos de esa lista, devolviendo el mismo sin imprimirlo


def promedio(lista):
    promedio = sum(lista)/len(lista)
    return(promedio)


          
print(reducir_lista(lista_numeros))
print(promedio(reducir_lista(lista_numeros)))










lista_numeros = [23,43,54,65,6,88,34]
#funcion 3
import random

#funcion lanzar_moneda sin argumentos, y devuelve cara o cruz
def lanzar_moneda():
    resultado = random.choice(["Cara","Cruz"])
    return resultado
print(lanzar_moneda())

#otra funcion probar_suerte que tome dos argumentos 1(el resultado de lanzar moneda) y 2(sera una lista de numeros cualquiera llamada lista_numeros)
def probar_suerte(lanzar,lista):
    if lanzar == "Cara":
        print("La lista se autodestruira ")
        return []
    elif lanzar == "Cruz":
        print("La lista fue salvada ")
        return lista
        
     
     
resultado = probar_suerte(lanzar_moneda(),lista_numeros)
print(resultado)






# Argumentos indefinidos (*args) o (*kwargs) [*args es una convencion, le podriamos poner *gato o lo que querramos.]nos permite hacer que el usuario pueda ingresar mas de dos argumentos en una funcion


def suma(a,b):
    return a+b


print(suma(5,6))



'''#nos dara error por darle mas de un parametro
def suma(a,b):
    return a+b


print(suma(5,6,8))'''




#vamos a usar *args (nos va a permitir pasar la cantidad de argumentos que querramos)
def suma(*args):
    total = 0
    for arg in args:
        total = total+arg
    return total


print(suma(5,6,7))





def suma(*args):
    total = 0
    for arg in args:
        total = total+arg
    return total


print(suma(5,6,7,600,300,10))





# funcion SUM y funcionaria igual y mas simple el codigo en este ejemplo
def suma(*args):
    return sum(args)

print(suma(5,6,7,600,300,10))




#probamos cambiar *ARGS y ponemos *PERROS y vemos que no le afecta y funciona igual, solo se recomienda usar args para facilitar la lectura
def suma(*perros):
    return sum(perros)

print(suma(5,6,7,600,300,10))






#practicas




def suma_cuadrados(*args):
    suma = 0
    for num in args:
        suma = suma+num**2
    
    return suma

print(suma_cuadrados(1,4,9))







def suma_absolutos(*args):
    absolute = 0
    for num in args:
        absolute = absolute+abs(num)
    return absolute
    
print(suma_absolutos(-20,10,20))    
        






#como lo resolvi yo igual resultado, pero no me lo toma
def numeros_persona(nombre,*args):
    suma = 0
    nombre = nombre
    for num in args:
        suma = suma+num
    print(f"{nombre}, la suma de tus números es {suma}")



numeros_persona("paimon",30,20,10)






#como lo pide 
def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f'{nombre}, la suma de tus números es {suma_numeros}'







# **KWARGS significa (key word args = palabra clave de argumento) osea para diccionario [nos permite darle un nombre o clave a cada parametro, pudiendo acceder a cada uno de ellos como un diccionario]



def suma(**kwargs):
    print(type(kwargs))
    

suma(x=3,y=5,z=2)





# aca itineramos y recorremos por las claves y sus valores dentro de kwargs y los imprimimos
def suma(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


suma(x=3,y=5,z=2)





#aca hacemos que se sumen luego sus valores y nos lo retorne para luego imprimirlos
def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total = total + valor
    return total    

print(suma(x=3,y=5,z=2))






#aca combinamos los tipos de argumentos, y van en ese orden en el caso de combinarlos
def prueba(num1,num2,*args,**kwargs):
    print(f"el primer valor es {num1}")    #aca hacemos que nos imprima el primer y el segundo valor del parametro o argumento comun
    print(f"el segundo valor es {num2}")
    for arg in args:                       #hacemos que con el FOR recorra todos los elementos o argumentos dentro de ARGS y los imprima
        print(f"arg = {arg}")
        
        
    for clave,valor in kwargs.items():     # hacemos que con el FOR recorra o itinere entre clave y valos de los valores con nombres y valor que le pasamos como un diccionario y los imprima
        print(f"{clave} = {valor}")
        
      

prueba(12,34,45,5676,675,7687,678,76,r=3,y="loco",p=23)   #en el resultado vemos como el codigo discrimina y reconoce solo los valores en sus lugares correspondientes de argumentos












#aca combinamos los tipos de argumentos, y van en ese orden en el caso de combinarlos
def prueba(num1,num2,*args,**kwargs):
    print(f"el primer valor es {num1}")    #aca hacemos que nos imprima el primer y el segundo valor del parametro o argumento comun
    print(f"el segundo valor es {num2}")
    for arg in args:                       #hacemos que con el FOR recorra todos los elementos o argumentos dentro de ARGS y los imprima
        print(f"arg = {arg}")
        
        
    for clave,valor in kwargs.items():     # hacemos que con el FOR recorra o itinere entre clave y valos de los valores con nombres y valor que le pasamos como un diccionario y los imprima
        print(f"{clave} = {valor}")
        
args = [45,5676,675,7687,678,76]           #aportandole los datos dentro de una variable como ARGS nos sirve para luego llamarla en la funcion como *ARGS y desempaquetar los valores (estos nombres tambien podrian a ver sido cualquiera gato, perro, con tal de luego al llamar la funcion los llamemos igual *PERRO)
kwargs = {"r":"3","y":"loco","p":"23"}     #aportandole los datos dentro de una variable como KWARGS nos sirve para luego llamarla en la funcion como *KWARGS y desempaquetar los valores (estos nombres tambien podrian a ver sido cualquiera gato, perro, con tal de luego al llamar la funcion los llamemos igual **PERRO)

prueba(12,34,*args,**kwargs)   #en el resultado vemos como el codigo discrimina y reconoce solo los valores en sus lugares correspondientes de argumentos, (y de esta forma funciona igual que la anterior devolviendonos lo mismo)








#practica




def cantidad_atributos(**kwargs):
    for num in kwargs:
        return len(kwargs)
    
print(cantidad_atributos(f=23,o="lol",p=8))    




#mi forma de hacerlo
def lista_atributos(**kwargs):
    for valor in kwargs:
        return [kwargs.values()]

print(lista_atributos(f=23,o="lol",p=8))






#la que me tomo el sistema
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista

print(lista_atributos(f=23,o="lol",p=8))





#como yo lo resolvi perfecto
def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}:")
    for caract,valor in kwargs.items():
        print(f"{caract}: {valor}")
        
describir_persona("paimon",color_de_ojos="verdes",color_de_pelo="castaño claro",profecion="hacking etico")        
        







#como me tomo el sistema (falla del sistema solo por el asento en caracteristicas)
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')


```

```python
import random
 
def lanzar_dados():
    return random.randint(1,6), random.randint(1,6)
print(lanzar_dados())
 
def evaluar_jugadas(dados1,dados2):
    for num in dado1,dado2:
        suma_total=dado1+dado2
        print(suma_total)
        if suma_total <= 6:
            print(f"La suma de tus dados es {suma_total}. Lamentable")
        elif suma_total > 6 and suma_total < 10:   
            print(f"La suma de tus dados es {suma_total}. Tienes buenas chances") 
        else:
            print(f"La suma de tus dados es {suma_total}. Parece una jugada ganadora") 
            
            
               
dado1,dado2 = lanzar_dados()
evaluar_jugadas(dado1,dado2)
    






lista = [3,6,8,2,6]
 
def mayor(lista):
    max = lista[0]
    for x in lista:
        if x > max:
            max = x
    return max
print(mayor(lista))







lista_numeros = [22,34,45,21,1,2,2,60,34]

def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista




def promedio(lista):
    promedio = sum(lista)/len(lista)
    return(promedio)


          
            

print(reducir_lista(lista_numeros))
print(promedio(reducir_lista(lista_numeros)))





lista_numeros = [23,43,54,65,6,88,34]
#funcion 3
import random

#funcion lanzar_moneda sin argumentos, y devuelve cara o cruz
def lanzar_moneda():
    resultado = random.choice(["Cara","Cruz"])
    return resultado
print(lanzar_moneda())




     



#otra funcion probar_suerte que tome dos argumentos 1(el resultado de lanzar moneda) y 2(sera una lista de numeros cualquiera llamada lista_numeros)

'''def probar_suerte(lanzar,lista):
    lista = [23,43,54,65,6,88,34]
    while lanzar == "CARA":
        lista.clear()
        return f"La lista se autodestruira {lista}"
    else:
        return f"La lista fue salvada{lista}"
     
     
resultado = probar_suerte(lanzar_moneda(),lista)
print(resultado)'''




def probar_suerte(lanzar,lista):
    if lanzar == "Cara":
        print("La lista se autodestruira ")
        return []
    elif lanzar == "Cruz":
        print("La lista fue salvada ")
        return lista
        
     
     
resultado = probar_suerte(lanzar_moneda(),lista_numeros)
print(resultado)






'''def letra_unica_orden(palabra):
    for letra in palabra:
        ordenadas = palabra.sort()
        unicas = set(palabra)
        return unicas
        
print(letra_unica_orden("caballo"))
'''







'''def numeros_primos(numero):
    for n in range(2,numero):
        if (numero%n) == 0:
            lista = list(range(0,numero))
            return lista
    for n in range(0,numero):
        listaa = list(range(0,numero))
        return listaa'''
            



'''print(numeros_primos(11))'''



def contar_primos(numero):
   
    primos = [2]
    iteracion = 3
    
    if numero < 2:
        return 0
    
    while iteracion <= numero:
        
        for n in range(3,iteracion,2):
            
            if (iteracion % n) == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    
    print(primos)
    return len(primos)


print(contar_primos(150))  
















#! EL AHORCADO





#comenzar el juefgo y elegir una palabra al azar CHOISE
import random


def comenzar():
    comenzar = input("(((BIENVENIDO AL AHORCADO))) SI QUIERE JUGAR RESPONDA - y - (PARA COMENZAR) de lo contrario - n - : ")
    if comenzar == "y":
        nombre = input("MUCHAS GRACIAS POR JUGAR, COMO TE LLAMAS??: ")
        palabra = random.choice(["helicoptero","atomica","bonsai","cocodrilo","videojuegos","computadora","mundial","atlantida"])
        return palabra
        
    else:
        return f"Muchas gracias {nombre} lo mismo, jugaremos en otra oportunidad"
        
print(comenzar())




#separar la palabra en letras


def fragmentar(palabra):
        for l in palabra:
            return palabra
        
print(fragmentar(comenzar()))









#transformar la palabra elejidad en _ _ _














#funciones : pedir al usuario una letra?, validar letra, chequear letra en palabra, verificar si gano o no (hacer las funciones y al ultimo el codigo que las implementa)


''''def elejir_letra(letra):
    while letra == "":
        eleccion = input("ELIJE UNA LETRA, TENDRAS 8 OPORTUNIDADES PARA DECIFRAR MI PALABRA")'''




def consulta(letraa):
    letra = input(f"MUCHAS GRACIAS {usuario}, ahora te voy a pedir que ingreses de a una ves la LETRA que piensas podria pertenecer a la palabra oculta que pense...(tendras 8 oportunidades) VAMOS A VER SI ADIVINAS..? jaja")
    vidas = 8
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    import random

usuario = input("HOLA COMO TE LLAMAS AMIGO: ")

def comenzar():
    comenzar = input(f"(((BIENVENIDO AL AHORCADO Sr/a. {usuario}))) SI QUIERE JUGAR RESPONDA - y - (PARA COMENZAR) de lo contrario - n - : ")
    if comenzar == "y":
        palabra = random.choice(["helicoptero","atomica","bonsai","cocodrilo","videojuegos","computadora","mundial","atlantida"])
        print(palabra)
        return palabra
    else:
        return f"Gracias sera la proxima amigo"
        
palabra = comenzar()
      
              
#palabra con guiones
def guion(palabra):
    palabra = (len(palabra))
    guiones = palabra * " _ "
    return guiones
    

palabra_cifrada = guion(comenzar())
print(guion(comenzar()))






#ingreso de letras del usuario


def consulta(palabra):
    vidas = 8
    while vidas == 0:
        letra = input(f"MUCHAS GRACIAS {usuario}, ahora te voy a pedir que ingreses de a una ves la LETRA que piensas podria pertenecer a la palabra oculta que pense...(tendras 8 oportunidades) VAMOS A VER SI ADIVINAS..? jaja")
        for l in palabra:
            if palabra.find(letra) == range(0,15):
                posicion = palabra.find(letra)
                decifrando = palabra_cifrada[posicion]= letra
                vidas = vidas - 1
                return decifrando

    


consulta(palabra)





#buscar coincidencia
```
````
