---
description: OBVIO FALTARIA AGREGARLE LOS ARCHIVOS DE IMAGENES AL QUE LO QUIERA PROBAR
---

# 😀 JUEGO INVACION ESPACIAL

````python
// Some code

```python
#!P4IgalaxyWar.py

#!modulo pygame para crear jugos, en este caso "invacion espacial"
#?para jugar se debe instalar el modulo pygame con el siguiente comando "pip install pygame"




import pygame                                                    #?1-importamos el modulo pygame
import random                                                    #?usamos el modulo random para adquirir posiciones al azar
import math                                                      #?usamos el modulo math para poder calcular el impacto o colision de disparos contra enemigos
from pygame import mixer                                         #?usamos mixer para añadir audio al juego


pygame.init()                                                    #?1-con pygame + el metodo .init() le damos inicio y digamos ejecucion para que el modulo pygame comience

#1-crear la pantalla
pantalla = pygame.display.set_mode((800, 600))                   #?1-con pygame + el metodo .display creamos la pantalla y mas sobre dispplay el metodo .set_mode(le podemos definir dentro las dimensiones de la pantalla en pixeles)


#2-cambiar el titulo, icono y colores
pygame.display.set_caption("P4IgalaxyWar")                       #?2-definimos el nombre que aparesera en el borde superior de la ventana, llamando a la pantalla con pygame.display mas ahora su metodo .set_caption(y aca dentro su titulo que querramos)
logo = pygame.image.load("pezp4imon.jpg")                        #?2-con el metodo .load cargamos dentro de una variable nuestra imagen de logo que se vera al lado del titulo en el borde superior de la ventana
pygame.display.set_icon(logo)                                    #?2-dentro de display con el metodo .set_icon(ponemos la variable que tiene nuestro logo) para ya poder usarla  


#7-fondo imagen
fondo = pygame.image.load("fondoespacio.png")


#12musica de fondo usando el modulo mixer y sus metodos, con (-1) lo hacemos que se repita el sonido en loop
mixer.music.load("musicafondo.mp3")
mixer.music.play(-1)



#3-jugador principal y 4-movimiento del personaje y 5-movimiento por teclado
img_jugador = pygame.image.load("astronave.png")                 #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
jugador_posicion_x = 368                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
jugador_posicion_y = 536                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
j_x_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
j_y_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas




#10creamos varios meteoritos usando lista para dar mas dinamismo al fondo nomas
img_meteoritos = []                    
meteoritos_posicion_x = []                       
meteoritos_posicion_y = []                      
m_x_cambio = []                                                
m_y_cambio = []                                                  
cantidad_de_meteoritos = 15
for m in range(cantidad_de_meteoritos):
    #6-posicion, etc de Un enemigos, y luego con append agregamos su valores las cantidad de veces de enemigos en la lista
    img_meteoritos.append(pygame.image.load("asteroide.png"))                #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
    meteoritos_posicion_x.append(random.randint(0,736))                      #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
    meteoritos_posicion_y.append(random.randint(50,65))                      #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
    m_x_cambio.append(0.1)                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
    m_y_cambio.append(20) 




#10creamos varios enemigos usando lista
img_enemigo = []                    
enemigo_posicion_x = []                       
enemigo_posicion_y = []                      
e_x_cambio = []                                                
e_y_cambio = []                                                  
cantidad_de_enemigos = 6
for e in range(cantidad_de_enemigos):
    #6-posicion, etc de Un enemigos, y luego con append agregamos su valores las cantidad de veces de enemigos en la lista
    img_enemigo.append(pygame.image.load("enemy2.png"))                    #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
    enemigo_posicion_x.append(random.randint(0,736))                       #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
    enemigo_posicion_y.append(random.randint(50,300))                      #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
    e_x_cambio.append(0.2)                                                 #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
    e_y_cambio.append(30)                                                  #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#8-posicion del disparo 
img_disparo = pygame.image.load("misil.png")
disparo_posicion_x = 0
disparo_posicion_y = 500
d_x_cambio = 0
d_y_cambio = 10
diparo_visible = False

#14mensaje final GAME OVER
gameover = pygame.font.Font("Transcorner.ttf", 60)
historia = pygame.font.Font("Transcorner.ttf", 30)
#14funcion que define el final del juego
def mensaje_final():
    gameoverfinal = gameover.render(f"PERDISTE MANITO", True, (255,255,100))
    historiafinal = historia.render(f"la tierra fue colonizada por alienigenas", True, (255,255,100))
    pantalla.blit(gameoverfinal, (130, 260))
    pantalla.blit(historiafinal, (30, 320))

#9nombre del juego
titulojuego = pygame.font.Font("Begok v15_2015___free.ttf", 32)                #?11con font.Font utilizamos el tipode fuente que qeurramos o las podemos descargar como en este caso
titulojuego_x = 450
titulojuego_y = 10
#11 funcion que muestra el nombre del juego
def titulojuego_pantalla(x, y):
    titulo = titulojuego.render(f"p4Igalaxywar", True, (255,255,100))          #?11con .render procesamos nuestro puntajepantalla para poner el texto que queremos que procese, con la letra ya elejida, tamaño, y aca definimos el color tambien
    pantalla.blit(titulo, (x, y))


#9nombre del creador YO.. aja
creadorjuego = pygame.font.Font("Begok v15_2015___free.ttf", 32)               #?11con font.Font utilizamos el tipode fuente que qeurramos o las podemos descargar como en este caso
creadorjuego_x = 555
creadorjuego_y = 566
#11 funcion que muestra el nombre del juego
def creadorjuego_pantalla(x, y):
    creador = creadorjuego.render(f"by p4im0n", True, (150,255,100))           #?11con .render procesamos nuestro puntajepantalla para poner el texto que queremos que procese, con la letra ya elejida, tamaño, y aca definimos el color tambien
    pantalla.blit(creador, (x, y))


#9puntaje
puntaje = 0
puntajepantalla = pygame.font.Font("QuirkyRobot.ttf", 62)                      #?11con font.Font utilizamos el tipode fuente que qeurramos o las podemos descargar como en este caso
puntaje_pantalla_x = 10
puntaje_pantalla_y = 10
#11 funcion que muestra el puntaje ganado
def puntaje_pantalla(x, y):
    puntos = puntajepantalla.render(f"Puntos: {puntaje}", True, (255,255,100)) #?11con .render procesamos nuestro puntajepantalla para poner el texto que queremos que procese, con la letra ya elejida, tamaño, y aca definimos el color tambien
    pantalla.blit(puntos, (x, y))
    

#3,4-funcion del personaje
def jugador(x,y):                                                              #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_jugador, (x,y))                                          #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn


#15-funcion meteoritos
def meteoritos(x,y, ene):                                                      #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_meteoritos[ene], (x,y))                                  #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn



#6-funcion enemigos
def enemigo(x,y, ene):                                                         #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_enemigo[ene], (x,y))                                     #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn



#8-funcion del disparo
def disparo(x, y):
    global diparo_visible, disparo_posicion_x, disparo_posicion_y                 #?8se las declara a las variables como globales para poder ser usadas en cualquier parte del programa
    if not diparo_visible:                                                        #?8en esta parrte verificamos si el misil no es visible dara true esta condision y se actualizara la posicion del misil al centro de la del jugador y se pondra la variable disparo_visible en True
        disparo_posicion_x = x + 16
        disparo_posicion_y = y + 10
        diparo_visible = True
    if disparo_posicion_y < 0:                                                    #?8aca vemois si el disparo llego al pixel 0 osea si llego a ala parte superior de la pantalla y el disparo_visible pasara a ser False y retomara su posicion original 500
        diparo_visible = False
        disparo_posicion_y = 500
    if diparo_visible:                                                            #?8y si el disparo_visible es True, el mismo aparecera en la pantalla y se ira modificando su posicion en el eje y para arriba de la pantalla
        pantalla.blit(img_disparo, (disparo_posicion_x, disparo_posicion_y))
        disparo_posicion_y -= d_y_cambio


#9funcion para detectar si nuestro disparo dio contra un enemigo
def detectar_muerte_enemiga(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-x_2, 2) + math.pow(y_1-y_2, 2))            #?9una funcion matematica comun para calcular las colisiones o choques entre dos objetos, en nuestro caso entre el misil y el enemigo
    if distancia < 20:                                                            #?9definimos la condision de True solo si se chocan en un radio dentre si de 20px, osea mientras mas chico mas presicion tendremos que tener
        return True
    else:
        return False




se_inicia = True                                                 #?1-creamos una variable con True para manejar luego el loop, si lo transformamos en False

while se_inicia:                                                 #?1-iniciamos while con la variable anterior en True
    #fodo de pantalla imagen
    pantalla.blit(fondo,(0, 0))                                  #?7-con blit agregamos la imagen en posicionde ancho de pùnta a punta 0, y alto de punta en punta con 0
    '''#color de fondo
    pantalla.fill((228,8,15))'''                                 #?2-llamando a nuetra variable que contienn la pantalla mas el metodo .fill((definimos el color de la pantalla en formato RGB)) pero luego tenemos que ejecutarlo o actualizarlo para que se vea 
    #lista de todos los eventos en el loop for
    for evento in pygame.event.get():                            #?1-con for vamos a iterar en cada evento que pases en la ventana de pygame, con pygame.event.get()(toma cualquier evento de pantalla)
        #evento de salir
        if evento.type == pygame.QUIT:                           #?1-damos la condicion que si el tipo de elemento tomado anteriormente en pantalla , es de tipo QUIT (salir), a continuacion pase a darle el valos de False a la variable se_inicia y pare el loop para cerrar el juego
            se_inicia = False
        #movimiento manual de nuestro personaje: presionar tecla
        if evento.type == pygame.KEYDOWN:                        #?5-con el tipo de evento con el metodo .KEYDOWN le decimos que cuando se baje o presiones una tecla   
            if evento.key == pygame.K_RIGHT:                     #?5-que cuando el evento de key osea tecla presionada derecha haga lo siguiente, y asi con cada direccion
                print("derecha")
                j_x_cambio = 2                                   #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a sumar 0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_LEFT:
                print("izquierda")
                j_x_cambio = -2                                  #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a restar -0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_UP:
                print("arriba")
                j_y_cambio = -2
            if evento.key == pygame.K_DOWN:
                print("abajo") 
                j_y_cambio = 2
            if evento.key == pygame.K_SPACE:
                sonido_disparo = mixer.Sound("disparo.mp3")              #?12con mixer. y su metodo .sound añandimos dentro de la variable el sonido del disparo par que se ejecute cada ves que se presiona
                sonido_disparo.play()
                disparo_realizado_x = jugador_posicion_x                 #?8creamos una variable aparte para trabajarla en el loop con las posicion del jugador  con respectos a sus ejes y o x y de esta forma al hacerce el loop el missil no va a depender o copiar la posicion de inicio con respecto a la nave jugador
                disparo_realizado_y = jugador_posicion_y                 #?8creamos una variable aparte para trabajarla en el loop con las posicion del jugador  con respectos a sus ejes y o x y de esta forma al hacerce el loop el missil no va a depender o copiar la posicion de inicio con respecto a la nave jugador
                disparo(jugador_posicion_x, jugador_posicion_y)          #?8disparo relizado desde la posicion x e y de la posicion jugador
        #soltar tecla
        if evento.type == pygame.KEYUP:                                  #?5-con el tipo de evento con el metodo .KEYUP le decimos que cuando suelte una tecla haga lo siguiente
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN or evento.key == pygame.K_SPACE:         #?que cuando suelt la tecla derecha, or o izquierda,etc haga lo siguiente
                print("tecla soltada")
                j_x_cambio = 0                                           #?5-deje de sumar valor de movimiento a los dos ejes y o x
                j_y_cambio = 0                                           #?5-deje de sumar valor de movimiento a los dos ejes y o x
    #actualizacion de la posicion del jugador
    jugador_posicion_y += j_y_cambio                                     #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla 
    jugador_posicion_x += j_x_cambio                                     #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla
    #10actualizacion de la posicion del enemigo
    for e in range(cantidad_de_enemigos):                                #?10creamos este loop foor para que itinere por cada posicion por separado de cada nave enemiga creada en la lista con informacion en el indice [e]
        #14final del juego gameover e historia
        if enemigo_posicion_y[e] > 500:
            for k in range(cantidad_de_enemigos):
                enemigo_posicion_y[k] = 1000
            mensaje_final()
            break    
        enemigo_posicion_y[e] += 0.2
        enemigo_posicion_x[e] += e_x_cambio[e]
        #bloqueo de margenes del enemigo
        if enemigo_posicion_x[e] <= 0:                                   #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 0 (osea la izquierda) la posicion de este cambie la direccion para la derercha 1 
            e_x_cambio[e] = 1                                   
        elif enemigo_posicion_x[e] >= 762:                               #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 736 (osea la derecha) y la posicion de este al llegar a 736 como limite, cambie de direccion para la izquierda a -1 
            e_x_cambio[e] = -1
        elif enemigo_posicion_y[e] <= 0:
            enemigo_posicion_y[e] = 0     
    #10actualizacion de la posicion de los meteoritos
        for m in range(cantidad_de_meteoritos):                          #?10creamos este loop foor para que itinere por cada posicion por separado de cada  meteorito creada en la lista con informacion en el indice [m]
            #14final del juego gameover e historia   
            meteoritos_posicion_y[m] += 0.03 
            meteoritos_posicion_x[m] += m_x_cambio[m]
            #bloqueo de margenes del enemigo
            if meteoritos_posicion_x[m] <= 0:                            #?6-definimos el limite definiendo que si en el eje x la posicion del meteorito es menor o igual a 0 (osea la izquierda) la posicion de este cambie la direccion para la derercha 1 
                m_x_cambio[m] = 1                                   
            elif meteoritos_posicion_x[m] >= 762:                        #?6-definimos el limite definiendo que si en el eje x la posicion del meteorito es menor o igual a 736 (osea la derecha) y la posicion de este al llegar a 736 como limite, cambie de direccion para la izquierda a -1 
                m_x_cambio[m] = -1
            elif meteoritos_posicion_y[m] <= 0:
                meteoritos_posicion_y[m] = 0     
        #9verificamos muerte enemiga y reaparicio
        muerte_enemiga = detectar_muerte_enemiga(enemigo_posicion_x[e],enemigo_posicion_y[e],disparo_posicion_x,disparo_posicion_y)      #?9ejecutamos nuestra funcion en el loop para que valla verificando constatntemengte si nuestro diasparo dio a un enemigo, y si dio con el restablesca las posiciones originales y en false lo visible
        if muerte_enemiga:
            print(muerte_enemiga)
            sonido_explosion = mixer.Sound("explosion.mp3")              #?12con mixer. y su metodo .sound añandimos dentro de la variable el sonido de explosion para que se ejecute cada ves que se da una colision detectando la muerte de un enemigo
            sonido_explosion.play()
            disparo_posicion_y = 500
            disparo_posicion_x = 0
            diparo_visible = False
            puntaje += 100
            enemigo_posicion_x[e] = random.randint(0,736)
            enemigo_posicion_y[e] = random.randint(50,300)
            print(f"Le diste mano: {puntaje} Puntos")
        enemigo(enemigo_posicion_x[e],enemigo_posicion_y[e], e)
        meteoritos(meteoritos_posicion_x[e],meteoritos_posicion_y[e], e)
    #bloqueo de margenes del jugador
    if jugador_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 0 (osea la izquierda) la posicion de este siga siendo 0 como limite
        jugador_posicion_x = 0                                   
    elif jugador_posicion_x >= 736:                              #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 736 (osea la  derecha) la posicion de este siga siendo 736 como limite (y asi sucesivamente con el eje y)
        jugador_posicion_x = 736
    if jugador_posicion_y <= 0:
        jugador_posicion_y = 0
    elif jugador_posicion_y >= 536:
        jugador_posicion_y = 536            
    #trayectoria del disparo separada de movimiento del jugador
    if diparo_visible:
        disparo(disparo_realizado_x, disparo_realizado_y)        #?8aca usamos las variables creadas de la posicion independiente de la del jugador para que no se vean afectadas en el loop con la posicion de nuestro jugador valga la redundancia
        print("disparo")
    jugador(jugador_posicion_x,jugador_posicion_y)               #?3-debemos ejecutar la funcion de nuestro personaje despues de la del color rgb de fondo, por que si no se tapara, y tambien teien que se antes del update de pantalla para que registre cada caambio de movimiento 
    titulojuego_pantalla(titulojuego_x,titulojuego_y)            #?11ejecutamos la funcion para el nombre del juego
    creadorjuego_pantalla(creadorjuego_x,creadorjuego_y)         #?11ejecutamos la funcion que muestra que lo cree  :)
    puntaje_pantalla(puntaje_pantalla_x,puntaje_pantalla_y)      #?11ejecutamos la funcion para que aparesca niuestro puntaje ya procesado como quisimos

    pygame.display.update()                                      #?2-con el metodo .update actualizamos para que tenga efecto el cambio de color y demas




#!fin by P4IM0N
```
````

