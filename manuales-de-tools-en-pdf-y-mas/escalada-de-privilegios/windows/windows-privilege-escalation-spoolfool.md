# 🙅‍♂️ Windows Privilege Escalation - SPOOLFOOL

Oliver Lyak publicó un artículo sobre una vulnerabilidad de escalada de privilegios de Windows que persistió en los sistemas Windows incluso después de parchear vulnerabilidades anteriores en Print Spooler CVE-2020.

1048 y CVE-2020-1337. A Oliver se le asignó CVE-2022-21999 para esta vulnerabilidad y comúnmente la denominó "SpoolFool". En este artículo, discutiremos los detalles técnicos asociados con el mismo y demostraremos dos métodos a través de los cuales un atacante puede aprovechar y obtener privilegios escalados como NT AUTHORITY\SYSTEM.

La vulnerabilidad permite a un usuario sin privilegios crear directorios arbitrarios y grabables configurando el atributo SpoolDirectory en una impresora. Dado que un usuario sin privilegios puede agregar impresoras remotas, un atacante puede crear una impresora remota y otorgar a TODOS el derecho a administrar esta impresora. Esto devolvería un identificador con el derecho PRINTER\_ACCESS\_ADMINISTER que puede usarse para realizar tareas como la inyección de DLL.



<figure><img src="../../../.gitbook/assets/Windows-Privilege-Escalation_-SpoolFool-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../../.gitbook/assets/Windows Privilege Escalation_ SpoolFool.pdf" %}



{% file src="../../../.gitbook/assets/Windows Privilege Escalation_ SpoolFool (español).pdf" %}
