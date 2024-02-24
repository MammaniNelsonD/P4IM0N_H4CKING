# 😀 GESTOR DE RESTORANTES

````python
// Some code

```python
#! Gestor de facturacion de restaurante - SISTEMA de P4IFacturacion - By P4IM0N

#?En caso de necesitar instalar las librerias necesarias, ejecutar el siguiente codigo:  pip3 install twilio Pillow qrcode[pil] 

#Seguido de esto, abajo en #!RECIBO POR WHATSAPP crear propia cuenta en twilio y remplazar las xxxxx con su llaves life para poder enviar el recibo por whatsapp atraves de esta plataforma, o de forma gratuita por sandbox añadiedo su numero para probar: (en dicho apartado estan los pasos a seguir.)

#?--------------------------------------------------------------------------------------------------------------------
#!importamos librerias necesarias
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

#librerias para twilio uso de whatsapps
from twilio.rest import Client
from tkinter import simpledialog
import tkinter as tk

#librerias para titulo con efecto
import random

#recibo QR
import qrcode
from PIL import ImageTk, Image

#?--------------------------------------------------------------------------------------------------------------------
#!LISTA de PRECIO de los productos
#la lista de precios e comidas, bebidas y postres 
# Lista de precios para productos alimenticios
precio_comida = [123, 104, 96, 157, 88, 140, 119, 105, 125, 165, 185, 65, 75, 135, 145]

# Lista de precios para productos bebibles
precio_bebida = [15, 35, 25, 35, 45, 55, 65, 65, 45, 75, 25, 35, 45, 45, 45]

# Lista de precios para productos de postres
precio_postre = [65, 45, 55, 75, 85, 45, 35, 55, 65, 45, 75, 85, 65, 95, 55]




#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de la CALCULADORA
#funcion para que aparesca el valor numerico de la tecla presioinada ded la calculadora, borrar nuemeros y igual osea resultado
operador = ''

def click_tecla_calculadora(numero):
    global operador
    operador = operador + numero
    visor_de_calculadora.delete(0, END)
    visor_de_calculadora.insert(END, operador)

def borrar_numeros():
    global operador
    operador=''
    visor_de_calculadora.delete(0, END)

def igual():
    global operador
    igual_a= str(eval(operador))                #?eval nos permite que evalue los valores  guardados en operador como str, y los evaluara lo msmo resolviendo que es una operacion matematica, con lo que devolvera un integer pero al estar casteado lo transformara de nuevo en str para poder mostrarlo en el visor de calculadora
    visor_de_calculadora.delete(0, END)
    visor_de_calculadora.insert(0, igual_a)
    operador = ''


#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de los CHECKBOX
#revisara si los checkbox estan activados o no
def control_check():
    x = 0
    for c in cuadros_de_comida:    
        if variables_de_comidas[x].get() == 1:
            cuadros_de_comida[x].config(state=NORMAL)
            if cuadros_de_comida[x].get() == '0':
                cuadros_de_comida[x].delete(0, END)
            cuadros_de_comida[x].focus()
        else:
            cuadros_de_comida[x].config(state=DISABLED)
            texto_de_comida[x].set('0')    
        x += 1    
    
    
    x = 0
    for c in cuadros_de_bebidas:    
        if variables_de_bebida[x].get() == 1:
            cuadros_de_bebidas[x].config(state=NORMAL)
            if cuadros_de_bebidas[x].get() == '0':
                cuadros_de_bebidas[x].delete(0, END)
            cuadros_de_bebidas[x].focus()
        else:
            cuadros_de_bebidas[x].config(state=DISABLED)
            texto_de_bebidas[x].set('0')    
        x += 1  
        
    
    x = 0
    for c in cuadros_de_postres:    
        if variables_de_postre[x].get() == 1:
            cuadros_de_postres[x].config(state=NORMAL)
            if cuadros_de_postres[x].get() == '0':
                cuadros_de_postres[x].delete(0, END)
            cuadros_de_postres[x].focus()
        else:
            cuadros_de_postres[x].config(state=DISABLED)
            texto_de_postres[x].set('0')    
        x += 1              
    
    

#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de costo TOTAL
#funcion que resolvera el costo total de los productos seleccionads por el cliente con respecto de su cantidad en los checkbox
def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_de_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precio_comida[p])
        p += 1
     
    
    
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_de_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precio_bebida[p])
        p += 1
    
    
    
    sub_total_postre = 0
    p = 0
    for cantidad in texto_de_postres:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precio_postre[p])
        p += 1
       
        
    sub_total= sub_total_comida+sub_total_bebida+sub_total_postre  
    impuestos = sub_total * 0.10
    total=  sub_total + impuestos   
    
    
    var_costo_de_la_comida.set(f'$ {round(sub_total_comida, 2)}') 
    var_costo_de_la_bebida.set(f'$ {round(sub_total_bebida, 2)}') 
    var_costo_de_la_postre.set(f'$ {round(sub_total_postre, 2)}')  
    var_subtotal.set(f'$ {round(sub_total, 2)}') 
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')        

#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION del RECIBO
#funcion del boton recibo que se encargara de hacer y entregar por pantalla el recibo del gasto consumido por el cliente
def recibo():
    #encabezado del recibo
    texto_del_recibo.delete(1.0, END)
    numero_recibo = f'Nº - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_del_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_del_recibo.insert(END, f'DATOS:\t\t{numero_recibo}\t\t{fecha_del_recibo}\n')
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, 'Producto\t\t  Cantidad\t\tCosto producto\n')
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    #loop para informacion del recibo
    x = 0
    for comida in texto_de_comida:
        if comida.get() != '0':
            texto_del_recibo.insert(END, f'{lista_de_productos_alimenticios[x]}\t\t\t{comida.get()}\t\t$ {int(comida.get()) * precio_comida[x]}\n')
        x += 1
    
    
    x = 0
    for bebida in texto_de_bebidas:
        if bebida.get() != '0':
            texto_del_recibo.insert(END, f'{lista_de_productos_bebibles[x]}\t\t\t{bebida.get()}\t\t$ {int(bebida.get()) * precio_bebida[x]}\n')
        x += 1
        
    
    x = 0
    for postre in texto_de_postres:
        if postre.get() != '0':
            texto_del_recibo.insert(END, f'{lista_de_productos_postres[x]}\t\t\t{postre.get()}\t\t$ {int(postre.get()) * precio_postre[x]}\n')
        x += 1  
        
    #cierre del recibo mostrando el  costo total discriminado por tipo de producto,subtotal,impuestos y total
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, f' Costo TOTAL de COMIDA: $ \t\t\t\t\t{var_costo_de_la_comida.get()}\n')  
    texto_del_recibo.insert(END, f' Costo TOTAL de BEBIDA: $ \t\t\t\t\t{var_costo_de_la_bebida.get()}\n')
    texto_del_recibo.insert(END, f' Costo TOTAL de POSTRE: $ \t\t\t\t\t{var_costo_de_la_postre.get()}\n')        
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, f' Costo SUBTOTAL: $ \t\t\t\t\t{var_subtotal.get()}\n')
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, f' Costo IMPUESTO: $ \t\t\t\t\t{var_impuestos.get()}\n')
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, f' Costo TOTAL: $ \t\t\t\t\t{var_total.get()}\n\n\n')
    texto_del_recibo.insert(END, f'/' * 85 + '\n')
    contenido_del_recibo = texto_del_recibo.get("1.0", END)
    return contenido_del_recibo

#?--------------------------------------------------------------------------------------------------------------------
#!GENERADOR del CODIGO QR del recibo 
# Define la función para generar el código QR y mostrarlo en un nuevo popup cuando se presiona el boton Rec QR
def generar_qr():
    # Llama a la función recibo para obtener la información del recibo
    informacion_recibo = recibo()

    # Crea el código QR
    qr = qrcode.QRCode(version=1, box_size=4, border=4)
    qr.add_data(informacion_recibo)
    qr.make(fit=True)

    # Convierte el código QR en una imagen
    img_qr = qr.make_image(fill='black', back_color='white')

    # Muestra la imagen del QR en un nuevo popup
    popup_qr = Toplevel()
    popup_qr.title("Código QR")
    popup_qr.geometry("450x450")

    # Convierte la imagen del QR en un formato compatible con Tkinter
    img_tk = ImageTk.PhotoImage(img_qr)

    # Crea un widget Label para mostrar la imagen del QR en el popup
    label_qr = Label(popup_qr, image=img_tk)
    label_qr.image = img_tk  # Guarda el atributo image
    label_qr.pack(pady=20)


    # Hace que el popup sea modal
    popup_qr.grab_set()





#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de enviar RECIBO POR WHATSAPP
#funcioin del boton guardar que guardara el recibo en un archivo txt de forma local
def enviar_por_whatsapp(informacion_recibo, numero_telefono):
    # Configurar las credenciales de Twilio aca
    account_sid = "ACb63c9670cbdefb231c2933b8b7576477"  #?se sacan de la pagina luego de registrarse, del que dice en vivo, life
    auth_token = "7291d1479b1779617b85a026f6600e80"     #?se sacan de la pagina luego de registrarse, del que dice en vivo, life
    numero_twilio = "whatsapp:+14155238886"             #?El número de teléfono proporcionado por Twilio para WhatsApp y emparejarlo de forma gratuita como sandbox con el numero nuestro de prueba al que enviaremos en recibo poniendolo en el pop-up completo sin espacios con con codigo pais nuestro, el codigo local y nuestro numero, lllegandonos por whatsapps el recibo

    # Configurar y envía el mensaje de WhatsApp
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=informacion_recibo,
            from_=numero_twilio,
            to=f"whatsapp:{numero_telefono}"
        )
    except Exception as e:
        print(f"Error al enviar el mensaje de WhatsApp: {e}")
        messagebox.showerror("Error", f"Error al enviar el mensaje de WhatsApp: {e}")

#Twilio - registrarse para probar y poner sus datos en # Configurar las credenciales de Twilio aca
'''Regístrese en Twilio: Visite https://www.twilio.com/try-twilio para registrarse en una cuenta gratuita de Twilio. Complete el proceso de registro y verificación.

Obtenga su Account SID y Auth Token: Inicie sesión en la Consola de Twilio en https://www.twilio.com/console. En la página principal de la Consola, encontrará su Account SID y Auth Token en el panel superior.

Configurar WhatsApp Sandbox: Visite https://www.twilio.com/console/sms/whatsapp/sandbox para configurar el entorno Sandbox de WhatsApp. Siga las instrucciones para unir su número de teléfono personal al entorno Sandbox enviando un mensaje de WhatsApp al número proporcionado por Twilio con el código indicado.

Obtenga el número de teléfono de Twilio Sandbox: En la misma página del entorno Sandbox de WhatsApp, encontrará el número de teléfono de Twilio que admite WhatsApp en el formato whatsapp:+1234567890. Tome nota de este número.

Configurar la aplicación: Reemplace las credenciales de Twilio y el número de teléfono de Twilio en el script de Python con las credenciales y el número de teléfono que obtuvo en los pasos 2 y 4. Asegúrese de guardar los cambios en el script.

Ejecute la aplicación: Ahora puede ejecutar la aplicación con sus propias credenciales de Twilio y probar la función de enviar recibos a través de WhatsApp.

Proporcionando estas instrucciones, permitirás a los usuarios configurar y probar tu aplicación de forma segura y sin comprometer tus propias credenciales de Twilio.

'''
#link directo para probar el envio de recibo gratis en modo sandbox por twilio: https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Flearn%3Fx-target-region%3Dus1



#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION del GUARDAR RECIBO
#funcioin del boton guardar que guardara el recibo en un archivo txt de forma local y da la opcion de enviarlo al cliente a traves de whatsapp
def guardar():
    #guarda el recibo en forma local en un txt
    informacion_recibo = texto_del_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')          #?metodo similar a los de os filedialog.asksaveasfile nos abrira el gestor de guardar en el sistema nuestro archivo con los parametros: modo de escritura mode='w', y extencion o formato a guardar defaultextension='.txt'
    archivo.write(informacion_recibo)                                              #?con write ya lo creamos al archivo con la informacion dentro y luego lo cerrarmos
    archivo.close()
    messagebox.showinfo('Informacion', 'Se guardo EXITOSAMENTE')

    # Crear un cuadro de diálogo emergente para preguntar si desea enviar el recibo por WhatsApp
    enviar_opcion = messagebox.askyesno("Enviar recibo", "¿Desea enviar el recibo al cliente por WhatsApp?", parent=aplicacion)

    if enviar_opcion:
        numero_telefono = simpledialog.askstring("Número de teléfono", "Ingrese el número de teléfono del cliente (incluyendo solo el codigo de area):", parent=aplicacion)
        numero_telefono = "+549"+numero_telefono
        if numero_telefono:
            enviar_por_whatsapp(informacion_recibo, numero_telefono)
            messagebox.showinfo('Informacion', 'Recibo enviado por WhatsApp')



#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de REINICIAR o LIMPIAR VENTANA
#funcion del boton resetear la cual limpiara todos los datos que esten en los paneles de la ventana
def resetear():
    #limpiamos el texto del panel RECIBO
    texto_del_recibo.delete(0.1, END)
    
    #limpiamos los texto del panel CANTIDAD DE PRODUCTOS
    for texto in texto_de_comida:
        texto.set('0')
    for texto in texto_de_bebidas:
        texto.set('0')
    for texto in texto_de_postres:
        texto.set('0')  
        
    #reiniciamos los cuadros de los CANTIDAD DE PRODUCTOS en 0 destildados los checkbox
    for cuadro in cuadros_de_comida:
        cuadro.config(state=DISABLED) 
    for cuadro in cuadros_de_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_de_postres:
        cuadro.config(state=DISABLED)  
        
    #sacar los check de los checkbox
    for v in variables_de_comidas:
        v.set(0) 
    for v in variables_de_bebida:
        v.set(0) 
    for v in variables_de_postre:
        v.set(0) 
        
    #limpiar los cuadros de costos, subtotal,  impuestos y total
    var_costo_de_la_comida.set('')
    var_costo_de_la_bebida.set('')
    var_costo_de_la_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')
                                
    
              
#?--------------------------------------------------------------------------------------------------------------------
#!inicio de aplicacion
#inicio tkinter
aplicacion = Tk()
    



#?--------------------------------------------------------------------------------------------------------------------
#!ventana
#defino el tamaño de la ventana (ponemos los pixeles de la pantalla y mas la posicion donde queremos que aparesca la ventana, con +0 el eje x y +0 en eje y)
aplicacion.geometry('1060x630+0+0')


#blokear la maximizacion de la ventana, ni en su eje y ni x.
aplicacion.resizable(0, 0)


#titulo del borde superior de la ventana 
aplicacion.title('GESTOR DE RESTAURANTE')


#coolor de fondo 
aplicacion.config(bg='CadetBlue2')


#?--------------------------------------------------------------------------------------------------------------------
#!panel SUPERIOR de titulo
#panel superior
#Función para cambiar el color del fondo de texto de manera aleatoria
from itertools import cycle
def cambiar_color_fondo_titulo():
    #Se elige un color aleatorio de una lista de colores para el fondo
    color = random.choice(['CadetBlue1', 'DodgerBlue2', 'SteelBlue2', 'RoyalBlue2', '#39FF14'])
    #Se configura el fondo de la etiqueta con el color elegido
    titulo_panel_sup.config(bg=color)
    #Se llama a la función after cada 1300 milisegundos para cambiar el color de fondo de manera automática
    titulo_panel_sup.after(1300, cambiar_color_fondo_titulo)

#Función para cambiar el color del texto del titulo de manera aleatoria
#Lista de colores para el texto
colors = cycle(['purple', 'deeppink', 'red', 'blue'])
def cambiar_color_texto_titulo():
    #Se configura el color del texto con el siguiente color de la lista de colores
    titulo_panel_sup.config(fg=next(colors))
    #Se llama a la función after cada 1300 milisegundos para cambiar el color del texto de manera automática
    titulo_panel_sup.after(1300, cambiar_color_texto_titulo)

#Creación del panel superior
panel_superior = Frame(aplicacion, bd=1.5, relief=RIDGE)       #?relief=RIDGE: Este parámetro define el tipo de borde que tendrá el frame. En este caso, el valor "RIDGE" se refiere a un borde con relieve en forma de "montañas" o "valles"
panel_superior.pack(side=TOP, fill=BOTH, expand=True)          #?expand=True: Este parámetro le indica al frame que debe expandirse para llenar todo el espacio disponible. Al establecerlo en "True", el frame se extenderá horizontalmente y verticalmente para llenar todo el espacio disponible en su contenedor.fill=BOTH: Este parámetro le indica al frame cómo debe llenar el espacio disponible en su contenedor. Al establecerlo en "BOTH", el frame se expandirá tanto horizontal como verticalmente para llenar todo el espacio disponible.

#Crear etiqueta con el título
titulo_panel_sup = Label(panel_superior, text='SISTEMA DE P4IFacturacion', font=('Dosis', 40), bg='CadetBlue1', width=30, relief=SUNKEN, bd=5)
titulo_panel_sup.place(relx=0.5, rely=0.5, anchor=CENTER)

#Llamar a la función para cambiar el color del fondo automáticamente
cambiar_color_fondo_titulo()

#Llamar a la función para cambiar el color del texto automáticamente
cambiar_color_texto_titulo()

#?--------------------------------------------------------------------------------------------------------------------
#!panel IZQUIERDO
#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)



#?--------------------------------------------------------------------------------------------------------------------
#!panel COSTO
#panel de costo
panel_costo = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='lightgreen', padx='110')
panel_costo.pack(side=BOTTOM)



#?--------------------------------------------------------------------------------------------------------------------
#!panel COMIDAS
#panel de comidas 
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='#FF69B4')       #?Labelframe seria como un cuadro que ya viene con la etiqueta incorporada
panel_comidas.pack(side=LEFT)




#?--------------------------------------------------------------------------------------------------------------------
#!panel BEBIDAS
#panel de bebidas 
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='#CC008C')       #?Labelframe seria como un cuadro que ya viene con la etiqueta incorporada
panel_bebidas.pack(side=LEFT)                    #?siguen llendo para la izquierda dado que toma el limite del panel anterior ubicado a la izquierda, osea que se pondra a su lado




#?--------------------------------------------------------------------------------------------------------------------
#!panel POSTRES
#panel de postres 
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='#660066')       #?Labelframe seria como un cuadro que ya viene con la etiqueta incorporada
panel_postres.pack(side=LEFT)





#?--------------------------------------------------------------------------------------------------------------------
#!panel DERECHO
#panel derecho de resultado y funciones del sistema 
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)




#?--------------------------------------------------------------------------------------------------------------------
#!panel CALCULADORA
#panel de calculadora 
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg='CadetBlue2')
panel_calculadora.pack()                                #?por defecto si no definimos nada en .pack viene en top osea se pondra arriba dentro de nuestro panel derecho




#?--------------------------------------------------------------------------------------------------------------------
#!panel recibo
#panel de recibo 
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='CadetBlue2')
panel_recibo.pack() 



#?--------------------------------------------------------------------------------------------------------------------
#!panel botones
#panel de botones 
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='CadetBlue2')
panel_botones.pack() 




#?--------------------------------------------------------------------------------------------------------------------
#!lista de COMIDAS
#lista de productos alimenticios 
lista_de_productos_alimenticios = ["Pizza","Hamburguesa","Ensalada César","Sushi","Tacos","Pollo a la parrilla","Spaghetti","Sándwich de pavo","Burrito","Curry","Filete","Hot dogs","Tostadas","Albóndigas","Pescado y papas fritas"]



#?--------------------------------------------------------------------------------------------------------------------
#!lista de BEBIDAS
#lista de productos bebibles 
lista_de_productos_bebibles = ["Agua","Refresco de cola","Limonada","Jugo de naranja","Té helado","Cerveza","Vino tinto","Vino blanco","Sidra","Margarita","Agua mineral","Zumo de manzana","Zumo de piña","Café americano","Café con leche"]



#?--------------------------------------------------------------------------------------------------------------------
#!lista de POSTRES
#lista de productos de postres 
lista_de_productos_postres = ["Tiramisú","Helado de vainilla","Pastel de chocolate","Flan","Cheesecake","Brownies","Galletas","Cupcakes","Natillas","Donuts","Pie de manzana","Crema catalana","Pudding","Macarons","Fresas con crema"]


#?--------------------------------------------------------------------------------------------------------------------
#!casillas CHECKBOX de COMIDAS
#creamos un loop para que itere entre cada comida de la lista y controlemos los valores de los checkboxseleccionados
variables_de_comidas = []                                                                                           #?creamos una variable para en ella guardar y gestionar luego el valor de onvalue y oofvalue
cuadros_de_comida = []
texto_de_comida = []
contador_de_comidas = 0

for comida in lista_de_productos_alimenticios:
    #crea los checkbutton
    variables_de_comidas.append('')
    variables_de_comidas[contador_de_comidas]= IntVar()                                                             #?controlamos que a partir de su indice dado por contador, en cada loop se guardara en la variable numerica dada por la clase InterVar() para controlar los check button           
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 9, 'bold'), onvalue=1, offvalue=0, variable=variables_de_comidas[contador_de_comidas], command=control_check)        #?Checkbox es un metodo de tkinter para crear una casilla para marcar, y luego le decimos donde debe estar osea en el panel_comidas, el resto de parameros, y le sumamos unos nuevos que daran valor a las casillas si esta marcada valdra 1 con onvalue=1 y 0 con offvalue=0, y luego gestionamos que en el loop controle si esta marcada la casilla con respecto al contador dentro de la variable_comidas que va almacenando en cada iteracion el valor de cada checkbox
    comida.grid(row=contador_de_comidas, column=0, sticky=W)                                                        #? luego ubicamos en que fila empiece a aparecer iterando entre cada producto que se selecciona y se va iterando con respecto a los productos seleccionados y el valor de contador. por ende la ubicacion de fila la pondremos con respecto al valor de contador, con : row=contador_de_productos   
    #crear los cuadros de ingreso
    #Crear los cuadros de ingreso para los platos de comida
    cuadros_de_comida.append('')                                            #?agregar una cadena vacía a la lista de cuadros de comida
    texto_de_comida.append('')                                              #?agregar una cadena vacía a la lista de texto de comida
    #damos el valor del ingreso de cantidad
    texto_de_comida[contador_de_comidas] = StringVar()                      #?con StringVar le decimos que la posicion doinde esta el ingreso de cantidad sea un valor de string
    texto_de_comida[contador_de_comidas].set('0')                           #?con set('0') le decimos que en default tenga el valor 0  en carda producto de la lista de comidads iteradas
    cuadros_de_comida[contador_de_comidas] = Entry(panel_comidas,           #?crear un objeto Entry y almacenarlo en la lista de cuadros de comida en la posición "contador_de_comidas"
                                                font=('Dosis', 13, 'bold'),
                                                bd=1,
                                                width=3,
                                                state=DISABLED,
                                                textvariable=texto_de_comida[contador_de_comidas])
    cuadros_de_comida[contador_de_comidas].grid(row=contador_de_comidas,    #?ubicar el cuadro de entrada en el panel de comidas en la fila "contador_de_comidas" y columna 1
                                                column=1)

    contador_de_comidas += 1 
    
    
    
    
#?--------------------------------------------------------------------------------------------------------------------
#!casillas CHECKBOX de bebida
#creamos un loop para que itere entre cada bebida de la lista y controlemos los valores de los checkboxseleccionados
variables_de_bebida = []                                                                                             #?creamos una variable para en ella guardar y gestionar luego el valor de onvalue y oofvalue
cuadros_de_bebidas = []
texto_de_bebidas = []
contador_de_bebida = 0

for bebida in lista_de_productos_bebibles:
    #crea los checkbutton
    variables_de_bebida.append('')
    variables_de_bebida[contador_de_bebida]= IntVar()                                                             #?controlamos que a partir de su indice dado por contador, en cada loop se guardara en la variable numerica dada por la clase InterVar() para controlar los check button           
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 9, 'bold'), onvalue=1, offvalue=0, variable=variables_de_bebida[contador_de_bebida], command=control_check)        #?Checkbox es un metodo de tkinter para crear una casilla para marcar, y luego le decimos donde debe estar osea en el panel_comidas, el resto de parameros, y le sumamos unos nuevos que daran valor a las casillas si esta marcada valdra 1 con onvalue=1 y 0 con offvalue=0, y luego gestionamos que en el loop controle si esta marcada la casilla con respecto al contador dentro de la variable_comidas que va almacenando en cada iteracion el valor de cada checkbox
    bebida.grid(row=contador_de_bebida, column=0, sticky=W)                                                        #? luego ubicamos en que fila empiece a aparecer iterando entre cada producto que se selecciona y se va iterando con respecto a los productos seleccionados y el valor de contador. por ende la ubicacion de fila la pondremos con respecto al valor de contador, con : row=contador_de_productos   
    #crear los cuadros de ingreso
    # Agregar un cuadro de entrada de bebidas a la lista cuadros_de_bebidas
    cuadros_de_bebidas.append('')

    # Agregar un texto de bebida a la lista texto_de_bebidas
    texto_de_bebidas.append('')
    #damos el valor del ingreso de cantidad
    texto_de_bebidas[contador_de_bebida] = StringVar()                      #?con StringVar le decimos que la posicion doinde esta el ingreso de cantidad sea un valor de string
    texto_de_bebidas[contador_de_bebida].set('0')                           #?con set('0') le decimos que en default tenga el valor 0  en carda producto de la lista de bebidas iteradas
    # Crear un cuadro de entrada de bebidas en la posición indicada por contador_de_bebida en panel_bebidas
    # El cuadro de entrada está desactivado (state=DISABLED), con una fuente y tamaño específicos y un borde de 1 píxel
    # Además, el cuadro de entrada está vinculado a una variable de texto en la lista texto_de_bebidas en la posición indicada por contador_de_bebida
    cuadros_de_bebidas[contador_de_bebida] = Entry(panel_bebidas,
                                                font=('Dosis', 13, 'bold'),
                                                bd=1,
                                                width=3,
                                                state=DISABLED,
                                                textvariable=texto_de_bebidas[contador_de_bebida])

    # Ubicar el cuadro de entrada de bebidas en la fila indicada por contador_de_bebida y la columna 1 de panel_bebidas
    cuadros_de_bebidas[contador_de_bebida].grid(row=contador_de_bebida,
                                                column=1)

    contador_de_bebida += 1 
    
    
    
    
    
#?--------------------------------------------------------------------------------------------------------------------
#!casillas CHECKBOX de POSTRES
#creamos un loop para que itere entre cada postre de la lista y controlemos los valores de los checkboxseleccionados
variables_de_postre = []                                                                                             #?creamos una variable para en ella guardar y gestionar luego el valor de onvalue y oofvalue
cuadros_de_postres = []
texto_de_postres = []
contador_de_postre = 0

for postre in lista_de_productos_postres:
    #crea los checkbutton
    variables_de_postre.append('')
    variables_de_postre[contador_de_postre]= IntVar()                                                             #?controlamos que a partir de su indice dado por contador, en cada loop se guardara en la variable numerica dada por la clase InterVar() para controlar los check button           
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 9, 'bold'), onvalue=1, offvalue=0, variable=variables_de_postre[contador_de_postre], command=control_check)        #?Checkbox es un metodo de tkinter para crear una casilla para marcar, y luego le decimos donde debe estar osea en el panel_comidas, el resto de parameros, y le sumamos unos nuevos que daran valor a las casillas si esta marcada valdra 1 con onvalue=1 y 0 con offvalue=0, y luego gestionamos que en el loop controle si esta marcada la casilla con respecto al contador dentro de la variable_comidas que va almacenando en cada iteracion el valor de cada checkbox
    postre.grid(row=contador_de_postre, column=0, sticky=W)                                                        #? luego ubicamos en que fila empiece a aparecer iterando entre cada producto que se selecciona y se va iterando con respecto a los productos seleccionados y el valor de contador. por ende la ubicacion de fila la pondremos con respecto al valor de contador, con : row=contador_de_productos   
    #crear los cuadros de ingreso
    cuadros_de_postres.append('')
    texto_de_postres.append('')
    #damos el valor del ingreso de cantidad
    texto_de_postres[contador_de_postre] = StringVar()                      #?con StringVar le decimos que la posicion doinde esta el ingreso de cantidad sea un valor de string
    texto_de_postres[contador_de_postre].set('0')                           #?con set('0') le decimos que en default tenga el valor 0  en carda producto de la lista de postres iteradas
    # crear un cuadro de entrada (Entry) para cada postre
    cuadros_de_postres[contador_de_postre] = Entry(panel_postres,
                                                   font=('Dosis', 13, 'bold'),
                                                   bd=1,
                                                   width=3,
                                                   state=DISABLED,  # deshabilitamos el cuadro de entrada
                                                   textvariable=texto_de_postres[contador_de_postre])
    # ubicar el cuadro de entrada en la fila correspondiente
    cuadros_de_postres[contador_de_postre].grid(row=contador_de_postre,
                                                column=1)
    contador_de_postre += 1   
    
  

#?--------------------------------------------------------------------------------------------------------------------
#!VARIABLES PARA COSTOS DE PRODUCTOS
var_costo_de_la_comida = StringVar()
var_costo_de_la_bebida = StringVar()
var_costo_de_la_postre = StringVar()

var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()


#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del panel de COSTO COMIDA
#se gestionaran las etiquetas osea titulos de cada costo y campos de entrada, e impuestos
etiqueta_costo_de_comida = Label(panel_costo,
                                 text='Costo comida',
                                 font=('Dosis',8,'bold'),
                                 bg='#9E0063',
                                 fg='#E6E6FA')
etiqueta_costo_de_comida.grid(row=0, 
                           column=0)
                                 
texto_costo_comida = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_costo_de_la_comida)
texto_costo_comida.grid(row=0, 
                        column=1, padx='41')                                  #?le ponemos column 1 para que este al lado de Label




#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del panel de COSTO BEBIDA
#se gestionaran las etiquetas osea titulos de cada costo y campos de entrada, e impuestos
etiqueta_costo_de_bebida = Label(panel_costo,
                                 text='Costo bebida',
                                 font=('Dosis',8,'bold'),
                                 bg='#9E0063',
                                 fg='#AF69EE')
etiqueta_costo_de_bebida.grid(row=1, 
                           column=0)
                                 
texto_costo_bebida = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_costo_de_la_bebida)
texto_costo_bebida.grid(row=1, 
                        column=1, padx='41')                                  #?le ponemos column 1 para que este al lado de Label





#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del panel de COSTO POSTRE
#se gestionaran las etiquetas osea titulos de cada costo y campos de entrada, e impuestos
etiqueta_costo_de_postre = Label(panel_costo,
                                 text='Costo postre',
                                 font=('Dosis',8,'bold'),
                                 bg='#9E0063',
                                 fg='#6B2C91')
etiqueta_costo_de_postre.grid(row=2, 
                           column=0)
                                 
texto_costo_postre = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_costo_de_la_postre)
texto_costo_postre.grid(row=2, 
                        column=1, padx='41')                                  #?le ponemos column 1 para que este al lado de Label




#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del SUBTOTAL
#se gestionaran las etiquetas osea titulos de subtotal y campos de entrada, e impuestos
etiqueta_subtotal = Label(panel_costo,
                                 text='Subtotal',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='sky blue')
etiqueta_subtotal.grid(row=0, 
                      column=2)
                                 
texto_subtotal = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, 
                   column=3, padx='41')                                       #?le ponemos column 3 para que este al lado de Label




#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del IMPUESTO
#se gestionaran las etiquetas osea titulos de impuesto y campos de entrada, e impuestos
etiqueta_impuesto = Label(panel_costo,
                                 text='impuesto',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='deepskyblue')
etiqueta_impuesto.grid(row=1, 
                       column=2)
                                 
texto_impuesto = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_impuestos)
texto_impuesto.grid(row=1, 
                   column=3, padx='41')                                       #?le ponemos column 1 para que este al lado de Label






#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del TOTAL
#se gestionaran las etiquetas osea titulos del total y campos de entrada, e impuestos
etiqueta_total = Label(panel_costo,
                                 text='total',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='blue')
etiqueta_total.grid(row=2, 
                    column=2)
                                 
texto_total = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_total)
texto_total.grid(row=2, 
                column=3, padx='41')                                          #?le ponemos column 1 para que este al lado de Label





#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion de BOTONES
#agremgamos los botones dentro del panel botones atraves de un loop
botones = ['TOTAL','RECIBO','GUARDAR','RESETEAR','Rec QR']
botones_creados = []
contador_columna = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',8,'bold'),
                   fg='red',
                   bg='azure4',
                   bd=1,
                   width=7)
    botones_creados.append(boton)
    boton.grid(row=0, 
           column=contador_columna)
    contador_columna += 1                               

botones_creados[0].config(command=total)                #?vamos a llamar a la funcion de arriba que nos dara el total tras precionar dicho boton
botones_creados[1].config(command=recibo)               #?vamos a llamar a la funcion de arriba que nos dara el recibo tras precionar dicho boton
botones_creados[2].config(command=guardar)              #?vamos a llamar a la funcion de arriba que nos guardara tras precionar dicho boton
botones_creados[3].config(command=resetear)             #?vamos a llamar a la funcion de arriba que nos reseteara tras precionar dicho boton
botones_creados[4].config(command=generar_qr)           #?vamos a llamar a la funcion de arriba que nos dara el QR en un pop-up tras precionar dicho boton

#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion de RECIBO
#mostrara el recibo
texto_del_recibo = Text(panel_recibo,
                        font=('Dosis', 8, 'bold'),
                        bd=1,
                        bg='grey',
                        width=50,
                        height=26)
texto_del_recibo.grid(row=0,
                      column=0)




#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion de la CALCULADORA
#gestion de la calculadora
visor_de_calculadora = Entry(panel_calculadora,             #?visualizaciondel resultado
                             font=('Dosis',8,'bold'),
                             width=55,
                             bd=1)
visor_de_calculadora.grid(row=0,
                          column=0,
                          columnspan=4)

#variables para ubicar teclas de la calculadora
fila_tecla = 1
columna_tecla = 0

botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','X','IGUAL','borrar','0','/']
botones_guardados = []


for teclas in botones_calculadora:
    teclas = Button(panel_calculadora,
                    text=teclas.title(),
                    font=('Dosis',8,'bold'),
                    fg='deeppink',
                    bg='azure4',
                    bd=1,
                    width=10)
    botones_guardados.append(teclas)
    teclas.grid(row=fila_tecla, 
                column=columna_tecla)
    if columna_tecla == 3:
        fila_tecla += 1
        
    columna_tecla += 1

    if columna_tecla == 4:
        columna_tecla = 0    


#llamadas por cada tecla de las funciones para el funcionamiento de la calculadora que estan al principio
botones_guardados[0].config(command=lambda : click_tecla_calculadora('7'))     #?con respecto al indice de los botones guardados mas .config, podemos definir las configuraciones con command = lamdnda : y dentro de lamnda nos permite activar la funcion de click_tecla_calculadora de arriba, para que al ingresarle en este caso '7' dentro de dicha funcion que seria el valor de la tecla precionada en dicho indice anteriormente, para luego ser mostrado en el visor de la calculadora
botones_guardados[1].config(command=lambda : click_tecla_calculadora('8'))
botones_guardados[2].config(command=lambda : click_tecla_calculadora('9'))
botones_guardados[3].config(command=lambda : click_tecla_calculadora('+'))
botones_guardados[4].config(command=lambda : click_tecla_calculadora('4'))
botones_guardados[5].config(command=lambda : click_tecla_calculadora('5'))
botones_guardados[6].config(command=lambda : click_tecla_calculadora('6'))
botones_guardados[7].config(command=lambda : click_tecla_calculadora('-'))
botones_guardados[8].config(command=lambda : click_tecla_calculadora('1'))
botones_guardados[9].config(command=lambda : click_tecla_calculadora('2'))
botones_guardados[10].config(command=lambda : click_tecla_calculadora('3'))
botones_guardados[11].config(command=lambda : click_tecla_calculadora('*'))
botones_guardados[12].config(command=igual)                                    #?con respecto al indice de los botones guardados mas .config, podemos definir las configuraciones con command = lamdnda : y dentro de lamnda nos permite activar la funcion de igual() de arriba, para que nos muestre el resultado, osea en fin con command nos permit hacer el llamado de la funcion que querramos para hacer uso de ella
botones_guardados[13].config(command=borrar_numeros)
botones_guardados[14].config(command=lambda : click_tecla_calculadora('0'))
botones_guardados[15].config(command=lambda : click_tecla_calculadora('/'))
    



#?--------------------------------------------------------------------------------------------------------------------
#!creamos el loop
# hago que la ventana no se cierre 
aplicacion.mainloop()

#! Gestor de facturacion de restaurante - SISTEMA de P4IFacturacion - By P4IM0N


```
````

