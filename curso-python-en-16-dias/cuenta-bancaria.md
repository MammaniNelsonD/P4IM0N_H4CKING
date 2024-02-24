# 😀 CUENTA BANCARIA

````python
// Some code

```python
#!APP DE CUENTA BANCARIA (P4IM0NB4NK)


#!clases


#clase 1 persona nombre y apellido y cuenta
#clase 1 persona nombre y apellido y cuenta, con metodo funcion 1 crea cliente y devuelve un cliente ya creado
class Persona:  
    def __init__(self,nombre,apellido,cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = cuenta  
    def datos_cliente(self):
        self.nombre = input("((BIENVENIDO A P4IM0NB4NK))\n Por favor ingrese su nombre para agregarlo al sistema: ")
        print("="*30+"\n")
        self.apellido = input("Ahora porfavor ingrese su apellido: ")							
        print("="*30+"\n")
        self.cuenta = input("Ingrese por favor su numero de cuenta: ")
        print("="*30+"\n")
        print('Usuario creado exitosamente: ') 
        print('Nombre de usuario: ' + self.nombre +" "+ self.apellido) 
        print('Numero de cuenta:' + self.cuenta)
        print("="*30+"\n")
        	
persona = Persona(" ", " ", " ")





#clase 2 cliente hereda de persona mas numero de cuenta y balance y tres metodos -imprimir cliente y su balance de cuenta , -depositar, -retirar. 
#codigo para q el usuario elija -deoositar o - retirar o -salir (con loop, debe ir llevando la cuenta del balance )
class Cliente(Persona):
    def __init__(self,balanze):
        self.obtener_datos()                                                              #?de esta forma obtenemos los self datos nombre apellido cuenta heredados de la clsae persona, para poder ser usados y llamados en unn texto dentro de esta clase
        super().__init__(self.nombre,self.apellido,self.cuenta)
        self.balanze = balanze   
    def depositar(self):
        positivo = int(input("Ingrese cuanto dinero quiere ingresar a su cuenta: $"))
        self.balanze = self.balanze+positivo
    def retirar(self):
        negativo = int(input("Ingrese cuanto dinero quiere retirar: $"))
        if negativo > int(self.balanze):                                                   #?con esta condicion,  transformo con casting int(self.balance) para que compare dos tipos iguales int y responda si se exedio de retiro por que su balance es menor, o si no que se retire el dinero y se guarde su balance.
            print("El monto a retirar supera su saldo actual. Porfavor ingrese un monto menor ")
        else:
            self.balanze = self.balanze-negativo
    def balance(self):
        print(f"Sr.{self.nombre} {self.apellido}, El saldo total de su cuenta Nº{self.cuenta}, es de: (( ${self.balanze} ))\n"+"/"*30)
    def obtener_datos(self):
        super().datos_cliente()    
        
cliente = Cliente(0)
cliente.balance() 


				
			
						


#!funciones
												

#funcion 1 para decidir si ingreasar o no al sistema appbanck
def entrar():
    decicion = input("quiere ingresar a nuestro sistema de gestion bancaria: (si o no) ")
    return decicion



#funcion 2 brinda el menu de opciones
def opciones():
    print("="*30)
    print("((BIENVENIDO A APPBANCK)) elija el numero de opcion que desea realizar: ")
    print("1- Depositar\n2- Retirar\n3- Ver balance\n"+"="*30)
    opcion =  int(input("porfavor elija la opcion: "))
    return opcion







#!ejecucion del programa


#funcion 3 es la q se encargaria de manejar todo el programa ((P4IM0NB4NK))y de mantener al usuario en elecciones de las opciones de gestion que se le da.
def P4IM0NB4NK():
    datos_clientes = persona.datos_cliente
    if entrar()=="si":
        opcion = opciones()
        if opcion == 1:
            print("="*30+"\n")
            cliente.depositar()
            print("\n"+"="*30+"\n")
            cliente.balance()
            print("="*30+"\n")
            continuar = input("Desea realizar otra operacion: (si o no) ")
            if continuar == "si":
                P4IM0NB4NK()
            else:
                print("="*30 +"\nMuchas gracias por usar nuestra  app amigo ")
        if opcion == 2:
            print("="*30+"\n")
            cliente.retirar() 
            print("\n"+"="*30+"\n")
            cliente.balance()
            print("="*30+"\n")
            continuar = input("Desea realizar otra operacion: (si o no) ")
            if continuar == "si":
                P4IM0NB4NK()
            else:
                print("="*30 +"\nMuchas gracias por usar nuestra  app amigo ") 
        if opcion == 3:
            print("="*30+"\n")
            cliente.balance() 
            print("="*30+"\n")
            continuar = input("Desea realizar otra operacion: (si o no) ")
            if continuar == "si":
                P4IM0NB4NK()
            else:
                print("="*30 +"\nMuchas gracias por usar nuestra  app amigo ")    
    else:
        print("="*30+"\nGracias sera la proxima amigo")   
        
        
        

P4IM0NB4NK()



#! by P4IM0NB4NK
```
````

