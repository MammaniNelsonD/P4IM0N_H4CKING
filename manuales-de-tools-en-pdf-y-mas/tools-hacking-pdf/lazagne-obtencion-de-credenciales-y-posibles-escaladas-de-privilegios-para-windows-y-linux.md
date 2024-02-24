# 👩‍🍳 LAZAGNE - obtencion de credenciales y posibles escaladas de privilegios para Windows y Linux

LaZagne es una aplicación de código abierto. Recupera contraseñas almacenadas en un sistema. Inyecta directamente el código Python en la memoria sin escribir nada en el disco. Esto hace que sea difícil de rastrear. Por lo general, cuando realizamos una sesión en un sistema de destino, nuestro principal objetivo es recopilar credenciales. Cuando un atacante ataca a un objetivo, hay dos formas en que puede comprometerlo. Si el atacante obtiene la sesión de meterpreter, lo único que hace es comprometer la seguridad del dispositivo.

Pero al utilizar algunos scripts y módulos posteriores a la explotación, el objetivo puede comprometer cada rincón de la seguridad de la víctima. Esto incluye contraseñas de correo electrónico, contraseñas de redes sociales, contraseñas SSH, información bancaria, etc. Normalmente, esta extracción de contraseñas es una tarea ruidosa y torpe, pero con LaZagne es muy simple y sigilosa.

Sin LaZagne, los atacantes normalmente ejecutan un montón de scripts diferentes dirigidos a diferentes aplicaciones que están instaladas en el sistema de destino. Pero LaZagne lo hace automáticamente. Primero verifica qué aplicación está instalada en el sistema de destino y luego ejecuta ese script específico para obtener la contraseña de esa aplicación en particular.

<figure><img src="../../.gitbook/assets/Post-Exploitation-on-Saved-Password-with-LaZagne-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../.gitbook/assets/Post Exploitation on Saved Password with LaZagne.pdf" %}



{% file src="../../.gitbook/assets/Post Exploitation on Saved Password with LaZagne (español).pdf" %}
