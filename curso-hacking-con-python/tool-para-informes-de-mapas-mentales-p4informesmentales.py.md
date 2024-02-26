# 👹 TOOL PARA INFORMES DE MAPAS MENTALES P4INformesmentales.py

Programa en Python para automatizar a través de una interfaz dinámica de ingresos de datos y comandos de forma guiada para que se valla creando un reporte en formato MARKDOWN y así también poder realizar con el en XMIND un mapa mental ya estructurado al que aparte podríamos personalizar después con imágenes recolectadas, etc

````python

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!programa para automatizar a traves de una interfas dinamica de ingresos de datos guiada para que se valla creando un reporte en formato MARKDOWN y asi tambien poder realizar con el en XMIND un mapa mental ya estructurado al qeu aparte podriamos personalizar despues con imagenes recolectadas,etc
#! P4INformesmentales.py 3.0v- By P4IM0N

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!TESTEADO EN KALI LINUX, LIBRERIAS E INSTALACION DE LAS MISMAS EN CASO DE NO TENERLAS
# Tener instalado la aplicacion XMIND.
# Bibliotecas necesarias para el funcionamientoo:
# -subprocess: Para ejecutar comandos y capturar su la salida.
   #Podes instalarlo con el siguiente comando:
    #? pip install subprocess
# -tabulate: Para crear tablas a partir de datos en listas.
   #Podes instalarlo con el siguiente commando:
    #? pip install tabulate

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Importamos librerias
from tabulate import tabulate
import subprocess

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Códigos de escape ANSI para cambiar el color del texto en la terminal
COLOR_RED = "\033[91m"
COLOR_PURPLE = '\x1b[35m'
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TEXTOS INFORMATIVOS

ayuda = '''
////////////////////////////////////////////////////////AYUDA MANITO///////////////////////////////////////////////////////////////////
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Método manual: Este método implica que el pentester realiza las acciones de forma directa y personalizada, sin usar herramientas automatizadas o scripts. Un ejemplo de cómo aplicar este método sería el siguiente:

    - El pentester accede al sitio web de Shoppy ([https://shoppy.com]) y observa su diseño, sus funcionalidades, sus productos y sus políticas.
    - El pentester intenta registrarse como un usuario normal y verifica si el sitio web valida correctamente los datos ingresados, como el correo electrónico, la contraseña o el número de tarjeta de crédito.
    - El pentester explora las opciones disponibles para el usuario, como el carrito de compras, el historial de pedidos, el perfil o la configuración.
    - El pentester prueba diferentes entradas en los campos del sitio web, como la búsqueda, el filtro, el comentario o la calificación, y verifica si el sitio web es vulnerable a ataques como la inyección SQL, la inyección XSS o la falsificación de solicitudes entre sitios (CSRF).
    - El pentester analiza el código fuente del sitio web y busca posibles fallos de seguridad, como comentarios, credenciales, rutas o versiones.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Método OSINT (Open Source Intelligence): Este método se basa en la recolección de información pública y accesible sobre el objetivo, usando fuentes como buscadores, redes sociales, bases de datos, registros públicos o medios de comunicación. Un ejemplo de cómo aplicar este método sería el siguiente:

    - El pentester usa un buscador como Bing o Google para encontrar información sobre Shoppy, como su dirección, su teléfono, su correo electrónico, su fecha de fundación o su misión.
    - El pentester usa redes sociales como Facebook, Twitter o LinkedIn para encontrar información sobre los empleados, los clientes o los competidores de Shoppy, como sus nombres, sus cargos, sus contactos o sus opiniones.
    - El pentester usa bases de datos como Shodan o Censys para encontrar información sobre los servidores, los dominios o los servicios asociados a Shoppy, como sus direcciones IP, sus puertos abiertos, sus sistemas operativos o sus certificados SSL.
    - El pentester usa registros públicos como WHOIS o DNS para encontrar información sobre la propiedad, el registro o la configuración del dominio shoppy.com, como su dueño, su proveedor, su fecha de expiración o sus registros A, MX o NS.
    - El pentester usa medios de comunicación como periódicos, revistas o blogs para encontrar información sobre la reputación, las noticias o los eventos relacionados con Shoppy, como sus logros, sus problemas, sus alianzas o sus promociones.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Método automatizado: Este método consiste en usar herramientas informáticas que realizan las acciones de forma rápida y eficiente, siguiendo unos parámetros predefinidos. Un ejemplo de cómo aplicar este método sería el siguiente:

    - El pentester usa una herramienta como Nmap o Zmap para realizar un escaneo de puertos del dominio shoppy.com y descubrir qué servicios están corriendo y qué vulnerabilidades pueden tener.
    - El pentester usa una herramienta como Nikto o Wapiti para realizar un escaneo de vulnerabilidades del sitio web shoppy.com y detectar posibles fallos de seguridad, como directorios listables, archivos sensibles o cabeceras mal configuradas.
    - El pentester usa una herramienta como Hydra o John the Ripper para realizar un ataque de fuerza bruta al servicio SSH del servidor shoppy.com y tratar de adivinar las credenciales de acceso usando diccionarios o generando combinaciones.
    - El pentester usa una herramienta como Burp Suite o OWASP ZAP para realizar un análisis dinámico del sitio web shoppy.com y capturar e interceptar las peticiones y respuestas HTTP entre el cliente y el servidor.
    - El pentester usa una herramienta como DirBuster o Gobuster para realizar un ataque de fuerza bruta al sitio web shoppy.com y tratar de descubrir directorios o archivos ocultos usando listas predefinidas.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Método mixto: Este método consiste en combinar los métodos anteriores para obtener una visión más completa y precisa del objetivo. Un ejemplo de cómo aplicar este método sería el siguiente:

    - El pentester usa una herramienta como Nmap para realizar un escaneo de puertos del dominio shoppy.com y descubre que el puerto 80 está abierto y que el servicio es Apache 2.4.41.
    - El pentester accede al sitio web shoppy.com y observa que tiene un formulario de inicio de sesión y un enlace a una página de administración.
    - El pentester usa una herramienta como Nikto para realizar un escaneo de vulnerabilidades del sitio web shoppy.com y detecta que la página de administración tiene una vulnerabilidad de inyección SQL.
    - El pentester explota la vulnerabilidad de inyección SQL usando una herramienta como sqlmap o manualmente y obtiene acceso a la base de datos del sitio web, donde encuentra los usuarios y las contraseñas de los administradores.
    - El pentester usa las credenciales obtenidas para iniciar sesión como administrador y acceder al panel de control del sitio web, donde puede modificar los productos, los precios o los pedidos.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Método de ingeniería social: Este método implica interactuar con personas y no solo con sistemas informáticos. Un ejemplo de cómo aplicar este método sería el siguiente:

    - El pentester usa el método OSINT para encontrar información sobre los empleados de Shoppy, como sus nombres, sus cargos, sus correos electrónicos o sus números de teléfono.
    - El pentester crea un correo electrónico falso que simula ser de Shoppy y que solicita a los empleados que ingresen a un enlace para verificar su identidad o actualizar su contraseña. El enlace lleva a una página falsa que captura las credenciales ingresadas.
    - El pentester llama por teléfono a los empleados de Shoppy y se hace pasar por un técnico de soporte o un cliente insatisfecho. El pentester trata de obtener información sensible o persuadir a los empleados para que realicen alguna acción, como abrir un archivo adjunto, descargar un programa o revelar una contraseña.
    - El pentester visita las instalaciones de Shoppy y se hace pasar por un repartidor, un mensajero o un auditor. El pentester trata de acceder a áreas restringidas, robar dispositivos, colocar dispositivos o observar las actividades.
    - El pentester deja un dispositivo USB infectado con un malware en el estacionamiento o la recepción de Shoppy. El pentester espera a que algún empleado lo encuentre y lo conecte a su computadora, lo que le permitirá al pentester tomar el control remoto del sistema.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

comandos = {
    "Ping Básico": f"ping {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ping simple al sitio web para verificar si está accesible.{COLOR_RESET}",
    "Ping con Intervalo de Tiempo Personalizado": f"ping -c 5 -i 0.2 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza 5 pings con un intervalo de 0.2 segundos entre ellos.{COLOR_RESET}",
    "Ping con Tamaño de Paquete Personalizado": f"ping -c 5 -s 100 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Envía paquetes de 100 bytes al sitio y registra si obtiene respuesta.{COLOR_RESET}",
    "Envío Indefinido de Paquetes": f"ping -i 1 -s 56 -D {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Envía paquetes de 56 bytes con intervalo de 1 segundo de forma indefinida.{COLOR_RESET}",
    "Registro de Resultados en un Archivo": f"ping -c 5 {COLOR_RED}https://objetivo.com{COLOR_RESET} > {COLOR_RED}resultados.txt{COLOR_RESET} - {COLOR_YELLOW}Realiza 5 pings y guarda los resultados en un archivo llamado 'resultados.txt'.{COLOR_RESET}",
    "Supresión de Resolución Inversa": f"ping -n -c 5 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza pings sin resolver direcciones IP inversas.{COLOR_RESET}",
    "Nmap Escaneo Básico de Puertos": f"nmap {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea los puertos abiertos en el objetivo y muestra información básica.{COLOR_RESET}",
    "Nmap Escaneo de Servicios y Sistema Operativo": f"nmap -sV -O {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Detecta versiones de servicios y sistema operativo del objetivo.{COLOR_RESET}",
    "Nmap Escaneo de Todos los Puertos y Scripts de Detección de Vulnerabilidades": f"nmap -p- -sV --script vuln {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea todos los puertos, detecta versiones y ejecuta scripts de detección de vulnerabilidades.{COLOR_RESET}",
    "Nmap Escaneo Rápido de los 1000 Puertos Más Comunes": f"nmap -F {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo rápido de los 1000 puertos más comunes.{COLOR_RESET}",
    "Nmap Escaneo UDP": f"nmap -sU {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea los puertos UDP abiertos en el objetivo.{COLOR_RESET}",
    "Nmap Escaneo de un Rango Personalizado de Puertos": f"nmap -p 80,443,8080 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea puertos específicos (80, 443 y 8080) en el objetivo.{COLOR_RESET}",
    "Nikto Escaneo Básico de Nikto": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de vulnerabilidades conocidas.{COLOR_RESET}",
    "Nikto Escaneo Completo de Nikto": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -C all - {COLOR_YELLOW}Realiza un escaneo completo, incluyendo todas las pruebas disponibles.{COLOR_RESET}",
    "Nikto Escaneo con Plugins de Vulnerabilidades": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -Plugins +vulnerabilities - {COLOR_YELLOW}Habilita plugins específicos que buscan vulnerabilidades en el sitio web.{COLOR_RESET}",
    "Nikto Escaneo SSL": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -ssl - {COLOR_YELLOW}Realiza un escaneo enfocado en SSL y sus vulnerabilidades.{COLOR_RESET}",
    "Nikto Escaneo Proxy": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -useproxy http://mi.proxy.com:8080 - {COLOR_YELLOW}Utiliza un proxy para realizar el escaneo.{COLOR_RESET}",
    "Nikto Escaneo Personalizado de Puertos": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -port 80,443 - {COLOR_YELLOW}Realiza el escaneo solo en los puertos 80 y 443.{COLOR_RESET}",
    "Dirb Escaneo Básico de Directorios": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de directorios y archivos ocultos en el objetivo.{COLOR_RESET}",
    "Dirb Escaneo con una Lista de Palabras Personalizada": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} /ruta/a/mi/wordlist.txt - {COLOR_YELLOW}Utiliza una lista de palabras personalizada para buscar directorios y archivos en el objetivo.{COLOR_RESET}",
    "Dirb Escaneo con Búsqueda de Extensiones Específicas": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -X .php,.html - {COLOR_YELLOW}Busca directorios y archivos con extensiones específicas, como .php y .html.{COLOR_RESET}",
    "Dirb Escaneo Recursivo": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -r - {COLOR_YELLOW}Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.{COLOR_RESET}",
    "Dirb Escaneo de Autenticación Básica": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -a usuario:contraseña - {COLOR_YELLOW}Realiza un escaneo en un sitio web que requiere autenticación básica HTTP.{COLOR_RESET}",
    "Dirb Escaneo con Límite de Tiempo Personalizado": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -t 30 - {COLOR_YELLOW}Establece un límite de tiempo para las solicitudes durante el escaneo.{COLOR_RESET}",
    "SQLMap Detección de Bases de Datos": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} - {COLOR_YELLOW}Detecta las bases de datos y las vulnerabilidades de inyección SQL en la URL proporcionada.{COLOR_RESET}",
    "SQLMap Enumeración de Bases de Datos": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --dbs - {COLOR_YELLOW}Enumera las bases de datos disponibles en el objetivo.{COLOR_RESET}",
    "SQLMap Enumeración de Tablas": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --dbs --tables - {COLOR_YELLOW}Enumera las tablas en una base de datos específica.{COLOR_RESET}",
    "SQLMap Explotación de una Inyección SQL": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --dump - {COLOR_YELLOW}Explota una vulnerabilidad de inyección SQL y recupera datos de la base de datos.{COLOR_RESET}",
    "SQLMap Escaneo de Inyección SQL a Ciegas": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --level 5 --risk 3 - {COLOR_YELLOW}Realiza un escaneo avanzado de inyección SQL a ciegas en el objetivo.{COLOR_RESET}",
    "SQLMap Explotación con Fuerza Bruta de Hashes": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --crack - {COLOR_YELLOW}Intenta crackear hashes de contraseñas recuperados de la base de datos.{COLOR_RESET}",
    "XSSer Escaneo Básico en Busca de Vulnerabilidades XSS": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} - {COLOR_YELLOW}Escanea la URL en busca de vulnerabilidades de Cross-Site Scripting (XSS).{COLOR_RESET}",
    "XSSer Escaneo con Enumeración de Enlaces Vulnerables": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -l - {COLOR_YELLOW}Escanea y enumera enlaces vulnerables a ataques XSS en la página.{COLOR_RESET}",
    "XSSer Escaneo con Análisis de Todas las Inyecciones de Parámetros": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -p all - {COLOR_YELLOW}Realiza un análisis exhaustivo de todas las inyecciones de parámetros en la URL.{COLOR_RESET}",
    "XSSer Escaneo con Filtrado Personalizado de Payloads": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -p all -fp 'mi_payload.txt' - {COLOR_YELLOW}Escanea utilizando payloads personalizados definidos en 'mi_payload.txt'.{COLOR_RESET}",
    "XSSer Escaneo con Límite de Tiempo Personalizado": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -t 10 - {COLOR_YELLOW}Establece un límite de tiempo para cada solicitud durante el escaneo.{COLOR_RESET}",
    "XSSer Escaneo con Seguimiento de Redirecciones": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -r - {COLOR_YELLOW}Realiza el escaneo siguiendo las redirecciones en la página web objetivo.{COLOR_RESET}",
    "Dnsrecon Escaneo Básico de DNS": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de registros DNS asociados al dominio.{COLOR_RESET}",
    "Dnsrecon Escaneo Utilizando Diccionario": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t std -D /ruta/a/mi/diccionario.txt - {COLOR_YELLOW}Utiliza un diccionario personalizado para realizar un escaneo exhaustivo de DNS.{COLOR_RESET}",
    "Dnsrecon Enumeración de Servidores de Nombres": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt - {COLOR_YELLOW}Enumera los servidores de nombres relacionados con el dominio.{COLOR_RESET}",
    "Dnsrecon Escaneo con un Límite de Tiempo Personalizado": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt -T 30 - {COLOR_YELLOW}Establece un límite de tiempo para el escaneo.{COLOR_RESET}",
    "Dnsrecon Escaneo en Búsqueda de Subdominios": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt -n - {COLOR_YELLOW}Busca subdominios relacionados con el dominio principal.{COLOR_RESET}",
    "Dnsrecon Escaneo Inverso de Direcciones IP": f"dnsrecon -r 192.168.1.1 - {COLOR_YELLOW}Realiza un escaneo inverso de una dirección IP específica.{COLOR_RESET}",
    "SQLNinja Detección de la Vulnerabilidad": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Detecta la vulnerabilidad de inyección SQL en el sitio web.{COLOR_RESET}",
    "SQLNinja Enumeración de Tablas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET}-m t - {COLOR_YELLOW}Enumera las tablas en la base de datos objetivo.{COLOR_RESET}",
    "SQLNinja Enumeración de Tablas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -tn - {COLOR_YELLOW}Enumera las tablas en la base de datos vulnerable.{COLOR_RESET}",
    "SQLNinja Enumeración de Columnas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -cn - {COLOR_YELLOW}Enumera las columnas en las tablas de la base de datos.{COLOR_RESET}",
    "SQLNinja Explotación de Inyección SQL": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -m {COLOR_RED}POST{COLOR_RESET} - {COLOR_YELLOW}Explota la vulnerabilidad de inyección SQL y recupera datos de la base de datos.{COLOR_RESET}",
    "SQLNinja Escalada de Privilegios": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -x {COLOR_RED}'EXEC sp_addsrvrolemember ''sysadmin'', ''usuario'';'{COLOR_RESET} - {COLOR_YELLOW}Realiza una escalada de privilegios para obtener control total del servidor SQL.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta SSH": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}ssh://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta SSH contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta FTP": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}ftp://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta FTP contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta Telnet": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}telnet://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta Telnet contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta HTTP POST": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}http-post://objetivo.com/login{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta HTTP POST contra un formulario de inicio de sesión.{COLOR_RESET}",
    "Gobuster Escaneo Básico de Directorios": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt - {COLOR_YELLOW}Realiza un escaneo básico de directorios en busca de directorios y archivos ocultos en el objetivo.{COLOR_RESET}",
    "Gobuster Escaneo con una Lista de Palabras Personalizada": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /ruta/a/mi/wordlist.txt - {COLOR_YELLOW}Utiliza una lista de palabras personalizada para buscar directorios en el objetivo.{COLOR_RESET}",
    "Gobuster Escaneo con Búsqueda de Extensiones Específicas": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/big.txt -x .php,.html - {COLOR_YELLOW}Busca directorios y archivos con extensiones específicas, como .php y .html.{COLOR_RESET}",
    "Gobuster Escaneo Recursivo": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -r - {COLOR_YELLOW}Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.{COLOR_RESET}",
    "Gobuster Escaneo de Autenticación Básica": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -U usuario -P contraseña - {COLOR_YELLOW}Escanea un sitio web que requiere autenticación HTTP básica.{COLOR_RESET}",
    "Gobuster Escaneo con Límite de Tiempo Personalizado": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -t 30 - {COLOR_YELLOW}Establece un límite de tiempo para las solicitudes durante el escaneo.{COLOR_RESET}"
}


tabla_de_comandos = [[comando, COLOR_PURPLE+descripcion+COLOR_RESET] for comando, descripcion in comandos.items()]    #conprension de lista para conseguir la tabla con los colores
tabla_de_comandos_terminada = (tabulate(tabla_de_comandos, headers=['DESCRIPCION','COMANDO','EXPLICACION'], tablefmt='grid'))

text_reconocimiento_pasivo = '''
BROWSER ---------------------------------> https://www.paimon.com.ar/
----------------------------------------

