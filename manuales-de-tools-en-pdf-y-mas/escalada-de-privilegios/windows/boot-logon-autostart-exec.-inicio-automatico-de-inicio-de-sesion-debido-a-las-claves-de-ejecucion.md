# ☠️ BOOT LOGON AUTOSTART EXEC. - inicio automático de inicio de sesión debido a las claves de ejecución

La carpeta de inicio de Windows puede ser el objetivo de un atacante para escalar privilegios o ataques de persistencia

Agregar una aplicación a una carpeta de inicio o hacer referencia a ella usando una clave de ejecución del Registro son dos formas de hacerlo.

Cuando un usuario inicia sesión, la aplicación vinculada se ejecutará si un elemento está en las "claves de ejecución" en el Registro o en la carpeta de inicio. Estos programas se ejecutarán bajo la perspectiva del usuario y tendrán el nivel de permisos asociado a la cuenta.

Inyectar un programa malicioso dentro de una carpeta de inicio también hará que ese programa se ejecute cuando un usuario inicie sesión, por lo que puede ayudar a un atacante a realizar ataques de persistencia o escalada de privilegios desde ubicaciones de carpetas de inicio mal configuradas.

Veremos esto mejor en el PDF:

<figure><img src="../../../.gitbook/assets/Boot-Logon-Autostart-Execution-Startup-Folder-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../../.gitbook/assets/Boot Logon Autostart Execution (Startup Folder).pdf" %}



{% file src="../../../.gitbook/assets/Boot Logon Autostart Execution (Startup Folder) (español).pdf" %}