CODEO DEL DIA 12:

````python
// Some code

```python
#! Gestor de facturacion de restaurante - practica - By P4IM0N

#?--------------------------------------------------------------------------------------------------------------------
#!importamos librerias necesarias
from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

#?--------------------------------------------------------------------------------------------------------------------
#!LISTA de PRECIO de los productos
#la lista de precios e comidas, bebidas y postres 
# Lista de precios para productos alimenticios
precio_comida = [123, 104, 96, 157, 88, 140, 119, 105, 125, 165, 185, 65, 75, 135, 145]

# Lista de precios para productos bebibles
precio_bebida = [15, 35, 25, 35, 45, 55, 65, 65, 45, 75, 25, 35, 45, 45, 45]

# Lista de precios para productos de postres
precio_postre = [65, 45, 55, 75, 85, 45, 35, 55, 65, 45, 75, 85, 65, 95, 55]




#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de la CALCULADORA
#funcion para que aparesca el valor numerico de la tecla presioinada ded la calculadora, borrar nuemeros y igual osea resultado
operador = ''

def click_tecla_calculadora(numero):
    global operador
    operador = operador + numero
    visor_de_calculadora.delete(0, END)
    visor_de_calculadora.insert(END, operador)

def borrar_numeros():
    global operador
    operador=''
    visor_de_calculadora.delete(0, END)

def igual():
    global operador
    igual_a= str(eval(operador))                #?eval nos permite que evalue los valores  guardados en operador como str, y los evaluara lo msmo resolviendo que es una operacion matematica, con lo que devolvera un integer pero al estar casteado lo transformara de nuevo en str para poder mostrarlo en el visor de calculadora
    visor_de_calculadora.delete(0, END)
    visor_de_calculadora.insert(0, igual_a)
    operador = ''


#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de los CHECKBOX
#revisara si los checkbox estan activados o no
def control_check():
    x = 0
    for c in cuadros_de_comida:    
        if variables_de_comidas[x].get() == 1:
            cuadros_de_comida[x].config(state=NORMAL)
            if cuadros_de_comida[x].get() == '0':
                cuadros_de_comida[x].delete(0, END)
            cuadros_de_comida[x].focus()
        else:
            cuadros_de_comida[x].config(state=DISABLED)
            texto_de_comida[x].set('0')    
        x += 1    
    
    
    x = 0
    for c in cuadros_de_bebidas:    
        if variables_de_bebida[x].get() == 1:
            cuadros_de_bebidas[x].config(state=NORMAL)
            if cuadros_de_bebidas[x].get() == '0':
                cuadros_de_bebidas[x].delete(0, END)
            cuadros_de_bebidas[x].focus()
        else:
            cuadros_de_bebidas[x].config(state=DISABLED)
            texto_de_bebidas[x].set('0')    
        x += 1  
        
    
    x = 0
    for c in cuadros_de_postres:    
        if variables_de_postre[x].get() == 1:
            cuadros_de_postres[x].config(state=NORMAL)
            if cuadros_de_postres[x].get() == '0':
                cuadros_de_postres[x].delete(0, END)
            cuadros_de_postres[x].focus()
        else:
            cuadros_de_postres[x].config(state=DISABLED)
            texto_de_postres[x].set('0')    
        x += 1              
    
    

#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de costo TOTAL
#funcion que resolvera el costo total de los productos seleccionads por el cliente con respecto de su cantidad en los checkbox
def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_de_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precio_comida[p])
        p += 1
     
    
    
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_de_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precio_bebida[p])
        p += 1
    
    
    
    sub_total_postre = 0
    p = 0
    for cantidad in texto_de_postres:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precio_postre[p])
        p += 1
       
        
    sub_total= sub_total_comida+sub_total_bebida+sub_total_postre  
    impuestos = sub_total * 0.10
    total=  sub_total + impuestos   
    
    
    var_costo_de_la_comida.set(f'$ {round(sub_total_comida, 2)}') 
    var_costo_de_la_bebida.set(f'$ {round(sub_total_bebida, 2)}') 
    var_costo_de_la_postre.set(f'$ {round(sub_total_postre, 2)}')  
    var_subtotal.set(f'$ {round(sub_total, 2)}') 
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')        

#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION del RECIBO
#funcion del boton recibo que se encargara de hacer y entregar por pantalla el recibo del gasto consumido por el cliente
def recibo():
    #encabezado del recibo
    texto_del_recibo.delete(1.0, END)
    numero_recibo = f'Nº - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_del_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_del_recibo.insert(END, f'DATOS:\t\t{numero_recibo}\t\t{fecha_del_recibo}\n')
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, 'Producto\t\t  Cantidad\t\tCosto producto\n')
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    #loop para informacion del recibo
    x = 0
    for comida in texto_de_comida:
        if comida.get() != '0':
            texto_del_recibo.insert(END, f'{lista_de_productos_alimenticios[x]}\t\t\t{comida.get()}\t\t$ {int(comida.get()) * precio_comida[x]}\n')
        x += 1
    
    
    x = 0
    for bebida in texto_de_bebidas:
        if bebida.get() != '0':
            texto_del_recibo.insert(END, f'{lista_de_productos_bebibles[x]}\t\t\t{bebida.get()}\t\t$ {int(bebida.get()) * precio_bebida[x]}\n')
        x += 1
        
    
    x = 0
    for postre in texto_de_postres:
        if postre.get() != '0':
            texto_del_recibo.insert(END, f'{lista_de_productos_postres[x]}\t\t\t{postre.get()}\t\t$ {int(postre.get()) * precio_postre[x]}\n')
        x += 1  
        
    #cierre del recibo mostrando el  costo total discriminado por tipo de producto,subtotal,impuestos y total
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, f' Costo TOTAL de COMIDA: $ \t\t\t\t\t{var_costo_de_la_comida.get()}\n')  
    texto_del_recibo.insert(END, f' Costo TOTAL de BEBIDA: $ \t\t\t\t\t{var_costo_de_la_bebida.get()}\n')
    texto_del_recibo.insert(END, f' Costo TOTAL de POSTRE: $ \t\t\t\t\t{var_costo_de_la_postre.get()}\n')        
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, f' Costo SUBTOTAL: $ \t\t\t\t\t{var_subtotal.get()}\n')
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, f' Costo IMPUESTO: $ \t\t\t\t\t{var_impuestos.get()}\n')
    texto_del_recibo.insert(END, f'=' * 38 + '\n')
    texto_del_recibo.insert(END, f' Costo TOTAL: $ \t\t\t\t\t{var_total.get()}\n\n\n')
    texto_del_recibo.insert(END, f'/' * 85 + '\n')



#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION del GUARDAR RECIBO
#funcioin del boton guardar que guardara el recibo en un archivo txt de forma local
def guardar():
    informacion_recibo = texto_del_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')          #?metodo similar a los de os filedialog.asksaveasfile nos abrira el gestor de guardar en el sistema nuestro archivo con los parametros: modo de escritura mode='w', y extencion o formato a guardar defaultextension='.txt'
    archivo.write(informacion_recibo)                                              #?con write ya lo creamos al archivo con la informacion dentro y luego lo cerrarmos
    archivo.close()
    messagebox.showinfo('Informacion', 'Se guardo EXITOSAMENTE')                   #?messagebox.showinfo  con estos metodos hacemos que nos salte un cartel de notificacion o alerta tipo pop-ups, con la notificacion que le dimos de parametro      




#?--------------------------------------------------------------------------------------------------------------------
#!FUNCION de REINICIAR o LIMPIAR VENTANA
#funcion del boton resetear la cual limpiara todos los datos que esten en los paneles de la ventana
def resetear():
    #limpiamos el texto del panel RECIBO
    texto_del_recibo.delete(0.1, END)
    
    #limpiamos los texto del panel CANTIDAD DE PRODUCTOS
    for texto in texto_de_comida:
        texto.set('0')
    for texto in texto_de_bebidas:
        texto.set('0')
    for texto in texto_de_postres:
        texto.set('0')  
        
    #reiniciamos los cuadros de los CANTIDAD DE PRODUCTOS en 0 destildados los checkbox
    for cuadro in cuadros_de_comida:
        cuadro.config(state=DISABLED) 
    for cuadro in cuadros_de_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_de_postres:
        cuadro.config(state=DISABLED)  
        
    #sacar los check de los checkbox
    for v in variables_de_comidas:
        v.set(0) 
    for v in variables_de_bebida:
        v.set(0) 
    for v in variables_de_postre:
        v.set(0) 
        
    #limpiar los cuadros de costos, subtotal,  impuestos y total
    var_costo_de_la_comida.set('')
    var_costo_de_la_bebida.set('')
    var_costo_de_la_postre.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')
                                
    
              
#?--------------------------------------------------------------------------------------------------------------------
#!inicio de aplicacion
#inicio tkinter
aplicacion = Tk()
    



#?--------------------------------------------------------------------------------------------------------------------
#!ventana
#defino el tamaño de la ventana (ponemos los pixeles de la pantalla y mas la posicion donde queremos que aparesca la ventana, con +0 el eje x y +0 en eje y)
aplicacion.geometry('1060x630+0+0')


#blokear la maximizacion de la ventana, ni en su eje y ni x.
aplicacion.resizable(0, 0)


#titulo del borde superior de la ventana 
aplicacion.title('GESTOR DE RESTAURANTE')


#coolor de fondo 
aplicacion.config(bg='CadetBlue2')


#?--------------------------------------------------------------------------------------------------------------------
#!panel SUPERIOR de titulo
#panel superior
panel_superior = Frame(aplicacion, bd=1.5, relief=FLAT)   #? con Frame decimos que haremos un cuadr, en donde? dentro de nuestra aplicacion, con un borde con bd=1 de ancho, y un relieve con relief= que pueden ser: FLAT, RAISED, SUNKEN, GROOVE, RIDGE
panel_superior.pack(side=TOP)                           #? con el metodo .pack ya lo ponemos al panel dentro de nuestra aplicacion, y definimos en que parte lo ponemos, aca le dimos TOP osea arriba.


#titulo de panel superior en etiqueta Label
titulo_panel_sup = Label(panel_superior, text='SISTEMA DE FACTURACION', fg='azure4', font=('Dosis', 40), bg='CadetBlue1', width=30)       #? label es etiqueta, el decimos donde va a ir esta etiqueta de titulo dentro de nuestro panel ya creado arriba (panel superioir, luego el texto que contendra con text=, luego el color de la letra con fg=, definimos luego el tipo de letra fuente, con font= tipo y tamaño, y color de fondo del titulo con bg=, y el ancho de la etiqueta titulo con width= ) 
titulo_panel_sup.grid(row=0, column=0)                                                                                                    #?luego ya colocamos y definimos la posicionde nuestro titulo etiqueta dentro de nuestro panel para que se coloque como lo definimos, y le podemos dar la ubicacion con row= fila numeriaca y con column= columna numeriaca donde lo quremos   


#?--------------------------------------------------------------------------------------------------------------------
#!panel IZQUIERDO
#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)



#?--------------------------------------------------------------------------------------------------------------------
#!panel COSTO
#panel de costo
panel_costo = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='lightgreen', padx='110')
panel_costo.pack(side=BOTTOM)



#?--------------------------------------------------------------------------------------------------------------------
#!panel COMIDAS
#panel de comidas 
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='azure4')       #?Labelframe seria como un cuadro que ya viene con la etiqueta incorporada
panel_comidas.pack(side=LEFT)




#?--------------------------------------------------------------------------------------------------------------------
#!panel BEBIDAS
#panel de bebidas 
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='azure4')       #?Labelframe seria como un cuadro que ya viene con la etiqueta incorporada
panel_bebidas.pack(side=LEFT)                    #?siguen llendo para la izquierda dado que toma el limite del panel anterior ubicado a la izquierda, osea que se pondra a su lado




#?--------------------------------------------------------------------------------------------------------------------
#!panel POSTRES
#panel de postres 
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 15, 'bold'), bd=1, relief=FLAT, fg='azure4')       #?Labelframe seria como un cuadro que ya viene con la etiqueta incorporada
panel_postres.pack(side=LEFT)





#?--------------------------------------------------------------------------------------------------------------------
#!panel DERECHO
#panel derecho de resultado y funciones del sistema 
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)




#?--------------------------------------------------------------------------------------------------------------------
#!panel CALCULADORA
#panel de calculadora 
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg='CadetBlue2')
panel_calculadora.pack()                                #?por defecto si no definimos nada en .pack viene en top osea se pondra arriba dentro de nuestro panel derecho




#?--------------------------------------------------------------------------------------------------------------------
#!panel recibo
#panel de recibo 
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='CadetBlue2')
panel_recibo.pack() 



#?--------------------------------------------------------------------------------------------------------------------
#!panel botones
#panel de botones 
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='CadetBlue2')
panel_botones.pack() 




#?--------------------------------------------------------------------------------------------------------------------
#!lista de COMIDAS
#lista de productos alimenticios 
lista_de_productos_alimenticios = ["Pizza","Hamburguesa","Ensalada César","Sushi","Tacos","Pollo a la parrilla","Spaghetti","Sándwich de pavo","Burrito","Curry","Filete","Hot dogs","Tostadas","Albóndigas","Pescado y papas fritas"]



#?--------------------------------------------------------------------------------------------------------------------
#!lista de BEBIDAS
#lista de productos bebibles 
lista_de_productos_bebibles = ["Agua","Refresco de cola","Limonada","Jugo de naranja","Té helado","Cerveza","Vino tinto","Vino blanco","Sidra","Margarita","Agua mineral","Zumo de manzana","Zumo de piña","Café americano","Café con leche"]



#?--------------------------------------------------------------------------------------------------------------------
#!lista de POSTRES
#lista de productos de postres 
lista_de_productos_postres = ["Tiramisú","Helado de vainilla","Pastel de chocolate","Flan","Cheesecake","Brownies","Galletas","Cupcakes","Natillas","Donuts","Pie de manzana","Crema catalana","Pudding","Macarons","Fresas con crema"]



#?--------------------------------------------------------------------------------------------------------------------
#!casillas CHECKBOX de COMIDAS
#creamos un loop para que itere entre cada comida de la lista y controlemos los valores de los checkboxseleccionados
variables_de_comidas = []                                                                                           #?creamos una variable para en ella guardar y gestionar luego el valor de onvalue y oofvalue
cuadros_de_comida = []
texto_de_comida = []
contador_de_comidas = 0

for comida in lista_de_productos_alimenticios:
    #crea los checkbutton
    variables_de_comidas.append('')
    variables_de_comidas[contador_de_comidas]= IntVar()                                                             #?controlamos que a partir de su indice dado por contador, en cada loop se guardara en la variable numerica dada por la clase InterVar() para controlar los check button           
    comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', 9, 'bold'), onvalue=1, offvalue=0, variable=variables_de_comidas[contador_de_comidas], command=control_check)        #?Checkbox es un metodo de tkinter para crear una casilla para marcar, y luego le decimos donde debe estar osea en el panel_comidas, el resto de parameros, y le sumamos unos nuevos que daran valor a las casillas si esta marcada valdra 1 con onvalue=1 y 0 con offvalue=0, y luego gestionamos que en el loop controle si esta marcada la casilla con respecto al contador dentro de la variable_comidas que va almacenando en cada iteracion el valor de cada checkbox
    comida.grid(row=contador_de_comidas, column=0, sticky=W)                                                        #? luego ubicamos en que fila empiece a aparecer iterando entre cada producto que se selecciona y se va iterando con respecto a los productos seleccionados y el valor de contador. por ende la ubicacion de fila la pondremos con respecto al valor de contador, con : row=contador_de_productos   
    #crear los cuadros de ingreso
    #Crear los cuadros de ingreso para los platos de comida
    cuadros_de_comida.append('')                                            #?agregar una cadena vacía a la lista de cuadros de comida
    texto_de_comida.append('')                                              #?agregar una cadena vacía a la lista de texto de comida
    #damos el valor del ingreso de cantidad
    texto_de_comida[contador_de_comidas] = StringVar()                      #?con StringVar le decimos que la posicion doinde esta el ingreso de cantidad sea un valor de string
    texto_de_comida[contador_de_comidas].set('0')                           #?con set('0') le decimos que en default tenga el valor 0  en carda producto de la lista de comidads iteradas
    cuadros_de_comida[contador_de_comidas] = Entry(panel_comidas,           #?crear un objeto Entry y almacenarlo en la lista de cuadros de comida en la posición "contador_de_comidas"
                                                font=('Dosis', 13, 'bold'),
                                                bd=1,
                                                width=3,
                                                state=DISABLED,
                                                textvariable=texto_de_comida[contador_de_comidas])
    cuadros_de_comida[contador_de_comidas].grid(row=contador_de_comidas,    #?ubicar el cuadro de entrada en el panel de comidas en la fila "contador_de_comidas" y columna 1
                                                column=1)

    contador_de_comidas += 1 
    
    
    
    
#?--------------------------------------------------------------------------------------------------------------------
#!casillas CHECKBOX de bebida
#creamos un loop para que itere entre cada bebida de la lista y controlemos los valores de los checkboxseleccionados
variables_de_bebida = []                                                                                             #?creamos una variable para en ella guardar y gestionar luego el valor de onvalue y oofvalue
cuadros_de_bebidas = []
texto_de_bebidas = []
contador_de_bebida = 0

for bebida in lista_de_productos_bebibles:
    #crea los checkbutton
    variables_de_bebida.append('')
    variables_de_bebida[contador_de_bebida]= IntVar()                                                             #?controlamos que a partir de su indice dado por contador, en cada loop se guardara en la variable numerica dada por la clase InterVar() para controlar los check button           
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', 9, 'bold'), onvalue=1, offvalue=0, variable=variables_de_bebida[contador_de_bebida], command=control_check)        #?Checkbox es un metodo de tkinter para crear una casilla para marcar, y luego le decimos donde debe estar osea en el panel_comidas, el resto de parameros, y le sumamos unos nuevos que daran valor a las casillas si esta marcada valdra 1 con onvalue=1 y 0 con offvalue=0, y luego gestionamos que en el loop controle si esta marcada la casilla con respecto al contador dentro de la variable_comidas que va almacenando en cada iteracion el valor de cada checkbox
    bebida.grid(row=contador_de_bebida, column=0, sticky=W)                                                        #? luego ubicamos en que fila empiece a aparecer iterando entre cada producto que se selecciona y se va iterando con respecto a los productos seleccionados y el valor de contador. por ende la ubicacion de fila la pondremos con respecto al valor de contador, con : row=contador_de_productos   
    #crear los cuadros de ingreso
    # Agregar un cuadro de entrada de bebidas a la lista cuadros_de_bebidas
    cuadros_de_bebidas.append('')

    # Agregar un texto de bebida a la lista texto_de_bebidas
    texto_de_bebidas.append('')
    #damos el valor del ingreso de cantidad
    texto_de_bebidas[contador_de_bebida] = StringVar()                      #?con StringVar le decimos que la posicion doinde esta el ingreso de cantidad sea un valor de string
    texto_de_bebidas[contador_de_bebida].set('0')                           #?con set('0') le decimos que en default tenga el valor 0  en carda producto de la lista de bebidas iteradas
    # Crear un cuadro de entrada de bebidas en la posición indicada por contador_de_bebida en panel_bebidas
    # El cuadro de entrada está desactivado (state=DISABLED), con una fuente y tamaño específicos y un borde de 1 píxel
    # Además, el cuadro de entrada está vinculado a una variable de texto en la lista texto_de_bebidas en la posición indicada por contador_de_bebida
    cuadros_de_bebidas[contador_de_bebida] = Entry(panel_bebidas,
                                                font=('Dosis', 13, 'bold'),
                                                bd=1,
                                                width=3,
                                                state=DISABLED,
                                                textvariable=texto_de_bebidas[contador_de_bebida])

    # Ubicar el cuadro de entrada de bebidas en la fila indicada por contador_de_bebida y la columna 1 de panel_bebidas
    cuadros_de_bebidas[contador_de_bebida].grid(row=contador_de_bebida,
                                                column=1)

    contador_de_bebida += 1 
    
    
    
    
    
#?--------------------------------------------------------------------------------------------------------------------
#!casillas CHECKBOX de POSTRES
#creamos un loop para que itere entre cada postre de la lista y controlemos los valores de los checkboxseleccionados
variables_de_postre = []                                                                                             #?creamos una variable para en ella guardar y gestionar luego el valor de onvalue y oofvalue
cuadros_de_postres = []
texto_de_postres = []
contador_de_postre = 0

for postre in lista_de_productos_postres:
    #crea los checkbutton
    variables_de_postre.append('')
    variables_de_postre[contador_de_postre]= IntVar()                                                             #?controlamos que a partir de su indice dado por contador, en cada loop se guardara en la variable numerica dada por la clase InterVar() para controlar los check button           
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 9, 'bold'), onvalue=1, offvalue=0, variable=variables_de_postre[contador_de_postre], command=control_check)        #?Checkbox es un metodo de tkinter para crear una casilla para marcar, y luego le decimos donde debe estar osea en el panel_comidas, el resto de parameros, y le sumamos unos nuevos que daran valor a las casillas si esta marcada valdra 1 con onvalue=1 y 0 con offvalue=0, y luego gestionamos que en el loop controle si esta marcada la casilla con respecto al contador dentro de la variable_comidas que va almacenando en cada iteracion el valor de cada checkbox
    postre.grid(row=contador_de_postre, column=0, sticky=W)                                                        #? luego ubicamos en que fila empiece a aparecer iterando entre cada producto que se selecciona y se va iterando con respecto a los productos seleccionados y el valor de contador. por ende la ubicacion de fila la pondremos con respecto al valor de contador, con : row=contador_de_productos   
    #crear los cuadros de ingreso
    cuadros_de_postres.append('')
    texto_de_postres.append('')
    #damos el valor del ingreso de cantidad
    texto_de_postres[contador_de_postre] = StringVar()                      #?con StringVar le decimos que la posicion doinde esta el ingreso de cantidad sea un valor de string
    texto_de_postres[contador_de_postre].set('0')                           #?con set('0') le decimos que en default tenga el valor 0  en carda producto de la lista de postres iteradas
    # crear un cuadro de entrada (Entry) para cada postre
    cuadros_de_postres[contador_de_postre] = Entry(panel_postres,
                                                   font=('Dosis', 13, 'bold'),
                                                   bd=1,
                                                   width=3,
                                                   state=DISABLED,  # deshabilitamos el cuadro de entrada
                                                   textvariable=texto_de_postres[contador_de_postre])
    # ubicar el cuadro de entrada en la fila correspondiente
    cuadros_de_postres[contador_de_postre].grid(row=contador_de_postre,
                                                column=1)
    contador_de_postre += 1         

#?--------------------------------------------------------------------------------------------------------------------
#!VARIABLES PARA COSTOS DE PRODUCTOS
var_costo_de_la_comida = StringVar()
var_costo_de_la_bebida = StringVar()
var_costo_de_la_postre = StringVar()

var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()


#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del panel de COSTO COMIDA
#se gestionaran las etiquetas osea titulos de cada costo y campos de entrada, e impuestos
etiqueta_costo_de_comida = Label(panel_costo,
                                 text='Costo comida',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='white')
etiqueta_costo_de_comida.grid(row=0, 
                           column=0)
                                 
texto_costo_comida = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_costo_de_la_comida)
texto_costo_comida.grid(row=0, 
                        column=1, padx='41')                                  #?le ponemos column 1 para que este al lado de Label




#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del panel de COSTO BEBIDA
#se gestionaran las etiquetas osea titulos de cada costo y campos de entrada, e impuestos
etiqueta_costo_de_bebida = Label(panel_costo,
                                 text='Costo bebida',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='white')
etiqueta_costo_de_bebida.grid(row=1, 
                           column=0)
                                 
texto_costo_bebida = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_costo_de_la_bebida)
texto_costo_bebida.grid(row=1, 
                        column=1, padx='41')                                  #?le ponemos column 1 para que este al lado de Label





#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del panel de COSTO POSTRE
#se gestionaran las etiquetas osea titulos de cada costo y campos de entrada, e impuestos
etiqueta_costo_de_postre = Label(panel_costo,
                                 text='Costo postre',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='white')
etiqueta_costo_de_postre.grid(row=2, 
                           column=0)
                                 
texto_costo_postre = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_costo_de_la_postre)
texto_costo_postre.grid(row=2, 
                        column=1, padx='41')                                  #?le ponemos column 1 para que este al lado de Label




#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del SUBTOTAL
#se gestionaran las etiquetas osea titulos de subtotal y campos de entrada, e impuestos
etiqueta_subtotal = Label(panel_costo,
                                 text='Subtotal',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='white')
etiqueta_subtotal.grid(row=0, 
                      column=2)
                                 
texto_subtotal = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, 
                   column=3, padx='41')                                       #?le ponemos column 3 para que este al lado de Label




#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del IMPUESTO
#se gestionaran las etiquetas osea titulos de impuesto y campos de entrada, e impuestos
etiqueta_impuesto = Label(panel_costo,
                                 text='impuesto',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='white')
etiqueta_impuesto.grid(row=1, 
                       column=2)
                                 
texto_impuesto = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_impuestos)
texto_impuesto.grid(row=1, 
                   column=3, padx='41')                                       #?le ponemos column 1 para que este al lado de Label






#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion y gestion del TOTAL
#se gestionaran las etiquetas osea titulos del total y campos de entrada, e impuestos
etiqueta_total = Label(panel_costo,
                                 text='total',
                                 font=('Dosis',8,'bold'),
                                 bg='azure4',
                                 fg='white')
etiqueta_total.grid(row=2, 
                    column=2)
                                 
texto_total = Entry(panel_costo,
                           font=('Dosis',8,'bold'),
                           bd=1,
                           width=8,
                           state='readonly',                       #?en state con el parametro readonly le indicamos que su estado es solo para que se pueda ver su valor y no puede ser modificado por es sector
                           textvariable=var_total)
texto_total.grid(row=2, 
                column=3, padx='41')                                          #?le ponemos column 1 para que este al lado de Label





#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion de BOTONES
#agremgamos los botones dentro del panel botones atraves de un loop
botones = ['TOTAL','RECIBO','GUARDAR','RESETEAR']
botones_creados = []
contador_columna = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',8,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)
    boton.grid(row=0, 
           column=contador_columna)
    contador_columna += 1                               

botones_creados[0].config(command=total)                #?vamos a llamar a la funcion de arriba que nos dara el total tras precionar dicho boton
botones_creados[1].config(command=recibo)               #?vamos a llamar a la funcion de arriba que nos dara el recibo tras precionar dicho boton
botones_creados[2].config(command=guardar)              #?vamos a llamar a la funcion de arriba que nos guardara tras precionar dicho boton
botones_creados[3].config(command=resetear)             #?vamos a llamar a la funcion de arriba que nos reseteara tras precionar dicho boton

#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion de RECIBO
#mostrara el recibo
texto_del_recibo = Text(panel_recibo,
                        font=('Dosis', 8, 'bold'),
                        bd=1,
                        width=50,
                        height=26)
texto_del_recibo.grid(row=0,
                      column=0)




#?--------------------------------------------------------------------------------------------------------------------
#!visualizacion de la CALCULADORA
#gestion de la calculadora
visor_de_calculadora = Entry(panel_calculadora,             #?visualizaciondel resultado
                             font=('Dosis',8,'bold'),
                             width=55,
                             bd=1)
visor_de_calculadora.grid(row=0,
                          column=0,
                          columnspan=4)

#variables para ubicar teclas de la calculadora
fila_tecla = 1
columna_tecla = 0

botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','X','IGUAL','borrar','0','/']
botones_guardados = []


for teclas in botones_calculadora:
    teclas = Button(panel_calculadora,
                    text=teclas.title(),
                    font=('Dosis',8,'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=10)
    botones_guardados.append(teclas)
    teclas.grid(row=fila_tecla, 
                column=columna_tecla)
    if columna_tecla == 3:
        fila_tecla += 1
        
    columna_tecla += 1

    if columna_tecla == 4:
        columna_tecla = 0    


#llamadas por cada tecla de las funciones para el funcionamiento de la calculadora que estan al principio
botones_guardados[0].config(command=lambda : click_tecla_calculadora('7'))     #?con respecto al indice de los botones guardados mas .config, podemos definir las configuraciones con command = lamdnda : y dentro de lamnda nos permite activar la funcion de click_tecla_calculadora de arriba, para que al ingresarle en este caso '7' dentro de dicha funcion que seria el valor de la tecla precionada en dicho indice anteriormente, para luego ser mostrado en el visor de la calculadora
botones_guardados[1].config(command=lambda : click_tecla_calculadora('8'))
botones_guardados[2].config(command=lambda : click_tecla_calculadora('9'))
botones_guardados[3].config(command=lambda : click_tecla_calculadora('+'))
botones_guardados[4].config(command=lambda : click_tecla_calculadora('4'))
botones_guardados[5].config(command=lambda : click_tecla_calculadora('5'))
botones_guardados[6].config(command=lambda : click_tecla_calculadora('6'))
botones_guardados[7].config(command=lambda : click_tecla_calculadora('-'))
botones_guardados[8].config(command=lambda : click_tecla_calculadora('1'))
botones_guardados[9].config(command=lambda : click_tecla_calculadora('2'))
botones_guardados[10].config(command=lambda : click_tecla_calculadora('3'))
botones_guardados[11].config(command=lambda : click_tecla_calculadora('*'))
botones_guardados[12].config(command=igual)                                    #?con respecto al indice de los botones guardados mas .config, podemos definir las configuraciones con command = lamdnda : y dentro de lamnda nos permite activar la funcion de igual() de arriba, para que nos muestre el resultado, osea en fin con command nos permit hacer el llamado de la funcion que querramos para hacer uso de ella
botones_guardados[13].config(command=borrar_numeros)
botones_guardados[14].config(command=lambda : click_tecla_calculadora('0'))
botones_guardados[15].config(command=lambda : click_tecla_calculadora('/'))
    



#?--------------------------------------------------------------------------------------------------------------------
#!creamos el loop
# hago que la ventana no se cierre 
aplicacion.mainloop()
```
````
