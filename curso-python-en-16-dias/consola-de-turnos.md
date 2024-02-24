# 😀 CONSOLA DE TURNOS

````python
// Some code

```python
#!turnerofarmaciaP4IM0N

from numerosdeturnosydecoP4IM0N import * 



#funcion 4 que imprime el turno ya listo y decorado, con la funcion 3 del otro modulo importado
@decoracion_turno
def turno_papel(sector,turno):
    print(f"----------[{sector}{turno}]---------")
    




#funcion 5 Principal que gestiona todo el sistema de turnerofarmaciaP4IM0N
def turnerofarmaciaP4IM0N():
    while True:
        sector_elejido = sector()
        turnos = turno(sector_elejido)            
        num_turno = next(turnos)
        turno_papel(sector_elejido,num_turno)
        continuar = input("Desea continuar: ")
        if continuar == "no":
            print("Muchas gracias, hasta la proxima ")  
            break      
    
    
    
    
#ejecucion de turnerofarmaciaP4IM0N
turnerofarmaciaP4IM0N()    
#!by P4IM0N    
```


#CREE MI PROPIO MODULO QEU TARBAJA CON EL CODIGO PRINCIPAL QEU ESTA ARRIBA:

```python
#!modulo de funciones a ser importadas para el uso del sistema turnerofarmaciaP4IM0N

#?todas estas funciones de este modulo seran importadas al modulo principal, de turnerofarmaciaP4IM0N para ser usadas por la funcion principal que gestiona el programa
#funcion 1 retorna el sector seleciconado por el cliente
def sector():
    decision = input("desea usar el sistema: ")
    while decision == "si":
        sector = input("elija el servicio: \n1-Farmacia\n2-Perfumeria\n3-Cosmeticos\n---->")
        if sector == "1":
            s = "F-"
            break
        elif sector == "2":
            s = "P-"
            break
        elif sector == "3":
            s = "C-"
            break
        else:
            print("ingrese un numero de opcion valida")       
    return s
            





#funcion 2 + contador, recibe el sector de la funcion 1 y retorna el numero de turno, a la ves contandolo en contador sector por sector.
contador = {"F-": 0, "P-": 0, "C-": 0}

def turno(sector):
    
    global contador
    turno = contador[sector]
    while turno < 200:
        contador[sector] += 1
        yield turno + 1
        
        

#funcion 3 se encarga de decorar el turno, envolviendo la funcion 4 de turno_papel, para detalle visual   
def decoracion_turno(funcion):
    def decoracion(sect,turn):
        print("************************\n    Este es su Turno:   |")
        funcion(sect,turn)
        print("Aguarde y sera Atendido |\n************************")      
    return decoracion    




#! by P4IM0N
```
````

CODEO DEL DIA 8:

````python
// Some code