NMAP ---------------------------------> https://nmap.org/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/nmap
----------------------------------------

WAYBACKMACHINE ---------------------------------> https://archive.org/web/
----------------------------------------

MALTEGO ---------------------------------> https://www.maltego.com/
----------------------------------------

SHODAN ---------------------------------> https://www.shodan.io/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/shodan
----------------------------------------

CENSYS ---------------------------------> https://search.censys.io/
----------------------------------------

WEB-CHECK ---------------------------------> https://web-check.xyz/
----------------------------------------

THEHARVESTER ---------------------------------> https://github.com/laramies/theHarvester
----------------------------------------

GOOGLE DORKS ---------------------------------> https://www.google.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking
----------------------------------------

WAPPALYZER ---------------------------------> https://www.wappalyzer.com/
----------------------------------------

DNSdumpster ---------------------------------> https://dnsdumpster.com/
----------------------------------------

ROBTEX ---------------------------------> https://www.robtex.com/#google_vignette
----------------------------------------

WHOIS ---------------------------------> https://who.is/
----------------------------------------

NSLOOKUP ---------------------------------> https://www.nslookup.io/
----------------------------------------

GHUNT ---------------------------------> https://github.com/mxrch/GHunt
----------------------------------------

LLANTUN ---------------------------------> https://github.com/lesandcl/Llaitun
----------------------------------------

DISCOVER ---------------------------------> https://github.com/leebaird/discover
----------------------------------------

SHERLOCK ---------------------------------> https://github.com/sherlock-project/sherlock
----------------------------------------

WHATWEB ---------------------------------> https://www.kali.org/tools/whatweb/
----------------------------------------

DIAGRAMAS ---------------------------------> https://app.diagrams.net/
----------------------------------------

P4INformesmentales ---------------------------------> https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/curso-hacking-con-python/tool-para-informes-de-mapas-mentales-p4informesmentales.py
----------------------------------------
'''

text_reconocimiento_forense = '''
AUTOPSY https://tools.kali.org/forensics/autopsy ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/autopsy-digital-forensics
----------------------------------------

VOLATILITY https://github.com/volatilityfoundation/volatility ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/volatility-memory-forensic
----------------------------------------

FTK https://www.accessdata.com/products-services/forensic-toolkit-ftk ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ftk-digital-forensic  
----------------------------------------

DFF (Digital Forensics Framework) https://github.com/arxsys/dff
----------------------------------------

TSK (The Sleuth Kit) https://tools.kali.org/forensics/sleuthkit
----------------------------------------

X-WAYS Forensics https://www.x-ways.net/forensics/index-m.html
----------------------------------------

FOREMOST https://github.com/korczis/foremost
----------------------------------------

HxD https://mh-nexus.de/en/hxd/
----------------------------------------

WIRESHARK ---------------------------------> https://github.com/wireshark/wireshark ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark
----------------------------------------

TSHARK ---------------------------------> https://www.kali.org/tools/wireshark/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark
----------------------------------------

XXD https://tools.kali.org/forensics/xxd
----------------------------------------
'''

text_reconocimiento_activo = '''
PING ---------------------------------> https://www.kali.org/tools/fping/
----------------------------------------

NMAP ---------------------------------> https://nmap.org/ --->PDF-TOOL
----------------------------------------

NESSUS ---------------------------------> https://es-la.tenable.com/products/nessus/nessus-essentials
----------------------------------------

OPENVAS ---------------------------------> https://github.com/greenbone/openvas-scanner
----------------------------------------

NIKTO ---------------------------------> https://github.com/sullo/nikto
----------------------------------------

METASPLOIT ---------------------------------> https://www.metasploit.com/ --->PDF-TOOL
----------------------------------------

BURP SUITE ---------------------------------> https://portswigger.net/web-security --->PDF-TOOL
----------------------------------------

OWASP ZAP ---------------------------------> https://github.com/zaproxy/zaproxy
---------------------------------------- 

WIRESHARK ---------------------------------> https://github.com/wireshark/wireshark ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark
----------------------------------------

DIRBUSTER ---------------------------------> https://github.com/KajanM/DirBuster ---> https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/dirbuster
----------------------------------------

SQLMAP ---------------------------------> https://github.com/sqlmapproject/sqlmap ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap
----------------------------------------

