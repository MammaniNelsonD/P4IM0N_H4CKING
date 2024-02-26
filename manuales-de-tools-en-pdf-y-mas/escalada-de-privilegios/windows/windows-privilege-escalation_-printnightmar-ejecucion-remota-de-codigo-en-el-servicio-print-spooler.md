---
description: CVE-2021-34527
---

# 📠 Windows Privilege Escalation\_ PRINTNIGHTMAR- ejecución remota de código en el servicio Print Spooler

Print Spooler ha estado en el radar de los investigadores desde que el gusano Stuxnet utilizó la vulnerabilidad de escalada de privilegios del print spooler para propagarse a través de la red en centrifugadoras de enriquecimiento nuclear de Irán e infectó más de 45.000 redes. PrintNightmare es el nombre común que se le da a una vulnerabilidad de ejecución remota de código en el servicio Print Spooler (spoolsv.exe) en los sistemas operativos Microsoft Windows. A la vulnerabilidad se le asignó CVE-2021-34527

Inicialmente, se pensó como una escalada de privilegios locales (LPE) y se le asignó CVE-2021-1675.

Los parches inmediatos para el LPE se lanzaron en junio de 2021 y se marcaron como de baja gravedad. Aproximadamente 2 semanas después, Microsoft cambió el estado de gravedad baja de LPE a grave, ya que se descubrió que se omitieron los parches y la ejecución remota de código logró la asignación de CVE-2021-34527. Hubo una controversia después de un malentendido entre los autores y Microsoft donde el exploit RCE se lanzó en GitHub antes de los parches, lo que lo convirtió en una vulnerabilidad de día 0. Sin embargo, fue inmediatamente revocado. En este artículo, nos centraremos en la escalada de privilegios utilizando esta vulnerabilidad de Print Spooler. La tracción que obtuvo en 2021 la convirtió en la vulnerabilidad del año

<figure><img src="../../../.gitbook/assets/Windows-Privilege-Escalation_-PrintNightmare-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../../.gitbook/assets/Windows Privilege Escalation_ PrintNightmare.pdf" %}



{% file src="../../../.gitbook/assets/Windows Privilege Escalation_ PrintNightmare (español).pdf" %}
