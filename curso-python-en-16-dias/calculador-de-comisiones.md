# 😃 CALCULADOR DE COMISIONES

````python
// Some code

```python
print("<<Bienvenido a su asistente de ganancias mensuales>>")
nombre = input(str("Ingrese por favor su nombre completo: "))
venta_total = input("ingrese el total vendido hasta este momento: ")
ganancia_total = float(venta_total)*13/100
ganancia_total = round(ganancia_total,2)
print(f"Sr. {nombre} sus ganancias totales hasta este momento son de ${ganancia_total}\n Espero le alla servido de ayuda, BUENOS DIAS")

```
````

CODEO APRENDIENDO LOS CONCEPTOS DEL DIA 2

````python
// Some code

```python
#variable para guardar un dato y print, y se va ejecutando de arriba para abajo aunque le demos el mismo nombre.

nombre = "david"
print(nombre)


nombre = "pedro"
print(nombre)

#sumando o concatenando variables

edad = 50
edadd = 50
print(edad+edadd)


nombre = input("di tu nombre: ")
print("tu nombre es "+ nombre)


nombre = "hola"
nombre2 = "python"
frase = nombre +" "+ nombre2
print(frase)


curso = "Python"
print("Estas tomando un curso de "+curso)

#numeros integers y float

mi_numero = 5
print(mi_numero)


mi_numero = 5 + 5
print(mi_numero + mi_numero)


mi_numero = 5 + 5
print(mi_numero - mi_numero)

mi_numero = 5.5
print(mi_numero + mi_numero)

mi_numero = 5.5
mi_numero = mi_numero + mi_numero
print(mi_numero)

mi_numero = 5 + 5.5
print(mi_numero)


#para que nos imprima el tipo de una variable que consultemos

print(type(mi_numero))


#edad = input("dime tu edad: ")   #todo ingreso input lo toma como string, a no ser que se especifique con conversiones (explisitas o implicita)
#print("tu edad es "+ edad)
#nueva_edad = 1 + edad
#print("El año entrante ya tendras "+nueva_edad+" "+"años")


num1 = 7.5
num2 = 2.5
print(type(num1+num2))


#conversiones inplicitas y explicitas

num1 = 20
num2 = 30.5
num1 = num1 + num2
print(type(num1))
print(type(num2))


num1 = 5.8
print(num1)
print(type(num1))

#conversion forzada, directamente resto los decimales, no lo redondea

num2 = int(num1)
print(num2)
print(type(num2))


edad = input("dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print(nueva_edad)



num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))


#uso de format o literales, y declarar las variables con f y luego dentro de las llaves (cadenas literales), o en el orden  que van (funcion format)

#normal
d = 20
h = 20
print("mis numeros son "+ str(d)+" y "+str(h))

#funcion format
d = 20
h = 20
print("mis numeros son {} y {}".format(d,h))

#cadenas literales
d = 20
h = 20
print(f"mis numeros son {d} y {h}")

color = "azul"
matricula = 5566
print(f"el auto es de color {color} y su matricula es {matricula}")



#practicas
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")



puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_anteriores+puntos_nuevos
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")


#operaciones matematicas

x = 6
o = 6
z = 7
print(f"{x} mas {o} es igual a {x+o}")
print(f"{x} menos {o} es igual a {x-o}")
print(f"{x} por {o} es igual a {x*o}")
print(f"{x} dividido {o} es igual a {x/o}")
#divicion al piso sin decimales
print(f"{z} dividido al piso de {o} es igual a {z//o}")
#divicion modulo, el restante de una division con numero enteros (osea lo que sobra de una division, el resto)
print(f"{z} modulo de {o} es igual a {z%o}")
#la potencia o elevado
print(f"{x} elevado a la {o} es igual a {x**o}")
#elevado al cubo
print(f"{x} elevado a la {3} es igual a {x**3}")
#la raiz cuadrada
print(f"La raiz cuadradad de {o} es igual a {x**0.5}")



#practicas

print(f"{874//27}")

print(f"{456%33}")

print(f"{783**0.5}")




#redondeao round (ej: 5.3 redodea a 5, 5.5 redondea a 6, 5.8 redondea a 6)

print(90/7)


print(round(90/7))


resultado = round(90/7)
print(resultado)


#deja elegir despues de la coma hasta cuantos numeros decimales queremos que se muestren
valor = round(96.77777777777,3)
print(valor)


valor = round(96.77777777777)
print(valor)
print(type(valor))


valor = 96.77777777777
print(round(valor))
print(type(valor))



#practicas

print(round(10/3,2))

print(round(5**0.5,4))



print(type(7.5 + 2.5))


num1 = 13.87
print(round(num1))     #redondea para arriba
print(int(num1))       # le saca los decimales irectamente




num1 = round(13/2,0)
print(type(num1))
```
````