WPSCAN ---------------------------------> https://wpscan.com/register/
----------------------------------------

JOOMSCAN ---------------------------------> https://www.kali.org/tools/joomscan/
----------------------------------------

GOBUSTER ---------------------------------> https://www.kali.org/tools/gobuster/
----------------------------------------

FFUF ---------------------------------> https://www.kali.org/tools/ffuf/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ffuf
----------------------------------------

TRACEROUTE ---------------------------------> https://www.kali.org/tools/traceroute/
----------------------------------------

SMBCLIENT ---------------------------------> https://www.kali.org/tools/samba/
----------------------------------------

TELNET ---------------------------------> https://wowgold-seller.com/es/stories/133-how-to-install-and-use-telnet-on-kali-linux
----------------------------------------

SSH ---------------------------------> https://www.kali.org/tools/openssh/ --->PDF-TOOL
----------------------------------------

NETCAT ---------------------------------> https://www.kali.org/tools/netcat/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones
----------------------------------------

FTP ---------------------------------> https://www.kali.org/tools/netkit-ftp/
----------------------------------------

TCPDUMP ---------------------------------> https://www.kali.org/tools/tcpdump/
----------------------------------------

TSHARK ---------------------------------> https://www.kali.org/tools/wireshark/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark
----------------------------------------

BETTERCAP ---------------------------------> https://www.kali.org/tools/bettercap/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/bettercap
----------------------------------------

SMBMAP ---------------------------------> https://www.kali.org/tools/smbmap/
----------------------------------------

WFUZZ ---------------------------------> https://www.kali.org/tools/wfuzz/
----------------------------------------

COMMIX ---------------------------------> https://www.kali.org/tools/commix/
----------------------------------------

SKIP-FISH ---------------------------------> https://www.kali.org/tools/skipfish/
----------------------------------------

WAPITI ---------------------------------> https://www.kali.org/tools/wapiti/
----------------------------------------

ETTERCAP ---------------------------------> https://www.kali.org/tools/ettercap/
----------------------------------------

WIFITE ---------------------------------> https://www.kali.org/tools/wifite/
----------------------------------------

SPOOFTOOPH ---------------------------------> https://www.kali.org/tools/spooftooph/
----------------------------------------

CRACKMAPEXEC ---------------------------------> https://www.kali.org/tools/crackmapexec/
----------------------------------------
'''

text_reconocimiento_OSINT = '''
OSINT Framework ---------------------------------> https://osintframework.com/
----------------------------------------

Maltego ---------------------------------> https://www.kali.org/tools/maltego/
----------------------------------------

Recon-ng ---------------------------------> https://www.paimon.com.ar/
----------------------------------------

theHarvester ---------------------------------> https://www.kali.org/tools/theharvester/
----------------------------------------

GOOGLE DORKS ---------------------------------> https://www.google.com/ --->PDF-TOOL
----------------------------------------

SHODAN ---------------------------------> https://www.shodan.io/ --->PDF-TOOL
----------------------------------------

OSRFrameworK ---------------------------------> https://www.kali.org/tools/osrframework/
----------------------------------------

SN0INT ---------------------------------> https://www.kali.org/tools/sn0int/
----------------------------------------

OSINTGRAM ---------------------------------> https://github.com/Datalux/Osintgram
----------------------------------------

TWOSINT ---------------------------------> https://github.com/falkensmz/tw1tter0s1nt
----------------------------------------

INTELLIGENCE X FACEBOOK ---------------------------------> https://intelx.io/tools?tab=facebook
----------------------------------------

INTELLIGENCE X PERSONAS ---------------------------------> https://intelx.io/tools?tab=person
----------------------------------------

INTELLIGENCE X TELEFONOS ---------------------------------> https://intelx.io/tools?tab=telephone
----------------------------------------

INTELLIGENCE X Ubicación 2 Mapa ---------------------------------> https://intelx.io/tools?tab=location
----------------------------------------

INTELLIGENCE X IMAGEN ---------------------------------> https://intelx.io/tools?tab=image
----------------------------------------

INTELLIGENCE X NOMBRE DE USUARIO ---------------------------------> https://intelx.io/tools?tab=username
----------------------------------------

INTELLIGENCE X HASH INVERSA ---------------------------------> https://intelx.io/tools?tab=hash
----------------------------------------

INTELLIGENCE X ARCHIVOS ---------------------------------> https://intelx.io/tools?tab=file
----------------------------------------

INTELLIGENCE X VIN VEHICULOS ---------------------------------> https://intelx.io/tools?tab=vin
----------------------------------------

'''

text_reconocimiento_hashes_desencriptado = '''
JOHN THE RIPPER ---------------------------------> https://www.kali.org/tools/john/ ---> PDF-TOOL https://paimonhacking.gitbook.io/p4im0n_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/john-the-ripper
----------------------------------------

HASHCAT ---------------------------------> https://www.kali.org/tools/hashcat/
----------------------------------------

RAINBOWCRACK ---------------------------------> https://www.kali.org/tools/rainbowcrack/
----------------------------------------

OPHCRACK ---------------------------------> https://www.kali.org/tools/ophcrack/
----------------------------------------

CRACKSTATION ---------------------------------> https://crackstation.net/
----------------------------------------

AIRCRACK-NG ---------------------------------> https://www.kali.org/tools/aircrack-ng/ ---> PDF-TOOL https://paimonhacking.gitbook.io/p4im0n_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/aircrack-ng-wireless-wi-fi-auditoria-y-fuerza-bruta-a-handshake
----------------------------------------

CAIN Y ABEL ---------------------------------> https://github.com/xchwarze/Cain
----------------------------------------

HYDRA ---------------------------------> https://www.kali.org/tools/hydra/ ---> PDF-TOOL https://paimonhacking.gitbook.io/p4im0n_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/hydra-fuerza-bruta
----------------------------------------

MEDUSA ---------------------------------> https://www.kali.org/tools/medusa/ ---> PDF-TOOL https://paimonhacking.gitbook.io/p4im0n_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/medusa
----------------------------------------

DAVEGRO1 ---------------------------------> https://github.com/octomagon/davegrohl
----------------------------------------

ElcomSoft Distributed Password Recovery ---------------------------------> https://www.elcomsoft.es/edpr.html
----------------------------------------

CRACK RAR ---------------------------------> https://github.com/TermuxHackz/Crack-rar
----------------------------------------

CRACK NINJA RAR ---------------------------------> https://github.com/SHUR1K-N/RARNinja-RAR-Password-Cracking-Utility
----------------------------------------

NCRACK ---------------------------------> https://www.kali.org/tools/ncrack/
----------------------------------------

CEWL WORDLIST ---------------------------------> https://www.kali.org/tools/cewl/ --->PDF-TOOL
----------------------------------------

CRUNCH WORDLIST ---------------------------------> https://www.kali.org/tools/crunch/ --->PDF-TOOL
----------------------------------------

P4Iwordlists ---------------------------------> https://paimonhacking.gitbook.io/p4im0n_h4cking/curso-hacking-con-python/generador-de-wordlist-para-fuerza-bruta-p4iwordlist.py-1.2v
----------------------------------------

CYBERCHEF ---------------------------------> https://gchq.github.io/CyberChef/
----------------------------------------

BASE64 DECODE ---------------------------------> https://www.base64decode.org/
----------------------------------------'''

text_reconocimiento_fuerza_bruta_logins = '''
HYDRA ---------------------------------> https://www.kali.org/tools/hydra/ --->PDF-TOOL
----------------------------------------

MEDUSA ---------------------------------> https://www.kali.org/tools/medusa/ --->PDF-TOOL
----------------------------------------

NCRACK ---------------------------------> https://www.kali.org/tools/ncrack/
----------------------------------------

161 ONESIXTYONE ---------------------------------> https://www.kali.org/tools/onesixtyone/
----------------------------------------

THC-PPTP-BRUTER ---------------------------------> https://www.kali.org/tools/thc-pptp-bruter/
----------------------------------------

BURP SUITE ---------------------------------> https://portswigger.net/web-security ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite
----------------------------------------

CRACKMAPEXEC ---------------------------------> https://www.kali.org/tools/crackmapexec/
----------------------------------------

CROWBAR RDP ---------------------------------> https://www.kali.org/tools/crowbar/
----------------------------------------

THE CRACKER PDF,ZIP,RAR,LOGIN ---------------------------------> https://github.com/XDeadHackerX/The_Cracker
----------------------------------------

THC-HYDRA ---------------------------------> https://github.com/vanhauser-thc/thc-hydra
----------------------------------------

T14M4T scaneo de servicios en puertos y fuerza bruta automatizado --------------------------------->https://github.com/MS-WEB-BN/t14m4t
----------------------------------------

FACEBOOK-BRUTE-FORCE ---------------------------------> https://github.com/likhonsible/Facebook-Brute-Force
----------------------------------------'''

text_reconocimiento_explot_y_payload = '''
METASPLOIT ---------------------------------> https://www.metasploit.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit
----------------------------------------

BURP SUITE ---------------------------------> https://portswigger.net/web-security ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite
----------------------------------------

SEARCHSPLOIT ---------------------------------> https://www.kali.org/tools/exploitdb/
----------------------------------------

EXPLOITDB ---------------------------------> https://www.exploit-db.com/
----------------------------------------

GITHUB SEARCH ---------------------------------> https://github.com/search
----------------------------------------

AWESOMEHACKING ---------------------------------> https://awesomehacking.org/
----------------------------------------

NVD VULNERABILITIES BASE ---------------------------------> https://nvd.nist.gov/vuln
----------------------------------------

MSFVENOM PAYLOAD ---------------------------------> https://www.kali.org/tools/metasploit-framework/ ---> PDF-TOOL https://paimonhacking.gitbook.io/p4im0n_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/msfvenom-generador-de-payloads
----------------------------------------

MSFPC PAYLOAD ---------------------------------> https://www.kali.org/tools/msfpc/
----------------------------------------

RAPID7 vulnerabilidades y exploits ---------------------------------> https://www.rapid7.com/db/
----------------------------------------

HACKTRICKS ---------------------------------> https://book.hacktricks.xyz/v/es/welcome/readme
----------------------------------------

HACKTOOL ---------------------------------> https://www.paimon.com.ar/
----------------------------------------'''

text_reconocimiento_explotacion = '''
NETCAT ---------------------------------> https://www.kali.org/tools/netcat/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones
----------------------------------------

METASPLOIT ---------------------------------> https://www.metasploit.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit
----------------------------------------

SOCAT ---------------------------------> https://www.kali.org/tools/socat/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones
----------------------------------------

SSH TUNNELS ---------------------------------> https://www.openssh.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet
----------------------------------------

SQLMAP ---------------------------------> https://github.com/sqlmapproject/sqlmap ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap
----------------------------------------

CRACKMAPEXEC ---------------------------------> https://www.kali.org/tools/crackmapexec/
----------------------------------------

VELO ---------------------------------> https://github.com/Veil-Framework/Veil
----------------------------------------

WEB2ATTACK ---------------------------------> https://github.com/santatic/web2attack
----------------------------------------

COMMIX ---------------------------------> https://www.kali.org/tools/commix/
----------------------------------------

WEBSPLOIT ---------------------------------> https://github.com/The404Hacking/websploit
----------------------------------------

BEEF FRAMEWORK EXPLOTACION---------------------------------> https://www.kali.org/tools/beef-xss/
----------------------------------------

HACKTRICKS ---------------------------------> https://book.hacktricks.xyz/v/es/welcome/readme
----------------------------------------'''

text_reconocimiento_privilegios_windows = '''
NETCAT ---------------------------------> https://www.kali.org/tools/netcat/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones
----------------------------------------

METASPLOIT ---------------------------------> https://www.metasploit.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit
----------------------------------------

