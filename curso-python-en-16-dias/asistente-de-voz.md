# 😀 ASISTENTE DE VOZ

````python
// Some code

```python
#!Practicas para hacer un asistenete de voz - apuntes - By P4IM0N

#?pyttsx3 - modulo que permite a python hablar con nosotros
#?speech_recognition - permite traducir la voz y pasarla a texto
#?webbrowser - permitehacer busquedas en un navegador web
#?pywhatkit - para conectar el codigo con muchos sitios web como: youtube, wikipedia, google, etc
#?yfinance - para poder buscar informacion de la bolsa de valores 
#?pyjokes - base de datos de chistes 
#?wikipedia - para buscar de todo un poco
#?selenium - para poder manipular automaticamente una ventana del explorador de internet google chrome

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!INSTRUCCIONES DE INSTALACIONES NECESARIAS A TENER EN CUENTA
#para INSTALAR LIBRERIAS NECESARIAS "LINUX" - en terminal el siguiente comando:  pip install pyttsx3, pip install SpeechRecognition, pip install webbrowser, pip install pywhatkit, pip install yfinance, pip install pyjokes, pip install wikipedia, sudo apt-get install libespeak1, sudo apt-get install alsa-utils

#para INSTALAR LIBRERIAS NECESARIAS "WINDOWS" - en terminal el siguiente comando:  pip install pyttsx3, pip install SpeechRecognition, pip install webbrowser, pip install pywhatkit, pip install yfinance, pip install pyjokes, pip install wikipedia

#para INSTALAR DRIVER CONTROLADORES DE "WINDOWS o LINUX" buscar dependiendo el OS que se este usando, y descargar de este link el .zip correspondiente mas sercana a su vercion de google crhome (se vee en los tres puntitos) y al descomprimir el archivo nos dara un .exe el cual debemos indicar la ruta dentor de la funcion de  obtener_respuesta_whatsapp() en su linea(driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')) para que encuentre el ejecutable al iniciar el driber asi abrira la ventana de whatsapps en este caso, y luego uso seleccionadores usando digamos metodos de scraping para apuntar al contacto, ingreso de texto msj y la respuesta(como se sabe el scraping puede variar de acuerdo al HTML que tenga o pueda cambiar whatsapps, por ende si no funciona verificar el HTML de cada elemento y configurar bien los selectores, por ende es un punto a tener en  CUENTA IMPORTANTE SI NO FUNCIONA!!), previo se debe agregar al contacto de LuzIA y agendarla con este nombre, se puede obtener desde esta pagina: https://soyluzia.com/

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!importamos las librerias necesarias
import pyttsx3
import speech_recognition as SR                      #?con as SR lo vamos a poder llamar con SR luego para hacer uso de esta libreria y no escribirla toda entera que seria mas complicado
import pywhatkit
import yfinance 
import pyjokes
import webbrowser
import datetime
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!BANNER
print('''
      
__________  _____ .___   _____      _____        .__          __                 __          
\______   \/  |  ||   | /     \    /  |  |  _____|__| _______/  |_  ____   _____/  |_  ____  
 |     ___/   |  ||   |/  \ /  \  /   |  |_/  ___/  |/  ___/\   __\/ __ \ /    \   __\/ __ \ 
 |    |  /    ^   /   /    Y    \/    ^   /\___ \|  |\___ \  |  | \  ___/|   |  \  | \  ___/ 
 |____|  \____   ||___\____|__  /\____   |/____  >__/____  > |__|  \___  >___|  /__|  \___  >
              |__|            \/      |__|     \/        \/            \/     \/          \/ 
------------------------------------------------------------------------------------By P4IM0N

      ''')


#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!ESCUCHAR EL MIROFONO y devolver el audio ingresado como un TEXTO
#estea funcion tomara el audio ingresado por el usuario y lo devolvera en forma de texto
def trasformar_audio_a_texto():
    #guardar o almacenar recognizer en una variable para usarla facilmente con sus metodos
    r = SR.Recognizer()                                                   #?"r" guarda una instancia del reconocedor de voz de la librería "speech_recognition", seria el reconocedor de voz
    
    #configuramos el microfono
    with SR.Microphone() as origen:                                       #?"origen" guarda una instancia del micrófono para ser utilizado por el reconocedor de voz
        
        #tiempo de espera para quee el microfono empiese a escuchar
        r.pause_threshold = 0.8
        
        #imformar que ya puededes hablar por microfono
        print('Ya puedes decirme lo que necesitas: ')
        
        #guardar lo que escuche el microfono como un audio
        audio_ingresado = r.listen(origen)                                 #?"audio_ingresado" guarda el audio capturado por el micrófono en forma de objeto
        
        try:
            #buscar en google el audio ingresado
            pedido = r.recognize_google(audio_ingresado, language='es-ar') #?"pedido" guarda el texto convertido a partir del audio capturado por el micrófono y reconocido Recognizer() por el reconocedor de voz, y utiliza el el servicio de reconocimiento de voz de Google a través del método recognize_google() y especificando el idioma de entrada como "es-ar"
            
            #prueba de que pudo ingresar el pedido de manera correcta
            print('Dijiste: '+ pedido)
            
            #devolver el pedido 
            return pedido
        
        #en el caso que nose comprendio el audio
        except SR.UnknownValueError:
            
            #respuesta si no se comprendio el audio o error
            print('Perdon, no comprendi tu solicitud')
            
            #devolver el error
            return 'vuelve a intentarlo de nuevo, te espero'
        
        #en el caso de no poder devolver el pedido
        except SR.RequestError:
            
            #respuesta si no se comprendio el audio o error
            print('Perdon, no se pudo procesar tu solicitud')
            
            #devolver el error
            return 'vuelve a intentarlo de nuevo de manera clara, te espero'
        
        #error inesperado
        except:
            
            #respuesta si no se comprendio el audio o error
            print('Perdon, algo salio mal con su solicitud')
            
            #devolver el error
            return 'vuelve a intentarlo y esperemos el error no persista, te espero'
        
        
               
'''trasformar_audio_a_texto()'''

#?---------------------------------------------------------------------------------------------------------------------------
#!PASAR el TEXTO a VOZ
#una funcion  que nos va a hacer que la repuesta cobseguida como texto, pueda ser escuchada a traves de una voz
def responder_hablando(mensaje):
    
    #prender el motor de pyttsx3
    engine_encendido = pyttsx3.init()
    
    voices = engine_encendido.getProperty('voices')       #?obtiene una lista de todas las voces disponibles
    engine_encendido.setProperty('voice', voices[0].id)   #?(windows)establece la voz este caso LINUX: [21] en "es-la-am" (español lanino america) y en WINDOWS: cambiar [0] o bien iterar con el loop comentado para ver su orden de lista de idiomas
    #engine_encendido.setProperty('voice', voices[21].id) #?(descomentar y usar esta linea en Kali linux)establece la voz este caso LINUX: [21] en "es-la-am" (español lanino america) y en WINDOWS: cambiar [0] o bien iterar con el loop comentado para ver su orden de lista de idiomas
    engine_encendido.setProperty('rate', 150)             #?establece la velocidad de habla en 150 palabras por minuto
    engine_encendido.setProperty('volume', 0.9)           #?establece el volumen en 0.7 (70% del volumen máximo)

    
    
    #leer o pronunciar el mensaje
    engine_encendido.say(mensaje)                     #?como parametro delñ metodo say le pasamos el texto que va a decir
    engine_encendido.runAndWait()                     #?runandWait hace que se ejecute y espere


'''responder_hablando(trasformar_audio_a_texto())'''


#!obtener voces de la lista de voces de pyttsx3 con getproperty iterando en ella, en este caso guarde una en la variable voz1 de linux, por eso lo dejo sin efecto para que sea compatible para window sin drama, pero si no podemos usar su indice como lo estoy haciendo
'''voz1 = '<Voice id=spanish-latin-am name=spanish-latin-am languages=[b\'\\x05es-la\'\] gender=male age=None>'
responder_hablando(trasformar_audio_a_texto())

engine = pyttsx3.init()
contador = 0
for voz in engine.getProperty('voices'):
    contador += 1
    print(f'{contador}:{voz}')'''
    

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#!INFORMAR FECHA
#funcion que se encargara de informar el dia de la fecha de hoy   
def fecha_de_hoy():
    
    #fecha completa del dia hoy
    dia = datetime.date.today()
    
    #dia de semana, (el metodo weekday me arroja un valor numerico del dia de semana en que estamos, por eso creo uin diccionario, para luego buscar en el diccionario la coincidencia en su llave usando el dato numerico devuelto por .weekday )
    dia_de_semana = dia.weekday()
    diccionario_dias_de_semana = {0:'Lunes',
                                  1:'Martes',
                                  2:'Mièrcoles',
                                  3:'Jueves',
                                  4:'Viernes',
                                  5:'Sàbado',
                                  6:'Domingo',}
    diccionario_dias_de_semana_listo = diccionario_dias_de_semana[dia_de_semana]
    
    #prender el motor de pyttsx3 para usar la VOZ
    engine_encendido = pyttsx3.init()
    
    # Configurar la voz y el idioma
    engine_encendido.setProperty('voice', 'spanish-latin-am')
    engine_encendido.setProperty('language', 'es')
    
    #leer o pronunciar el mensaje
    engine_encendido.say(f' Hoy es {dia} del dia {diccionario_dias_de_semana_listo}')                     #?como parametro delñ metodo say le pasamos el texto que va a decir
    engine_encendido.runAndWait()                                                                         #?runandWait hace que se ejecute y espere

    
'''fecha_de_hoy()'''

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!INFORMAR la HORA
#esta funcion va a decir la hora del momento
def hora_de_ahora():
    
    #creo una variable con los datos de la hora obtenidos en bruto
    hora = datetime.datetime.now()
    
    #damos una mejor forma o formato a la hora
    hora = f'Estan siendo las {hora.hour} horas y {hora.minute} minutos, en este momento'
    
    #decir la hora
    responder_hablando(hora)
    
    
    
'''hora_de_ahora()'''

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!SALUDO INICIAL
#esta funcion ejecutara el saludo inincial
def saludo_inicial():
    
    #datos de la hora actual
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:                 #?condicional de si son mas de las 20hs y antes de las 06hs 
        momento = 'Buenas noches mano'
    elif hora.hour >= 6 or hora.hour <=20:              #?condicional de si son mas de las 06hs y antes de las 20hs 
        momento = 'Buenos dias mano'    
    
    #decir el saludo
    responder_hablando(f'{momento} como estas manito, decime que te hace falta')
    
    
    
'''saludo_inicial()'''    

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!FUNCION PARA CHAT CON INTELIGENCIA ARTIFICIAL (LuzIA)
# Inicializar con selenium el driver controlador del navegador web de Chrome para abrirlo en este caso
driver = webdriver.Chrome('/home/paimon/cursopython/dia13-asistentedevoz/chromedriver')

# Ruta para Abrir WhatsApp Web en este caso(se puede poner cualquier pagina, obviamente se deberia recomfigurar todos los selectores con sus devidas rutas HTML a las que squeremos apuntar)
driver.get("https://web.whatsapp.com/")

def obtener_respuesta_whatsapp_LuzIA(mensaje):
    

    # Esperar 5 segundos para que el usuario escanee el código QR y cargue la página completamente
    time.sleep(5)
    print("Escanea el código QR para continuar")

    #SELECTOR: para buscar el contacto al que quiero enviar el mensaje de pregunta del usuario usando metodos de selenium, y digamos una ruta que apunta al elemento al que seleccionara con un click
    contacto = driver.find_element("xpath","//span[@title='LuzIA']")
    #hacemos click con el metodo en el contacto seleccionado arriba usando en el el metodo de selenium, .click
    contacto.click()

    #SELCTOR: para seleccionar el cuadro de texto donde se va escribir el mensaje de pregunta ingresado por voz a texto del usuario y luego enviarse al chat LuzIA
    ingreso_de_texto = driver.find_element("xpath","//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")


    # Escribir el mensaje que lo mandamos de parametro a la funciion .send_keys y enviarlo con el mismo metodo, pero con un parametro ingresandole otro metodo a keys indicandole que precione la tecla enter con .ENTER (podria funcionar lo mismo indicando ESPACIO, etc)
    ingreso_de_texto.send_keys(mensaje)
    ingreso_de_texto.send_keys(Keys.ENTER)

    # Esperar a recibir una respuesta del contacto
    time.sleep(16) # Esperamos 25 segundos para darle tiempo a que el chat de LuzIA nos responda

    #SELECTOR: para buscamos el elemento que contiene la respuesta con el selector HTML correspondiente y obtener su texto de respuesta correcto con el codicional definiendo que queremos el -1 osea ultimo elemento cargado en esa etiqueta HTML o selectos como le quieras decir
    respuestas = driver.find_elements("xpath", "//div[@class='cm280p3y to2l77zo n1yiu2zv c6f98ldp ooty25bp oq31bsqd']//span[@class='_11JPr selectable-text copyable-text']")

    # Verificar si se encontraron respuestas
    if len(respuestas) >= 1:
        # Obtener el texto de la última respuesta
        respuesta_a_pregunta = respuestas[-1].text
        print(respuesta_a_pregunta)
    else:
        # En caso de no encontrar respuestas
        print("Disculpa manito, no se encontró la respuesta")
    

    return respuesta_a_pregunta

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!FUNCION PARA ENVIAR MENSJES A CONTACTOS
def enviar_mensaje_whatsapp_contacto(contacto,mensaje):
    
    #seleccionar a quien enviar el mensaje
    #mensaje = trasformar_audio_a_texto().lower(input('que mensaje queres enviar manito'))

    # Esperar 5 segundos para que el usuario escanee el código QR y cargue la página completamente
    time.sleep(5)
    print("Escanea el código QR para continuar")

    contacto_elegido =f"//span[@title='{str(contacto)}']"
    time.sleep(4)
    #SELECTOR: para buscar el contacto al que quiero enviar el mensaje de pregunta del usuario usando metodos de selenium, y digamos una ruta que apunta al elemento al que seleccionara con un click
    contacto = driver.find_element("xpath",contacto_elegido)
    #hacemos click con el metodo en el contacto seleccionado arriba usando en el el metodo de selenium, .click
    contacto.click()

    #SELCTOR: para seleccionar el cuadro de texto donde se va escribir el mensaje de pregunta ingresado por voz a texto del usuario y luego enviarse al chat LuzIA
    ingreso_de_texto = driver.find_element("xpath","//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")


    # Escribir el mensaje que lo mandamos de parametro a la funciion .send_keys y enviarlo con el mismo metodo, pero con un parametro ingresandole otro metodo a keys indicandole que precione la tecla enter con .ENTER (podria funcionar lo mismo indicando ESPACIO, etc)
    ingreso_de_texto.send_keys(mensaje)
    ingreso_de_texto.send_keys(Keys.ENTER)


#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!MANEJO CENTRAL DE TODO EL SISTEMA
#funcion que manejara todas las funciones y el manejo del asistente de voz
def asistente_de_voz():
    
    #saludo inicial
    saludo_inicial()
    
    #loop para que continue la comunicacion con los distintos requerimientos, y una variable de corte con valor TRUE para poder cambiarla luego cuando querramos detener el loop
    inicio = True
    while inicio:
        
        #activamos el microfono y guardamos la voz ingresada como un texto, y con .lower lo pasamos todo en minuscula
        pregunta = trasformar_audio_a_texto().lower()
        
        #damos condicionales para gestionar que hara el asistente, enn este caso if si encuentra en la pregunta capturada del usuario una solicitud que diga 'abri youtube' ejecutara eso, etc...
        
        #!abrir youtube
        if 'abrir youtube' in pregunta:
            responder_hablando('Perfecto, youtube se esta abriendo manito')
            webbrowser.open('https://www.youtube.com')                      #?utilizamos la libreria webbrowser para manipular el navegador y entrar a youtube
            continue
        
        #!abrir google
        elif 'abrir google' in pregunta:
            responder_hablando('Perfecto, google se esta abriendo manito')
            webbrowser.open('https://www.google.com')
            continue
        
        #!abrir chatgpt
        elif 'abrir chatgpt' in pregunta:
            responder_hablando('Perfecto, chatgpt se esta abriendo manito')
            webbrowser.open('https://www.openai.com')
            continue
        
        #!abrir Udemy
        elif 'abrir udemy' in pregunta:
            responder_hablando('Perfecto, udemy se esta abriendo manito')
            webbrowser.open('https://www.udemy.com')
            continue
        
        #!abrir hackthebox
        elif 'abrir hackthebox' in pregunta:
            responder_hablando('Perfecto, hackthebox se esta abriendo manito')
            webbrowser.open('https://www.hackthebox.com')
            continue
        
        #!abrir tryhackme
        elif 'abrir tryhackme' in pregunta:
            responder_hablando('Perfecto, tryhackme se esta abriendo manito')
            webbrowser.open('https://www.tryhackme.com')
            continue
        
        #!informar que dia es
        elif 'qué día es hoy' in pregunta:
            fecha_de_hoy()
            continue
        
        #!informar que hora es
        elif 'qué hora es' in pregunta:
            hora_de_ahora()
            continue
        
        #!buscar algo que indiquemos en wikipedia
        elif 'busca en wikipedia' in pregunta:
            responder_hablando('bien manito Voy a buscar en wikipedia')
            pregunta = pregunta.replace('busca en wikipedia', '' )
            wikipedia.set_lang('es')                                      #? el metodo et_lang configura la pagina de wiki en español
            respuesta = wikipedia.summary(pregunta, sentences=1)          #?con summary optendra informacion de la pagina, con dos parametros, el primero sera el tema que se buscara y sentense=1 indica que nos devuelva el primer parrafo o resumen de informacion
            responder_hablando('Mano esto dice en wiki: ')
            responder_hablando(respuesta)
            continue
        
        #!buscar algo que indiquemos en google
        elif 'busca en google' in pregunta:
            responder_hablando('¡Claro! Voy a realizar una búsqueda en Google')
            parte_despues = pregunta.split('busca en google', 1)[-1].strip()    #?Eliminar todo lo que está antes de 'busca en google'
            palabras = parte_despues.split()                                    #?Eliminar espacios al inicio y al final de la pregunta
            palabras = ' '.join(palabras)                                       #?Convertir la lista de palabras en una cadena
            pywhatkit.search(palabras)
            responder_hablando(f'¡Claro! mira manito esto encontre en Google de {palabras}')
            continue
        
        #!buscar ubicacion en googlemap
        elif 'busca en mapa' in pregunta:
            responder_hablando('¡Claro! Voy a buscar en Google Maps')
            parte_despues = pregunta.split('busca en mapa')[-1].strip()
            palabras = parte_despues.split()
            palabras = ' '.join(palabras)
            url_busqueda = f'https://www.google.com/maps/search/{palabras}'
            print(url_busqueda)
            webbrowser.open(url_busqueda)
            responder_hablando(f'¡Aquí tienes! Abriendo Google Maps con la ubicación de {palabras}')
            continue
        
        #!poner play a un video
        elif 'dale play' in pregunta:
            responder_hablando('Bien le doy Play al video manito')
            pywhatkit.playonyt(pregunta)
            continue
        
        #!contar un chiste
        elif 'chiste' in pregunta:
            responder_hablando(pyjokes.get_joke('es'))
            continue
        
        #!buscar precios de las acciones de la bolsa
        elif 'precio acciones' in pregunta:
            # Dividimos la pregunta donde encuentre 'de' con .split y obtenemos lo siguiente como una acción ya limpia y limpiamos aún más los espacios con .strip
            acciones = pregunta.split('de')[-1].strip()
            cartera = {'apple':'AAPL',
            'amazon':'AMZN',
            'google':'GOOG',
            'microsoft':'MSFT',
            'facebook':'FB',
            'tesla':'TSLA',
            'netflix':'NFLX',
            'invidia':'NVDA',
            'jpmorgan chase':'JPM',
            'johnson and johnson':'JNJ',
            'procter and gamble':'PG',
            'visa':'V',
            'unitedhealth group':'UNH',
            'home depot':'HD',
            'intel':'INTC',
            'crowdstrike holdings': 'CRWD',
            'zscaler': 'ZS',
            'okta': 'OKTA',
            'sentinelone': 'S',
            'palo alto networks': 'PANW',
            'fortinet': 'FTNT',
            'splunk': 'SPLK',
            'data dog': 'DDOG',
            'akamai': 'AKAM'}

            try:
                #buscamos la accion seleccionada para encontrar la coinsidencia de la clave dentro del diccionario cartera y obtener su simbolo para buscarlo con yfinace luego.
                simbolo_dela_accion = cartera[acciones]
                # Obtener los datos históricos de la acción seleccionada con .history y guardarlos para ser seleccionado luego en la variable historial.
                accion = yfinance.Ticker(simbolo_dela_accion)
                historial_de_precios_dela_accion = accion.history(period="1d")

                # Obtener el precio de cierre más reciente de la acción seleccionada con historial y su parámetro 'Close'
                precio_cierre = historial_de_precios_dela_accion['Close'][-1]

                # Paso el precio de la acción seleccionada a pesos argentinos
                dolar_blue = 488
                precio_cierre_pesos_ARG = precio_cierre * dolar_blue
                print(f'La encontré manito, y de las acciones de {acciones} el precio es AR${round(precio_cierre_pesos_ARG)}')

                # Responde el precio de la acción seleccionada
                responder_hablando(f'La encontré manito, y de las acciones de {acciones} el precio es AR${round(precio_cierre_pesos_ARG)}')
            
            except KeyError:
                print(f'Lo siento manito, no pude encontrar la acción de {acciones} en mi diccionario.')
                responder_hablando(f'Lo siento manito, no pude encontrar la acción {acciones} en mi diccionario.')

    
        
        #!buscar algo que indiquemos a inteligencia artificial LuzIA simil GPT
        elif 'lucía busca' in pregunta:
            responder_hablando('¡Claro! Voy a realizar una pregunta a LuzIA')
            pregunta = pregunta.replace('lucía busca', '' )
            respuesta= obtener_respuesta_whatsapp_LuzIA(pregunta)
            responder_hablando('Mano esto dice LuzIA: ')
            responder_hablando(respuesta)
            continue
        
        #!buscar algo que indiquemos a inteligencia artificial LuzIA simil GPT
        elif 'enviar mensaje a' in pregunta:
            pregunta = pregunta.replace('enviar mensaje a', '' )
            pregunta = pregunta.strip()
            responder_hablando(f'¡Claro! Voy a enviar un mensaje a {pregunta}, dime que mensaje le queres enviar? ')
            mensaje_a_enviar = trasformar_audio_a_texto().lower()
            enviar_mensaje_whatsapp_contacto(pregunta,mensaje_a_enviar)
            responder_hablando(f'Mano se envio el mensaje a {pregunta}')
            continue

        
        #!agradecer
        elif 'gracias' in pregunta:
            responder_hablando('De nada manito para ayudarte estoy, espero te alla servido mi ayuda ')
            continue
        
        #!cerramos el asistente de voz
        elif 'nos vemos manito' in pregunta:
            responder_hablando('Dale manito, ya nos volvemos a ver pronto, cuidate bebe')
            #Cerramos el navegador web de Chrome
            driver.quit()
            #indicamos que la variable inicio valdra False por ende se terminara el loop por no cumplir el condicional del while y se cerrara el asistente de voz
            inicio=False
            

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!iniciamos el asistente de voz
asistente_de_voz()
```
````

