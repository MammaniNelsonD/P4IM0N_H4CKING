# 👀 FLUXION - wireless WI-FI

Fluxion es una herramienta que se puede utilizar para realizar pruebas de penetración o auditorías de seguridad en puntos de acceso inalámbricos. Utiliza ingeniería social para obtener la contraseña de autenticación de los usuarios. Intenta recopilar la clave WPA/WPA2 del punto de acceso objetivo mediante un ataque de phishing. Se pueden realizar dos ataques usando Fluxion. Uno es el ataque Handshake Snooper y otro es Captive Portal.

El ataque Handshake Snooper intenta recopilar los hashes de autenticación WPA/WPA2 del protocolo de enlace de 4 vías. Utiliza el desautenticador para desconectar a todos los usuarios que están conectados al punto de acceso de destino y luego, cuando los usuarios intentan volver a conectarse al punto de acceso, captura los hashes. Estos hashes pueden ser utilizados por el ataque del Portal Cautivo,

El ataque al portal cautivo intenta recopilar la contraseña WPA/WPA2 del punto de acceso objetivo mediante la creación de una red fraudulenta. En sentido general, realiza un ataque Evil-Twin en el que se crea una red con el mismo SID y todos los usuarios se desconectan del punto de acceso objetivo. Luego, con el uso de ataques de phishing, se engaña a los usuarios para que proporcionen la contraseña del punto de acceso objetivo.

Nota: Para realizar ataques usando Fluxion, necesita una tarjeta Wi-Fi externa con modo de monitoreo

<figure><img src="../../.gitbook/assets/Wireless-Penetration-Testing_-Fluxion-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../.gitbook/assets/Wireless Penetration Testing_ Fluxion.pdf" %}



{% file src="../../.gitbook/assets/Wireless Penetration Testing_ Fluxion (español).pdf" %}