SOCAT ---------------------------------> https://www.kali.org/tools/socat/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones
----------------------------------------

SSH TUNNELS ---------------------------------> https://www.openssh.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet
----------------------------------------

POWERUP ---------------------------------> https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerUp/PowerUp.ps1
----------------------------------------

LaZagne ---------------------------------> https://github.com/AlessandroZ/LaZagne ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/47/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/lazagne-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows-y-linux
----------------------------------------

MIMIKATZ ---------------------------------> https://www.kali.org/tools/mimikatz/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/47/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/mimikatz-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows
----------------------------------------

ROTTENPOTATO ---------------------------------> https://github.com/breenmachine/RottenPotatoNG
----------------------------------------

WINDOWS EXPLOITS SUGGESTER ---------------------------------> https://github.com/AonCyberLabs/Windows-Exploit-Suggester
----------------------------------------

ACCESSCHK ---------------------------------> https://github.com/ankh2054/windows-pentest
----------------------------------------

PSEXEC ---------------------------------> https://learn.microsoft.com/en-us/sysinternals/downloads/psexec
----------------------------------------

WINPEAS ---------------------------------> https://www.kali.org/tools/peass-ng/ ---> https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS
----------------------------------------

BLOODHOUND ---------------------------------> https://github.com/BloodHoundAD/BloodHound
----------------------------------------

CRACKMAPEXEC ---------------------------------> https://www.kali.org/tools/crackmapexec/
----------------------------------------

EMPIRE POWERSHELL Y LINUX ---------------------------------> https://www.kali.org/tools/powershell-empire/ -->https://github.com/EmpireProject/Empire
----------------------------------------

RESPONDER ---------------------------------> https://www.kali.org/tools/responder/ -->https://github.com/SpiderLabs/Responder
----------------------------------------

LOLBAS ---------------------------------> https://lolbas-project.github.io/#
----------------------------------------

WADCOMS comandos ---------------------------------> https://wadcoms.github.io/
----------------------------------------

HIJACKLIBS DLL ---------------------------------> https://hijacklibs.net/
----------------------------------------

PRINTSPOOFER ---------------------------------> https://github.com/itm4n/PrintSpoofer
----------------------------------------

ROGUEWINRM ---------------------------------> https://github.com/antonioCoco/RogueWinRM
----------------------------------------

WINDOWSPRIVESC metodos ---------------------------------> https://github.com/debiantano/WindowsPrivesc
----------------------------------------

PRIV-ESCALATION metodos ---------------------------------> https://github.com/KevinLiebergen/priv-escalation
----------------------------------------

FILESEC GTFO win y linux ---------------------------------> https://filesec.io/
----------------------------------------

HACKTRICKS ---------------------------------> https://book.hacktricks.xyz/v/es/welcome/readme
----------------------------------------

POWERSPLOIT ---------------------------------> https://www.kali.org/tools/powersploit/
----------------------------------------

EVIL-WINRM ---------------------------------> https://www.kali.org/tools/evil-winrm/
----------------------------------------
'''

text_reconocimiento_privilegios_linux = '''
NETCAT ---------------------------------> https://www.kali.org/tools/netcat/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones
----------------------------------------

METASPLOIT ---------------------------------> https://www.metasploit.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit
----------------------------------------

SOCAT ---------------------------------> https://www.kali.org/tools/socat/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones
----------------------------------------

SSH TUNNELS ---------------------------------> https://www.openssh.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet
----------------------------------------

LaZagne ---------------------------------> https://github.com/AlessandroZ/LaZagne ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/47/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/lazagne-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows-y-linux
----------------------------------------

GTFObins ---------------------------------> https://gtfobins.github.io/
----------------------------------------

LINUX KERNEL CVEs --------------------------------->https://www.linuxkernelcves.com/cves
----------------------------------------

LINENUM ---------------------------------> https://github.com/rebootuser/LinEnum
----------------------------------------

LINPEAS ---------------------------------> https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS
----------------------------------------

ENUMERACION SMART LINUX ---------------------------------> https://github.com/diego-treitos/linux-smart-enumeration
----------------------------------------

LINUXPRIVCHECKER ---------------------------------> https://github.com/sleventyeleven/linuxprivchecker
----------------------------------------

LINUX EXPLOIT SUGGESTER ---------------------------------> https://github.com/The-Z-Labs/linux-exploit-suggester
----------------------------------------

HACKTRICKS ---------------------------------> https://book.hacktricks.xyz/v/es/welcome/readme
----------------------------------------

CHKROOTKIT ---------------------------------> https://github.com/Magentron/chkrootkit
----------------------------------------

LYNIS ---------------------------------> https://github.com/CISOfy/lynis
----------------------------------------

UNIX-PRIVESC-CHECK ---------------------------------> https://github.com/pentestmonkey/unix-privesc-check
----------------------------------------

DIRDTYCOW ---------------------------------> https://github.com/firefart/dirtycow
----------------------------------------

PRIV-ESCALATION metodos ---------------------------------> https://github.com/KevinLiebergen/priv-escalation
----------------------------------------

FILESEC GTFO win y linux ---------------------------------> https://filesec.io/
----------------------------------------

RESPONDER ---------------------------------> https://www.kali.org/tools/responder/ -->https://github.com/SpiderLabs/Responder
----------------------------------------'''

text_reconocimiento_pivoting = '''
SSH TUNNELS ---------------------------------> https://www.openssh.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet
----------------------------------------

PROXYCHAINS ---------------------------------> https://github.com/rofl0r/proxychains-ng
----------------------------------------

SOCAT ---------------------------------> https://www.kali.org/tools/socat/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones
----------------------------------------

NCAT ---------------------------------> https://nmap.org/ncat/
----------------------------------------

CHISEL ---------------------------------> https://github.com/jpillora/chisel ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/chisel-creacion-de-tunel-entre-servidores-local-y-remoto-tambien-para-aprovechar-pivoting
----------------------------------------

CORKSCREW ---------------------------------> https://github.com/bryanpkc/corkscrew
----------------------------------------

METASPLOIT ---------------------------------> https://www.metasploit.com/ ---> PDF-TOOL https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit
----------------------------------------

METERPRETER ---------------------------------> https://www.metasploit.com/
----------------------------------------

REGEORG ---------------------------------> https://github.com/sensepost/reGeorg
----------------------------------------

RPIVOT ---------------------------------> https://github.com/klsecservices/rpivot
----------------------------------------'''


#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
banner = f'''

