# 🙀 ESCALACION DE PRIVILEGIOS - por SEBACKUPPRIVILEGE

Esta escalada de privilegios específica se basa en el acto de asignar a un usuario SeBackupPrivilege. Fue diseñado para permitir a los usuarios crear copias de seguridad del sistema. Ya que no es posible hacer una copia de seguridad de algo que no puedes leer. Este privilegio tiene el costo de proporcionar al usuario acceso completo de lectura al sistema de archivos. Este privilegio debe omitir cualquier ACL que el administrador haya colocado en la red.

Entonces, en pocas palabras, este privilegio permite al usuario leer cualquier archivo en su totalidad, que también puede incluir algunos archivos confidenciales, como el archivo SAM o el archivo de Registro del SISTEMA. Desde la perspectiva del atacante, esto puede explotarse después de lograr un punto de apoyo inicial en el sistema y luego ascender a un shell elevado esencialmente leyendo los archivos SAM y posiblemente descifrando las contraseñas de los usuarios con privilegios elevados en el sistema o la red. Este artículo lo ayudará a configurar el privilegio en un entorno de VM para aprenderlo, explorarlo en detalle y luego explotarlo a través de Kali Linux.

<figure><img src="../../../.gitbook/assets/Windows-Privilege-Escalation_-SeBackupPrivilege-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../../.gitbook/assets/Windows Privilege Escalation_ SeBackupPrivilege.pdf" %}



{% file src="../../../.gitbook/assets/Windows Privilege Escalation_ SeBackupPrivilege (español).pdf" %}
