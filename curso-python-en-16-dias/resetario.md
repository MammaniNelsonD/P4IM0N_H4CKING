# 😀 RESETARIO

````python
// Some code

```python
#!recetario  BY PAIMON

from pathlib import Path


#!Funcion 1 conteo del total de resetas
home = Path.home()
ruta = Path(home,"Recetas")

def total_resetas():
    nombre = input("*"*60 +"\n Bienvenido Sr/a al recetario de ((DON PAIMON)) por favor diganos su nombre: \n"+ "*"*60+":")
    print(f"Muy Bien Sr/a {nombre} la ruta de directorio de las RECETAS es la siguiente {ruta} \n"+"*"*60)
    cantidad = 0
    for txt in Path(ruta).glob("**/*.txt"):                                                       #!funcion 1 ejem3  TERMINADA
        cantidad = cantidad + 1
    return (f"Y la cantidad total de recetas alojadas en nuestro sistema son: {cantidad}\n"+"*"*60) 

print(total_resetas())









#!funcion 2 elije usar el sistema y opciones a relizar, devuelve eleccion y opcion
def opciones():
    print(f"Porfavor a posterior le mostraremos una lista de acciones que puede realizar, e ingrese su numero de opcion a elejir: \n *****************************************************")
    print("[1]-Leer receta\n[2]-Crear receta\n[3]-Crear categoria\n[4]-Eliminar receta\n[5]-Eliminar categoria\n[6]-Finalizar programa \n *******************************************************")
    eleccion =input("Quiere usar nuestro sistema (si o no): ")
    opcion =int(input("Ingrese aqui la opcion que elije: "))
    return eleccion, opcion 
    




eleccion,opcion = opciones()




    
'''print("Esta es la lista de categotegorias: \n ----------------------------------------------")'''




#!funcion 3 por ahora funciona opcion 1 , 2 , 3 , 4 , 5 , 6
def elejir_opcion1(start,opcion):
    from pathlib import Path
    base = Path.home()
    rutaa = Path(base, "Recetas")
    while start == "si":
        print("Esta es la lista de categotegorias: \n ----------------------------------------------")
        if opcion == 1:                                                  #leer recetas
            for path in Path(rutaa).iterdir():                           #itera para ver los subdirectorios dentro de recetas
                if path.is_dir():
                    print(path.stem)
            categoria_elejida = input("Elija la Categoria de recetas que desea ver, con su respectivo nombre: ")
            recetas = Path(base, "Recetas", categoria_elejida)
            print("Estas son las recetas que tenemos en esta categoria: ")
            for txt in Path(recetas).glob("*.txt"):                      #itera para mostrar las recetas dentro de la categoria elejida
                print(txt.stem)  
            receta_elejida_leer = input("Elija la receta que desea leer con su respectivo nombre: ")
            leer_receta = Path(base, "Recetas", categoria_elejida, receta_elejida_leer+".txt")
            print(leer_receta.read_text()) 
            volver = input("-"*40+"\n Desea volver al menu de opciones, si (Y) o no (N)") 
            if volver == "Y":
                   opciones()
            else:
                '''print("---------Muchas gracias por usar el sistema--------")'''
                break       
              
        break
    while start == "si":
       
        if opcion == 2:                                                  #crear recetas
            for path in Path(rutaa).iterdir():                           #itera para ver los subdirectorios dentro de recetas
                if path.is_dir():
                    print(path.stem)
            categoria_elejida = input("Elija la Categoria de recetas que desea ver, con su respectivo nombre: ")      #elije la categoria donde creara la receta nueva
            new_recet = input(f"Muy bien estamos dentro de la categoria ({categoria_elejida}), designe el nombre de su receta: ")+".txt"       #ingresa el nombre de la receta a crear y agrego el formato txt
            recetas = Path(base, "Recetas", categoria_elejida, new_recet)                                                                      #ruta ya actualizada donde ingresara el nuevo nombre de receta 
            new_recet_creada = Path.touch(recetas)                                                                                              #variable de nueva receta ya creada dentro de la ruta anterior, pero vacia      
            contenido = input(f"Ingrese porfavor el contenido de su receta {new_recet}: ")                                                      #contenido de la receta por el usuario
            contenido_new_recet = Path(recetas)                                                                                                 #ruta de la receta con su noimbre creada
            contenido_new_recet.write_text(contenido)                                                                                           #con write ingreso el contenido ingresado por el usuario de la receta
            receta_final = open(contenido_new_recet)                                                                                            #abro el archivo
            print(receta_final.read())                                                                                                          #leo el archivo para que vea el usuario
            print(f"------------------------------------------------ \n Muy bien se añadio el contenido indicado en la receta ({new_recet})")
            volver = input("-"*40+"\n Desea volver al menu de opciones, si (Y) o no (N)") 
            if volver == "Y":
                   opciones()
            else:
                print("---------Muchas gracias por usar el sistema--------")
            break 
        break  
    while start == "si":
        
        if opcion == 3:                                                  #crear categoria
            for path in Path(rutaa).iterdir():                           #itera para ver los subdirectorios dentro de recetas
                if path.is_dir():
                    print(path.stem)
            categoria_crear = input("Muy bien estams dentro del directorio de categorias, Designe el nombre de la categoria a crear: ")      #elije nombre la categoria a crear
            ruta = Path(base, "Recetas",categoria_crear)                                                                                     #ruta de la categoria a crear                        
            ruta.mkdir(parents=True)                                                                                                         #con mkdir creamos el directorio categoria, en la ruta indicada
            for path in Path(rutaa).iterdir():                                                                                               #itinero nuevamente para mostrar al usuario que su categoria se creo correctamente
                if path.is_dir(): 
                    print(path.stem) 
            print(f"---------------------------------------------- \n muy bien su categoria ({categoria_crear}) ya fue creada")                                                                                                            
            volver = input("-"*40+"\n Desea volver al menu de opciones, si (Y) o no (N)") 
            if volver == "Y":
                   opciones()
            else:
                print("---------Muchas gracias por usar el sistema--------")
            break
        break    
            
         
    while start == "si":
        
        if opcion == 4:                                                  #eliminar recetas
            '''print("Esta es la lista de categotegorias: \n ----------------------------------------------")'''
            for path in Path(rutaa).iterdir():                           #itera para ver los subdirectorios dentro de recetas
                if path.is_dir():
                    print(path.stem)
            categoria_elejida = input("Elija la Categoria de recetas que desea ver, con su respectivo nombre: ")
            recetas = Path(base, "Recetas", categoria_elejida)
            print("Estas son las recetas que tenemos en esta categoria: ")
            for txt in Path(recetas).glob("*.txt"):                      #itera para mostrar las recetas dentro de la categoria elejida
                print(txt.stem)  
            receta_elejida_aeliminar = input("Elija la receta que desea ELIMINAR con su respectivo nombre: ")+".txt"        #nombre de la receta a elliminar agregado .txt
            ruta_recet_a_eliminar = Path(base, "Recetas", categoria_elejida, receta_elejida_aeliminar)                      #ruta de la receta a eliminar
            ruta_recet_a_eliminar.unlink()                                                                                  #con unlink nos permite eliminar archivos que le demos en la ruta indicada
            for txt in Path(recetas).glob("*.txt"):
                print(txt.stem)
            print(f"-------------------------------------------- \n Muy bien su receta ({receta_elejida_aeliminar} se elimino correctamente")
            volver = input("-"*40+"\n Desea volver al menu de opciones, si (Y) o no (N)") 
            if volver == "Y":
                    opciones()
            else:
                print("---------Muchas gracias por usar el sistema--------")
            break
        break
         
    while start == "si":
        
        if opcion == 5:                                                  #eliminar categorias
            for path in Path(rutaa).iterdir():                           #itera para ver los subdirectorios de categorias dentro de recetas
                if path.is_dir():
                    print(path.stem)
            categoria_elejida_a_eliminar = input("Elija la Categoria que desea ELIMINAR, con su respectivo nombre: ")
            ruta_categoria_a_eliminar = Path(base, "Recetas", categoria_elejida_a_eliminar)
            ruta_categoria_a_eliminar.rmdir()
            for path in Path(rutaa).iterdir():                           #itera para ver los subdirectorios de categorias dentro de recetas y demostrar que se elimino correctamente
                if path.is_dir():
                    print(path.stem)
            print(f"------------------------------------------- \n Muy bien su categoria ({categoria_elejida_a_eliminar}) fue eliminada correctamente")        
            volver = input("-"*40+"\n Desea volver al menu de opciones, si (Y) o no (N)") 
            if volver == "Y":
                   opciones()
            else:
                print("---------Muchas gracias por usar el sistema--------")
            break
        break   
    while start == "si":
        if opcion == 6:
            print("-------Muy bien, muchas gracias por usar mi sistema ----------")  
        break    
    
               

            
        
    


elejir_opcion1(eleccion,opcion)
```
````