__________  _____ .___ _______   _____                                                         __         .__                 
\______   \/  |  ||   |\      \_/ ____\___________  _____   ____   ______ _____   ____   _____/  |______  |  |   ____   ______
 |     ___/   |  ||   |/   |   \   __\/  _ \_  __ \/     \_/ __ \ /  ___//     \_/ __ \ /    \   __\__  \ |  | _/ __ \ /  ___/
 |    |  /    ^   /   /    |    \  | (  <_> )  | \/  Y Y  \  ___/ \___ \|  Y Y  \  ___/|   |  \  |  / __ \|  |_\  ___/ \___ \ 
 |____|  \____   ||___\____|__  /__|  \____/|__|  |__|_|  /\___  >____  >__|_|  /\___  >___|  /__| (____  /____/\___  >____  >
              |__|            \/                        \/     \/     \/      \/     \/     \/          \/          \/     \/ 
{COLOR_PURPLE}By P4IM0N{COLOR_RESET}'''
print(banner)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    interructor = True
    try:
        # Crear o abrir el archivo en modo de escritura
        with open('P4InformeMentalPentesting.md', 'a') as archivo:
            # Recopilar información sobre la máquina objetivo
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LA EMPRESA O MAQUINA OBJETIVO: "+ COLOR_RESET)
            maquina_o_empresa_objetivo = ingresa_multipleslineas()
            archivo.write(f"# {maquina_o_empresa_objetivo}\n")  # Escribir el título de la máquina objetivo
            archivo.flush()
            
            # Agregar un cartel de "Descripción" antes del bucle de reconocimiento
            archivo.write("## DESCRIPCION\n")
            archivo.flush()
            
            sub_banner_menu = f'''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██{COLOR_PURPLE}█{COLOR_RESET} ██▌░░░▐██{COLOR_PURPLE}█{COLOR_RESET} ██│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
████████████████{COLOR_PURPLE}By P4IM0N!!!{COLOR_RESET}
            '''
            menu_de_opciones = [[" 1. RECONOCIMIENTO PASIVO"], [" 2. ANALISIS FORENSE"], [" 3. RECONOCIMIENTO ACTIVO"], [" 4. INVESTIGACION OSINT"], [" 5. HASHES Y DESENCRIPTADOS"], [" 6. FUERZA BRUTA A LOGINS"], [" 7. SCRIPT DE EXPLOIT Y PAYLOADS"], [" 8. EXPLOTACION"], [" 9. ESCALADA DE PRIVILEGIOS WINDOWS"], [" 10. ESCALADA DE PRIVILEGIOS LINUX"], [" 11. PIVOTING"], [" 12. VISTA PREVIA"], [" 13. AYUDA"], [" 14. FINALIZAR PENTESTING"]]
            
            while True:
                # Recopilar descripciones o información sobre la máquina objetivo
                print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"INGRESE DESCRIPCIONES O INFORMACION EXTRA DE LA EMPRESA O MAQUINA A REALIZAR EL PENTESTING: "+COLOR_RESET)
                description = ingresa_multipleslineas()
                print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                # Agregar la descripción al nivel de la sección de "Descripción"
                archivo.write(f"{description}\n")  # Escribir la descripción
                archivo.flush()
                
                # Agregar un cartel de "Reconocimiento" después de la descripción
                archivo.write("#### RECONOCIMIENTO\n")
                archivo.flush()
                
                while True:
                    
                    tabla_de_opciones = tabulate(menu_de_opciones, ['Nº OPCION'], tablefmt='grid')
                    print(sub_banner_menu)
                    print(tabla_de_opciones)
                    
                    print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                    elige_opcion = input(COLOR_RED+"ELIJA EL TIPO DE RECONOCIMIENTO QUE REALIZARA: "+COLOR_RESET)

                    if elige_opcion == '1':
                        archivo.write("##### RECONOCIMIENTO PASIVO\n")
                        investigacion_reconocimiento_pasivo(archivo)  
                        archivo.flush()
                    elif elige_opcion == '2':
                        archivo.write("##### ANALISIS FORENSE\n")
                        investigacion_analisis_forense(archivo)  
                        archivo.flush()
                    elif elige_opcion == '3':
                        archivo.write("##### RECONOCIMIENTO ACTIVO\n")
                        investigacion_reconocimiento_activo(archivo)  
                        archivo.flush()
                    elif elige_opcion == '4':
                        archivo.write("##### INVESTIGACION OSINT\n")
                        investigacion_investigacion_osint(archivo)
                        archivo.flush()
                    elif elige_opcion == '5':
                        archivo.write("##### HASHES Y DESENCRIPTADOS\n")
                        investigacion_hashes_y_desencriptados(archivo)
                        archivo.flush()
                    elif elige_opcion == '6':
                        archivo.write("##### FUERZA BRUTA A LOGINS\n")
                        investigacion_fuerza_bruta_logins(archivo)
                        archivo.flush()
                    elif elige_opcion == '7':
                        archivo.write("##### SCRIPT DE EXPLOIT Y PAYLOADS\n")
                        investigacion_script_exploit_y_payload(archivo)
                        archivo.flush()
                    elif elige_opcion == '8':
                        archivo.write("##### EXPLOTACION\n")
                        investigacion_explotacion(archivo)
                        archivo.flush() 
                    elif elige_opcion == '9':
                        archivo.write("##### ESCALADA DE PRIVILEGIOS WINDOWS\n")
                        investigacion_escalada_privilegios_windows(archivo)
                        archivo.flush()
                    elif elige_opcion == '10':
                        archivo.write("##### ESCALADA DE PRIVILEGIOS LINUX\n")
                        investigacion_escalada_privilegios_linux(archivo)
                        archivo.flush()  
                    elif elige_opcion == '11':
                        archivo.write("##### PIVOTING\n")
                        investigacion_pivoting(archivo)
                        archivo.flush()                     
                    elif elige_opcion == '12':
                        investigacion_vista_previa()
                    elif elige_opcion == '13':
                        leer_ayuda(ayuda)
                    elif elige_opcion == '14':
                        print("Pentesting finalizado. Gracias por usar P4Informesmentales manito.")                                      
                        return
                    else:
                        print("Opción no válida 8( ")

                

    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        
#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#permite ingresar multiples lineas, signos, hacer saltos de lineas, maneja limites de escrituras OK
def ingresa_multipleslineas(max_chars_per_line=100):
    try:
        lista_lineas_ingresadas = []
        print(COLOR_PURPLE+'---------------------------------------------'+COLOR_RESET)
        print(COLOR_PURPLE+'Manito preciona (f) y ENTER para continuar /'+COLOR_RESET)
        print(COLOR_PURPLE+'-------------------------------------------'+COLOR_RESET)
        while True:
            linea = input()
            linea = linea.strip()  # Eliminar espacios en blanco y saltos de línea al principio y al final
            # Eliminar almohadillas, guiones, signos más y espacios al principio de cada línea
            linea = linea.lstrip('#-+ ')
            
            if linea.upper() == 'F' or linea.upper() == 'STOP':
                break
            
            
            # Dividir la línea en segmentos más pequeños si supera el límite de caracteres por línea
            while len(linea) > max_chars_per_line:
                segmento = linea[:max_chars_per_line]
                lista_lineas_ingresadas.append(segmento)
                linea = linea[max_chars_per_line:]
            
            lista_lineas_ingresadas.append(linea)
            
        
        return '\n'.join(lista_lineas_ingresadas)
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al ingresar texto en bruto Manito, proba sacar algun simbolo que este causando el conflicto: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        return ""


#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Permite ingresar comandos en tiempo real y ser mostrados y guardados en el .md
def ejecutar_comandos():
    try:
        print(tabla_de_comandos_terminada)
        archivo_nombre = 'P4InformeMentalPentesting.md'
        with open(archivo_nombre, "a") as archivo_mapa:
            archivo_mapa.write("- COMANDO:\n")
            archivo_mapa.write('''  - ┌──(root㉿kalipaimon)-[/]
  - └─# ''')
            
            while True:
                print(COLOR_PURPLE+'----------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_PURPLE+"MANITO, INGRESA EL COMANDO A EJECUTAR (o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'---------------------------------------------------------------------'+COLOR_RESET)
                comando = input(f'''- {COLOR_YELLOW}┌──{COLOR_RESET}{COLOR_PURPLE}({COLOR_RESET}{COLOR_RED}root{COLOR_RESET}{COLOR_PURPLE}㉿{COLOR_RESET}{COLOR_RED}kalipaimon{COLOR_RESET}{COLOR_PURPLE}){COLOR_RESET}{COLOR_YELLOW}-[{COLOR_RESET}{COLOR_RED}/{COLOR_RESET}{COLOR_YELLOW}]
- └─{COLOR_RESET}#  ''')
                if comando.lower() == 'fin':
                    break

                archivo_mapa.write(comando + '\n')

                proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)    
                for linea in proceso.stdout:
                    print(linea, end='')  # Imprime en tiempo real en la terminal
                    archivo_mapa.write('  - ' + linea)  # Escribe lo de la terminal en el archivo

        print(COLOR_YELLOW+"\n\nManito el resultado quedo guardado en"+COLOR_RESET, archivo_nombre)

    except subprocess.CalledProcessError as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print("Error al ejecutar el comando manito:", error)
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
    except KeyboardInterrupt:
        print(COLOR_PURPLE+'---------------------------------------------'+COLOR_RESET)
        print("\n\nComando cancelado.")        

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Metodo para procesar el analisis RECONOCIMIENTO PASIVO      
def investigacion_reconocimiento_pasivo(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE RECONOCIMIENTO PASIVO /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_pasivo)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// RECONOCIMIENTO PASIVO /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
             
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA RESULTADOS COMPLETOS: "+COLOR_RESET)    
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()

            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
        
                    
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO RECONOCIMIENTO PASIVO? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis MANUAL Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
          
#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el ANALISIS FORENSE
def investigacion_analisis_forense(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE FORENSE /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_forense)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// ANALISIS FORENSE /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultado in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"DAME TUS CONCLUSIONES MANITO: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- CONCLUSIONES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANALISIS FORENSE? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis OSINT Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis RECONOCIMIENTO ACTIVO
def investigacion_reconocimiento_activo(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE RECONOCIMIENTO ACTIVO /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_activo)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// RECONOCIMIENTO ACTIVO /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultado in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"DAME TUS CONCLUSIONES MANITO: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- CONCLUSIONES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO RECONOCIMIENTO ACTIVO? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis OSINT Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis INVESTIGACION OSINT
def investigacion_investigacion_osint(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE RECONOCIMIENTO OSINT /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_OSINT)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// INVESTIGACION OSINT /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultado in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"DAME TUS CONCLUSIONES MANITO: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- CONCLUSIONES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRA INVESTIGACION OSINT? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis OSINT Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis HASHES Y DESENCRIPTADOS
def investigacion_hashes_y_desencriptados(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE HASHES Y DESENCRIPTADO /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_hashes_desencriptado)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HASHES Y DESENCRIPTADOS /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultado in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"DAME TUS CONCLUSIONES MANITO: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- CONCLUSIONES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANALISIS DE HASHES Y DESENCRIPTADOS? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis OSINT Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        
        
        
#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis FUERZA BRUTA A LOGINS
def investigacion_fuerza_bruta_logins(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE FUERZA BRUTA A LOGINS /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_fuerza_bruta_logins)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// FUERZA BRUTA A LOGINS /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultado in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"DAME TUS CONCLUSIONES MANITO: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- CONCLUSIONES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRA FUERZA BRUTA A LOGINS? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis OSINT Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        



#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis SCRIPT DE EXPLOIT Y PAYLOAD
def investigacion_script_exploit_y_payload(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE SCRIPT DE EXPLOIT Y PAYLOAD /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_explot_y_payload)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// SCRIPT DE EXPLOIT Y PAYLOAD /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultado in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"DAME TUS CONCLUSIONES MANITO: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- CONCLUSIONES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO SCRIPT DE EXPLOIT Y PAYLOAD? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis OSINT Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)                                        

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis de EXPLOTACION
def investigacion_explotacion(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE EXPLOTACION /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_explotacion)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// EXPLOTACION /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            herramienta = ingresa_multipleslineas()
            archivo.write(f"###### HERRAMIENTA: {herramienta}\n")  # Escribir el título de la herramienta
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultado = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_de_resultado in resultado.splitlines():
                archivo.write(f"  - {cada_linea_de_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar resultados importantes como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            resultados_importantes = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_resultado_importante in resultados_importantes.splitlines():
                archivo.write(f"  - {cada_linea_resultado_importante}\n")  # Escribir resultados importantes como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otra_herramienta = input(COLOR_RED+"¿QUERES USAR OTRA EXPLOTACION? (s/n): "+COLOR_RESET)
            if otra_herramienta.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis AUTOMATIZADO Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Método para procesar el análisis ESCALADAD DE PRIVILEGIOS WINDOWS 
def investigacion_escalada_privilegios_windows(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE RECONOCIMIENTO ESCALADA PRIVILEGIOS WINDOWS /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_privilegios_windows)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// ESCALADAD DE PRIVILEGIOS WINDOWS /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANLISIS DE ESCALADAD DE PRIVILEGIOS WINDOWS? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis de INGENIERIA SOCIAL Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Método para procesar el análisis ESCALADA DE PRIVILEGIOS LINUX
def investigacion_escalada_privilegios_linux(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE ESCALADA DE PRIVILEGIOS LINUX /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_privilegios_linux)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// ESCALADAD DE PRIVILEGIOS LINUX /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()
                
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANALISIS DE ESCALADA DE PRIVILEGIOS LINUX? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis MIXTO Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)


#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis de PIVOTING
def investigacion_pivoting(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// HERRAMIENTAS DE PIVOTING /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(text_reconocimiento_pivoting)
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(f'{COLOR_PURPLE}/////////////////// PIVOTING /////////////////////{COLOR_RESET}')
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL METODO O HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            herramienta = ingresa_multipleslineas()
            archivo.write(f"###### HERRAMIENTA: {herramienta}\n")  # Escribir el título de la herramienta
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultado = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_de_resultado in resultado.splitlines():
                archivo.write(f"  - {cada_linea_de_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar resultados importantes como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            resultados_importantes = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_resultado_importante in resultados_importantes.splitlines():
                archivo.write(f"  - {cada_linea_resultado_importante}\n")  # Escribir resultados importantes como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otra_herramienta = input(COLOR_RED+"¿QUERES USAR OTRA HERRAMIENTA DE PIVOTING? (s/n): "+COLOR_RESET)
            if otra_herramienta.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis AUTOMATIZADO Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)



#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#abrir XMIN para VISTA PREVIA
def investigacion_vista_previa():
    print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
    print(f'{COLOR_PURPLE}/////////////////// VISTA PREVIA DEL MAPA MENTAL EN XMIND /////////////////////{COLOR_RESET}')
    print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
    archivo = "P4InformeMentalPentesting"
    # Comando para abrir el archivo .md con Xmind
    comando = ["xmind", "open", f'/home/paimon/actualizacionP4Informesmentales-borrardirectorio/{archivo}.md']    

    # Ejecuta el comando
    try:
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Error al abrir el archivo con Xmind manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ver menu de AYUDA
def leer_ayuda(ayuda):
    print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
    print(f'{COLOR_PURPLE}/////////////////// AYUDA /////////////////////{COLOR_RESET}')
    print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
    try:
        print(ayuda)
         
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f'Se produjo un error manito: {error}')
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
if __name__ == "__main__":
    main()


#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


```
````

````python
// Some code VERSION VIEJA

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!programa para automatizar a traves de una interfas dinamica de ingresos de datos guiada para que se valla creando un reporte en formato MARKDOWN y asi tambien poder realizar con el en XMIND un mapa mental ya estructurado al qeu aparte podriamos personalizar despues con imagenes recolectadas,etc
#! P4INformesmentales.py 2.0v- By P4IM0N

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!TESTEADO EN KALI LINUX, LIBRERIAS E INSTALACION DE LAS MISMAS EN CASO DE NO TENERLAS
# Bibliotecas necesarias para el funcionamientoo:
# -subprocess: Para ejecutar comandos y capturar su la salida.
   #Podes instalarlo con el siguiente comando:
    #? pip install subprocess
# -tabulate: Para crear tablas a partir de datos en listas.
   #Podes instalarlo con el siguiente commando:
    #? pip install tabulate

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Importamos librerias
from tabulate import tabulate
import subprocess

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Códigos de escape ANSI para cambiar el color del texto en la terminal
COLOR_RED = "\033[91m"
COLOR_PURPLE = '\x1b[35m'
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''comandos = {
    "Ping Básico": "ping https://objetivo.com - Realiza un ping simple al sitio web para verificar si está accesible.",
    "Ping con Intervalo de Tiempo Personalizado": "ping -c 5 -i 0.2 https://objetivo.com - Realiza 5 pings con un intervalo de 0.2 segundos entre ellos.",
    "Ping con Tamaño de Paquete Personalizado": "ping -c 5 -s 100 https://objetivo.com - Envía paquetes de 100 bytes al sitio y registra si obtiene respuesta.",
    "Envío Indefinido de Paquetes": "ping -i 1 -s 56 -D https://objetivo.com - Envía paquetes de 56 bytes con intervalo de 1 segundo de forma indefinida.",
    "Registro de Resultados en un Archivo": "ping -c 5 https://objetivo.com > resultados.txt - Realiza 5 pings y guarda los resultados en un archivo llamado 'resultados.txt'.",
    "Supresión de Resolución Inversa": "ping -n -c 5 https://objetivo.com - Realiza pings sin resolver direcciones IP inversas.",
    "Nmap Escaneo Básico de Puertos": "nmap https://objetivo.com - Escanea los puertos abiertos en el objetivo y muestra información básica.",
    "Nmap Escaneo de Servicios y Sistema Operativo": "nmap -sV -O https://objetivo.com - Detecta versiones de servicios y sistema operativo del objetivo.",
    "Nmap Escaneo de Todos los Puertos y Scripts de Detección de Vulnerabilidades": "nmap -p- -sV --script vuln https://objetivo.com - Escanea todos los puertos, detecta versiones y ejecuta scripts de detección de vulnerabilidades.",
    "Nmap Escaneo Rápido de los 1000 Puertos Más Comunes": "nmap -F https://objetivo.com - Realiza un escaneo rápido de los 1000 puertos más comunes.",
    "Nmap Escaneo UDP": "nmap -sU https://objetivo.com - Escanea los puertos UDP abiertos en el objetivo.",
    "Nmap Escaneo de un Rango Personalizado de Puertos": "nmap -p 80,443,8080 https://objetivo.com - Escanea puertos específicos (80, 443 y 8080) en el objetivo.",
    "Nikto Escaneo Básico de Nikto": "nikto -h https://objetivo.com - Realiza un escaneo básico en busca de vulnerabilidades conocidas.",
    "Nikto Escaneo Completo de Nikto": "nikto -h https://objetivo.com -C all - Realiza un escaneo completo, incluyendo todas las pruebas disponibles.",
    "Nikto Escaneo con Plugins de Vulnerabilidades": "nikto -h https://objetivo.com -Plugins +vulnerabilities - Habilita plugins específicos que buscan vulnerabilidades en el sitio web.",
    "Nikto Escaneo SSL": "nikto -h https://objetivo.com -ssl - Realiza un escaneo enfocado en SSL y sus vulnerabilidades.",
    "Nikto Escaneo Proxy": "nikto -h https://objetivo.com -useproxy http://mi.proxy.com:8080 - Utiliza un proxy para realizar el escaneo.",
    "Nikto Escaneo Personalizado de Puertos": "nikto -h https://objetivo.com -port 80,443 - Realiza el escaneo solo en los puertos 80 y 443.",
    "Dirb Escaneo Básico de Directorios": "dirb https://objetivo.com - Realiza un escaneo básico en busca de directorios y archivos ocultos en el objetivo.",
    "Dirb Escaneo con una Lista de Palabras Personalizada": "dirb https://objetivo.com /ruta/a/mi/wordlist.txt - Utiliza una lista de palabras personalizada para buscar directorios y archivos en el objetivo.",
    "Dirb Escaneo con Búsqueda de Extensiones Específicas": "dirb https://objetivo.com -X .php,.html - Busca directorios y archivos con extensiones específicas, como .php y .html.",
    "Dirb Escaneo Recursivo": "dirb https://objetivo.com -r - Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.",
    "Dirb Escaneo de Autenticación Básica": "dirb https://objetivo.com -a usuario:contraseña - Realiza un escaneo en un sitio web que requiere autenticación básica HTTP.",
    "Dirb Escaneo con Límite de Tiempo Personalizado": "dirb https://objetivo.com -t 30 - Establece un límite de tiempo para las solicitudes durante el escaneo.",
    "SQLMap Detección de Bases de Datos": "sqlmap -u 'https://objetivo.com/page?id=1' - Detecta las bases de datos y las vulnerabilidades de inyección SQL en la URL proporcionada.",
    "SQLMap Enumeración de Bases de Datos": "sqlmap -u 'https://objetivo.com/page?id=1' --dbs - Enumera las bases de datos disponibles en el objetivo.",
    "SQLMap Enumeración de Tablas": "sqlmap -u 'https://objetivo.com/page?id=1' --dbs --tables - Enumera las tablas en una base de datos específica.",
    "SQLMap Explotación de una Inyección SQL": "sqlmap -u 'https://objetivo.com/page?id=1' --data 'parametro=valor' --dump - Explota una vulnerabilidad de inyección SQL y recupera datos de la base de datos.",
    "SQLMap Escaneo de Inyección SQL a Ciegas": "sqlmap -u 'https://objetivo.com/page?id=1' --data 'parametro=valor' --level 5 --risk 3 - Realiza un escaneo avanzado de inyección SQL a ciegas en el objetivo.",
    "SQLMap Explotación con Fuerza Bruta de Hashes": "sqlmap -u 'https://objetivo.com/page?id=1' --data 'parametro=valor' --crack - Intenta crackear hashes de contraseñas recuperados de la base de datos.",
    "XSSer Escaneo Básico en Busca de Vulnerabilidades XSS": "xsstrike -u 'https://objetivo.com' - Escanea la URL en busca de vulnerabilidades de Cross-Site Scripting (XSS).",
    "XSSer Escaneo con Enumeración de Enlaces Vulnerables": "xsstrike -u 'https://objetivo.com' -l - Escanea y enumera enlaces vulnerables a ataques XSS en la página.",
    "XSSer Escaneo con Análisis de Todas las Inyecciones de Parámetros": "xsstrike -u 'https://objetivo.com' -p all - Realiza un análisis exhaustivo de todas las inyecciones de parámetros en la URL.",
    "XSSer Escaneo con Filtrado Personalizado de Payloads": "xsstrike -u 'https://objetivo.com' -p all -fp 'mi_payload.txt' - Escanea utilizando payloads personalizados definidos en 'mi_payload.txt'.",
    "XSSer Escaneo con Límite de Tiempo Personalizado": "xsstrike -u 'https://objetivo.com' -t 10 - Establece un límite de tiempo para cada solicitud durante el escaneo.",
    "XSSer Escaneo con Seguimiento de Redirecciones": "xsstrike -u 'https://objetivo.com' -r - Realiza el escaneo siguiendo las redirecciones en la página web objetivo.",
    "Dnsrecon Escaneo Básico de DNS": "dnsrecon -d https://objetivo.com - Realiza un escaneo básico en busca de registros DNS asociados al dominio.",
    "Dnsrecon Escaneo Utilizando Diccionario": "dnsrecon -d https://objetivo.com -t std -D /ruta/a/mi/diccionario.txt - Utiliza un diccionario personalizado para realizar un escaneo exhaustivo de DNS.",
    "Dnsrecon Enumeración de Servidores de Nombres": "dnsrecon -d https://objetivo.com -t brt - Enumera los servidores de nombres relacionados con el dominio.",
    "Dnsrecon Escaneo con un Límite de Tiempo Personalizado": "dnsrecon -d https://objetivo.com -t brt -T 30 - Establece un límite de tiempo para el escaneo.",
    "Dnsrecon Escaneo en Búsqueda de Subdominios": "dnsrecon -d https://objetivo.com -t brt -n - Busca subdominios relacionados con el dominio principal.",
    "Dnsrecon Escaneo Inverso de Direcciones IP": "dnsrecon -r 192.168.1.1 - Realiza un escaneo inverso de una dirección IP específica.",
    "SQLNinja Detección de la Vulnerabilidad": "sqlninja -i https://objetivo.com - Detecta la vulnerabilidad de inyección SQL en el sitio web.",
    "SQLNinja Enumeración de Tablas": "sqlninja -i https://objetivo.com -m t - Enumera las tablas en la base de datos objetivo.",
    "SQLNinja Enumeración de Columnas": "sqlninja -i https://objetivo.com -m c - Enumera las columnas en las tablas de la base de datos.",
    "SQLNinja Explotación de Inyección SQL": "sqlninja -i https://objetivo.com -m s - Explota la vulnerabilidad de inyección SQL y recupera información de la base de datos.",
    "SQLNinja Escaneo de Credenciales": "sqlninja -i https://objetivo.com -m u - Escanea y recupera credenciales de la base de datos.",
    "SQLNinja Explotación con Fuerza Bruta": "sqlninja -i https://objetivo.com -m f - Intenta adivinar contraseñas utilizando un ataque de fuerza bruta.",
    "Gobuster Escaneo Básico de Directorios": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/common.txt - Realiza un escaneo básico de directorios en busca de directorios y archivos ocultos en el objetivo.",
    "Gobuster Escaneo con una Lista de Palabras Personalizada": "gobuster dir -u https://objetivo.com -w /ruta/a/mi/wordlist.txt - Utiliza una lista de palabras personalizada para buscar directorios en objetivo",
    "Gobuster Escaneo con Búsqueda de Extensiones Específicas": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/big.txt -x .php,.html - Busca directorios y archivos con extensiones específicas, como .php y .html.",
    "Gobuster Escaneo Recursivo": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/common.txt -r - Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.",
    "Gobuster Escaneo de Autenticación Básica": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/common.txt -U usuario -P contraseña - Escanea un sitio web que requiere autenticación HTTP básica.",
    "Gobuster Escaneo con Límite de Tiempo Personalizado": "gobuster dir -u https://objetivo.com -w /usr/share/wordlists/dirb/common.txt -t 30 - Establece un límite de tiempo para las solicitudes durante el escaneo."
}'''

comandos = {
    "Ping Básico": f"ping {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ping simple al sitio web para verificar si está accesible.{COLOR_RESET}",
    "Ping con Intervalo de Tiempo Personalizado": f"ping -c 5 -i 0.2 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza 5 pings con un intervalo de 0.2 segundos entre ellos.{COLOR_RESET}",
    "Ping con Tamaño de Paquete Personalizado": f"ping -c 5 -s 100 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Envía paquetes de 100 bytes al sitio y registra si obtiene respuesta.{COLOR_RESET}",
    "Envío Indefinido de Paquetes": f"ping -i 1 -s 56 -D {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Envía paquetes de 56 bytes con intervalo de 1 segundo de forma indefinida.{COLOR_RESET}",
    "Registro de Resultados en un Archivo": f"ping -c 5 {COLOR_RED}https://objetivo.com{COLOR_RESET} > {COLOR_RED}resultados.txt{COLOR_RESET} - {COLOR_YELLOW}Realiza 5 pings y guarda los resultados en un archivo llamado 'resultados.txt'.{COLOR_RESET}",
    "Supresión de Resolución Inversa": f"ping -n -c 5 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza pings sin resolver direcciones IP inversas.{COLOR_RESET}",
    "Nmap Escaneo Básico de Puertos": f"nmap {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea los puertos abiertos en el objetivo y muestra información básica.{COLOR_RESET}",
    "Nmap Escaneo de Servicios y Sistema Operativo": f"nmap -sV -O {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Detecta versiones de servicios y sistema operativo del objetivo.{COLOR_RESET}",
    "Nmap Escaneo de Todos los Puertos y Scripts de Detección de Vulnerabilidades": f"nmap -p- -sV --script vuln {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea todos los puertos, detecta versiones y ejecuta scripts de detección de vulnerabilidades.{COLOR_RESET}",
    "Nmap Escaneo Rápido de los 1000 Puertos Más Comunes": f"nmap -F {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo rápido de los 1000 puertos más comunes.{COLOR_RESET}",
    "Nmap Escaneo UDP": f"nmap -sU {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea los puertos UDP abiertos en el objetivo.{COLOR_RESET}",
    "Nmap Escaneo de un Rango Personalizado de Puertos": f"nmap -p 80,443,8080 {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Escanea puertos específicos (80, 443 y 8080) en el objetivo.{COLOR_RESET}",
    "Nikto Escaneo Básico de Nikto": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de vulnerabilidades conocidas.{COLOR_RESET}",
    "Nikto Escaneo Completo de Nikto": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -C all - {COLOR_YELLOW}Realiza un escaneo completo, incluyendo todas las pruebas disponibles.{COLOR_RESET}",
    "Nikto Escaneo con Plugins de Vulnerabilidades": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -Plugins +vulnerabilities - {COLOR_YELLOW}Habilita plugins específicos que buscan vulnerabilidades en el sitio web.{COLOR_RESET}",
    "Nikto Escaneo SSL": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -ssl - {COLOR_YELLOW}Realiza un escaneo enfocado en SSL y sus vulnerabilidades.{COLOR_RESET}",
    "Nikto Escaneo Proxy": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -useproxy http://mi.proxy.com:8080 - {COLOR_YELLOW}Utiliza un proxy para realizar el escaneo.{COLOR_RESET}",
    "Nikto Escaneo Personalizado de Puertos": f"nikto -h {COLOR_RED}https://objetivo.com{COLOR_RESET} -port 80,443 - {COLOR_YELLOW}Realiza el escaneo solo en los puertos 80 y 443.{COLOR_RESET}",
    "Dirb Escaneo Básico de Directorios": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de directorios y archivos ocultos en el objetivo.{COLOR_RESET}",
    "Dirb Escaneo con una Lista de Palabras Personalizada": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} /ruta/a/mi/wordlist.txt - {COLOR_YELLOW}Utiliza una lista de palabras personalizada para buscar directorios y archivos en el objetivo.{COLOR_RESET}",
    "Dirb Escaneo con Búsqueda de Extensiones Específicas": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -X .php,.html - {COLOR_YELLOW}Busca directorios y archivos con extensiones específicas, como .php y .html.{COLOR_RESET}",
    "Dirb Escaneo Recursivo": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -r - {COLOR_YELLOW}Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.{COLOR_RESET}",
    "Dirb Escaneo de Autenticación Básica": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -a usuario:contraseña - {COLOR_YELLOW}Realiza un escaneo en un sitio web que requiere autenticación básica HTTP.{COLOR_RESET}",
    "Dirb Escaneo con Límite de Tiempo Personalizado": f"dirb {COLOR_RED}https://objetivo.com{COLOR_RESET} -t 30 - {COLOR_YELLOW}Establece un límite de tiempo para las solicitudes durante el escaneo.{COLOR_RESET}",
    "SQLMap Detección de Bases de Datos": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} - {COLOR_YELLOW}Detecta las bases de datos y las vulnerabilidades de inyección SQL en la URL proporcionada.{COLOR_RESET}",
    "SQLMap Enumeración de Bases de Datos": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --dbs - {COLOR_YELLOW}Enumera las bases de datos disponibles en el objetivo.{COLOR_RESET}",
    "SQLMap Enumeración de Tablas": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --dbs --tables - {COLOR_YELLOW}Enumera las tablas en una base de datos específica.{COLOR_RESET}",
    "SQLMap Explotación de una Inyección SQL": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --dump - {COLOR_YELLOW}Explota una vulnerabilidad de inyección SQL y recupera datos de la base de datos.{COLOR_RESET}",
    "SQLMap Escaneo de Inyección SQL a Ciegas": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --level 5 --risk 3 - {COLOR_YELLOW}Realiza un escaneo avanzado de inyección SQL a ciegas en el objetivo.{COLOR_RESET}",
    "SQLMap Explotación con Fuerza Bruta de Hashes": f"sqlmap -u {COLOR_RED}'https://objetivo.com/page?id=1'{COLOR_RESET} --data 'parametro=valor' --crack - {COLOR_YELLOW}Intenta crackear hashes de contraseñas recuperados de la base de datos.{COLOR_RESET}",
    "XSSer Escaneo Básico en Busca de Vulnerabilidades XSS": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} - {COLOR_YELLOW}Escanea la URL en busca de vulnerabilidades de Cross-Site Scripting (XSS).{COLOR_RESET}",
    "XSSer Escaneo con Enumeración de Enlaces Vulnerables": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -l - {COLOR_YELLOW}Escanea y enumera enlaces vulnerables a ataques XSS en la página.{COLOR_RESET}",
    "XSSer Escaneo con Análisis de Todas las Inyecciones de Parámetros": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -p all - {COLOR_YELLOW}Realiza un análisis exhaustivo de todas las inyecciones de parámetros en la URL.{COLOR_RESET}",
    "XSSer Escaneo con Filtrado Personalizado de Payloads": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -p all -fp 'mi_payload.txt' - {COLOR_YELLOW}Escanea utilizando payloads personalizados definidos en 'mi_payload.txt'.{COLOR_RESET}",
    "XSSer Escaneo con Límite de Tiempo Personalizado": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -t 10 - {COLOR_YELLOW}Establece un límite de tiempo para cada solicitud durante el escaneo.{COLOR_RESET}",
    "XSSer Escaneo con Seguimiento de Redirecciones": f"xsstrike -u {COLOR_RED}'https://objetivo.com'{COLOR_RESET} -r - {COLOR_YELLOW}Realiza el escaneo siguiendo las redirecciones en la página web objetivo.{COLOR_RESET}",
    "Dnsrecon Escaneo Básico de DNS": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un escaneo básico en busca de registros DNS asociados al dominio.{COLOR_RESET}",
    "Dnsrecon Escaneo Utilizando Diccionario": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t std -D /ruta/a/mi/diccionario.txt - {COLOR_YELLOW}Utiliza un diccionario personalizado para realizar un escaneo exhaustivo de DNS.{COLOR_RESET}",
    "Dnsrecon Enumeración de Servidores de Nombres": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt - {COLOR_YELLOW}Enumera los servidores de nombres relacionados con el dominio.{COLOR_RESET}",
    "Dnsrecon Escaneo con un Límite de Tiempo Personalizado": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt -T 30 - {COLOR_YELLOW}Establece un límite de tiempo para el escaneo.{COLOR_RESET}",
    "Dnsrecon Escaneo en Búsqueda de Subdominios": f"dnsrecon -d {COLOR_RED}https://objetivo.com{COLOR_RESET} -t brt -n - {COLOR_YELLOW}Busca subdominios relacionados con el dominio principal.{COLOR_RESET}",
    "Dnsrecon Escaneo Inverso de Direcciones IP": f"dnsrecon -r 192.168.1.1 - {COLOR_YELLOW}Realiza un escaneo inverso de una dirección IP específica.{COLOR_RESET}",
    "SQLNinja Detección de la Vulnerabilidad": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Detecta la vulnerabilidad de inyección SQL en el sitio web.{COLOR_RESET}",
    "SQLNinja Enumeración de Tablas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET}-m t - {COLOR_YELLOW}Enumera las tablas en la base de datos objetivo.{COLOR_RESET}",
    "SQLNinja Enumeración de Tablas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -tn - {COLOR_YELLOW}Enumera las tablas en la base de datos vulnerable.{COLOR_RESET}",
    "SQLNinja Enumeración de Columnas": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -cn - {COLOR_YELLOW}Enumera las columnas en las tablas de la base de datos.{COLOR_RESET}",
    "SQLNinja Explotación de Inyección SQL": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -m {COLOR_RED}POST{COLOR_RESET} - {COLOR_YELLOW}Explota la vulnerabilidad de inyección SQL y recupera datos de la base de datos.{COLOR_RESET}",
    "SQLNinja Escalada de Privilegios": f"sqlninja -i {COLOR_RED}https://objetivo.com{COLOR_RESET} -x {COLOR_RED}'EXEC sp_addsrvrolemember ''sysadmin'', ''usuario'';'{COLOR_RESET} - {COLOR_YELLOW}Realiza una escalada de privilegios para obtener control total del servidor SQL.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta SSH": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}ssh://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta SSH contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta FTP": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}ftp://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta FTP contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta Telnet": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}telnet://objetivo.com{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta Telnet contra un servidor remoto.{COLOR_RESET}",
    "Hydra Ataque de Fuerza Bruta HTTP POST": f"hydra -l usuario -P /ruta/a/mi/lista_de_contraseñas.txt {COLOR_RED}http-post://objetivo.com/login{COLOR_RESET} - {COLOR_YELLOW}Realiza un ataque de fuerza bruta HTTP POST contra un formulario de inicio de sesión.{COLOR_RESET}",
    "Gobuster Escaneo Básico de Directorios": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt - {COLOR_YELLOW}Realiza un escaneo básico de directorios en busca de directorios y archivos ocultos en el objetivo.{COLOR_RESET}",
    "Gobuster Escaneo con una Lista de Palabras Personalizada": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /ruta/a/mi/wordlist.txt - {COLOR_YELLOW}Utiliza una lista de palabras personalizada para buscar directorios en el objetivo.{COLOR_RESET}",
    "Gobuster Escaneo con Búsqueda de Extensiones Específicas": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/big.txt -x .php,.html - {COLOR_YELLOW}Busca directorios y archivos con extensiones específicas, como .php y .html.{COLOR_RESET}",
    "Gobuster Escaneo Recursivo": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -r - {COLOR_YELLOW}Realiza un escaneo recursivo para buscar directorios y archivos en profundidad.{COLOR_RESET}",
    "Gobuster Escaneo de Autenticación Básica": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -U usuario -P contraseña - {COLOR_YELLOW}Escanea un sitio web que requiere autenticación HTTP básica.{COLOR_RESET}",
    "Gobuster Escaneo con Límite de Tiempo Personalizado": f"gobuster dir -u {COLOR_RED}https://objetivo.com{COLOR_RESET} -w /usr/share/wordlists/dirb/common.txt -t 30 - {COLOR_YELLOW}Establece un límite de tiempo para las solicitudes durante el escaneo.{COLOR_RESET}"
}


tabla_de_comandos = [[comando, COLOR_PURPLE+descripcion+COLOR_RESET] for comando, descripcion in comandos.items()]    #conprension de lista para conseguir la tabla con los colores
tabla_de_comandos_terminada = (tabulate(tabla_de_comandos, headers=['DESCRIPCION','COMANDO','EXPLICACION'], tablefmt='grid'))
#print(tabla_de_comandos_terminada)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
banner = f'''

__________  _____ .___ _______   _____                                                         __         .__                 
\______   \/  |  ||   |\      \_/ ____\___________  _____   ____   ______ _____   ____   _____/  |______  |  |   ____   ______
 |     ___/   |  ||   |/   |   \   __\/  _ \_  __ \/     \_/ __ \ /  ___//     \_/ __ \ /    \   __\__  \ |  | _/ __ \ /  ___/
 |    |  /    ^   /   /    |    \  | (  <_> )  | \/  Y Y  \  ___/ \___ \|  Y Y  \  ___/|   |  \  |  / __ \|  |_\  ___/ \___ \ 
 |____|  \____   ||___\____|__  /__|  \____/|__|  |__|_|  /\___  >____  >__|_|  /\___  >___|  /__| (____  /____/\___  >____  >
              |__|            \/                        \/     \/     \/      \/     \/     \/          \/          \/     \/ 
{COLOR_PURPLE}By P4IM0N{COLOR_RESET}'''
print(banner)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    try:
        # Crear o abrir el archivo en modo de escritura
        with open('P4InformeMentalPentesting.md', 'a') as archivo:
            # Recopilar información sobre la máquina objetivo
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LA EMPRESA O MAQUINA OBJETIVO: "+ COLOR_RESET)
            maquina_o_empresa_objetivo = ingresa_multipleslineas()
            archivo.write(f"# {maquina_o_empresa_objetivo}\n")  # Escribir el título de la máquina objetivo
            archivo.flush()
            
            # Agregar un cartel de "Descripción" antes del bucle de reconocimiento
            archivo.write("## DESCRIPCION\n")
            archivo.flush()
            
            sub_banner_menu = f'''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██{COLOR_PURPLE}█{COLOR_RESET} ██▌░░░▐██{COLOR_PURPLE}█{COLOR_RESET} ██│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
████████████████{COLOR_PURPLE}By P4IM0N!!!{COLOR_RESET}
            '''
            menu_de_opciones = [[" 1. MANUAL"], [" 2. OSINT"], [" 3. AUTOMATIZADO"], [" 4. INGENIERIA SOCIAL"], [" 5. MIXTO"],[" 6. VISTA PREVIA"],[" 7. AYUDA"],[" 8. FINALIZAR PENTESTING"]]
            
            while True:
                # Recopilar descripciones o información sobre la máquina objetivo
                print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"INGRESE DESCRIPCIONES O INFORMACION EXTRA DE LA EMPRESA O MAQUINA A REALIZAR EL PENTESTING: "+COLOR_RESET)
                description = ingresa_multipleslineas()
                print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                # Agregar la descripción al nivel de la sección de "Descripción"
                archivo.write(f"{description}\n")  # Escribir la descripción
                archivo.flush()
                
                # Agregar un cartel de "Reconocimiento" después de la descripción
                archivo.write("#### RECONOCIMIENTO\n")
                archivo.flush()
                
                while True:
                    
                    tabla_de_opciones = tabulate(menu_de_opciones, ['Nº OPCION'], tablefmt='grid')
                    print(sub_banner_menu)
                    print(tabla_de_opciones)
                    
                    print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
                    elige_opcion = input(COLOR_RED+"ELIJA EL TIPO DE RECONOCIMIENTO QUE REALIZARA: "+COLOR_RESET)

                    if elige_opcion == '1':
                        archivo.write("##### MANUAL\n")
                        investigacion_manual(archivo)  # Llamar al método para procesar el análisis manual
                        archivo.flush()
                    elif elige_opcion == '2':
                        archivo.write("##### OSINT\n")
                        investigacion_osint(archivo)  # Llamar al método para procesar el análisis OSINT
                        archivo.flush()
                    elif elige_opcion == '3':
                        archivo.write("##### AUTOMATIZADO\n")
                        investigacion_automatizada(archivo)  # Llamar al método para procesar el análisis automatizado
                        archivo.flush()
                    elif elige_opcion == '4':
                        archivo.write("##### INGENIERIA SOCIAL\n")
                        investigacion_ing_social(archivo)
                        archivo.flush()
                    elif elige_opcion == '5':
                        archivo.write("##### MIXTO\n")
                        investigacion_mixto(archivo)
                        archivo.flush()
                    elif elige_opcion == '6':
                        investigacion_vista_previa()
                    elif elige_opcion == '7':
                        leer_ayuda()
                    elif elige_opcion == '8':
                        print("Pentesting finalizado.")
                        return
                    else:
                        print("Opción no válida 8( ")

                

    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        
#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#permite ingresar multiples lineas, signos, hacer saltos de lineas, maneja limites de escrituras OK
def ingresa_multipleslineas(max_chars_per_line=100):
    try:
        lista_lineas_ingresadas = []
        print(COLOR_PURPLE+'---------------------------------------------'+COLOR_RESET)
        print(COLOR_PURPLE+'Manito preciona (f) y ENTER para continuar /'+COLOR_RESET)
        print(COLOR_PURPLE+'-------------------------------------------'+COLOR_RESET)
        while True:
            linea = input()
            linea = linea.strip()  # Eliminar espacios en blanco y saltos de línea al principio y al final
            # Eliminar almohadillas, guiones, signos más y espacios al principio de cada línea
            linea = linea.lstrip('#-+ ')
            
            if linea.upper() == 'F' or linea.upper() == 'STOP':
                break
            
            
            # Dividir la línea en segmentos más pequeños si supera el límite de caracteres por línea
            while len(linea) > max_chars_per_line:
                segmento = linea[:max_chars_per_line]
                lista_lineas_ingresadas.append(segmento)
                linea = linea[max_chars_per_line:]
            
            lista_lineas_ingresadas.append(linea)
            
        
        return '\n'.join(lista_lineas_ingresadas)
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al ingresar texto en bruto Manito, proba sacar algun simbolo que este causando el conflicto: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        return ""


#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Permite ingresar comandos en tiempo real y ser mostrados y guardados en el .md
def ejecutar_comandos():
    try:
        print(tabla_de_comandos_terminada)
        archivo_nombre = 'P4InformeMentalPentesting.md'
        with open(archivo_nombre, "a") as archivo_mapa:
            archivo_mapa.write("- COMANDO:\n")
            archivo_mapa.write('''  - ┌──(root㉿kalipaimon)-[/]
  - └─# ''')
            
            while True:
                print(COLOR_PURPLE+'----------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_PURPLE+"MANITO, INGRESA EL COMANDO A EJECUTAR (o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'---------------------------------------------------------------------'+COLOR_RESET)
                comando = input(f'''- {COLOR_YELLOW}┌──{COLOR_RESET}{COLOR_PURPLE}({COLOR_RESET}{COLOR_RED}root{COLOR_RESET}{COLOR_PURPLE}㉿{COLOR_RESET}{COLOR_RED}kalipaimon{COLOR_RESET}{COLOR_PURPLE}){COLOR_RESET}{COLOR_YELLOW}-[{COLOR_RESET}{COLOR_RED}/{COLOR_RESET}{COLOR_YELLOW}]
- └─{COLOR_RESET}#  ''')
                if comando.lower() == 'fin':
                    break

                archivo_mapa.write(comando + '\n')

                proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                for linea in proceso.stdout:
                    print(linea, end='')  # Imprime en tiempo real en la terminal
                    archivo_mapa.write('  - ' + linea)  # Escribe lo de la terminal en el archivo

        print(COLOR_YELLOW+"\n\nManito el resultado quedo guardado en"+COLOR_RESET, archivo_nombre)

    except subprocess.CalledProcessError as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print("Error al ejecutar el comando manito:", error)
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
    except KeyboardInterrupt:
        print(COLOR_PURPLE+'---------------------------------------------'+COLOR_RESET)
        print("\n\nComando cancelado.")        

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Metodo para procesar el analisis MANUAL      
def investigacion_manual(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL TIPO DE ANALISIS [[MANUAL]] QUE VAS A HACER: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
             
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA RESULTADOS COMPLETOS: "+COLOR_RESET)    
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()

            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
        
                    
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANÁLISIS MANUAL? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis MANUAL Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
          
#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis OSINT
def investigacion_osint(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL TIPO DE ANALISIS OSINT QUE VAS A HACER: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultado in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"DAME TUS CONCLUSIONES MANITO: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- CONCLUSIONES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANALISIS OSINT? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis OSINT Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
# Método para procesar el análisis automatizado
def investigacion_automatizada(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME LA HERRAMIENTA QUE VAS A USAR: "+COLOR_RESET)
            herramienta = ingresa_multipleslineas()
            archivo.write(f"###### HERRAMIENTA: {herramienta}\n")  # Escribir el título de la herramienta
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultado = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_de_resultado in resultado.splitlines():
                archivo.write(f"  - {cada_linea_de_resultado}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar resultados importantes como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            resultados_importantes = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_resultado_importante in resultados_importantes.splitlines():
                archivo.write(f"  - {cada_linea_resultado_importante}\n")  # Escribir resultados importantes como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otra_herramienta = input(COLOR_RED+"¿QUERES USAR OTRA HERRAMIENTA MANITO? (s/n): "+COLOR_RESET)
            if otra_herramienta.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis AUTOMATIZADO Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Método para procesar el análisis Ingenieria social
def investigacion_ing_social(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL TIPO DE ANALISIS DE [[INGENIERIA SOCIAL]] QUE VAS A HACER: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()
            
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANLISIS DE INGENIERIA SOCIAL? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis de INGENIERIA SOCIAL Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Método para procesar el análisis mixto
def investigacion_mixto(archivo):
    try:
        while True:
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO DECIME EL TIPO DE ANALISIS [[MIXTO]] QUE VAS A HACER: "+COLOR_RESET)
            tipo_de_analisis = ingresa_multipleslineas()
            archivo.write(f"###### {tipo_de_analisis}\n")  # Escribir el título del tipo de análisis
            archivo.flush()
            
            # Agregar para ejecutar comandos y guardar con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
             
            print(COLOR_RED+"MANITO, ¿QUERES EJECUTAR UN COMANDO? (s/n): "+COLOR_RESET)
            ejecutar_comando = input()
            if ejecutar_comando.lower() == 's':
                print(COLOR_PURPLE+'-----------------------------------------------------------------------------------------------'+COLOR_RESET)
                print(COLOR_RED+"MANITO, PARA INGRESA EL COMANDO A EJECUTAR PRESIONA ((ENTER)),(o escribe 'fin' para salir): /"+COLOR_RESET)
                print(COLOR_PURPLE+'----------------------------------------------------------------------------------------------'+COLOR_RESET)
                comando = input()
                if comando.lower() == 'fin':
                    break  # Salir del loop si se ingresa "fin"
                ejecutar_comandos()
            
            # Agregar resultados como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"INGRESA LOS RESULTADOS COMPLETOS MANITO: "+COLOR_RESET)
            resultados = ingresa_multipleslineas()
            archivo.write("- RESULTADOS:\n")
            for cada_linea_resultados in resultados.splitlines():
                archivo.write(f"  - {cada_linea_resultados}\n")  # Escribir resultados como listas
                archivo.flush()
                
            # Agregar conclusiones como listas con guiones
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            print(COLOR_RED+"MANITO INGRESA LO IMPORTANTE QUE SACASTE DE LOS RESULTADOS: "+COLOR_RESET)
            conclusiones = ingresa_multipleslineas()
            archivo.write("- RESULTADOS IMPORTANTES:\n")
            for cada_linea_conclusiones in conclusiones.splitlines():
                archivo.write(f"  - {cada_linea_conclusiones}\n")  # Escribir conclusiones como listas
                archivo.flush()
            
            print(COLOR_YELLOW+'-------------------------------------------------------------------------------------------------------'+COLOR_RESET)
            otro_analisis = input(COLOR_RED+"¿MANITO QUERES HACER OTRO ANALISIS MIXTO? (s/n): "+COLOR_RESET)
            if otro_analisis.lower() != 's':
                break
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Se produjo un error al procesar el análisis MIXTO Manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#abrir XMIN para vista previa
def investigacion_vista_previa():
    archivo = "P4InformeMentalPentesting.md"
    # Comando para abrir el archivo .md con Xmind
    comando = ["xmind", "open", f'/home/paimon/cursopythonhacking/herramientaparainformesYmapamental/{archivo}.md']

    # Ejecuta el comando
    try:
        subprocess.run(comando, check=True)
    except subprocess.CalledProcessError as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f"Error al abrir el archivo con Xmind manito: {error}")
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ver menu de AYUDA
def leer_ayuda():
    try:
        # Abrir el archivo en modo de lectura ('r')
        with open('ayuda.txt', 'r') as archivo:
            # Realiza las operaciones de lectura aquí
            contenido = archivo.read()
            return print(COLOR_YELLOW+contenido+COLOR_RESET)  # Esto imprimirá el contenido 
    except Exception as error:
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)
        print(f'Se produjo un error manito: {error}')
        print(COLOR_RED+'***********************************************************************************************************'+COLOR_RESET)

#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------        
if __name__ == "__main__":
    main()


#?-----------------------------------------------------------------------------------------------------------------------------------------------------------------------


```
````
