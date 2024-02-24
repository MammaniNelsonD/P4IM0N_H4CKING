---
cover: ../../.gitbook/assets/nmap.jpg
coverY: 0
layout:
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# 👁️ NMAP

Nmap (Network Mapper) es una herramienta de código abierto ampliamente utilizada para el descubrimiento y escaneo de redes, así como para la auditoría de seguridad. Aquí están los alcances y usos clave de Nmap en Kali Linux:

1. **Descubrimiento de Dispositivos en Red:** Nmap puede utilizarse para descubrir dispositivos activos en una red, identificando direcciones IP disponibles y dispositivos conectados.
2. **Escaneo de Puertos:** Permite identificar los puertos abiertos en un sistema, lo que es esencial para comprender la superficie de ataque de un sistema y encontrar servicios en ejecución.
3. **Detección de Versiones de Servicios:** Nmap puede identificar las versiones específicas de los servicios que se están ejecutando en los puertos abiertos. Esto es útil para evaluar la seguridad de los servicios y para identificar vulnerabilidades conocidas asociadas con versiones específicas.
4. **Detección de Sistemas Operativos:** Puede intentar identificar el sistema operativo de los hosts en la red, basándose en las respuestas a paquetes específicos enviados durante el escaneo.
5. **Escaneo de Vulnerabilidades:** Nmap puede utilizarse para realizar escaneos de vulnerabilidades en sistemas, aunque se recomienda complementar esta funcionalidad con herramientas especializadas como Nessus o OpenVAS para obtener resultados más detallados.
6. **Escaneo de Redes Específicas:** Permite dirigir el escaneo a rangos de direcciones IP específicos o a redes individuales, lo que es útil para enfocarse en segmentos específicos de la red.
7. **Escaneo de Scripts y Escaneo Agresivo:** Nmap incluye la capacidad de ejecutar scripts personalizados (Nmap Scripting Engine) que pueden proporcionar información adicional sobre servicios y configuraciones. También puede realizar escaneos más agresivos para obtener información detallada.
8. **Generación de Mapas de Red:** Puede generar mapas visuales de la red que representan la topología y los dispositivos descubiertos.
9. **Identificación de Firewall:** Nmap puede ayudar a identificar la existencia de firewalls y filtros de red al analizar las respuestas a sus paquetes de escaneo.
10. **Personalización y Flexibilidad:** Nmap es altamente configurable y se puede personalizar para adaptarse a diversos escenarios de prueba de seguridad. Ofrece una amplia variedad de opciones de línea de comandos.