CODEO DEL DIA 6:

````python
// Some code

```python
#!dia 6

#manipulacion de archivos

'''mi_archivo = open("ejemplo1.txt")              #?guardamos nuestro archivo que esta en nuestra ruta, dentro de esta variable

print(mi_archivo)'''                              #?nos imprime descripciones del archivo, no su contenido





'''print(mi_archivo.read())                       #?ahora si con elñ metodo READ, nos permite imprimir su contenido




linea1 = mi_archivo.readline()                    #?nos lee la primer linea del comntenido
print(linea1)''' 






'''linea1 = mi_archivo.readline()                    #?nos lee la primer linea del comntenido
print(linea1) 
linea1 = mi_archivo.readline()                    #?pero al ejecutarlo de nuevo, nos imprime la siguiente linea 2 por que queda en la memoria de readline el progreso de lectura anterior , por tanto sigue desde ahi y nos imprime la que sigue
print(linea1) 
linea1 = mi_archivo.readline()                    #?pero al ejecutarlo de nuevo, nos imprime la siguiente linea 2 por que queda en la memoria de readline el progreso de lectura anterior , por tanto sigue desde ahi y nos imprime la que sigue
print(linea1)''' 






'''linea1 = mi_archivo.readline()                    #?nos lee la primer linea del comntenido
print(linea1.rstrip())                              #?hace que se quite el salto de linea, y se imprime sin ese espacio entra medio
linea1 = mi_archivo.readline()                    #?pero al ejecutarlo de nuevo, nos imprime la siguiente linea 2 por que queda en la memoria de readline el progreso de lectura anterior , por tanto sigue desde ahi y nos imprime la que sigue
print(linea1.upper())                               #?nos imprime el texto en mayuscula
linea1 = mi_archivo.readline()                    #?pero al ejecutarlo de nuevo, nos imprime la siguiente linea 2 por que queda en la memoria de readline el progreso de lectura anterior , por tanto sigue desde ahi y nos imprime la que sigue
print(linea1)''' 





#readlines nos imprime todas las lineas de nuestro archivo dentro de una lista por separado
'''todas = mi_archivo.readlines()
print(todas)'''




#con pop eliminamos la ultima linea de nuestro archivo y la podemos guardar en una variable para imprimirla
'''eliminar_ultima = mi_archivo.pop() 
print(eliminar_ultima)'''





#podemos itinerar con un loop FOR para que nos imprima cada linea
'''for l in mi_archivo:
    print("En esta linea dice: "+l)'''






#practicas


'''archivo = open("texto.txt")
print(archivo.read())'''





'''archivo = open("texto.txt")
print(archivo.readline())

archivo.close()'''




'''archivo = open("texto.txt")
linea2 = archivo.readline()
linea2 = archivo.readline()
print(linea2)'''




'''mi_archivo.close() '''    #?nos produce el cierrre del archivo





#crear y escribir archivos 
'''archivo = open("ejemplo2.txt","r")                       #?OPEN tiene otro segundo parametro para darle R que es de read lectura
archivo.write("nuevo texto ingresado al archivo")           #?con write nos permite escribir sobre un archivo, pero en este caso estamos con el segundo parametro anterior en permisos para read ler, asi que nos dara error, tenemos que cambiarlo a A o W
print(archivo.read())
archivo.close()'''





'''archivo = open("ejemplo2.txt","w")                       #?OPEN tiene otro segundo parametro para darle W que es de write escribir y si el archivo existe lo borra al contenido e ingresa lo que le escribamos, y si este no existe lo crea con el contenido dado
archivo.write("nuevo texto ingresado al archivo")           #?con write nos permite escribir sobre un archivo, pero en este caso estamos con el segundo parametro anterior en permisos para read ler, asi que nos dara error, tenemos que cambiarlo a A o W
print(archivo.read())
archivo.close()'''





'''archivo = open("ejemplo2.txt","a")                                        #?OPEN tiene otro segundo parametro para darle A que es escribir a partir de la ultima linea del contenido del archivo existente
archivo.write("mentira YO soy el nuevo texto ingresado al archivo")       #?con write nos permite escribir sobre un archivo, pero en este caso estamos con el segundo parametro anterior en permisos para read ler, asi que nos dara error, tenemos que cambiarlo a A o W (write, al escribir varias veces no nos da saltos de linea se los tenemos qie dar nosotros co \n)
print(archivo.read())
archivo.close()'''





'''archivo = open("ejemplo3.txt","r")                                        #?OPEN tiene otro segundo parametro para darle W y creao otro archivo en este caso
archivo.writelines(["mentira","soy","nuevo","texto","ingresado","archivo"])      #?con writelines nos permite escribir lineas, y nos permite pasar lista de string (es medio inesesario por que te escribe toda una linea junta, y se podria usar mejor for )
print(archivo.read())
archivo.close()'''



#!nos da muchas opciones esto de crear o modificar archivos y sobrescribir
#asi con FOR podemos hacer los ingresos por separado, sacando los elementos de una lista dada
'''archivo = open("ejemplo3.txt","r")

lista = ["mentira","soy","nuevo","texto","ingresado","archivo"]

for p in lista:
    archivo.write(p + " ")
    print(archivo.read())'''





#practicas



'''archivo = open("mi_archivo.txt","w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt","r")
print(archivo.read())'''





#Práctica Crear y Escribir Archivos 2
#Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

#Imprime el contenido completo de "mi_archivo.txt" al finalizar.

#Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.

'''archivo = open("mi_archivo.txt","a")
archivo.writelines("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt","r")
print(archivo.read())'''







#Práctica Crear y Escribir Archivos 3
#Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

#registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

#Imprime el contenido completo de "registro.txt" al finalizar.

#Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.

'''archivo = open("registro.txt","a")
registro_ultima_sesion = ["Federico", "\t20/12/2021", "\t08:17:32 hs", "\tSin errores de carga"]
archivo.writelines(registro_ultima_sesion)
archivo.close()
archivo = open("registro.txt","r")
print(archivo.read())'''







#rutas de directorios para abrir o manipular archivos utilizando OS o PATH

#!EN WINDOWS : la ruta se define con doble barras invertidas por lo que se manda la misma como un string y si no no se toma la barra invertida, ej: ("C:\\users\\mipc\\archivo.txt")

#?EN MAC o LINUX se escribe la linea como string entre comillas tambien, pero con barra normal, ej: ("C:/users/mipc/archivo.txt")


#!---------MODULO OS  --------------------

import os                                                  #?importamos el moulo OS




ruta = os.getcwd()                                         #?el metodo GET nos permite ver la ruta del directorio actual que le demos





ruta = os.chdir("C:\\users\\mipc")                         #?el metodo CHDIR  significa, cambiar directorio, osea que es la que nos permite abrir archivos fuera de nuestro directorio actual
archivo = open("archivo.txt")                              #?ahora que por ejemplo ya le dimos e imaginariamente estamos en otra ruta, a posterior si nos dejara abrirlo con OPEN a pesar de no estar realmente en ese directorio
print(archivo.read())





ruta = os.makedirs("C:\\users\\mipc\\nuevodirectorio")         #?MAKEDIRS nos permite crear una carpeta osea otro directorio, en este ejemplo en la ruta que le emos dado creamos la carpeta NUEVODIRECTORIO





ruta = "C:\\users\\mipc\\archivo.txt"                         #?nos creamos la ruta con el archivo que queremos        
elemento = os.path.basename(ruta)                             #?con OS.PATH.BASENAME nos muestra el nombre de base osea el nombre del archivo
print(elemento)                          





ruta = "C:\\users\\mipc\\archivo.txt"                         #?nos creamos la ruta con el archivo que queremos        
elemento = os.path.dirname(ruta)                              #?con OS.PATH.DIRNAME nos muestra la ruta del archivo que le dimos
print(elemento)






#tambien se puede recibir ambos elementos BASENAME y DIRNAME en una tupla ceparados
ruta = "C:\\users\\mipc\\archivo.txt"                         #?nos creamos la ruta con el archivo que queremos        
elemento = os.path.split(ruta)                                #?con OS.PATH.SPLIT nos permite dividir como se lo usa tambien, y nos devuelve ambos eleementos en una tupla ceparados
print(elemento)





os.rmdir("C:\\users\\mipc\\archivo.txt")                      #?RMDIR nos permite remover el directorio(carpeta) que le indiquemos en la ruta





#podemos abrir un archivo indicandole la ruta del mismo 
archivo = open("C:\\users\\mipc\\archivo.txt")
print(archivo.read())






#!------------ MODULO PATHLIB y su OBJETO PATH -------------------(nos permite manipularlo con cualquier sistema operativo)




from pathlib import Path                  #?importamos el modulo PATHLIB y su OBJETO PATH

ruta = Path("C:/users/mipc")              #?poniendo que lo abrimos con PATH y su ruta del proximo archivo que le vamos a concatenar a esta variable abajo: (de esta forma con PATH tambien permitimos que se pueda abrir con cualquier sistema operativo, principalmemte linux, mac y hastab windows)
archivo = ruta / "archivo.txt"            #?aca concatenamos la variable RUTA con el numbre dekl archivo a abrir
mi_archivo = open(archivo)                #?le damos la orden de abrir nuestro archivo
print(mi_archivo.read())                  #?e imprimimos la lectura READ




#otra forma de hacer lo mismo anterior
ruta = Path("C:/users/mipc") / "archivo.txt"
mi_archivo = open(ruta)
print(mi_archivo.read())




#!PATHLIB


#PATHLIB nos permite realizar mas cosas de una forma mas facil, en este ejemplo, lo abrimos y leemos a la ves al archivo, usando directamente READ_TEXT() sin nececitar OPEN y luego READ como en OS
carpeta = Path("C:/users/mipc/archivo.txt")
print(carpeta.read_text())                   #?READ_TEXT nos lee el archivo





carpeta = Path("C:/users/mipc/archivo.txt")
print(carpeta.name())                        #?NAME nos da el nombre del archivo





carpeta = Path("C:/users/mipc/archivo.txt")
print(carpeta.suffix())                      #?SUFFIX nos muestra la extencion o tipò de archivo





carpeta = Path("C:/users/mipc/archivo.txt")
print(carpeta.stem())                        #?STEM nos da solo el nombre del archivo sin su extencion 





#podemos ver si un archivo existe o no, con EXISTS
carpeta = Path("C:/users/mipc/archivo.txt")
if not carpeta.exists():                     #?EXISTS nos permite ver si existe o no uun archivo, y si no existe como le dijimos de condicion con el IF, nos devolvera true por ende imprimira lo siguiente:
    print("este archivo no existe")
else:
    print("el archivo si existe")





#importando a la ves PUREWINDOWSPATH nos imprime la ruta pura en el formato de windows con las baras imvertidas
from pathlib import Path, PureWindowsPath
carpeta = Path("C:/users/mipc/archivo.txt")
ruta_pura = PureWindowsPath(carpeta)                              #?con PUREWINDOWSPATH le entregamos la ruta y nos la va a devolver luego con el print la ruta pura con el formato de windows
print(ruta_pura)




#!PATH 


from pathlib import Path


guia = Path("perro","gato","sapo","dinosaurio.txt")              #?con PATH nos genera cualquier string que le demos como rutas, nos generara directorios en ese orden jerarquico y cada uno con el nombre de cada string que le dimos, y en este caso tambien nos creara dentro de la ultima carpeta o directorio SAPO, un archivo DINOSAURIO.TXT (nos lo devolvera con la ruta pura del sistema operativo que estemos usando)(nos dara una ruta alternativa donde se empesara a crear los directorios dados, por que no le especificamos en este caso)
print(guia)




base = Path.home()                                               #?nos da la ruta absoluta de HOME para a posterior aportarla a la guia ruta , para que a partir de ese directorio se agregue y concatenen los otros directorios que le dimos de ruta mas el archivo txt.        
guia = Path(base, "perro","gato","sapo","dinosaurio.txt")
print(base)
print(guia)







base = Path.home() 
guia = Path(base, "perro","gato","sapo","dinosaurio.txt")
guia2 = guia.with_name("auto.txt")                              #?con WITH_NAME nos permite utilizar el mismo noobre de ruta anterior y crear un archivo o directorio dentro de el tambien
print(guia)
print(guia2)









base = Path.home()
guia = Path(base, "perro","gato","sapo","dinosaurio.txt")
print(guia.parent)                                              #?PAREN nos imprime el directorio pariente ultimamente creado, y si lo ejecutamos vuelve a realizarlo imprimiendo la carpeta que le siga como decendiente







#podemos hacer que con un loop nos imprima los archivos dentro de un directorio, o tambien los archivos dentro de un directorio y ramificandoce tambien a imprimir el contenido de archivos dentro de directorios dentro del principal
base = Path.home()
guia = Path(base, "perro","gato","sapo","dinosaurio.txt","pantera.txt")   #?le pasariamos hasta la ruta SAPO, en el ejemplo pongo vicible los TXT nomas, pero no irian
for txt in Path(guia).glob("*.txt"):                                      #?con un loop,que itinere con el metodo GLOB nos va a implimir *.TXT todos los rutas de archivos TXT dentro de esa carpeta solamente
    print(txt)                                                            #?e imprimimos esos TXT en este caso sus rutas dinosaurio.txt","pantera.txt







base = Path.home()
guia = Path(base, "perro","gato","sapo","dinosaurio.txt","pantera.txt")      #?le pasariamos hasta la ruta SAPO, en el ejemplo pongo vicible los TXT nomas, pero no irian
for txt in Path(guia).glob("**/*.txt"):                                      #?con un loop,que itinere con el metodo GLOB nos va a implimir con **/*.TXT todos los rutas de archivos TXT dentro de esa carpeta y a la ves se ramificara y obtendra los txt dentro de los directorios que estan dentro de el tambien, dandonos sus rutas
    print(txt)                                                               #?e imprimimos esos TXT









#practica



from pathlib import Path
ruta_base = Path.home()




from  pathlib import Path 
ruta = Path("Curso Python","Día 6","practicas_path.py")





from pathlib import Path
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")







#LIMPIAR CONSOLA

from os import system                                   #? importando system nos va a permitir en este caso borrar lo que ingresan en la consoa cuando lo ejecutemos

nombre = input("dime tu nombre: ")
edad =  input("dime tu edad: ")
system("clear")                                         #?aca los ejecutamos con SYSTEM(clear) o (cls) y nos borraa todo lo anterior, para limpiar la consola y solo quede el print que le sigue, ahi que configurar el IDE utilizado para usarlo

print(f"tu nombre es {nombre} y tu edad es {edad}")







#!podemos tener funciones ejecutando la apertura de archivos, como ejemplo con archivo.open() etc.





#practica



def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()






def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("contenido eliminado")





def registro_error(archivo):
    mi_archivo = open(archivo, "a")
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()

```
````
