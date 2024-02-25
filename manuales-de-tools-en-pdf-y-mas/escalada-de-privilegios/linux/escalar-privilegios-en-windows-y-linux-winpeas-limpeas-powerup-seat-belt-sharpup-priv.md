# 👑 ESCALAR PRIVILEGIOS EN WINDOWS Y LINUX - WINPEAS, LIMPEAS, POWERUP, SEAT BELT, SHARPUP, PRIV

Cuando un atacante ataca un sistema operativo Windows la mayor parte del tiempo, obtendrá una sesión base shell o meterpreter. Este caparazón está limitado en las acciones que puede realizar. Entonces, para elevar los privilegios, necesitamos enumerar diferentes archivos, directorios, permisos, registros y archivos SAM. La cantidad de archivos dentro de un sistema operativo Windows es abrumadora. Por lo tanto, realizar esta tarea manualmente es muy difícil incluso cuando sabes dónde buscar. Entonces, ¿por qué no automatizar esta tarea mediante scripts?

<figure><img src="../../../.gitbook/assets/Automated-Privilege-Escalation-español-pdf.png" alt=""><figcaption></figcaption></figure>

{% file src="../../../.gitbook/assets/Automated Privilege Escalation.pdf" %}



{% file src="../../../.gitbook/assets/Automated Privilege Escalation (español).pdf" %}



<figure><img src="../../../.gitbook/assets/Introduction-to-Logical-Privilege-Escalation-on-Windows-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../../.gitbook/assets/Introduction to Logical Privilege Escalation on Windows.pdf" %}



{% file src="../../../.gitbook/assets/Introduction to Logical Privilege Escalation on Windows (español) (1).pdf" %}



Nos centraremos en explorar diversas técnicas para modificar el archivo etc/passwd, permitiéndonos crear o modificar un usuario y otorgarle privilegios de root. Resulta crucial comprender cómo editar su propio usuario dentro del archivo /etc/passwd cuando se trata de una escalada de privilegios en el sistema comprometido. Si está interesado, ya hemos demostrado este método para escalar privilegios en nuestros artículos anteriores.

En primer lugar, debemos conocer en profundidad el archivo /etc/passwd antes de llegar al punto. Dentro del directorio etc, obtendremos los tres archivos más importantes, es decir, passwd, group y shadow.

<figure><img src="../../../.gitbook/assets/Editing-_etc_passwd-File-for-Privilege-Escalation-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../../.gitbook/assets/Editing _etc_passwd File for Privilege Escalation.pdf" %}



{% file src="../../../.gitbook/assets/Editing _etc_passwd File for Privilege Escalation (español).pdf" %}
