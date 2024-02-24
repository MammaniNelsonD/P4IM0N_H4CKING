# 😀 RECONOCIMIENTO FACIAL PARA CONTROL DE ASISTENCIA

````python
// Some code

```python
#!P4IMReconFacial.py - OFICIAL TERMINADO - es un control de asistencia que utiliza el reconocimiento facial - By P4IM0N & gpt

#?------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!explicacion de librerias
#?cv2 - es parte de OpenCV y se utiliza para el procesamiento de imágenes y visión por computadora.
#?face_recognition - es utilizada para el reconocimiento facial en imágenes y videos.
#?import csv - Permite trabajar con archivos CSV (Comma-Separated Values) para leer y escribir datos tabulares.
#?from datetime import datetime, timedelta - Permite trabajar con fechas y horas. datetime proporciona funciones y métodos para manipular fechas y horas, mientras que timedelta permite representar y realizar operaciones con diferencias de tiempo.
#?import os - Proporciona funciones para interactuar con el sistema operativo, como crear, renombrar o eliminar archivos y directorios, obtener información del sistema

#?------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!IMPORTANTE - INSTALACION DE LIBRERIAS E INDICACIONES
#para instalar las librerias necesarias ejecutamos los siguientes comandos (pip install opencv-python) y (pip install face_recognition)

#?------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!IMPORTAMOS LIBRERIAS NECESARIAS
import os
import cv2
import face_recognition
import csv
from datetime import datetime, timedelta



#?------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!BANNER
print('''
__________  _____ .___   _____ __________                           ___________             .__       .__   
\______   \/  |  ||   | /     \\______   \ ____   ____  ____   ____ \_   _____/____    ____ |__|____  |  |  
 |     ___/   |  ||   |/  \ /  \|       _// __ \_/ ___\/  _ \ /    \ |    __) \__  \ _/ ___\|  \__  \ |  |  
 |    |  /    ^   /   /    Y    \    |   \  ___/\  \__(  <_> )   |  \|     \   / __ \\  \___|  |/ __ \|  |__
 |____|  \____   ||___\____|__  /____|_  /\___  >\___  >____/|___|  /\___  /  (____  /\___  >__(____  /____/
              |__|            \/       \/     \/     \/           \/     \/        \/     \/        \/      
                                                                                 By P4IM0N & gpt
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

#?------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!RUTAS principales de EMPLEADOS BASE DE DATOS e ITERACION para obtener cada imagen de cada uno y codificarla para su posterior comparacion con .face_recognition.compare_face
# Obtener la lista de nombres de los empleados desde la carpeta "empleados"
base_de_datos_path = "Empleados/"
# Obtenemos la ruta de la carpeta donde se encuentran los empleados.

lista_empleados = [os.path.splitext(empleado)[0] for empleado in os.listdir(base_de_datos_path)]
# Utilizamos os.listdir para obtener una lista de archivos en la carpeta especificada.
# Usamos os.path.splitext para dividir el nombre del archivo y la extensión, y obtener solo el nombre.

# Cargar las imágenes y codificarlas
lista_empleados_codificados = []
# Inicializamos una lista para almacenar las codificaciones faciales de los empleados.

for empleado in lista_empleados:
    # Cargar la imagen del empleado desde la carpeta "empleados"
    imagen_empleado = face_recognition.load_image_file(base_de_datos_path + empleado + ".jpg")
    # Utilizamos face_recognition.load_image_file para cargar la imagen del archivo especificado.

    # Codificar la imagen del empleado para su reconocimiento facial
    codificacion_empleado = face_recognition.face_encodings(imagen_empleado)[0]
    # Utilizamos face_recognition.face_encodings para codificar la imagen y obtener las características faciales.

    # Agregar la codificación del empleado a la lista de empleados codificados
    lista_empleados_codificados.append(codificacion_empleado)

# Inicializar la cámara
cam = cv2.VideoCapture(0)
# Utilizamos cv2.VideoCapture para inicializar la cámara.

# Crear un diccionario para almacenar la última asistencia registrada de cada empleado
ultima_asistencia = {}

#?------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!LOOP principal para mantener el sistema corrriendo y capturando imagen para su comparacion
while True:
    # Capturar imagen de la cámara
    ret, imagen_capturada = cam.read()
    # Utilizamos cam.read para capturar una imagen de la cámara.

    # Convertir la imagen a formato RGB (necesario para face_recognition)
    imagen_capturada_rgb = cv2.cvtColor(imagen_capturada, cv2.COLOR_BGR2RGB)
    # Utilizamos cv2.cvtColor para convertir la imagen de BGR (formato de OpenCV) a RGB.

    # Detectar caras en la imagen capturada
    ubicacion_caras = face_recognition.face_locations(imagen_capturada_rgb)
    # Utilizamos face_recognition.face_locations para detectar las ubicaciones de las caras en la imagen.

    codificacion_caras = face_recognition.face_encodings(imagen_capturada_rgb, ubicacion_caras)
    # Utilizamos face_recognition.face_encodings para codificar las caras detectadas y obtener sus características.

    # Comparar las caras detectadas con las imágenes de los empleados
    for codificacion_cara, ubicacion_cara in zip(codificacion_caras, ubicacion_caras):
        resultados_comparacion = face_recognition.compare_faces(lista_empleados_codificados, codificacion_cara, tolerance=0.5)
        # Utilizamos face_recognition.compare_faces para comparar las caras detectadas con las caras de los empleados.

        nombre_empleado = "Desconocido"

        if True in resultados_comparacion:
            indice_empleado = resultados_comparacion.index(True)
            nombre_empleado = lista_empleados[indice_empleado]
            # Si se encuentra una coincidencia, obtenemos el nombre del empleado correspondiente.
        else:
            nombre_empleado = f"Desconocido_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        with open('registro_asistencia.csv', 'r') as archivo_csv:
            reader = csv.reader(archivo_csv)
            ultima_asistencia = None

            # Obtener la última asistencia registrada para el empleado actual
            for row in reversed(list(reader)):
                if len(row) > 0 and row[0] == nombre_empleado:
                    ultima_asistencia = datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
                    break

            # Verificar si ha pasado un intervalo de 8 horas desde la última asistencia
            if ultima_asistencia is None or datetime.now() - ultima_asistencia >= timedelta(hours=8):

                # Dibujar un rectángulo alrededor de la cara detectada
                y1, x2, y2, x1 = ubicacion_cara
                color = (0, 255, 0) if nombre_empleado != "Desconocido" else (0, 0, 255)
                cv2.rectangle(imagen_capturada, (x1, y1), (x2, y2), color, 2)
                # Utilizamos cv2.rectangle para dibujar un rectángulo alrededor de la cara detectada.

                # Escribir el nombre del empleado en el rectángulo
                cv2.putText(imagen_capturada, nombre_empleado, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
                # Utilizamos cv2.putText para escribir el nombre del empleado en el rectángulo.

                # Guardar los datos en un archivo CSV
                with open('registro_asistencia.csv', 'a', newline='') as archivo_csv:
                    writer = csv.writer(archivo_csv)
                    writer.writerow([nombre_empleado, datetime.now()])
                # Abrimos un archivo CSV y utilizamos csv.writer para escribir los datos de asistencia.

                if nombre_empleado == "Desconocido":
                    if not os.path.exists("Desconocidos"):
                        os.makedirs("Desconocidos")
                    # Crear directorio "Desconocidos" si no existe
                
                if "Desconocido" in nombre_empleado:
                    # Guardar la captura de la persona desconocida como un archivo JPG
                    nombre_captura = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
                    ruta_captura = "Desconocidos/" + nombre_captura
                    cv2.imwrite(ruta_captura, imagen_capturada)

                    # Guardar los datos en el archivo CSV
                    with open('registro_asistencia.csv', 'a', newline='') as archivo_csv:
                        writer = csv.writer(archivo_csv)
                        writer.writerow(["Desconocido", datetime.now(), nombre_captura])
                else:
                    nombre_empleado = "Desconocido"
                    # Si no hay coincidencia, establecemos el nombre del empleado como "Desconocido".

                    
            
    # Dibujar un rectángulo alrededor de la cara detectada
    y1, x2, y2, x1 = ubicacion_cara
    color = (0, 255, 0) if nombre_empleado != "Desconocido" else (0, 0, 255)
    cv2.rectangle(imagen_capturada, (x1, y1), (x2, y2), color, 2)
    # Utilizamos cv2.rectangle para dibujar un rectángulo alrededor de la cara detectada.

    # Escribir el nombre del empleado en el rectángulo
    cv2.putText(imagen_capturada, nombre_empleado, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    # Utilizamos cv2.putText para escribir el nombre del empleado en el rectángulo.

    # Mostrar la imagen capturada con las detecciones y nombres de los empleados
    cv2.imshow('Asistencia de Empleados', imagen_capturada)
    # Utilizamos cv2.imshow para mostrar la imagen capturada con las detecciones y nombres de los empleados.

    # Detener el bucle si se presiona la tecla 'q'
    key = cv2.waitKeyEx(1)
    # cv2.waitKeyEx(1) espera durante 1 milisegundo la entrada del teclado y devuelve un valor numérico.

#?------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!PARAMOS EL LOOP al precionar Q para cerrar el sistema
    if key == ord('q'):
        break
        # Si el valor numérico de la tecla presionada coincide con el valor numérico de 'q' (113),
        # se sale del bucle y se cierra la aplicación.


#?------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!CERRAMOS LA VENTANA Y REINICIAMOS LA CAMARA
# Liberar la cámara y cerrar las ventanas
cam.release()
cv2.destroyAllWindows()
# Liberamos la cámara y cerramos las ventanas abiertas.
```
````