CODEO DEL DIA 10:

````python
// Some code

```python
#!P4IgalaxyWar.py

#!modulo pygame para crear jugos, en este caso "invacion espacial"
#?para jugar se debe instalar el modulo pygame con el siguiente comando "pip install pygame"




import pygame                                                    #?1-importamos el modulo pygame
import random

pygame.init()                                                    #?1-con pygame + el metodo .init() le damos inicio y digamos ejecucion para que el modulo pygame comience

#1-crear la pantalla
pantalla = pygame.display.set_mode((800, 600))                   #?1-con pygame + el metodo .display creamos la pantalla y mas sobre dispplay el metodo .set_mode(le podemos definir dentro las dimensiones de la pantalla en pixeles)


#2-cambiar el titulo, icono y colores
pygame.display.set_caption("P4IgalaxyWar")                       #?2-definimos el nombre que aparesera en el borde superior de la ventana, llamando a la pantalla con pygame.display mas ahora su metodo .set_caption(y aca dentro su titulo que querramos)
logo = pygame.image.load("pezp4imon.jpg")                        #?2-con el metodo .load cargamos dentro de una variable nuestra imagen de logo que se vera al lado del titulo en el borde superior de la ventana
pygame.display.set_icon(logo)                                    #?2-dentro de display con el metodo .set_icon(ponemos la variable que tiene nuestro logo) para ya poder usarla  


#3-jugador principal y 4-movimiento del personaje y 5-movimiento por teclado
img_jugador = pygame.image.load("astronave.png")                 #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
jugador_posicion_x = 368                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
jugador_posicion_y = 536                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
j_x_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
j_y_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#6-posicion, etc de enemigos
img_enemigo = pygame.image.load("enemy2.png")                    #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
enemigo_posicion_x = random.randint(0,736)                       #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
enemigo_posicion_y = random.randint(50,300)                      #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
e_x_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
e_y_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#3,4-funcion del personaje
def jugador(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_jugador, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn

#6-funcion enemigos
def enemigo(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_enemigo, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn

se_inicia = True                                                 #?1-creamos una variable con True para manejar luego el loop, si lo transformamos en False

while se_inicia:                                                 #?1-iniciamos while con la variable anterior en True
    #color de fondo
    pantalla.fill((228,8,15))                                    #?2-llamando a nuetra variable que contienn la pantalla mas el metodo .fill((definimos el color de la pantalla en formato RGB)) pero luego tenemos que ejecutarlo o actualizarlo para que se vea 
    #lista de todos los eventos en el loop for
    for evento in pygame.event.get():                            #?1-con for vamos a iterar en cada evento que pases en la ventana de pygame, con pygame.event.get()(toma cualquier evento de pantalla)
        #evento de salir
        if evento.type == pygame.QUIT:                           #?1-damos la condicion que si el tipo de elemento tomado anteriormente en pantalla , es de tipo QUIT (salir), a continuacion pase a darle el valos de False a la variable se_inicia y pare el loop para cerrar el juego
            se_inicia = False
        #movimiento manual de nuestro personaje: presionar tecla
        if evento.type == pygame.KEYDOWN:                        #?5-con el tipo de evento con el metodo .KEYDOWN le decimos que cuando se baje o presiones una tecla   
            if evento.key == pygame.K_RIGHT:                     #?5-que cuando el evento de key osea tecla presionada derecha haga lo siguiente, y asi con cada direccion
                print("derecha")
                j_x_cambio = 0.5                                 #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a sumar 0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_LEFT:
                print("izquierda")
                j_x_cambio = -0.5                                #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a restar -0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_UP:
                print("arriba")
                j_y_cambio = -0.5
            if evento.key == pygame.K_DOWN:
                print("abajo") 
                j_y_cambio = 0.5 
        #soltar tecla
        if evento.type == pygame.KEYUP:                          #?5-con el tipo de evento con el metodo .KEYUP le decimos que cuando suelte una tecla haga lo siguiente
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:         #?que cuando suelt la tecla derecha, or o izquierda,etc haga lo siguiente
                print("tecla soltada")
                j_x_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
                j_y_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
    #actualizacion de la posicion del jugador
    jugador_posicion_y += j_y_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla 
    jugador_posicion_x += j_x_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla
    #bloqueo de margenes
    if jugador_posicion_x <= 0:                                  #?definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 0 (osea la izquierda) la posicion de este siga siendo 0 como limite
        jugador_posicion_x = 0                                   
    elif jugador_posicion_x >= 736:                              #?definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 736 (osea la izquierda) la posicion de este siga siendo 736 como limite (y asi sucesivamente con el eje y)
        jugador_posicion_x = 736
    if jugador_posicion_y <= 0:
        jugador_posicion_y = 0
    elif jugador_posicion_y >= 536:
        jugador_posicion_y = 536            
    jugador(jugador_posicion_x,jugador_posicion_y)               #?3-debemos ejecutar la funcion de nuestro personaje despues de la del color rgb de fondo, por que si no se tapara, y tambien teien que se antes del update de pantalla para que registre cada caambio de movimiento 
    enemigo(enemigo_posicion_x,enemigo_posicion_y)
    pygame.display.update()                                      #?2-con el metodo .update actualizamos para que tenga efecto el cambio de color y demas




#cambiar el titulo, icono y colores






























































#!P4IgalaxyWar.py

#!modulo pygame para crear jugos, en este caso "invacion espacial"
#?para jugar se debe instalar el modulo pygame con el siguiente comando "pip install pygame"




import pygame                                                    #?1-importamos el modulo pygame
import random

pygame.init()                                                    #?1-con pygame + el metodo .init() le damos inicio y digamos ejecucion para que el modulo pygame comience

#1-crear la pantalla
pantalla = pygame.display.set_mode((800, 600))                   #?1-con pygame + el metodo .display creamos la pantalla y mas sobre dispplay el metodo .set_mode(le podemos definir dentro las dimensiones de la pantalla en pixeles)


#2-cambiar el titulo, icono y colores
pygame.display.set_caption("P4IgalaxyWar")                       #?2-definimos el nombre que aparesera en el borde superior de la ventana, llamando a la pantalla con pygame.display mas ahora su metodo .set_caption(y aca dentro su titulo que querramos)
logo = pygame.image.load("pezp4imon.jpg")                        #?2-con el metodo .load cargamos dentro de una variable nuestra imagen de logo que se vera al lado del titulo en el borde superior de la ventana
pygame.display.set_icon(logo)                                    #?2-dentro de display con el metodo .set_icon(ponemos la variable que tiene nuestro logo) para ya poder usarla  


#7-fondo imagen
fondo = pygame.image.load("fondoespacio.png")


#3-jugador principal y 4-movimiento del personaje y 5-movimiento por teclado
img_jugador = pygame.image.load("astronave.png")                 #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
jugador_posicion_x = 368                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
jugador_posicion_y = 536                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
j_x_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
j_y_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#6-posicion, etc de enemigos
img_enemigo = pygame.image.load("enemy2.png")                    #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
enemigo_posicion_x = random.randint(0,736)                       #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
enemigo_posicion_y = random.randint(50,300)                      #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
e_x_cambio = 0.3                                                 #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
e_y_cambio = 50                                                  #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#8-posicion del disparo 
img_disparo = pygame.image.load("misil.png")
disparo_posicion_x = 0
disparo_posicion_y = 500
d_x_cambio = 0
d_y_cambio = 1
diparo_visible = False

#3,4-funcion del personaje
def jugador(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_jugador, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn


#6-funcion enemigos
def enemigo(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_enemigo, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn



#8-funcion del disparo
'''def disparo(x, y):
    global diparo_visible, d_y_cambio
    diparo_visible = True
    pantalla.blit(img_disparo, (x + 16, y + d_y_cambio))'''
   

def disparo(x, y):
    global diparo_visible, d_y_cambio
    diparo_visible = True
    pantalla.blit(img_disparo, (x + 16, y + d_y_cambio))
    d_y_cambio = d_y_cambio - 1
    '''if disparo_posicion_y <= 0:
        diparo_visible = False
        d_y_cambio = 1'''




se_inicia = True                                                 #?1-creamos una variable con True para manejar luego el loop, si lo transformamos en False

while se_inicia:                                                 #?1-iniciamos while con la variable anterior en True
    #fodo de pantalla imagen
    pantalla.blit(fondo,(0, 0))                                  #?7-con blit agregamos la imagen en posicionde ancho de pùnta a punta 0, y alto de punta en punta con 0
    '''#color de fondo
    pantalla.fill((228,8,15))'''                                 #?2-llamando a nuetra variable que contienn la pantalla mas el metodo .fill((definimos el color de la pantalla en formato RGB)) pero luego tenemos que ejecutarlo o actualizarlo para que se vea 
    #lista de todos los eventos en el loop for
    for evento in pygame.event.get():                            #?1-con for vamos a iterar en cada evento que pases en la ventana de pygame, con pygame.event.get()(toma cualquier evento de pantalla)
        #evento de salir
        if evento.type == pygame.QUIT:                           #?1-damos la condicion que si el tipo de elemento tomado anteriormente en pantalla , es de tipo QUIT (salir), a continuacion pase a darle el valos de False a la variable se_inicia y pare el loop para cerrar el juego
            se_inicia = False
        #movimiento manual de nuestro personaje: presionar tecla
        if evento.type == pygame.KEYDOWN:                        #?5-con el tipo de evento con el metodo .KEYDOWN le decimos que cuando se baje o presiones una tecla   
            if evento.key == pygame.K_RIGHT:                     #?5-que cuando el evento de key osea tecla presionada derecha haga lo siguiente, y asi con cada direccion
                print("derecha")
                j_x_cambio = 1                                   #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a sumar 0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_LEFT:
                print("izquierda")
                j_x_cambio = -1                                  #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a restar -0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_UP:
                print("arriba")
                j_y_cambio = -1
            if evento.key == pygame.K_DOWN:
                print("abajo") 
                j_y_cambio = 1
            if evento.key == pygame.K_SPACE:
                disparo(jugador_posicion_x, jugador_posicion_y)
                '''if disparo_posicion_y <= -0:
                    diparo_visible = False'''
        d_y_cambio = 1
        #soltar tecla
        if evento.type == pygame.KEYUP:                          #?5-con el tipo de evento con el metodo .KEYUP le decimos que cuando suelte una tecla haga lo siguiente
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN or evento.key == pygame.K_SPACE:         #?que cuando suelt la tecla derecha, or o izquierda,etc haga lo siguiente
                if disparo_posicion_y <= 0:
                    diparo_visible = False
                    disparo_posicion_y = 1
                print("tecla soltada")
                j_x_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
                j_y_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
    #actualizacion de la posicion del jugador
    jugador_posicion_y += j_y_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla 
    jugador_posicion_x += j_x_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla
    #actualizacion de la posicion del enemigo
    enemigo_posicion_y += 0.5
    enemigo_posicion_x += e_x_cambio
    #bloqueo de margenes del jugador
    if jugador_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 0 (osea la izquierda) la posicion de este siga siendo 0 como limite
        jugador_posicion_x = 0                                   
    elif jugador_posicion_x >= 736:                              #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 736 (osea la  derecha) la posicion de este siga siendo 736 como limite (y asi sucesivamente con el eje y)
        jugador_posicion_x = 736
    if jugador_posicion_y <= 0:
        jugador_posicion_y = 0
    elif jugador_posicion_y >= 536:
        jugador_posicion_y = 536 
    #bloqueo de margenes del enemigo
    if enemigo_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 0 (osea la izquierda) la posicion de este cambie la direccion para la derercha 1 
        e_x_cambio = 1                                   
    elif enemigo_posicion_x >= 762:                              #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 736 (osea la derecha) y la posicion de este al llegar a 736 como limite, cambie de direccion para la izquierda a -1 
        e_x_cambio = -1
    elif enemigo_posicion_y <= 0:
        enemigo_posicion_y = 0              
    #recarga del disparo
    '''if disparo_posicion_y <= -64:
        disparo_posicion_y = 500
        diparo_visible = False'''
    #trayectoria del disparo
    if diparo_visible:
        disparo(jugador_posicion_x, jugador_posicion_y)
        print("disparo")
    jugador(jugador_posicion_x,jugador_posicion_y)               #?3-debemos ejecutar la funcion de nuestro personaje despues de la del color rgb de fondo, por que si no se tapara, y tambien teien que se antes del update de pantalla para que registre cada caambio de movimiento 
    enemigo(enemigo_posicion_x,enemigo_posicion_y)
    pygame.display.update()                                      #?2-con el metodo .update actualizamos para que tenga efecto el cambio de color y demas


















































#!P4IgalaxyWar.py

#!modulo pygame para crear jugos, en este caso "invacion espacial"
#?para jugar se debe instalar el modulo pygame con el siguiente comando "pip install pygame"




import pygame                                                    #?1-importamos el modulo pygame
import random

pygame.init()                                                    #?1-con pygame + el metodo .init() le damos inicio y digamos ejecucion para que el modulo pygame comience

#1-crear la pantalla
pantalla = pygame.display.set_mode((800, 600))                   #?1-con pygame + el metodo .display creamos la pantalla y mas sobre dispplay el metodo .set_mode(le podemos definir dentro las dimensiones de la pantalla en pixeles)


#2-cambiar el titulo, icono y colores
pygame.display.set_caption("P4IgalaxyWar")                       #?2-definimos el nombre que aparesera en el borde superior de la ventana, llamando a la pantalla con pygame.display mas ahora su metodo .set_caption(y aca dentro su titulo que querramos)
logo = pygame.image.load("pezp4imon.jpg")                        #?2-con el metodo .load cargamos dentro de una variable nuestra imagen de logo que se vera al lado del titulo en el borde superior de la ventana
pygame.display.set_icon(logo)                                    #?2-dentro de display con el metodo .set_icon(ponemos la variable que tiene nuestro logo) para ya poder usarla  


#7-fondo imagen
fondo = pygame.image.load("fondoespacio.png")


#3-jugador principal y 4-movimiento del personaje y 5-movimiento por teclado
img_jugador = pygame.image.load("astronave.png")                 #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
jugador_posicion_x = 368                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
jugador_posicion_y = 536                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
j_x_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
j_y_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#6-posicion, etc de enemigos
img_enemigo = pygame.image.load("enemy2.png")                    #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
enemigo_posicion_x = random.randint(0,736)                       #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
enemigo_posicion_y = random.randint(50,300)                      #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
e_x_cambio = 0.3                                                 #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
e_y_cambio = 50                                                  #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#8-posicion del disparo 
img_disparo = pygame.image.load("misil.png")
disparo_posicion_x = 0
disparo_posicion_y = 500
d_x_cambio = 0
d_y_cambio = 1
diparo_visible = False

#3,4-funcion del personaje
def jugador(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_jugador, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn


#6-funcion enemigos
def enemigo(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_enemigo, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn



#8-funcion del disparo
'''def disparo(x, y):
    global diparo_visible, d_y_cambio
    diparo_visible = True
    pantalla.blit(img_disparo, (x + 16, y + d_y_cambio))'''
   

def disparo(x, y):
    global diparo_visible, d_y_cambio, disparo_posicion_y
    diparo_visible = True
    pantalla.blit(img_disparo, (x + 16, y + d_y_cambio))
    d_y_cambio = d_y_cambio - 1
    '''if disparo_posicion_y <= 0:
        diparo_visible = False
        d_y_cambio = 1'''




se_inicia = True                                                 #?1-creamos una variable con True para manejar luego el loop, si lo transformamos en False

while se_inicia:                                                 #?1-iniciamos while con la variable anterior en True
    #fodo de pantalla imagen
    pantalla.blit(fondo,(0, 0))                                  #?7-con blit agregamos la imagen en posicionde ancho de pùnta a punta 0, y alto de punta en punta con 0
    '''#color de fondo
    pantalla.fill((228,8,15))'''                                 #?2-llamando a nuetra variable que contienn la pantalla mas el metodo .fill((definimos el color de la pantalla en formato RGB)) pero luego tenemos que ejecutarlo o actualizarlo para que se vea 
    #lista de todos los eventos en el loop for
    for evento in pygame.event.get():                            #?1-con for vamos a iterar en cada evento que pases en la ventana de pygame, con pygame.event.get()(toma cualquier evento de pantalla)
        #evento de salir
        if evento.type == pygame.QUIT:                           #?1-damos la condicion que si el tipo de elemento tomado anteriormente en pantalla , es de tipo QUIT (salir), a continuacion pase a darle el valos de False a la variable se_inicia y pare el loop para cerrar el juego
            se_inicia = False
        #movimiento manual de nuestro personaje: presionar tecla
        if evento.type == pygame.KEYDOWN:                        #?5-con el tipo de evento con el metodo .KEYDOWN le decimos que cuando se baje o presiones una tecla   
            if evento.key == pygame.K_RIGHT:                     #?5-que cuando el evento de key osea tecla presionada derecha haga lo siguiente, y asi con cada direccion
                print("derecha")
                j_x_cambio = 1                                   #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a sumar 0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_LEFT:
                print("izquierda")
                j_x_cambio = -1                                  #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a restar -0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_UP:
                print("arriba")
                j_y_cambio = -1
            if evento.key == pygame.K_DOWN:
                print("abajo") 
                j_y_cambio = 1
            if evento.key == pygame.K_SPACE:
                disparo(jugador_posicion_x, jugador_posicion_y)
        #soltar tecla
        if evento.type == pygame.KEYUP:                          #?5-con el tipo de evento con el metodo .KEYUP le decimos que cuando suelte una tecla haga lo siguiente
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN or evento.key == pygame.K_SPACE:         #?que cuando suelt la tecla derecha, or o izquierda,etc haga lo siguiente
                print("tecla soltada")
                j_x_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
                j_y_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
    #actualizacion de la posicion del jugador
    jugador_posicion_y += j_y_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla 
    jugador_posicion_x += j_x_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla
    #actualizacion de la posicion del enemigo
    enemigo_posicion_y += 0.5
    enemigo_posicion_x += e_x_cambio
    #bloqueo de margenes del jugador
    if jugador_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 0 (osea la izquierda) la posicion de este siga siendo 0 como limite
        jugador_posicion_x = 0                                   
    elif jugador_posicion_x >= 736:                              #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 736 (osea la  derecha) la posicion de este siga siendo 736 como limite (y asi sucesivamente con el eje y)
        jugador_posicion_x = 736
    if jugador_posicion_y <= 0:
        jugador_posicion_y = 0
    elif jugador_posicion_y >= 536:
        jugador_posicion_y = 536 
    #bloqueo de margenes del enemigo
    if enemigo_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 0 (osea la izquierda) la posicion de este cambie la direccion para la derercha 1 
        e_x_cambio = 1                                   
    elif enemigo_posicion_x >= 762:                              #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 736 (osea la derecha) y la posicion de este al llegar a 736 como limite, cambie de direccion para la izquierda a -1 
        e_x_cambio = -1
    elif enemigo_posicion_y <= 0:
        enemigo_posicion_y = 0              
    #recarga del disparo
    if disparo_posicion_y <= -64:
        disparo_posicion_y = 500
        diparo_visible = False
    #trayectoria del disparo
    if diparo_visible:
        disparo(jugador_posicion_x, jugador_posicion_y)
        print("disparo")
    jugador(jugador_posicion_x,jugador_posicion_y)               #?3-debemos ejecutar la funcion de nuestro personaje despues de la del color rgb de fondo, por que si no se tapara, y tambien teien que se antes del update de pantalla para que registre cada caambio de movimiento 
    enemigo(enemigo_posicion_x,enemigo_posicion_y)
    pygame.display.update()                                      #?2-con el metodo .update actualizamos para que tenga efecto el cambio de color y demas






































#!P4IgalaxyWar.py

#!modulo pygame para crear jugos, en este caso "invacion espacial"
#?para jugar se debe instalar el modulo pygame con el siguiente comando "pip install pygame"




import pygame                                                    #?1-importamos el modulo pygame
import random

pygame.init()                                                    #?1-con pygame + el metodo .init() le damos inicio y digamos ejecucion para que el modulo pygame comience

#1-crear la pantalla
pantalla = pygame.display.set_mode((800, 600))                   #?1-con pygame + el metodo .display creamos la pantalla y mas sobre dispplay el metodo .set_mode(le podemos definir dentro las dimensiones de la pantalla en pixeles)


#2-cambiar el titulo, icono y colores
pygame.display.set_caption("P4IgalaxyWar")                       #?2-definimos el nombre que aparesera en el borde superior de la ventana, llamando a la pantalla con pygame.display mas ahora su metodo .set_caption(y aca dentro su titulo que querramos)
logo = pygame.image.load("pezp4imon.jpg")                        #?2-con el metodo .load cargamos dentro de una variable nuestra imagen de logo que se vera al lado del titulo en el borde superior de la ventana
pygame.display.set_icon(logo)                                    #?2-dentro de display con el metodo .set_icon(ponemos la variable que tiene nuestro logo) para ya poder usarla  


#7-fondo imagen
fondo = pygame.image.load("fondoespacio.png")


#3-jugador principal y 4-movimiento del personaje y 5-movimiento por teclado
img_jugador = pygame.image.load("astronave.png")                 #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
jugador_posicion_x = 368                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
jugador_posicion_y = 536                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
j_x_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
j_y_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#6-posicion, etc de enemigos
img_enemigo = pygame.image.load("enemy2.png")                    #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
enemigo_posicion_x = random.randint(0,736)                       #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
enemigo_posicion_y = random.randint(50,300)                      #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
e_x_cambio = 0.3                                                 #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
e_y_cambio = 50                                                  #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#8-posicion del disparo 
img_disparo = pygame.image.load("misil.png")
disparo_posicion_x = 0
disparo_posicion_y = 500
d_x_cambio = 0
d_y_cambio = 1
diparo_visible = False

#3,4-funcion del personaje
def jugador(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_jugador, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn


#6-funcion enemigos
def enemigo(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_enemigo, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn



#8-funcion del disparo
def disparo(x, y):                                                   #!ver estooooo, solucione poder disparar mas veces
    global diparo_visible, d_y_cambio, disparo_posicion_y
    diparo_visible = True
    pantalla.blit(img_disparo, (x + 16,  y + d_y_cambio))
    d_y_cambio = d_y_cambio - 1
    if d_y_cambio <= -572:
        '''disparo_posicion_y = 500'''
        diparo_visible = False
        disparo_posicion_y = 500
        d_y_cambio = 1



se_inicia = True                                                 #?1-creamos una variable con True para manejar luego el loop, si lo transformamos en False

while se_inicia:                                                 #?1-iniciamos while con la variable anterior en True
    #fodo de pantalla imagen
    pantalla.blit(fondo,(0, 0))                                  #?7-con blit agregamos la imagen en posicionde ancho de pùnta a punta 0, y alto de punta en punta con 0
    '''#color de fondo
    pantalla.fill((228,8,15))'''                                 #?2-llamando a nuetra variable que contienn la pantalla mas el metodo .fill((definimos el color de la pantalla en formato RGB)) pero luego tenemos que ejecutarlo o actualizarlo para que se vea 
    #lista de todos los eventos en el loop for
    for evento in pygame.event.get():                            #?1-con for vamos a iterar en cada evento que pases en la ventana de pygame, con pygame.event.get()(toma cualquier evento de pantalla)
        #evento de salir
        if evento.type == pygame.QUIT:                           #?1-damos la condicion que si el tipo de elemento tomado anteriormente en pantalla , es de tipo QUIT (salir), a continuacion pase a darle el valos de False a la variable se_inicia y pare el loop para cerrar el juego
            se_inicia = False
        #movimiento manual de nuestro personaje: presionar tecla
        if evento.type == pygame.KEYDOWN:                        #?5-con el tipo de evento con el metodo .KEYDOWN le decimos que cuando se baje o presiones una tecla   
            if evento.key == pygame.K_RIGHT:                     #?5-que cuando el evento de key osea tecla presionada derecha haga lo siguiente, y asi con cada direccion
                print("derecha")
                j_x_cambio = 1                                   #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a sumar 0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_LEFT:
                print("izquierda")
                j_x_cambio = -1                                  #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a restar -0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_UP:
                print("arriba")
                j_y_cambio = -1
            if evento.key == pygame.K_DOWN:
                print("abajo") 
                j_y_cambio = 1
            if evento.key == pygame.K_SPACE:
                disparo(jugador_posicion_x, jugador_posicion_y)
        #soltar tecla
        if evento.type == pygame.KEYUP:                          #?5-con el tipo de evento con el metodo .KEYUP le decimos que cuando suelte una tecla haga lo siguiente
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN or evento.key == pygame.K_SPACE:         #?que cuando suelt la tecla derecha, or o izquierda,etc haga lo siguiente
                print("tecla soltada")
                j_x_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
                j_y_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
    #actualizacion de la posicion del jugador
    jugador_posicion_y += j_y_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla 
    jugador_posicion_x += j_x_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla
    #actualizacion de la posicion del enemigo
    enemigo_posicion_y += 0.5
    enemigo_posicion_x += e_x_cambio
    #bloqueo de margenes del jugador
    if jugador_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 0 (osea la izquierda) la posicion de este siga siendo 0 como limite
        jugador_posicion_x = 0                                   
    elif jugador_posicion_x >= 736:                              #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 736 (osea la  derecha) la posicion de este siga siendo 736 como limite (y asi sucesivamente con el eje y)
        jugador_posicion_x = 736
    if jugador_posicion_y <= 0:
        jugador_posicion_y = 0
    elif jugador_posicion_y >= 536:
        jugador_posicion_y = 536 
    #bloqueo de margenes del enemigo
    if enemigo_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 0 (osea la izquierda) la posicion de este cambie la direccion para la derercha 1 
        e_x_cambio = 1                                   
    elif enemigo_posicion_x >= 762:                              #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 736 (osea la derecha) y la posicion de este al llegar a 736 como limite, cambie de direccion para la izquierda a -1 
        e_x_cambio = -1
    elif enemigo_posicion_y <= 0:
        enemigo_posicion_y = 0              
    #recarga del disparo
    '''elif jugador_posicion_y <= 0:
        disparo_posicion_y = 500
        diparo_visible = False'''
    #trayectoria del disparo
    if diparo_visible:
        disparo(jugador_posicion_x, jugador_posicion_y)
        print("disparo")
    '''if jugador_posicion_y <= 0:
        disparo_posicion_y = 500
        diparo_visible = False '''
          
    jugador(jugador_posicion_x,jugador_posicion_y)               #?3-debemos ejecutar la funcion de nuestro personaje despues de la del color rgb de fondo, por que si no se tapara, y tambien teien que se antes del update de pantalla para que registre cada caambio de movimiento 
    enemigo(enemigo_posicion_x,enemigo_posicion_y)
    pygame.display.update()                                      #?2-con el metodo .update actualizamos para que tenga efecto el cambio de color y demas























































#!P4IgalaxyWar.py

#!modulo pygame para crear jugos, en este caso "invacion espacial"
#?para jugar se debe instalar el modulo pygame con el siguiente comando "pip install pygame"




import pygame                                                    #?1-importamos el modulo pygame
import random
import math

pygame.init()                                                    #?1-con pygame + el metodo .init() le damos inicio y digamos ejecucion para que el modulo pygame comience

#1-crear la pantalla
pantalla = pygame.display.set_mode((800, 600))                   #?1-con pygame + el metodo .display creamos la pantalla y mas sobre dispplay el metodo .set_mode(le podemos definir dentro las dimensiones de la pantalla en pixeles)


#2-cambiar el titulo, icono y colores
pygame.display.set_caption("P4IgalaxyWar")                       #?2-definimos el nombre que aparesera en el borde superior de la ventana, llamando a la pantalla con pygame.display mas ahora su metodo .set_caption(y aca dentro su titulo que querramos)
logo = pygame.image.load("pezp4imon.jpg")                        #?2-con el metodo .load cargamos dentro de una variable nuestra imagen de logo que se vera al lado del titulo en el borde superior de la ventana
pygame.display.set_icon(logo)                                    #?2-dentro de display con el metodo .set_icon(ponemos la variable que tiene nuestro logo) para ya poder usarla  


#7-fondo imagen
fondo = pygame.image.load("fondoespacio.png")


#3-jugador principal y 4-movimiento del personaje y 5-movimiento por teclado
img_jugador = pygame.image.load("astronave.png")                 #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
jugador_posicion_x = 368                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
jugador_posicion_y = 536                                         #?3-creamos dos variables para guardar la posicion de nuestro jugador con respecto a los pixeles de los ejes x , y
j_x_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
j_y_cambio = 0                                                   #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#6-posicion, etc de enemigos
img_enemigo = pygame.image.load("enemy2.png")                    #?3-igual que con el logo calrgamos la imagen que usaremos para nuestro personaje
enemigo_posicion_x = random.randint(0,736)                       #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
enemigo_posicion_y = random.randint(50,300)                      #?3-creamos dos variables para guardar la posicion de nuestro enemigo con respecto a los pixeles de los ejes x , y (y le damos con randomy elñ metodo .randint una posicion aleatoria)
e_x_cambio = 0.3                                                 #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas                                       
e_y_cambio = 50                                                  #?5-creamos una variable para x o y la cual estara en 0 de inicio y guardara cada valor sumado o restado por cada pusacion de teclas


#8-posicion del disparo 
img_disparo = pygame.image.load("misil.png")
disparo_posicion_x = 0
disparo_posicion_y = 500
d_x_cambio = 0
d_y_cambio = 10
diparo_visible = False


#puntaje
puntaje = 0


#3,4-funcion del personaje
def jugador(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_jugador, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn


#6-funcion enemigos
def enemigo(x,y):                                                #?4-definimos parametros para nuestra funcion, los cuales seran alimentados a posterior para poder darle propiedades de movimiento
    pantalla.blit(img_enemigo, (x,y))                            #?3-funcion, para poner nuestro jugador en pantalla, y con el metodo .blit(imagen de nuestro jugador, (mas su posicion)) le decimos que lo agregue y dentr podn



#8-funcion del disparo
'''def disparo(x, y):                                                   #!ver estooooo, solucione poder disparar mas veces
    global diparo_visible, d_y_cambio, disparo_posicion_y
    diparo_visible = True
    pantalla.blit(img_disparo, (x + 16,  y + d_y_cambio))
    d_y_cambio = d_y_cambio - 1
    if d_y_cambio <= -572:
        diparo_visible = False
        disparo_posicion_y = 500
        d_y_cambio = 1'''


#8-funcion del disparo
def disparo(x, y):
    global diparo_visible, disparo_posicion_x, disparo_posicion_y                 #?se las declara a las variables como globales para poder ser usadas en cualquier parte del programa
    if not diparo_visible:                                                        #?en esta parrte verificamos si el misil no es visible dara true esta condision y se actualizara la posicion del misil al centro de la del jugador y se pondra la variable disparo_visible en True
        disparo_posicion_x = x + 16
        disparo_posicion_y = y + 10
        diparo_visible = True
    if disparo_posicion_y < 0:                                                    #?aca vemois si el disparo llego al pixel 0 osea si llego a ala parte superior de la pantalla y el disparo_visible pasara a ser False y retomara su posicion original 500
        diparo_visible = False
        disparo_posicion_y = 500
    if diparo_visible:                                                            #?y si el disparo_visible es True, el mismo aparecera en la pantalla y se ira modificando su posicion en el eje y para arriba de la pantalla
        pantalla.blit(img_disparo, (disparo_posicion_x, disparo_posicion_y))
        disparo_posicion_y -= d_y_cambio


#funcion para detectar si nuestro disparo dio contra un enemigo
def detectar_muerte_enemiga(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1-y_1,2) + math.pow(x_2-y_2,2))       #?una funcion matematica comun para calcular las colisiones o choques entre dos objetos, en nuestro caso entre el misil y el enemigo
    if distancia < 27:
        return True
    else:
        return False




se_inicia = True                                                 #?1-creamos una variable con True para manejar luego el loop, si lo transformamos en False

while se_inicia:                                                 #?1-iniciamos while con la variable anterior en True
    #fodo de pantalla imagen
    pantalla.blit(fondo,(0, 0))                                  #?7-con blit agregamos la imagen en posicionde ancho de pùnta a punta 0, y alto de punta en punta con 0
    '''#color de fondo
    pantalla.fill((228,8,15))'''                                 #?2-llamando a nuetra variable que contienn la pantalla mas el metodo .fill((definimos el color de la pantalla en formato RGB)) pero luego tenemos que ejecutarlo o actualizarlo para que se vea 
    #lista de todos los eventos en el loop for
    for evento in pygame.event.get():                            #?1-con for vamos a iterar en cada evento que pases en la ventana de pygame, con pygame.event.get()(toma cualquier evento de pantalla)
        #evento de salir
        if evento.type == pygame.QUIT:                           #?1-damos la condicion que si el tipo de elemento tomado anteriormente en pantalla , es de tipo QUIT (salir), a continuacion pase a darle el valos de False a la variable se_inicia y pare el loop para cerrar el juego
            se_inicia = False
        #movimiento manual de nuestro personaje: presionar tecla
        if evento.type == pygame.KEYDOWN:                        #?5-con el tipo de evento con el metodo .KEYDOWN le decimos que cuando se baje o presiones una tecla   
            if evento.key == pygame.K_RIGHT:                     #?5-que cuando el evento de key osea tecla presionada derecha haga lo siguiente, y asi con cada direccion
                print("derecha")
                j_x_cambio = 2                                   #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a sumar 0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_LEFT:
                print("izquierda")
                j_x_cambio = -2                                  #?5-la variable antes definida de cambio, le decimos que por cada pulsacion se le va a restar -0.4 para luego en el loop ser sumada al final de la funcion a su posicion inicial y produsca el movimiento para el respectivo lado(y asi sucesivamente)
            if evento.key == pygame.K_UP:
                print("arriba")
                j_y_cambio = -2
            if evento.key == pygame.K_DOWN:
                print("abajo") 
                j_y_cambio = 2
            if evento.key == pygame.K_SPACE:
                disparo_realizado_x = jugador_posicion_x         #?8creamos una variable aparte para trabajarla en el loop con las posicion del jugador  con respectos a sus ejes y o x y de esta forma al hacerce el loop el missil no va a depender o copiar la posicion de inicio con respecto a la nave jugador
                disparo_realizado_y = jugador_posicion_y         #?8creamos una variable aparte para trabajarla en el loop con las posicion del jugador  con respectos a sus ejes y o x y de esta forma al hacerce el loop el missil no va a depender o copiar la posicion de inicio con respecto a la nave jugador
                disparo(jugador_posicion_x, jugador_posicion_y)  #?8disparo relizado desde la posicion x e y de la posicion jugador
        #soltar tecla
        if evento.type == pygame.KEYUP:                          #?5-con el tipo de evento con el metodo .KEYUP le decimos que cuando suelte una tecla haga lo siguiente
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_LEFT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN or evento.key == pygame.K_SPACE:         #?que cuando suelt la tecla derecha, or o izquierda,etc haga lo siguiente
                print("tecla soltada")
                j_x_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
                j_y_cambio = 0                                   #?5-deje de sumar valor de movimiento a los dos ejes y o x
            
    #actualizacion de la posicion del jugador
    jugador_posicion_y += j_y_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla 
    jugador_posicion_x += j_x_cambio                             #?5-al final le decimos que a nuestras variables de posicion inicial de x o y le sume su valor y el valor sumado por cada presion de tecla
    #actualizacion de la posicion del enemigo
    enemigo_posicion_y += 0.5
    enemigo_posicion_x += e_x_cambio
    #bloqueo de margenes del jugador
    if jugador_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 0 (osea la izquierda) la posicion de este siga siendo 0 como limite
        jugador_posicion_x = 0                                   
    elif jugador_posicion_x >= 736:                              #?6-definimos el limite definiendo que si en el eje x la posicion del jugador es menor o igual a 736 (osea la  derecha) la posicion de este siga siendo 736 como limite (y asi sucesivamente con el eje y)
        jugador_posicion_x = 736
    if jugador_posicion_y <= 0:
        jugador_posicion_y = 0
    elif jugador_posicion_y >= 536:
        jugador_posicion_y = 536 
    #bloqueo de margenes del enemigo
    if enemigo_posicion_x <= 0:                                  #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 0 (osea la izquierda) la posicion de este cambie la direccion para la derercha 1 
        e_x_cambio = 1                                   
    elif enemigo_posicion_x >= 762:                              #?6-definimos el limite definiendo que si en el eje x la posicion del enemigo es menor o igual a 736 (osea la derecha) y la posicion de este al llegar a 736 como limite, cambie de direccion para la izquierda a -1 
        e_x_cambio = -1
    elif enemigo_posicion_y <= 0:
        enemigo_posicion_y = 0              
    #trayectoria del disparo separada de movimiento del jugador
    if diparo_visible:
        disparo(disparo_realizado_x, disparo_realizado_y)        #?8aca usamos las variables creadas de la posicion independiente de la del jugador para que no se vean afectadas en el loop con la posicion de nuestro jugador valga la redundancia
        print("disparo")
    muerte_enemiga= detectar_muerte_enemiga(enemigo_posicion_x,enemigo_posicion_y,disparo_posicion_x,disparo_posicion_y)      #?ejecutamos nuestra funcion en el loop para que valla verificando constatntemengte si nuestro diasparo dio a un enemigo, y si dio con el restablesca las posiciones originales y en false lo visible
    if muerte_enemiga:
        disparo_posicion_y = 500
        disparo_posicion_x = 0
        diparo_visible = False
        puntaje += 1
        enemigo_posicion_x = random.randint(0,736)
        enemigo_posicion_y = random.randint(50,300)
        print(puntaje)
          
    jugador(jugador_posicion_x,jugador_posicion_y)               #?3-debemos ejecutar la funcion de nuestro personaje despues de la del color rgb de fondo, por que si no se tapara, y tambien teien que se antes del update de pantalla para que registre cada caambio de movimiento 
    enemigo(enemigo_posicion_x,enemigo_posicion_y)
    pygame.display.update()                                      #?2-con el metodo .update actualizamos para que tenga efecto el cambio de color y demas



```
````
