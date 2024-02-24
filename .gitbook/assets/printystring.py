#print nmeros y comillas

print("hola mundo")

print("hola \"gente\" como estan")       #lo que sigue de la barra lo trata como caracter especial

print('this isn\'t a number')     

print('this isn\\t a number')

print("hola mundo como estan 'pongo comillas'")

print(50)

print("50 + 50")


#cadenas de strings, espacios

print("hola" + 'drako')

print("hola " + 'drako')

print("hola" + ' drako')

print("hola" + "" + 'drako')

print("hola" + " " + 'drako')


#dos lineas dentro de un mismo print

print("hola como estas\nya te queria ver mano")      

#para dar una sangria o espacio al principio, osea tabular y da cuatro espacios

print("\thola como estas ya te queria ver mano")

print('this isn\'t a number')


#practicas

print("A\tB\tC\nD\tE\tF\nG\tH\tI")

print("Barra Normal: /\nBarra Invertida: \\")


#uso de input , ingreso de datos

input("ingresa tu nombre aqui: ")              #ingreso de datos pero no lo guarda

print(input("ingresa tu nombre aqui: "))       #ingreso de datos pero no lo guarda, pero lo imprime

#usando a la ves concatenacion en la repuesta (entre texto y una funcion)
print("Ya lo se..!! Usted se llama "+input("ingresa tu nombre aqui: "))

print("Ya lo se..!! Usted se llama "+input("ingresa tu nombre aqui: ")+" "+input("ingrese su apellido: "))