COSEO DEL DIA 13:

````python
// Some code

```python
#!Practicas para hacer un asistenete de voz - apuntes - By P4IM0N

#?pyttsx3 - modulo que permite a python hablar con nosotros
#?speech_recognition - permite traducir la voz y pasarla a texto
#?webbrowser - permitehacer busquedas en un navegador web
#?pywhatkit - para conectar el codigo con muchos sitios web como: youtube, wikipedia, google, etc
#?yfinance - para poder buscar informacion de la bolsa de valores 
#?pyjokes - base de datos de chistes 
#?wikipedia - para buscar de todo un poco
#?selenium - para poder manipular automaticamente una ventana del explorador de internet google chrome

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!INSTRUCCIONES DE INSTALACIONES NECESARIAS A TENER EN CUENTA
#para INSTALAR LIBRERIAS NECESARIAS "LINUX" - en terminal el siguiente comando:  pip install pyttsx3, pip install SpeechRecognition, pip install webbrowser, pip install pywhatkit, pip install yfinance, pip install pyjokes, pip install wikipedia, sudo apt-get install libespeak1, sudo apt-get install alsa-utils

#para INSTALAR LIBRERIAS NECESARIAS "WINDOWS" - en terminal el siguiente comando:  pip install pyttsx3, pip install SpeechRecognition, pip install webbrowser, pip install pywhatkit, pip install yfinance, pip install pyjokes, pip install wikipedia

#para INSTALAR DRIVER CONTROLADORES DE "WINDOWS o LINUX" buscar dependiendo el OS que se este usando, y descargar de este link el .zip correspondiente mas sercana a su vercion de google crhome (se vee en los tres puntitos) y al descomprimir el archivo nos dara un .exe el cual debemos indicar la ruta dentor de la funcion de  obtener_respuesta_whatsapp() en su linea(driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')) para que encuentre el ejecutable al iniciar el driber asi abrira la ventana de whatsapps en este caso, y luego uso seleccionadores usando digamos metodos de scraping para apuntar al contacto, ingreso de texto msj y la respuesta(como se sabe el scraping puede variar de acuerdo al HTML que tenga o pueda cambiar whatsapps, por ende si no funciona verificar el HTML de cada elemento y configurar bien los selectores, por ende es un punto a tener en  CUENTA IMPORTANTE SI NO FUNCIONA!!), previo se debe agregar al contacto de LuzIA y agendarla con este nombre, se puede obtener desde esta pagina: https://soyluzia.com/

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!importamos las librerias necesarias
import pyttsx3
import speech_recognition as SR                      #?con as SR lo vamos a poder llamar con SR luego para hacer uso de esta libreria y no escribirla toda entera que seria mas complicado
import pywhatkit
import yfinance as YF
import pyjokes
import webbrowser
import datetime
import wikipedia
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!ESCUCHAR EL MIROFONO y devolver el audio ingresado como un TEXTO
#estea funcion tomara el audio ingresado por el usuario y lo devolvera en forma de texto
def trasformar_audio_a_texto():
    #guardar o almacenar recognizer en una variable para usarla facilmente con sus metodos
    r = SR.Recognizer()                                                   #?"r" guarda una instancia del reconocedor de voz de la librería "speech_recognition", seria el reconocedor de voz
    
    #configuramos el microfono
    with SR.Microphone() as origen:                                       #?"origen" guarda una instancia del micrófono para ser utilizado por el reconocedor de voz
        
        #tiempo de espera para quee el microfono empiese a escuchar
        r.pause_threshold = 0.8
        
        #imformar que ya puededes hablar por microfono
        print('Ya puedes decirme lo que necesitas: ')
        
        #guardar lo que escuche el microfono como un audio
        audio_ingresado = r.listen(origen)                                 #?"audio_ingresado" guarda el audio capturado por el micrófono en forma de objeto
        
        try:
            #buscar en google el audio ingresado
            pedido = r.recognize_google(audio_ingresado, language='es-ar') #?"pedido" guarda el texto convertido a partir del audio capturado por el micrófono y reconocido Recognizer() por el reconocedor de voz, y utiliza el el servicio de reconocimiento de voz de Google a través del método recognize_google() y especificando el idioma de entrada como "es-ar"
            
            #prueba de que pudo ingresar el pedido de manera correcta
            print('Dijiste: '+ pedido)
            
            #devolver el pedido 
            return pedido
        
        #en el caso que nose comprendio el audio
        except SR.UnknownValueError:
            
            #respuesta si no se comprendio el audio o error
            print('Perdon, no comprendi tu solicitud')
            
            #devolver el error
            return 'vuelve a intentarlo de nuevo, te espero'
        
        #en el caso de no poder devolver el pedido
        except SR.RequestError:
            
            #respuesta si no se comprendio el audio o error
            print('Perdon, no se pudo procesar tu solicitud')
            
            #devolver el error
            return 'vuelve a intentarlo de nuevo de manera clara, te espero'
        
        #error inesperado
        except:
            
            #respuesta si no se comprendio el audio o error
            print('Perdon, algo salio mal con su solicitud')
            
            #devolver el error
            return 'vuelve a intentarlo y esperemos el error no persista, te espero'
        
        
               
'''trasformar_audio_a_texto()'''

#?---------------------------------------------------------------------------------------------------------------------------
#!PASAR el TEXTO a VOZ
#una funcion  que nos va a hacer que la repuesta cobseguida como texto, pueda ser escuchada a traves de una voz
def responder_hablando(mensaje):
    
    #prender el motor de pyttsx3
    engine_encendido = pyttsx3.init()
    
    voices = engine_encendido.getProperty('voices')      #?obtiene una lista de todas las voces disponibles
    engine_encendido.setProperty('voice', voices[0].id) #?establece la voz este caso LINUX: [21] en "es-la-am" (español lanino america) y en WINDOWS: cambiar [0] o bien iterar con el loop comentado para ver su orden de lista de idiomas
    engine_encendido.setProperty('rate', 150)            #?establece la velocidad de habla en 150 palabras por minuto
    engine_encendido.setProperty('volume', 0.9)          #?establece el volumen en 0.7 (70% del volumen máximo)

    
    
    #leer o pronunciar el mensaje
    engine_encendido.say(mensaje)                     #?como parametro delñ metodo say le pasamos el texto que va a decir
    engine_encendido.runAndWait()                     #?runandWait hace que se ejecute y espere


'''responder_hablando(trasformar_audio_a_texto())'''


#!obtener voces de la lista de voces de pyttsx3 con getproperty iterando en ella, en este caso guarde una en la variable voz1 de linux, por eso lo dejo sin efecto para que sea compatible para window sin drama, pero si no podemos usar su indice como lo estoy haciendo
'''voz1 = '<Voice id=spanish-latin-am name=spanish-latin-am languages=[b\'\\x05es-la\'\] gender=male age=None>'
responder_hablando(trasformar_audio_a_texto())

engine = pyttsx3.init()
contador = 0
for voz in engine.getProperty('voices'):
    contador += 1
    print(f'{contador}:{voz}')'''
    

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#!INFORMAR FECHA
#funcion que se encargara de informar el dia de la fecha de hoy   
def fecha_de_hoy():
    
    #fecha completa del dia hoy
    dia = datetime.date.today()
    
    #dia de semana, (el metodo weekday me arroja un valor numerico del dia de semana en que estamos, por eso creo uin diccionario, para luego buscar en el diccionario la coincidencia en su llave usando el dato numerico devuelto por .weekday )
    dia_de_semana = dia.weekday()
    diccionario_dias_de_semana = {0:'Lunes',
                                  1:'Martes',
                                  2:'Mièrcoles',
                                  3:'Jueves',
                                  4:'Viernes',
                                  5:'Sàbado',
                                  6:'Domingo',}
    diccionario_dias_de_semana_listo = diccionario_dias_de_semana[dia_de_semana]
    
    #prender el motor de pyttsx3 para usar la VOZ
    engine_encendido = pyttsx3.init()
    
    # Configurar la voz y el idioma
    engine_encendido.setProperty('voice', 'spanish-latin-am')
    engine_encendido.setProperty('language', 'es')
    
    #leer o pronunciar el mensaje
    engine_encendido.say(f' Hoy es {dia} del dia {diccionario_dias_de_semana_listo}')                     #?como parametro delñ metodo say le pasamos el texto que va a decir
    engine_encendido.runAndWait()                                                                         #?runandWait hace que se ejecute y espere

    
'''fecha_de_hoy()'''

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!INFORMAR la HORA
#esta funcion va a decir la hora del momento
def hora_de_ahora():
    
    #creo una variable con los datos de la hora obtenidos en bruto
    hora = datetime.datetime.now()
    
    #damos una mejor forma o formato a la hora
    hora = f'Estan siendo las {hora.hour} horas y {hora.minute} minutos, en este momento'
    
    #decir la hora
    responder_hablando(hora)
    
    
    
'''hora_de_ahora()'''

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!SALUDO INICIAL
#esta funcion ejecutara el saludo inincial
def saludo_inicial():
    
    #datos de la hora actual
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:                 #?condicional de si son mas de las 20hs y antes de las 06hs 
        momento = 'Buenas noches mano'
    elif hora.hour >= 6 or hora.hour <=20:              #?condicional de si son mas de las 06hs y antes de las 20hs 
        momento = 'Buenos dias mano'    
    
    #decir el saludo
    responder_hablando(f'{momento} como estas manito, decime que te hace falta')
    
    
    
'''saludo_inicial()'''    

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!FUNCION PARA CHAT CON INTELIGENCIA ARTIFICIAL (LuzIA)
# Inicializar con selenium el driver controlador del navegador web de Chrome para abrirlo en este caso
driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')

# Ruta para Abrir WhatsApp Web en este caso(se puede poner cualquier pagina, obviamente se deberia recomfigurar todos los selectores con sus devidas rutas HTML a las que squeremos apuntar)
driver.get("https://web.whatsapp.com/")

def obtener_respuesta_whatsapp_LuzIA(mensaje):
    

    # Esperar 5 segundos para que el usuario escanee el código QR y cargue la página completamente
    time.sleep(5)
    print("Escanea el código QR para continuar")

    #SELECTOR: para buscar el contacto al que quiero enviar el mensaje de pregunta del usuario usando metodos de selenium, y digamos una ruta que apunta al elemento al que seleccionara con un click
    contacto = driver.find_element("xpath","//span[@title='LuzIA']")
    #hacemos click con el metodo en el contacto seleccionado arriba usando en el el metodo de selenium, .click
    contacto.click()

    #SELCTOR: para seleccionar el cuadro de texto donde se va escribir el mensaje de pregunta ingresado por voz a texto del usuario y luego enviarse al chat LuzIA
    ingreso_de_texto = driver.find_element("xpath","//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")


    # Escribir el mensaje que lo mandamos de parametro a la funciion .send_keys y enviarlo con el mismo metodo, pero con un parametro ingresandole otro metodo a keys indicandole que precione la tecla enter con .ENTER (podria funcionar lo mismo indicando ESPACIO, etc)
    ingreso_de_texto.send_keys(mensaje)
    ingreso_de_texto.send_keys(Keys.ENTER)

    # Esperar a recibir una respuesta del contacto
    time.sleep(16) # Esperamos 25 segundos para darle tiempo a que el chat de LuzIA nos responda

    #SELECTOR: para buscamos el elemento que contiene la respuesta con el selector HTML correspondiente y obtener su texto de respuesta correcto con el codicional definiendo que queremos el -1 osea ultimo elemento cargado en esa etiqueta HTML o selectos como le quieras decir
    respuestas = driver.find_elements("xpath", "//div[@class='cm280p3y to2l77zo n1yiu2zv c6f98ldp ooty25bp oq31bsqd']//span[@class='_11JPr selectable-text copyable-text']")

    # Verificar si se encontraron respuestas
    if len(respuestas) >= 1:
        # Obtener el texto de la última respuesta
        respuesta_a_pregunta = respuestas[-1].text
        print(respuesta_a_pregunta)
    else:
        # En caso de no encontrar respuestas
        print("Disculpa manito, no se encontró la respuesta")
    

    return respuesta_a_pregunta

#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!FUNCION PARA ENVIAR MENSJES A CONTACTOS
def enviar_mensaje_whatsapp_contacto(contacto,mensaje):
    
    #seleccionar a quien enviar el mensaje
    #mensaje = trasformar_audio_a_texto().lower(input('que mensaje queres enviar manito'))

    # Esperar 5 segundos para que el usuario escanee el código QR y cargue la página completamente
    time.sleep(5)
    print("Escanea el código QR para continuar")

    contacto_elegido =f"//span[@title='{str(contacto)}']"
    time.sleep(4)
    #SELECTOR: para buscar el contacto al que quiero enviar el mensaje de pregunta del usuario usando metodos de selenium, y digamos una ruta que apunta al elemento al que seleccionara con un click
    contacto = driver.find_element("xpath",contacto_elegido)
    #hacemos click con el metodo en el contacto seleccionado arriba usando en el el metodo de selenium, .click
    contacto.click()

    #SELCTOR: para seleccionar el cuadro de texto donde se va escribir el mensaje de pregunta ingresado por voz a texto del usuario y luego enviarse al chat LuzIA
    ingreso_de_texto = driver.find_element("xpath","//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")


    # Escribir el mensaje que lo mandamos de parametro a la funciion .send_keys y enviarlo con el mismo metodo, pero con un parametro ingresandole otro metodo a keys indicandole que precione la tecla enter con .ENTER (podria funcionar lo mismo indicando ESPACIO, etc)
    ingreso_de_texto.send_keys(mensaje)
    ingreso_de_texto.send_keys(Keys.ENTER)


#?-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!FUNCIONO PERFECTO
'''def obtener_respuesta_whatsapp(mensaje):
    # Inicializar el navegador web de Chrome
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')

    # Abrir WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Esperar a que el usuario escanee el código QR y cargue la página completamente
    time.sleep(18)
    print("Escanea el código QR para continuar")

    # Buscar el contacto al que quieres enviarle un mensaje
    contacto = driver.find_element("xpath","//span[@title='LuzIA']")


    contacto.click()

    # Esperar a que aparezca el cuadro de texto para escribir un mensaje
    input_box = driver.find_element("xpath","//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")


    # Escribir el mensaje y enviarlo
    input_box.send_keys(mensaje)
    input_box.send_keys(Keys.ENTER)

    # Esperar a recibir una respuesta del contacto
    time.sleep(25) # Esperar 25 segundos para dar tiempo a que llegue la respuesta

    # Buscar el elemento que contiene la respuesta y obtener su texto
    respuestas = driver.find_elements("xpath", "//div[@class='cm280p3y to2l77zo n1yiu2zv c6f98ldp ooty25bp oq31bsqd']//span[@class='_11JPr selectable-text copyable-text']")
    if len(respuestas) >= 1:
        segunda_respuesta = respuestas[-1].text
        print(segunda_respuesta)
    else:
        print("No se encontró la segunda respuesta")
        

    # Cerrar el navegador web de Chrome
    #driver.quit()
    

    return segunda_respuesta'''



'''import time
from selenium import webdriver

def obtener_respuesta_whatsapp(mensaje):
    # Inicializar el navegador web de Chrome
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')

    # Abrir WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Esperar a que el usuario escanee el código QR y cargue la página completamente
    input("Presiona enter cuando hayas escaneado el código QR y cargado la página completamente")

    # Buscar el contacto al que quieres enviarle un mensaje
    contacto = driver.find_element_by_name("//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
    contacto.click()

    # Esperar a que aparezca el cuadro de texto para escribir un mensaje
    input_box = driver.find_element_by_name("//div[@class='_3FRCZ copyable-text selectable-text']")

    # Escribir el mensaje y enviarlo
    input_box.send_keys(mensaje)
    input_box.send_keys(Keys.ENTER)

    # Esperar a recibir una respuesta del contacto
    time.sleep(5) # Esperar 5 segundos para dar tiempo a que llegue la respuesta

    # Buscar el elemento que contiene la respuesta y obtener su texto
    respuesta = driver.find_element_by_name("//div[@class='cm280p3y to2l77zo n1yiu2zv c6f98ldp ooty25bp oq31bsqd']//span[@class='_11JPr selectable-text copyable-text']")
    texto_respuesta = respuesta.text

    # Cerrar el navegador web de Chrome
    driver.quit()

    return texto_respuesta'''



'''def obtener_respuesta_whatsapp(mensaje):
    # Inicializar el navegador web de Chrome
    driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')

    # Abrir WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Esperar a que el usuario escanee el código QR y cargue la página completamente
    input("Presiona enter cuando hayas escaneado el código QR y cargado la página completamente")

    # Buscar el contacto al que quieres enviarle un mensaje
    contacto = driver.find_element_by_xpath("//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
    contacto.click()

    # Esperar a que aparezca el cuadro de texto para escribir un mensaje
    input_box = driver.find_element_by_xpath("//div[@class='_3FRCZ copyable-text selectable-text']")

    # Escribir el mensaje y enviarlo
    input_box.send_keys(mensaje)
    input_box.send_keys(Keys.ENTER)

    # Esperar a recibir una respuesta del contacto
    time.sleep(5) # Esperar 5 segundos para dar tiempo a que llegue la respuesta

    # Buscar el elemento que contiene la respuesta y obtener su texto
    respuesta = driver.find_element_by_xpath("//div[@class='cm280p3y to2l77zo n1yiu2zv c6f98ldp ooty25bp oq31bsqd']//span[@class='_11JPr selectable-text copyable-text']")
    texto_respuesta = respuesta.text

    # Cerrar el navegador web de Chrome
    driver.quit()

    return texto_respuesta'''



'''# Configura el controlador del navegador (ejemplo con Chrome)
driver = webdriver.Chrome()

# Navega a la página de ChatGPT de OpenAI
driver.get('https://poe.com/P4lMB0T')

# Función para interactuar con el chat
def interactuar_con_chat_gpt(pregunta):
    campo_entrada = driver.find_element_by_css_selector('.ChatMessageInputView_textInput__Aervw')
    campo_entrada.send_keys(pregunta)
    campo_entrada.send_keys(Keys.RETURN)

    # Espera un momento para que aparezca la respuesta en el chat
    time.sleep(2)

    # Encuentra el elemento que contiene la respuesta en el chat
    respuesta = driver.find_element_by_css_selector('.Markdown_markdownContainer__UyYrv p')

    return respuesta.text

#campo de ingreso de pregunta en gpt me sale una etiqueta textarea con este id="prompt-textarea" .

#<p>¡Hola! ¿En qué puedo ayudarte hoy?</p>
'''

'''# Configura el controlador del navegador (ejemplo con Chrome)
driver = webdriver.Chrome()

# Navega a la página de ChatGPT de OpenAI
driver.get('https://chat.openai.com/?model=text-davinci-002-render-sha')

# Función para interactuar con el chat
def interactuar_con_chat_gpt(pregunta):
    campo_entrada = driver.find_element_by_id('prompt-textarea')
    campo_entrada.send_keys(pregunta)
    campo_entrada.send_keys(Keys.RETURN)

    # Espera un momento para que aparezca la respuesta en el chat
    time.sleep(2)

    # Encuentra el elemento que contiene la respuesta en el chat
    respuesta = driver.find_element_by_css_selector('.message:last-child p')

    return respuesta.text

#campo de ingreso de pregunta en gpt me sale una etiqueta textarea con este id="prompt-textarea" .

#<p>¡Hola! ¿En qué puedo ayudarte hoy?</p>'''


```
````