CODEO DEL DIA 7:

````python
// Some code

```python
#!programacion orientada a objetos  oop    o  poo



#creando una clase
class Pajaros:                                         #por convencion el nombre de la clase se la comienza en mayuscula
    pass




#creando un objeto de esta clase osea una instancia
mi_pajaro = Pajaros()


print(mi_pajaro)                                       #vemos que nos dic que ya es un objeto

print(type(mi_pajaro))                                 #es de tyipo main


#ejemplo siguen ciendo de la misma clase Pajaros, pero de otra especie cada uno, con caracteristicas difereentes qie le demos
otro_pajaro = Pajaros()                                #podemos crear otor objeto osea otro pajaro con la misma clase para luego darle otras propiedades, y ya vemos que no la crea con otro numero de instancia o ubicacion


print(otro_pajaro)




#practicas



class Personaje:
    pass

harry_potter = Personaje()




class Dinosaurio:
    pass

velociraptor = Dinosaurio()
tiranosaurio_rex = Dinosaurio()
braquiosaurio = Dinosaurio()





class PlataformaStreaming:
    pass


netflix = PlataformaStreaming()
hbo_max = PlataformaStreaming()
amazon_prime_video = PlataformaStreaming()








#!atributos de instancias



class Pajaro:
#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color):
        #atributo (color) = parametro ("verde")
        self.color = color
        
    
loro = Pajaro("verde")

    
print(loro.color)








class Pajaro:
#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    
loro = Pajaro("verde","loro")

    
print(loro.especie)








class Pajaro:
#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    
loro = Pajaro("verde","loro")

    
print(f"mi pajaro es un ave de la especie ({loro.especie}) y tiene un plumaje de color ({loro.color}) muy bello")










#!atributos de clase

class Pajaro:
    
    alas = "largas"               #le damos este atributo a todos los pajaros que creamos en esta clase de esta forma. y lo llamamos de la misma forma a posterior.


#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    
loro = Pajaro("verde","loro")

    
print(f"mi pajaro es un ave de la especie ({loro.especie}) y tiene un plumaje de color ({loro.color}) muy bello, y tienen alas muy {loro.alas}")      #se lo sigue llamando igual que a los otros atributos









#pradcticas


class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco",4)





class Cubo:
    caras = 6
    
    def __init__(self,color):
        self.color = color


cubo_rojo = Cubo("rojo")  







class Personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad
        
harry_potter = Personaje("Humano",True,17) 

print(f"Harry es de la especie {harry_potter.especie}, dicen que tiene magia y eso es {harry_potter.magico}, teniendo tan solo {harry_potter.edad} años")







#!metodos





class Pajaro:
    
    alas = "largas"               #le damos este atributo de clase a todos los pajaros que creamos en esta clase de esta forma. y lo llamamos de la misma forma a posterior.


#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    def cantar(self):                               #el metodo tambien lo hacemos como una funcion , en este caso para que cuando se ejecute la funcion el pajaro imprima y haga pio pio
        print("pio pio y soy de color {}".format(self.color))   #con {}".format(self+atributo color) le podemos pasr y hacer uso de atributos de instancia que ya le hemos dado
    def volar(self, metros):                        #tambien creamos otro metodo o funcion para que el pajaro vuele la cantidad de metros que le ingresemos
        print(f"el pajaro ha volado {metros} metros")
        
        
        




    
loro = Pajaro("verde","loro")

loro.cantar()                       #dichas funciones las llamamos o invocamos para quye se realizen, de esta forma
loro.volar(100)                     #dichas funciones las llamamos o invocamos para quye se realizen, de esta forma, y en este caso le pasamos el parametro 100 dentro de la funcion
    
print(f"mi pajaro es un ave de la especie ({loro.especie}) y tiene un plumaje de color ({loro.color}) muy bello, y tienen alas muy {loro.alas}")      #se lo sigue llamando igual que a los otros atributos







#practicas




class Perro:
    def ladrar(self):
        print("Guau!")
 
perro = Perro()
        
perro.ladrar() 





class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
    
merlin = Mago()

merlin.lanzar_hechizo()






class Alarma:
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

alarma = Alarma() 

alarma.postergar(15)








#!decoradores -metodos de instancia -metodos de clase @classmethod -metodos estaticos @staticmethod





#!metodos de instancias

#?accedemos y modificamos atributos del objeto
class Pajaro:
    
    alas = "largas"               #le damos este atributo de clase a todos los pajaros que creamos en esta clase de esta forma. y lo llamamos de la misma forma a posterior.


#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    def cantar(self):                               #el metodo tambien lo hacemos como una funcion , en este caso para que cuando se ejecute la funcion el pajaro imprima y haga pio pio
        print("pio pio y soy de color {}".format(self.color))   #con {}".format(self+atributo color) le podemos pasr y hacer uso de atributos de instancia que ya le hemos dado
    def volar(self, metros):                        #tambien creamos otro metodo o funcion para que el pajaro vuele la cantidad de metros que le ingresemos
        print(f"el pajaro ha volado {metros} metros")
    def pintar_negro(self):
        self.color = "blanco"                       #?aca le cambiamos el color que le dimos con self.color, decignandole nuevamente con el mismo atributo , el parametro de color blanco
        print(f"ahora el pajaro es {self.color}")  



loro = Pajaro("verde","loro")

loro.pintar_negro()








#?acceder a otros metodos
class Pajaro:
    
    alas = "largas"               #le damos este atributo de clase a todos los pajaros que creamos en esta clase de esta forma. y lo llamamos de la misma forma a posterior.


#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    def cantar(self):                               #el metodo tambien lo hacemos como una funcion , en este caso para que cuando se ejecute la funcion el pajaro imprima y haga pio pio
        print("pio pio y soy de color {}".format(self.color))   #con {}".format(self+atributo color) le podemos pasr y hacer uso de atributos de instancia que ya le hemos dado
    def volar(self, metros):                        #tambien creamos otro metodo o funcion para que el pajaro vuele la cantidad de metros que le ingresemos
        print(f"el pajaro ha volado {metros} metros")
        self.cantar()                                #?desde un metod en funcion, podemos accedder a otros metodos declarados
        
        
        




    
loro = Pajaro("verde","loro")

loro.volar(100)













#?modificar el estado de la clase
class Pajaro:
    
    alas = "largas"            #?este es el setado actual de la clase   #le damos este atributo de clase a todos los pajaros que creamos en esta clase de esta forma. y lo llamamos de la misma forma a posterior.


#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    def cantar(self):                               #el metodo tambien lo hacemos como una funcion , en este caso para que cuando se ejecute la funcion el pajaro imprima y haga pio pio
        print("pio pio y soy de color {}".format(self.color))   #con {}".format(self+atributo color) le podemos pasr y hacer uso de atributos de instancia que ya le hemos dado
    def volar(self, metros):                        #tambien creamos otro metodo o funcion para que el pajaro vuele la cantidad de metros que le ingresemos
        print(f"el pajaro ha volado {metros} metros")
        
        
        




    
loro = Pajaro("verde","loro")

loro.alas = "cortas"                  #?al final nos permite tambien podemos modificar su estado de clase por el parametro que le decignemos, en este caso "cortas"
print(loro.alas)















#!metodos de clases


#?@classmethod , (no pueden acceder a los atributos de instancias ej: self.color da error) pero si podemos hacerlo con los atributoas y parametros de clase, ej: alas
class Pajaro:
    
    alas = "largas"               #le damos este atributo de clase a todos los pajaros que creamos en esta clase de esta forma. y lo llamamos de la misma forma a posterior.


#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    def cantar(self):                               #el metodo tambien lo hacemos como una funcion , en este caso para que cuando se ejecute la funcion el pajaro imprima y haga pio pio
        print("pio pio y soy de color {}".format(self.color))   #con {}".format(self+atributo color) le podemos pasr y hacer uso de atributos de instancia que ya le hemos dado
    def volar(self, metros):                        #tambien creamos otro metodo o funcion para que el pajaro vuele la cantidad de metros que le ingresemos
        print(f"el pajaro ha volado {metros} metros")
    @classmethod                                    #?con @classmethod no nesecitamos de ninguna instancia para poder ejecutarce
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")            #?nos imprime con la cantidad que le ingresamos abajo a la funcion a posterior
        cls.alas = "plumudas"                       #?con cls, similar como con self, podemos llamar a un atributoi de clase opara poder modificar su parametro, aca ej: plumudas
        print(Pajaro.alas)                          #?imprimimos el atributo de clase ya modificado



    
'''loro = Pajaro("verde","loro")'''                #?aca vemos que no nececita ninguna instancia declarada para poder ejecutarse



Pajaro.poner_huevos(5)








#!metodos estaticos 


#?@staticmethod (este metodo, no se refiere a ningun elemento de clase ni de instancias, Por tanto no trabaja con ningun argumento, ni atributo ni parametro de clase e instancia)
class Pajaro:
    
    alas = "largas"               #le damos este atributo de clase a todos los pajaros que creamos en esta clase de esta forma. y lo llamamos de la misma forma a posterior.


#def como funcion o metodo + init como constructor del atributo que le daremos + self es la instancia del objeto a crear, se puede usar cualquier otra palabra, pero por convencion se usa self + mas el atributo color que es el que creamos
    def __init__(self, color, especie):         #podemos darle varios atributos
        #atributo (color) = parametro ("verde")
        self.color = color
        self.especie = especie
    def cantar(self):                               #el metodo tambien lo hacemos como una funcion , en este caso para que cuando se ejecute la funcion el pajaro imprima y haga pio pio
        print("pio pio y soy de color {}".format(self.color))   #con {}".format(self+atributo color) le podemos pasr y hacer uso de atributos de instancia que ya le hemos dado
    def volar(self, metros):                        #tambien creamos otro metodo o funcion para que el pajaro vuele la cantidad de metros que le ingresemos
        print(f"el pajaro ha volado {metros} metros")
    @staticmethod                                   #?(este metodo, no se refiere a ningun elemento de clase ni de instancias, Por tanto no trabaja con ningun argumento, ni atributo ni parametro de clase e instancia)
    def mirar():
        print("Te mira fijo a los ojos") 
        
        
        




    
'''loro = Pajaro("verde","loro")'''                #?no requiere de una instancia para ejecutarce tampoco

Pajaro.mirar()                                     #?lo invocamos 









#practicas





class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
    
Mascota.respirar()




class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(Jugador.vivo)
        
Jugador.revivir() 








class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1
        print(self.cantidad_flechas)
    
    
flechas = Personaje(10)
flechas.lanzar_flecha()







#!herencia (se puede usasr mucho para no repetir codigo, como se suele decir DRY )



class Animal:
    pass

class Perro(Animal):         #?poniendo el nombre de la clase que queremeos que herede propiedades nuestro class lo ponemos entre parentesis
    pass

class Gato(Animal):
    pass

class Pez(Animal):
    pass



print(Perro.__bases__)            #?la propiedad __bases__ nos permite ver de quien hereda propiedades nuestro elemento o class en este caso. Seria similar a un type

print(Animal.__subclasses__())    #?la propiedad __subclasess nos devuelve las clases que toman su herencia











class Animal:
    def nacer(self):
        print("el animal nacio")

class Perro(Animal): 
    pass

class Gato(Animal):
    pass

class Pez(Animal):
    pass



gatito = Gato()
gatito.nacer()                             #?vemos como al herredar las propiedades de Animal, nos aparece y heredo el metodo Nacer 












class Animal:
    def __init__(self,edad,color):          #?le damos como ejemplo do atributos de instancia con parametros, los cuales los heredara a sus clases hijos
        self.edad=edad
        self.color= color
    def nacer(self):
        print("el animal nacio")

class Perro(Animal): 
    pass

class Gato(Animal):
    pass

class Pez(Animal):
    pass



gatito = Gato(12,"marron")                   #?vemos como ahora al heredar dos atributos de class Animal, nuestro class Gato se queja y nos solicita las dos propoiedades o parametros para sus dos atributos heredados
gatito.nacer()
print(gatito.color)
print(gatito.edad)







#practicas




class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Alumno(Persona):  
    pass






class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
class Perro(Mascota):
    pass







class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass
class Automovil(Vehiculo):
    pass






#!herencia extendida LOS ELEMENTOS HIJOS(pueden tener metodos heredados, metodos heredados y luego modificados, o sus propioos metos nuevos) y herencias multiples (osea de heredar atributos de varias clases padres )







#?modificar metodos o atributos heredados, agregar nuevos metodos a una clase heredera

class Animal:
    def __init__(self,edad,color):          #?le damos como ejemplo do atributos de instancia con parametros, los cuales los heredara a sus clases hijos
        self.edad=edad
        self.color= color
    def nacer(self):
        print("el animal nacio")
    def hablar(self):                        #?le damos un meto hablar para que luego se lo herede a otro class y al mismo lo modificaremso a posteriori
        print("este animal no habla")    

class Perro(Animal):
    def hablar(self):                        #?dentro de una clase que heredo los atributos, llamamos al metodo a modificar con su mismo nombre con el qu figura en su padre, y lo modificamos, y se respetara esa modificacion a la hora de imprimirlo o llamarlo
        print("este animal ladra")
    def nuevo_metodo(self):
        print("nuevo metodo dado al class hijo")    #?nuevo metodo dado a una clase que hereda 

class Gato(Animal):
    pass

class Pez(Animal):
    pass



perrito = Perro(10,"negro")

perrito.hablar()
perrito.nuevo_metodo()









#?agregar nuevos atribustos de instancia a una clase heredera




class Animal:
    def __init__(self,edad,color):          #?le damos como ejemplo do atributos de instancia con parametros, los cuales los heredara a sus clases hijos
        self.edad=edad
        self.color= color
    def nacer(self):
        print("el animal nacio")

class Perro(Animal): 
    def __init__(self, edad, color, velocidad):     #?esta es -1- una forma de agregar atributos de instancia unicos a una clase heredera de un padre
        self.edad = edad
        self.color = color
        self.velocidad = velocidad
               
        
class Gato(Animal):
    def __init__(self, edad, color, gordo):
        super().__init__(edad, color, gordo)        #?esta es -2- forma, con el uso de super()__init__ hacemos un codigo mucho mas compacto, para evitar ir declarando una por una cada atributo con self
        
    

class Pez(Animal):
    pass





padre = Animal(20,"rojo")
perros = Perro(30,"naranja","100km/h")     #?vemos como nos pide el tercer atributo nuevo que le dimos a la clase heredera, que este atributo nuevo su padre no lo va a tener











#?herencias multiples

class Padre:                              #?padre dara su herencia al hijo
    pass

class Hijo(Padre):                        #?hijo hereda lo del padre, y dara sus propiedades mas las que heredo de su padre, al nieto
    pass

class Nieto(Hijo):                        #?el nieto heredo los del Hijo y el padre
    pass












class Padre:
    def hablar(self):
        print("hola")
    pass

class Hijo(Padre):         
    pass

class Nieto(Hijo):
    pass




mi_nieto = Nieto()      
mi_nieto.hablar()             #? aca vemos como nieto heredo el metodo hola del padre que se transmitio atraves de hijo











#?herencia dada de  multiples clases

class Padre:
    def hablar(self):
        print("hola")
class Madre:
    def reir(self):
        print("riooooo")    

class Hijo(Padre, Madre):         #?agregando a madre , le decimos que tambien herede lo de madre a la ves lo de padre y heredarlo de generacion en generacion
    pass

class Nieto(Hijo):                #?por ende nieto tendra tambien las dos propiedades de clases que heredo hijo
    pass




mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()













class Padre:
    def hablar(self):
        print("hola")
class Madre:
    def reir(self):
        print("riooooo")  
    def hablar(self):             #?agregmos un metodo igual que el de padre para ver cual tiene percistencia, y aca tendria percistencia Padre por que dentro del parentecis heredo primero de padre, si fuese alrevese tomaria el de madre   
        print("que tal")      

class Hijo(Padre, Madre):         #?agregando a madre , le decimos que tambien herede lo de madre a la ves lo de padre y heredarlo de generacion en generacion
    pass

class Nieto(Hijo):                #?por ende nieto tendra tambien las dos propiedades de clases que heredo hijo
    pass





mi_nieto = Nieto()
mi_nieto.hablar()
print(Nieto.__mro__)             #?__mro__ metod order resolucion, seria la ruta en el orden que que se resuelve un metodo, para el caso de nieto en este ejmplo












#practicas




class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre, Padre):
    pass







class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass











class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"












#!Polimorfismo (muchas - formas) (nos permite ejecutar en dos objetos o clases distintas, metodos llamados con el mismo nombre sin problema )





class Vaca:                                          #?creo una clase objeto 
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):                                #?creamos un metodo funcion igual llamado al de la clase siguiente
        print(self.nombre + " dice muuu")    
        
        

class Oveja:                                         #?creo una clase objeto 
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice beee")   




vaca1 = Vaca("aurora")                               #?creo la instancias
oveja1 = Oveja("shaun")



vaca1.hablar()                                       #?esto es lo que nos permite l polimorfismo, llanmar a dos classes o objetos con un metodo nombrado igual para las dos y no nos causa ningun conflicto. se ejecutan bien ambos por separado
oveja1.hablar()










#?vamos a crear una lista para un bucle para ver mejor el uso deel polimorfismo
class Vaca:                                          #?creo una clase objeto 
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):                                #?creamos un metodo funcion igual llamado al de la clase siguiente
        print(self.nombre + " dice muuu")    
        
        

class Oveja:                                         #?creo una clase objeto 
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice beee")   




vaca1 = Vaca("aurora")                               #?creo la instancias
oveja1 = Oveja("shaun")



animales = [vaca1, oveja1]                           #?creamos una lista con nuestros dos objetos en instancias creadas

for animal in animales:                              #?creamos elñ loop para que itinere entre cada animal (palabra) que esta dentro de nuestra lista animales y ejecute el metodo siguiente que es el mismo que tienen  ambos objetos. y vemos como se ejecutan sin ningun pproblema a pesar de llamarse ugual y estarse itinerando
    animal.hablar()
















#?tambien lo podemos ver claro al polimorfismo atraves de una funcion
class Vaca:                                          #?creo una clase objeto 
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):                                #?creamos un metodo funcion igual llamado al de la clase siguiente
        print(self.nombre + " dice muuu")    
        
        

class Oveja:                                         #?creo una clase objeto 
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print(self.nombre + " dice beee")   




vaca1 = Vaca("aurora")                               #?creo la instancias
oveja1 = Oveja("shaun")


def animañ_habla(animal):                            #?creamos una fiuncion para que tome nuestros objetos animales
    animal.hablar()                                  #?y ejecute el metodo igual en ambos


animañ_habla(vaca1)                                  #? le damos nuestro objeto a la funcion y nos arroja el mismo resultado sin ningun problema aunque el metodo se llame igual.
animañ_habla(oveja1)







#practicas


palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

def itinera(palabra, lista, tupla):
    print(len(palabra))
    print(len(lista))
    print(len(tupla))


itinera(palabra, lista, tupla)










class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        

mago = Mago()
arquero = Arquero()
samurai = Samurai()

personajes = [arquero, mago, samurai]

for personaje in personajes:
    personaje.atacar()













class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")



mago = Mago()
arquero = Arquero()
samurai = Samurai()

def personaje_defender(personaje):
    personaje.defender()









#!metodos especiales (son los que comiensan con doble guion bajo y terminan igual. ej: __init__, __mro__,etc)




mi_lista = [1,1,1,1,1,1,1,1]
print(len(mi_lista))                      #?fuera de un objeto class pordemos usar metodos funciones como len, pero dentro de class NO, salvao usemos metodos especialses





class Objeto:
    pass

mi_objeto = Objeto()           
'''print(len(mi_objeto))'''                      #?aca vemos como nos da error al querer usar len dentro de un class






class Objeto:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones 
    def __str__(self):                                          #?usando el metodo __str__ es como que castearamos con str o list, osea transforma el contenido de lols atribuitos de nuestra clase en string y los podemos imprimir sin problemas
        return f"albun: {self.titulo} de {self.autor} en pista {self.canciones}"
    def __len__(self):                                          #?usando _len__ podemos hacer el conteo numerico digamos 
        return (self.canciones)
    def __del__(self):                                          #? con del solo no nos muestra nada, solo borra el objeto que le demos, pero usandolo dentro de un metodo __del__ podemos hacer que nos arroje un mensaje cuando se alla eliminado el objeto
        print("se elimino el cd")
        
mi_cd = Objeto("mana","quisiera",20)

print(mi_cd)
print(len(mi_cd))
del mi_cd











#practicas





class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'
        
mi_libro = Libro("traisionera", "mana", 20)

print(mi_libro)









class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas
        
libro = Libro("traisionera", "mana", 20)
print(len(libro))










class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")
        
libro = Libro("traisionera", "mana", 20)
del libro

























# Define la clase User
class User: 
  def __init__(self, username, password): 
    self.username = username 
    self.password = password 

  def create(self): 
    # obtiene los datos del usuario 
    username = input('Ingresa tu nombre de usuario: ') 
    password = input('Ingresa tu contraseña: ') 
    print('Usuario creado exitosamente: ') 
    print('Nombre de usuario: ' + username) 
    print('Contraseña: ' + password)





# crea una nueva instancia de la clase User 
user = User(" ", " ") 
user.create()

# imprime los detalles del usuario 
'''print('Usuario creado exitosamente: ') 
print('Nombre de usuario: ' + user.username) 
print('Contraseña: ' + user.password) 
'''
# crea un nuevo usuario 
```
````