CODEO DIA 14:

````python
// Some code

```python
#!P4IMreconFacial - PRACTICA 1 - es un control de asistencia que utiliza el reconocimiento facial - By P4IM0N

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!explicacion de librerias
#?cv2 - es parte de OpenCV y se utiliza para el procesamiento de imágenes y visión por computadora.
#?face_recognition - es utilizada para el reconocimiento facial en imágenes y videos.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!IMPORTANTE - INSTALACION DE LIBRERIAS E INDICACIONES
#para instalar las librerias necesarias ejecutamos los siguientes comandos (pip install opencv-python) y (pip install face_recognition)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!IMPORTAMOS LIBRERIAS 
import cv2
import face_recognition
import os 

import pygame
import pygame.camera


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!BASE DE DATOS
ruta = 'Empleados'                                   #?ruta donde estan las fotos de la base de datos de empleados 
imagen_capturada = []
nombre_empleado = []
lista_empleado = os.listdir(ruta)                    #?creo una variable que cguardara los nombres de todos los elementos capturados por el metodo .listdir dentro de la ruta ingresada como parametro, osea en este cado lo que hay dentro del directorio Empleados 

print(lista_empleado)

for nombre in lista_empleado:                             #?revisaremos con un loop que por cada nombre que encuentre dentro de la lista de elementos optenidos dentro del directorio Empleados
    imagen_actual = cv2.imread(os.path.join(ruta, nombre))#?con cv2 y el metodo .imread y dandole la ruta armandola con las variables digamos de forma dinamica por cada una que tiene que ir leyendo
    imagen_capturada.append(imagen_actual)                #?y cada una de klas imagenes leidas y obtenidas las guardaremos con .append denro de la lista que estaba vacia llamada imagen_capturada
    nombre_empleado.append(os.path.splitext(nombre)[0])   #?luego obtenemos y guardamos cada nombre de empleado, osea el nombre puro de cada elemento sin su extencion, utilizando append para agregarlo, y antes capturamos solo el nombre puro con os.path.splitext seleccionando solo el nombre indicandole su indice [0] para qeu lo devielva y guarde sin su extencion, osea sin su .jpg digamos.
    
print(nombre_empleado)    

#!deberia codifivcarlas aca y tambien location de caras (o quisas no es necesario es solo ubiacr la cara)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!CODIFICAR IMAGENES de la BASE DE DATOS
#funcion que preparara las imagenes para luego ser codificadas y poder ser tratadas a posterior para ser comparadas con face.recognition 
def codificar_img(imagenes):
    
    #lista de imagenes codificadas
    lista_img_codificada = []
    
    #pasar todas las imagen a formato rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        
        #codificador
        imagen_codificada = face_recognition.face_encodings(imagen)[0]
        
        #agregar ala lista
        lista_img_codificada.append(imagen_codificada)
        
    #devolver la lista de las imagenes ya codifiucadas
    return lista_img_codificada


lista_empleados_codificados = codificar_img(imagen_capturada)

'''print(len(lista_empleados_codificados))'''    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!CODIFICAR IMAGENES del EMPLEADO A SER CONTROLADO
#funcion que preparara las imagenes para luego ser codificadas y poder ser tratadas a posterior para ser comparadas con face.recognition 
'''def codificar_img_para_comparar(imagenes):
    
    #lista de imagenes codificadas
    lista_img_para_comparar_codificada = []
    
    #pasar todas las imagen a formato rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        
        #codificador
        imagen_codificada = face_recognition.face_encodings(imagen)[0]
        
        #agregar ala lista
        lista_img_para_comparar_codificada.append(imagen_codificada)
        
    #devolver la lista de las imagenes ya codifiucadas
    return lista_img_para_comparar_codificada'''

#imagen_para_comparar = codificar_img_para_comparar(imagen_capturada)

'''def codificar_img_para_comparar(imagenes):
    
    
    
    #pasar todas las imagen a formato rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        
        #codificador
        imagen_codificada = face_recognition.face_encodings(imagen)[0]
        
        
        
    #devolver la lista de las imagenes ya codifiucadas
    return imagen_codificada'''


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!FUNCION PARA COMPARAR y MARCAR ROSTRO
#funcion que debe comparar las fotos de base datos (A) y foto para comparar (B)
'''def comparar_imagen(foto_A, foto_B):
    foto_B_ok = face_recognition.face_locations(foto_B)[0]
    for foto in foto_A:
        #foto_A_ok = face_recognition.face_locations(foto_A)
        fotos_resultado = face_recognition.compare_faces(foto, foto_B_ok)
    return fotos_resultado   ''' 
    
    
'''def comparar_imagen(foto_A, foto_B):
    #foto_B_ok = face_recognition.face_locations(foto_B)[0]
    
        #foto_A_ok = face_recognition.face_locations(foto_A)
    fotos_resultado = face_recognition.compare_faces(foto_A, foto_B)
    return fotos_resultado'''  

def comparar_imagen(foto_A, foto_B):
    if foto_B is None:
        return []
    fotos_resultado = []
    for foto in foto_A:
        resultado = face_recognition.compare_faces([foto], foto_B)
        fotos_resultado.append(resultado)
    return fotos_resultado         


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!CAPTURAR IMAGEN A CONTROLAR CON WEBCAP
'''if __name__ == "__main__":
    webcam_imagen_para_comparar = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    exito, imagen = webcam_imagen_para_comparar.read()
    if not exito:
        print('No se pudo tomar la foto, intenta nuevamente')
    else:
        imagen_codificada = codificar_img_para_comparar([imagen])
        resultado = comparar_imagen(lista_empleados_codificados, imagen_codificada)
        print(resultado)'''
        


'''webcam_imagen_para_comparar = cv2.VideoCapture(0, cv2.CAP_DSHOW)
exito, imagen = webcam_imagen_para_comparar.read()
if not exito:
    print('No se pudo tomar la foto, intenta nuevamente')
else:
    imagen_codificada = codificar_img_para_comparar([imagen])
    resultado = comparar_imagen(lista_empleados_codificados, imagen_codificada)
    print(resultado) '''  
    

'''webcam_imagen_para_comparar = cv2.VideoCapture(0, cv2.CAP_DSHOW)
exito, imagen = webcam_imagen_para_comparar.read()
if not exito:
    print('No se pudo tomar la foto, intenta nuevamente')
else:
    imagen_codificada = codificar_img_para_comparar([imagen])
    resultado = comparar_imagen(lista_empleados_codificados, imagen_codificada)
    print(resultado) '''       

'''webcam_imagen_para_comparar = cv2.VideoCapture(0, cv2.CAP_DSHOW)
exito = webcam_imagen_para_comparar.isOpened()  # Verificar si la cámara se abrió correctamente

if not exito:
    print('No se pudo abrir la cámara. Verifica que esté conectada y disponible.')
else:
    exito, imagen = webcam_imagen_para_comparar.read()  # Leer la imagen de la cámara

    if not exito:
        print('No se pudo capturar la imagen de la cámara. Intenta nuevamente.')
    else:
        imagen_codificada = codificar_img_para_comparar([imagen])
        resultado = comparar_imagen(lista_empleados_codificados, imagen_codificada)
        print(resultado)'''





'''pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

imagen = cam.get_image()


#reconocer la cara en la captura tomada para comparar
confirmacion = comparar_imagen(lista_empleados_codificados, [imagen])     
print(confirmacion)

cam.stop()
pygame.quit()'''


pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

imagen = cam.get_image()
imagen_array = pygame.surfarray.array3d(imagen)
imagen_cv2 = cv2.cvtColor(imagen_array, cv2.COLOR_RGB2BGR)

imagen_codificada = None
face_locations = face_recognition.face_locations(imagen_cv2)
if len(face_locations) > 0:
    imagen_codificada = face_recognition.face_encodings(imagen_cv2)[0]



# Comparar la imagen capturada con todas las imágenes de la base de datos
confirmacion = comparar_imagen(lista_empleados_codificados, imagen_codificada)
print(confirmacion)

cam.stop()
pygame.quit()



# Rotar la imagen capturada antes de mostrarla
imagen_rotada = cv2.rotate(imagen_cv2, cv2.ROTATE_90_CLOCKWISE)

# Mostrar la imagen rotada
cv2.imshow('Imagen Capturada', imagen_rotada)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''# CAPTURAR IMAGEN A CONTROLAR CON WEBCAM
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

imagen = cam.get_image()

cam.stop()
pygame.quit()

# RECONOCIMIENTO DE ROSTRO
imagen_cv2 = pygame.surfarray.array3d(imagen)
imagen_codificada = face_recognition.face_encodings(imagen_cv2)[0]

# Comparar la imagen capturada con todas las imágenes de la base de datos
confirmacion = comparar_imagen(lista_empleados_codificados, imagen_codificada)
print(confirmacion)

# Rotar la imagen capturada antes de mostrarla
imagen_rotada = cv2.rotate(imagen_cv2, cv2.ROTATE_90_CLOCKWISE)

# Mostrar la imagen rotada
cv2.imshow('Imagen Capturada', imagen_rotada)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!FUNCION PARA COMPARAR y MARCAR ROSTRO
#funcion que debe comparar las fotos de base datos (A) y foto para comparar (B)
'''def comparar_imagen(foto_A, foto_B):
    foto_B_ok = face_recognition.face_locations(foto_B)[0]
    for foto in foto_A:
        foto_A_ok = face_recognition.face_locations(foto_A)
        fotos_resultado = face_recognition.compare_faces(foto, foto_B_ok)
    return fotos_resultado    '''
        



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!MANTENEMOS EL PROGRAMA EN EJECUCION
#mantenemos el programa en ejecucion para que no se cierre con el metoso .waitKey(0)
cv2.waitKey(0)
```
````
