# 👹 SCRAPING de PALABRAS en WEB     P4Iestractwebscraping.py

Este script en Python, llamado "P4Iestracwebscraping.py" y creado por P4IM0N, es una herramienta diseñada para extraer posibles palabras clave de una URL con el fin de generar listas de palabras (wordlists). Aquí hay una breve explicación de su funcionalidad y estructura:

1. **Funcionalidad**: El script toma una o varias URL de sitios web como entrada. Luego, realiza un scraping de estas páginas web para extraer palabras significativas que podrían ser útiles para la generación de wordlists, útiles en tareas como análisis de seguridad o pruebas de penetración.
2. **Uso**:
   * Se ejecuta el script desde la línea de comandos.
   * Se ingresan una o varias URL de sitios web separadas por comas.
   * El script procesa cada URL, extrae palabras clave y las muestra en la consola.

En resumen, este script proporciona una forma rápida de recopilar palabras clave de sitios web para su uso en diversas aplicaciones, como ingeniería inversa, pruebas de seguridad o análisis de datos.



````python
// Some code

```python
#! Programa que extrae posibles palbras para una wordlists de una URL -  P4Iestracwebscraping.py - By P4IM0N

#---------------------------------------------------------------------------------------------
#?INSTALACIONES REQUERIDAS
#pip install requests
#pip install beautifulsoup4

#---------------------------------------------------------------------------------------------
#?IMPORTAMOS LIBRERIAS
import requests
from bs4 import BeautifulSoup
import re 

#---------------------------------------------------------------------------------------------
#?COLORES ANSI
color_purpura = '\033[95m'  
color_rojoso = '\033[91m'  
color_rosa_electrico = '\033[95m' 
reset = '\033[0m'  

#---------------------------------------------------------------------------------------------
#?BANNER
banner= f'''{color_rosa_electrico}

__________  _____ .___                 __                                    ___.                                     .__                
\______   \/  |  ||   | ____   _______/  |_____________    ______  _  __ ____\_ |__   ______ ________________  ______ |__| ____    ____  
 |     ___/   |  ||   |/ __ \ /  ___/\   __\_  __ \__  \ _/ ___\ \/ \/ // __ \| __ \ /  ___// ___\_  __ \__  \ \____ \|  |/    \  / ___\ 
 |    |  /    ^   /   \  ___/ \___ \  |  |  |  | \// __ \  \___\     /\  ___/| \_\ \___  \  \___|  | \// __ \|  |_> >  |   |  \/ /_/  >
 |____|  \____   ||___|\___  >____  > |__|  |__|  (____  /\___  >\/\_/  \___  >___  /____  >\___  >__|  (____  /   __/|__|___|  /\___  / 
              |__|         \/     \/                   \/     \/            \/    \/     \/     \/           \/|__|           \//_____/  
{reset}{color_rojoso}By P4IM0N{reset}'''
print(banner)

#---------------------------------------------------------------------------------------------
#?FUNCION QUE EXTRAE LAS POSIBLES PALABRAS CLAVES PARA LA WORDLIST
def extraer_palabras(url):
    
    palabras_no_deseadas = {
    'result', 'false', 'hash', 'null', 'areas', 'static', 'type', 'Filtros', 
    'center', 'keyframes', 'http', 'https', 'busca', 'busqueda', 'blog', 
    'arrow', 'default', 'format', 'filter', 'div', 'span', ' static ', ' type ', 
    'class_type', 'subtype', 'truetype', 'opentype', 'class', 'truetype', 'true',  
    'html', 'head', 'title', 'meta', 'link', 'body', 'script', 'style', 'div', 
    'span', 'form', 'input', 'button', 'select', 'option', 'textarea', 'label', 
    'img', 'a', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'table', 
    'tr', 'td', 'th', 'thead', 'tbody', 'tfoot', 'iframe', 'nav', 'header', 'footer', 
    'section', 'article', 'aside', 'main', 'video', 'audio', 'canvas', 'svg', 'map', 
    'fieldset', 'legend', 'caption', 'abbr', 'address', 'b', 'bdi', 'bdo', 'cite', 
    'code', 'data', 'dfn', 'em', 'i', 'kbd', 'mark', 'q', 'rp', 'rt', 'rtc', 'ruby', 
    's', 'samp', 'small', 'strong', 'sub', 'sup', 'time', 'u', 'var', 'wbr', 'area', 
    'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 
    'track', 'wbr', 'abbr', 'accept', 'accept-charset', 'accesskey', 'action', 'align', 
    'alt', 'async', 'autocomplete', 'autofocus', 'autoplay', 'autosave', 'bgcolor', 'border', 
    'buffered', 'challenge', 'charset', 'checked', 'cite', 'class', 'codebase', 'color', 
    'cols', 'colspan', 'content', 'contenteditable', 'contextmenu', 'controls', 'coords', 
    'data', 'datetime', 'default', 'defer', 'dir', 'dirname', 'disabled', 'download', 
    'draggable', 'dropzone', 'enctype', 'for', 'form', 'formaction', 'headers', 'height', 
    'hidden', 'high', 'href', 'hreflang', 'http-equiv', 'icon', 'id', 'ismap', 'itemprop', 
    'keytype', 'kind', 'label', 'lang', 'language', 'list', 'loop', 'low', 'manifest', 
    'max', 'maxlength', 'media', 'method', 'min', 'multiple', 'muted', 'name', 'novalidate', 
    'open', 'optimum', 'pattern', 'ping', 'placeholder', 'poster', 'preload', 'radiogroup', 
    'readonly', 'rel', 'required', 'reversed', 'rows', 'rowspan', 'sandbox', 'scope', 
    'scoped', 'seamless', 'selected', 'shape', 'size', 'sizes', 'span', 'spellcheck', 
    'src', 'srcdoc', 'srclang', 'srcset', 'start', 'step', 'style', 'summary', 'tabindex', 
    'target', 'title', 'type', 'usemap', 'value', 'width', 'wrap',
    'doctype', 'xmlns:xlink', 'xmlns:xhtml', 'xmlns:math', 'xmlns:x',

    }
    
    patron_px = re.compile(r'\d+px$', re.IGNORECASE)
    
    palabras = set()
    
    encabezado_user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=encabezado_user_agent)
    
    if response.status_code == 200:
        
        html = response.content
        
        soup = BeautifulSoup(html, 'html5lib')
        
        #? Eliminamos las etiquetas de script y estilo 
        for script in soup(["script", "style"]):
            script.extract()

        #? Extraemos solo el texto visible
        textos = soup.stripped_strings
        
        for texto in textos:
            
            palabras.update(re.findall(r'\b[a-zA-Z]{4,10}\b', texto))
            
            palabras.update(re.findall(r'\b\d{1,4}\b', texto))
    
    palabras_filtradas = [palabra for palabra in palabras if palabra not in palabras_no_deseadas and not patron_px.match(palabra)]        
            
    return palabras_filtradas


#---------------------------------------------------------------------------------------------
#?FUNCION PRINCIPAL QUE MANEJA EL PROGRAMA Y LAS URL APORTADAS
def main():
    print(f'{color_purpura}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{reset}')
    urls = input('Manito ingresa una o varias url de sitios objetivos para obtener posibles palbras claves para la generacion de la WORDLIST (si desas podes pasar varias url EJ:url,url,url):').split(',')
    
    for url in urls:
        
        palabras = extraer_palabras(url)   
        
        print(f'{color_purpura}*************************************************************************************************************{reset}')
        print(f'{color_rosa_electrico}SE AGREGARON A LA LISTA PARA LA WORDLIST, Y ESTAS SON LAS PALABRAS EXTRAIDAS MANITO de LA URL:{reset} \n {color_purpura}{url}{reset}')  
        print(palabras)
        print(f'{color_purpura}*************************************************************************************************************{reset}')


#---------------------------------------------------------------------------------------------        
if __name__=='__main__':
    main()               
        

#---------------------------------------------------------------------------------------------         

```
````
