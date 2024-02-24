# 👹 ESCANEO DE PUERTOS P4IINmap.py

````python
// Some code

```python
#!programa para analisi de comucacion con puertos - P4INmap.py - By P4IM0N

#---------------------------------------------------------------------------------
#!INSTALACION DE LIBRERIAS NECESARIAS: 
# pip install tabulate
# pip install nmap-python

#---------------------------------------------------------------------------------
import nmap
from tabulate import tabulate as tabla

#---------------------------------------------------------------------------------
# Definir códigos de escape ANSI para colores
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"

#---------------------------------------------------------------------------------
banner = f'''

__________  _____ .___ _______                         
\______   \/  |  ||   |\      \   _____ _____  ______  
 |     ___/   |  ||   |/   |   \ /     \|__  \ \____ \ 
 |    |  /    ^   /   /    |    \  Y Y  \/ __ \|  |_> >
 |____|  \____   ||___\____|__  /__|_|  (____  /   __/ 
              |__|            \/      \/     \/|__|    
{MAGENTA}By P4IM0N{RESET}''' 

print(banner)
print(f'{BLUE}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}')

#---------------------------------------------------------------------------------
def main():
    informacion_escaneo_tabla = []
    detalles_puertos_tabla = []
    detalles_scripts_tabla = []
    while True:
        nmap_iniciado = nmap.PortScanner() 
        objetivo = input('Manito dame la ip o el domimnio a escanear: ')
        print(f'{BLUE}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}')
        opciones_de_escaneo = input('Manito dame ahora los argumentos que uso para escanear?: ejem(-sV, -O): ')
        print(f'{BLUE}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}')
        puertos = input('Manito ingresa entre qu puerto quieres que agamos el escaneo?: ejem(22-500): ')
        print(f'{BLUE}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++{RESET}')
        nmap_iniciado.scan(objetivo, puertos, arguments=opciones_de_escaneo) 
        
        if objetivo in nmap_iniciado.all_hosts():
            informacion_escaneo_tabla.append(['HOST', objetivo])
            informacion_escaneo_tabla.append(['ESTADO', nmap_iniciado[objetivo].state()])
            direccion_ipv4 = nmap_iniciado[objetivo]['addresses']['ipv4']
            informacion_escaneo_tabla.append(['DIRECCIO ipv4', direccion_ipv4])
            
            if 'ipv6' in nmap_iniciado[objetivo]['addresses']:
                direccion_ipv6 = nmap_iniciado[objetivo]['addresses']['ipv6']
                informacion_escaneo_tabla.append(['DIRECCIO ipv6', direccion_ipv6])
            
            if 'osclass' in nmap_iniciado[objetivo]:
                informacion_escaneo_tabla.append(['SISTEMA OPERATIVO', f"{nmap_iniciado[objetivo]['osclass'][0]['osfamily']} {nmap_iniciado[objetivo]['osclass'][0]['osgen']}"])
            else:
                informacion_escaneo_tabla.append(['SISTEMA OPERATIVO', 'No disponible']) 
            
            for protocol in  nmap_iniciado[objetivo].all_protocols():
                informacion_escaneo_tabla.append(['PROTOCOLO', protocol])
                if protocol in nmap_iniciado[objetivo]:
                    lista_puertos = list(nmap_iniciado[objetivo][protocol].keys())
                    lista_puertos.sort()
                    
                    for puerto in lista_puertos:
                        informacion_de_puertos = nmap_iniciado[objetivo][protocol][puerto]
                        detalles_puertos_tabla.append([f'PUERTO {puerto}', informacion_de_puertos['state']]) 
                        detalles_puertos_tabla.append([f'NOMBRE DEL SERVICIO', informacion_de_puertos['name']])
                        detalles_puertos_tabla.append([f'PRODUCTO', informacion_de_puertos['product']])
                        detalles_puertos_tabla.append([f'VERSION', informacion_de_puertos['version']])
                        detalles_puertos_tabla.append([f'RAZON', informacion_de_puertos['reason']])
                    #informacion_escaneo_tabla.append(['SERVICIOS', tabla(detalles_puertos_tabla, ['DETALLES','VALORES'], tablefmt=f'grid')])
                    tabla_de_puertos = tabla(detalles_puertos_tabla, ['DETALLES','VALORES'], tablefmt=f'grid')
                    tabla_de_puertos_coloreada = f'{RED}{tabla_de_puertos}{RESET}' 
                    informacion_escaneo_tabla.append(['SERVICIOS', tabla_de_puertos_coloreada])
            
            if 'scripts' in nmap_iniciado[objetivo]:
                for script in nmap_iniciado[objetivo]['scripts'].items():
                    detalles_scripts_tabla.append(['SCRIPT ID', script])
                    detalles_scripts_tabla.append(['SCRIPT SALIDA', script['output']])
                informacion_escaneo_tabla.append(['SCRIPTS NMAP', tabla(detalles_scripts_tabla, ['DETALLE','VALOR'], tablefmt='grid')])
        
        else:
            informacion_escaneo_tabla.append(['HOST', objetivo])
            informacion_escaneo_tabla.append(['ESTADO', 'ESCANEO NO ENCONTRO RESULTADO MANITO'])
        
        return tabla(informacion_escaneo_tabla, ['DETALLES', 'VALORES'],tablefmt='grid')     

#---------------------------------------------------------------------------------                        
if __name__=='__main__':
    try:
        print(main())
    except nmap.PortScannerError as error:
        print(f'Manito ocurrio un erro en nmap: {error}')    
    except KeyboardInterrupt:
        print('manito se cerro el programa corretamente')
        exit()    

#---------------------------------------------------------------------------------


```
````