```python
#! dia 8 - programa una consola de turno 

#buscar paquetes en google e info de como aplicarlos y que nos ofrece




#modulos y paquetes
#?Los modulos se demonia a cualquier codigo guardado en un archivo .py (ejemplo.py, con una funcion dentro def cosa():),para luego porder ser importado, osea usado en cualquiuer otro archivo .py , llamandolo o importandolo de la suguiente forma: import ejemplo
#?Los paquetes son grupos de modulos dentro de el. ejem: carpeta(matematica)dentro tiene modulo, ejem: suma.py,resta.py y si o si para indicarle que es un conjunto de modulos empaquetados dentro de la carpeta, si o si debe contener dentro un archivo __init__.py. (tambien puede contener subcarpetas dentro)
#?Para hacer uso de un a funciion que est dentro de un modulo la llamariamos, en el ejemplo de arriba, de la siguienteforma: from ejemplo import cosa .  




#manejo de errores (try: intenta ejecutar el siguiente codigo, except: ejecuta pero si surge algo mal, has lo siguiente que te digo...., finaly: no importa si ahi un error al ejecutar, sucedad lo que seceda haz esto...)

#?esta da error cuando el usuario en ves de ingrasar un numero, ingresa un a letra y no se termina de ejecutar por lo menos el ultimo print (para esto va a servir saber el manejo de errrores)
'''def suma():
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print(num1 + num2)
    print("gracias por usar mi sistema")
    
suma()  '''  


#?ejemplo de uso y para que se usan estos metodos 
'''try:
    #codigo que queremos probar 
except:
    #codigo a ejecutar si no hay un error
   else:
       #codigo a ejeecutar si non  hay un error  
finally:
    #codigo que se va a ejecutar de todos modos '''            



def suma():
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))
    print(num1 + num2)
    print("gracias por usar mi sistema")
    



try:
    suma() 
except:
    print("algo no salio bien")
else:
    print("hisciste todo perfecto mano") 
finally:
    print("finalizamos con el uso de mis sistema, gracias")







#?otros tipos de errores(los podemos buscar en documentacuion de python en  google, el nombre de cada erro  para que el que queremos que se hagan excepciones)
def suma():
    num1 = int(input("primer numero: "))
    num2 = int(input("segundo numero: "))        #?tambien podemos probar ingresar una letra para que se active el except de ingreso de un valueerror
    print(num1 + num2)
    print("gracias por usar mi sistema"+ num2)   #?en este caso aca le metemos el error 
    



try:
    suma() 
except TypeError:
    print("haz querido concatenar tipos de valores diferentees (un integer + string) por eso este error")
except ValueError:
    print("no haz ingresado un numero ")
else:
    print("hisciste todo perfecto mano") 
finally:
    print("finalizamos con el uso de mis sistema, gracias")
    
    
    
    
    


#otra forma que podemos usar el manejo de errores en loops, ejem plos(en fin se los puede usar similares a un if o elif y else):    
def ingresa_numero():
    
    while True:
        try:
            numero = int(input("ingresa un numero"))  
        except:
            print("ese no es un numero")      
        else:
            print(f"ingresaste bien, el siguiente numero : {numero}")
            break
        
    print("gracias por usar nuestro sistema bien")
    
ingresa_numero()   






#practicas


def suma(num1,num2):
        
    
    try: 
        print(num1+num2)
    except:
        print("Error inesperado")
        
        


def cociente(num1,num2):
        
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")   
        
        
        
        
        
        
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")        
             





#buscar errores con pylint y unittest


#?provocamos un error a proposito en el nombre de la variable con la mayuscula

numero1 = 100
#print(Numero1)


#!lo chequeamos en consola o terminal con el siguiente comando (mostrara muchos datos,errores, puntage del codigo, etc): pylint modulospaqueteserrorpylintunittestdecogeneradores.py -r y





#Decoradores (nos permite como un interruptor habilitar o desabilitar acciones que querramos agregar a funciones, nos sirve para no duplicar codigo y hacerlo mas corto)
#! En python podemos definir funciones dentro de variables, o funciones dentro de otras funciones, o funciones como parametros de otras funcionea.


def mayuscula(palabra):
    print(palabra.upper())




def minuscula(palabra):
    print(palabra.lower())



def funcion(funcion):                               #?funcion dentro de otra como parametro
    return funcion

funcion(mayuscula("mayuscula"))                     #?funcion dentro de otra como parametro







#!las funciones se las puede trabajar como objeto, por ende podemos poner funciones dentro de funciiones y que esta funcion padre o viceversa se traten comom objetos, y guardarlas como objetos dentrto de variables, etc......

def cambiar_las_letras(tipo):
    def mayuscula(palabra):                 #?funcion 1
        print(palabra.upper())


    def minuscula(palabra):                 #?funcion 2
        print(palabra.lower())
        

    if tipo == "mayus":                     #?condicional de eleccion del usuario que va a retornar la funcion elejida (funcion 1 o funcion 2), lista para ingresarle su parametro PALABRA
        return mayuscula
    elif tipo == "minus":
        return minuscula
    
eleccion = cambiar_las_letras("minus")      #?creamos una variable con la funcion grande padre, dentro con el parametro de la eleccion del usuario, por ende como le ingresamos su parametro TIPO, comparara los condicionales, devolviendonos la funcion que tambien esta dentro, por ende la variable como qu se transformara en funcion, digamos, segun la eleccion pasaria a valer la funcion 1 o funcion 2. 
eleccion("MayUscUlaA")                      #?usamos la variable ELECCION que ya vale la funcion devuelta por retun del condicional, por  ende ya le ingresamos el parametro comom si estuvieramos trabajando directamente con la funcion 1 elejida de manuscula() o funcion 2 minuscula().







#!ahora si decoradores ya sabiendo y entendiendo lo anterior




def decoracion_visual(funcion):
    def otra_funcion(palabra): 
        print("******************") 
        funcion(palabra) #?<-----------|            
        print("//////////////////") #? |
    return otra_funcion             #? |
                                    #? |
                                    #? |
@decoracion_visual                  #? |DE ESTA MANERA LLAMAMOS AL DECORADOR : es como que al haber definido otra funcion antes, de esta forma la llaamos para usarla comom un decorador, por ende lo que va a hacer es envolver a la respuesta de nuestra funcion 1 y 2, dentro de los print de la funcion otra_funcion y la tomara y pondra en donde declaramos funcion(palabra)
def mayuscula(palabra):             #? --funcion 1
    print(palabra.upper())


def minuscula(palabra):                 #?funcion 2
    print(palabra.lower())     



mayuscula("mayuscula decorada")





#Generadores (lo que nos hace es ir retornando progresivamente un resultado a medida que lo vallamos nececitando(por ende ahorra espacios en memorias sin generar todo el resultado de golpe))



def funcion_normal():
    return 4


def funcion_generador():
    yield 4 




print(funcion_normal())                #?esta nos lo produce al instante de ejecutarse, ocupando el espacio en memoria
print(funcion_generador())             #?esta nos lo produce pero digamos como de manera virtual, sin devolverlo de manera visual al instante de ser ejecutado, por ende no ocupa tanto espacio ded memoria.(por ende para ya imprimirlo de manera visual y que ocupe espacio, devemos primero meter nuestra funcion de generador def funcion_generador dentro de una variable y luego llamarla e imprimirla en este caso, con next(variable creada) de la siguiente manera:)

n = funcion_generador()
print(next(n))                         






 
 
 
def funcion_normal():                 #?funcionNORMAL
    lista = []
    for x in range(1,4):
        lista.append(x*10)
    return lista    


def funcion_generador():              #?funcion GENERADOR
    for x in range(1,4):
        yield x*10 




print(funcion_normal())                #?esta nos lo produce al instante de ejecutarse, ocupando el espacio en memoria
print(funcion_generador())             #?esta nos lo produce pero digamos como de manera virtual, sin devolverlo de manera visual al instante de ser ejecutado, por ende no ocupa tanto espacio ded memoria.(por ende para ya imprimirlo de manera visual y que ocupe espacio, devemos primero meter nuestra funcion de generador def funcion_generador dentro de una variable y luego llamarla e imprimirla en este caso, con next(variable creada) de la siguiente manera:)

n = funcion_generador()
print(next(n))                         #?de esta forma el resultado de nuestra funcion generadora ya ocupa su espacio entero de manera sistematica y visual digamos para entenderlo.
print(next(n))                         #!aca vemos como con el generador podemos ir haciendo uso e ir solicitando el resultado generado de manera progresiva #?de esta forma el resultado de nuestra funcion generadora ya ocupa su espacio entero de manera sistematica y visual digamos para entenderlo. (el generador tiene memoria y recuerda, aunque alla ejecutado mas funciones o cosas entre medio, si al final del codigo la llamo, va a recordar por que resulatdo le tocaba generar)


 
 
 
 
 
#practicas

 
def generador():
    numero = 0
    while True:
        numero = numero + 1
        yield numero
        
generador = generador()  
```
````
