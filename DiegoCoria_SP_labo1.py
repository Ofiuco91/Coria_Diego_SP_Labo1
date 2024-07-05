import pygame
import json
import colores
from data_carrera_UTN import lista


lista_preguntas=[]
lista_respuesta_a=[]
lista_respuesta_b=[]
lista_respuesta_c=[]
lista_correcta=[]
posicion_personaje = [155,300]
comenzar = False
contador_preguntas = -1
contador_puntaje=0
usuario_ingresado=False
juego_terminado = False
bandera_inicio = False



imagen_logo = pygame.image.load("carreraUTN.png")
imagen_logo = pygame.transform.scale(imagen_logo,(225,150))
imagen_casilleros = pygame.image.load("carreraUTNcasilleros.png")
imagen_casilleros = pygame.transform.scale(imagen_casilleros,(750,200))
imagen_personaje = pygame.image.load("carreraUTNpersonaje.png")
imagen_personaje = pygame.transform.scale(imagen_personaje,(30,50))

for e_lista in lista:  #genero las distintas listas con los datos correspondientes
    lista_preguntas.append(e_lista["pregunta"])
    lista_respuesta_a.append(e_lista["a"])
    lista_respuesta_b.append(e_lista["b"])
    lista_respuesta_c.append(e_lista["c"])
    lista_correcta.append(e_lista["correcta"])

pygame.init()


pantalla= pygame.display.set_mode((800,600))

#defino los textos
fuente= pygame.font.SysFont("Comic Sans",28)
fuente2 = pygame.font.SysFont("Comic Sans",15)
fuente3 = pygame.font.SysFont("Comic Sans",20)
texto_PUNTAJE = fuente3.render(str("PUNTAJE:"),True,colores.RED2)
texto_TIEMPO = fuente3.render(str("TIEMPO:"),True,colores.RED2)
texto_COMENZAR = fuente.render(str("COMENZAR"),True,colores.BLACK)
texto_TERMINAR = fuente.render(str("TERMINAR"),True,colores.BLACK)
texto_puntaje= fuente3.render(str(contador_puntaje),True,colores.COLOR_ROJO)
texto_usuario = fuente.render(str("INGRESE SU NOMBRE:"),True,colores.BLACK)
#timer
timer_segundos = pygame.USEREVENT
#seteo el tiempo
pygame.time.set_timer(timer_segundos,1000) 
segundos = "5"
fin_tiempo = False



ingreso = ""
ingreso_rect = pygame.Rect(210,230,300,40) 

flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get() #creo una lista de eventos
    for evento in lista_eventos:  # se verifica que el usuario no presionó la cruz para cerrar el programa
        if evento.type == pygame.QUIT: 
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos) 
            
            #boton de comenzar
            if (posicion_click [0] > 185 and posicion_click [0] < 385) and (posicion_click [1] > 500 and posicion_click[1]<550)and comenzar == False: 
                bandera_inicio = True #hago una segunda bandera por si el usuario selecciona terminar el juego antes de empezarlo
                comenzar=True
                if contador_preguntas <= (len(lista_preguntas)-1):
                    contador_preguntas += 1
                
                 
            if posicion_personaje[1] < 400:#si estoy en el renglon de arriba
                if (posicion_click [0] > 256 and posicion_click [0] < 391) and (posicion_click [1] > 160 and posicion_click[1]<190)and comenzar ==True:
                    if(lista_correcta[contador_preguntas]=="a"):
                        contador_puntaje = contador_puntaje + 10 
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        if posicion_personaje[0] > 660:#si me encuentro en el ultimo casillero de arriba
                          posicion_personaje[0] = posicion_personaje[0]-65
                          posicion_personaje[1] = posicion_personaje[1] + 100
                        else:
                         posicion_personaje[0] = posicion_personaje[0] + 130
                    else:#si la opcion elegida es incorrecta
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        if posicion_personaje[0] > 275:
                         posicion_personaje[0] = posicion_personaje[0] - 65
                    

                if (posicion_click [0] > 395 and posicion_click [0] < 530) and (posicion_click [1] > 160 and posicion_click[1]<190)and comenzar ==True:
                    if(lista_correcta[contador_preguntas]=="b"):
                        contador_puntaje = contador_puntaje + 10   
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        posicion_personaje[0] = posicion_personaje[0] + 130             
                    else:
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        if posicion_personaje[0] > 275:
                         posicion_personaje[0] = posicion_personaje[0] - 65

                
                if (posicion_click [0] > 531 and posicion_click [0] < 664) and (posicion_click [1] > 160 and posicion_click[1]<190)and comenzar ==True:
                    if(lista_correcta[contador_preguntas]=="c"):
                        contador_puntaje = contador_puntaje + 10 
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        if posicion_personaje[0] > 660:
                         posicion_personaje[0] = posicion_personaje[0] - 130
                         posicion_personaje[1] = posicion_personaje[1] +100
                        else:
                            posicion_personaje[0] = posicion_personaje[0] + 130

                    else:
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        if posicion_personaje[0] > 275:
                         posicion_personaje[0] = posicion_personaje[0] - 65
            if posicion_personaje[1] > 390:#si estoy en el renglon de abajo
                if (posicion_click [0] > 256 and posicion_click [0] < 391) and (posicion_click [1] > 160 and posicion_click[1]<190)and comenzar ==True:
                    if(lista_correcta[contador_preguntas]=="a"):
                        contador_puntaje = contador_puntaje + 10 
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        posicion_personaje[0] = posicion_personaje[0] - 130
                    elif posicion_personaje[0]<660:
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        posicion_personaje[0] = posicion_personaje[0] +65
                    elif posicion_personaje[0] > 660:
                         contador_preguntas = contador_preguntas +1 
                         segundos = "5"
                         posicion_personaje[1] = posicion_personaje[1] - 100
                    

                if (posicion_click [0] > 395 and posicion_click [0] < 530) and (posicion_click [1] > 160 and posicion_click[1]<190)and comenzar ==True:
                    if(lista_correcta[contador_preguntas]=="b"):
                        contador_puntaje = contador_puntaje + 10   
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        posicion_personaje[0] = posicion_personaje[0] - 130             
                    elif posicion_personaje[0]<660:
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        posicion_personaje[0] = posicion_personaje[0] +65
                    elif posicion_personaje[0] > 660:
                         contador_preguntas = contador_preguntas +1 
                         segundos = "5"
                         posicion_personaje[1] = posicion_personaje[1] - 100

                
                if (posicion_click [0] > 531 and posicion_click [0] < 664) and (posicion_click [1] > 160 and posicion_click[1]<190)and comenzar ==True:
                    if(lista_correcta[contador_preguntas]=="c"):
                        contador_puntaje = contador_puntaje + 10 
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        posicion_personaje[0] = posicion_personaje[0] - 130             
                    elif posicion_personaje[0]<660:
                        contador_preguntas = contador_preguntas +1 
                        segundos = "5"
                        posicion_personaje[0] = posicion_personaje[0] +65
                    elif posicion_personaje[0] > 660:
                         contador_preguntas = contador_preguntas +1 
                         segundos = "5"
                         posicion_personaje[1] = posicion_personaje[1] - 100

            #si caigo en el casillero "avanza1"    
            if (posicion_personaje[0]> 535 and posicion_personaje[0]<595) and (posicion_personaje[1] < 400):
                posicion_personaje[0] = posicion_personaje[0] + 65
            #si caigo en el casillero "retrocede1"
            if (posicion_personaje[0]> 400 and posicion_personaje[0]<465) and (posicion_personaje[1] > 390):
                posicion_personaje[0] = posicion_personaje[0] + 65
            

            #hago que el personaje pase al renglon de abajo
            if(posicion_personaje[0]>720) and posicion_personaje[1]<400:
                posicion_personaje[1] = posicion_personaje[1] + 100
                posicion_personaje[0] = posicion_personaje[0] - 65
                
               
            if contador_preguntas < len(lista_preguntas):   
                texto_puntaje= fuente3.render(str(contador_puntaje),True,colores.COLOR_ROJO)
                texto_pregunta=fuente2.render(lista_preguntas[contador_preguntas],True,colores.RED1)#renderizo las opciones para pasarla a imagen
                texto_opcion_a=fuente2.render(lista_respuesta_a[contador_preguntas],True,colores.RED1)
                texto_opcion_b=fuente2.render(lista_respuesta_b[contador_preguntas],True,colores.RED1)
                texto_opcion_c=fuente2.render(lista_respuesta_c[contador_preguntas],True,colores.RED1)
            #si clickeo en TERMINAR
            if  (posicion_click [0] > 410 and posicion_click [0] < 610) and (posicion_click [1] > 500 and posicion_click[1]<550) and bandera_inicio == True :
                    comenzar = False
                    juego_terminado = True
                    pantalla.fill(colores.COLOR_CELESTE)
                    pantalla.blit(texto_usuario,(220,220))
                   
        if evento.type == pygame.USEREVENT:
            if evento.type == timer_segundos:
              if fin_tiempo == False and comenzar == True:

                segundos = int(segundos) - 1 #hago q baje el tiempo
                if int(segundos) == 0:
                  if contador_preguntas < (len(lista_preguntas)-1):
                    fin_tiempo = True #aviso cuando llega el reloj a 0
                    contador_preguntas = contador_preguntas +1
                    segundos = "5"
                    texto_pregunta=fuente2.render(lista_preguntas[contador_preguntas],True,colores.RED1)#renderizo las opciones para pasarla a imagen
                    texto_opcion_a=fuente2.render(lista_respuesta_a[contador_preguntas],True,colores.RED1)
                    texto_opcion_b=fuente2.render(lista_respuesta_b[contador_preguntas],True,colores.RED1)
                    texto_opcion_c=fuente2.render(lista_respuesta_c[contador_preguntas],True,colores.RED1)
                    
                    fin_tiempo = False
                  else:
                      comenzar = False
        
    
        
        texto_segundos = fuente.render(str(segundos),True,colores.RED1) #renderizo segundos
        pantalla.blit(texto_segundos,(100,100))#hago q aparezca en pantalla

        pantalla.fill(colores.BLUE) #genero la pantalla principal
        pygame.draw.rect(pantalla,colores.BROWN,(185,500,200,50)) #creo el rectangulo que va a ser uno de los botones
        pygame.draw.rect(pantalla,colores.BROWN,(410,500,200,50))
        #pantalla de opciones
        pygame.draw.rect(pantalla,colores.AQUAMARINE3,(255,25,410,200))
        #para las opciones
        pygame.draw.rect(pantalla,colores.BLUE4,(256,160,135,30))
        pygame.draw.rect(pantalla,colores.BLUE4,(395,160,135,30))
        pygame.draw.rect(pantalla,colores.BLUE4,(531,160,133,30))
        
        #fundo imagen en la pantalla y pongo el tamaño      
        pantalla.blit(imagen_casilleros,(20,280),)
        pantalla.blit(imagen_logo,(25,25))
        pantalla.blit(imagen_personaje,posicion_personaje)
        pantalla.blit(texto_COMENZAR,(200,510))
        pantalla.blit(texto_TERMINAR,(430,510))
        pantalla.blit(texto_PUNTAJE,(670,90))#la pregunta de arriba
        pantalla.blit(texto_TIEMPO,(670,40))
        pantalla.blit(texto_puntaje,(770,90))

        texto_segundos = fuente3.render(str(segundos),True,colores.RED1) #renderizo segundos

        pantalla.blit(texto_segundos,(760,40))#hago q aparesca en pantalla
        
        
        
        if comenzar == True:
            pantalla.blit(texto_pregunta,(260,35)) 
            pantalla.blit(texto_opcion_a,(260,165))
            pantalla.blit(texto_opcion_b,(395,165))
            pantalla.blit(texto_opcion_c,(530,165))


        
        #si llego a la meta
        if (posicion_personaje[0] < 200) and (posicion_personaje [1] >380):
                juego_terminado = True
                comenzar = False
                pantalla.fill(colores.COLOR_CELESTE)
                pantalla.blit(texto_usuario,(220,220))


       
        if (contador_preguntas == len(lista_preguntas)): #si lo dejo selecciono la ultima respuesta y pasa 
           comenzar = False
          
        # ingreso mi nombre
        if juego_terminado == True and usuario_ingresado == False:
            pantalla.fill(colores.BLUE)
            texto_INGRESO = fuente.render(str("ingrese su nombre y presione enter"),True,colores.BLACK)
            pantalla.blit(texto_INGRESO,(150,160))
            if evento.type == pygame.KEYDOWN: #para que el usuario escriba
                
                if evento.key == pygame.K_BACKSPACE:#es para cuando el usuario toque la tecla de borrar
                    ingreso = ingreso[0:-1]
                elif evento.key == pygame.K_RETURN:  
                     usuario_ingresado = True
                else:
                    ingreso += evento.unicode
                    


            #guardo el usuario y puntaje en un archivo json
            if usuario_ingresado ==True:
                try:
                    with open("puntajes.json", "r") as file:
                        puntajes = json.load(file)
                except FileNotFoundError:
                    puntajes = []

                puntajes.append({"nombre": ingreso, "puntaje": contador_puntaje})
                puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)[:10] #uso sorted para que se ordenen por puntaje
                mejores_puntajes = puntajes[:10] #que solo muestre los mejores 10

                with open("puntajes.json", "w") as file:
                    json.dump(mejores_puntajes, file, indent=4)
        

            
            pygame.draw.rect(pantalla,colores.COLOR_ROJO,ingreso_rect,3) #ingreso el rectangulo del texto de ingreso
            texto_superficie = fuente.render(ingreso,True,colores.BLACK)
            pantalla.blit(texto_superficie,(ingreso_rect.x+5,ingreso_rect.y+1))
            
        
      


        #muestro el ranking
        if juego_terminado == True and usuario_ingresado == True:
                
                with open('puntajes.json', 'r') as archivo:
                  datos = json.load(archivo)
                comenzar = False
                pantalla.fill(colores.CADETBLUE4)
                imagen_personaje = pygame.image.load("carreraUTNpersonaje.png")#la cargo por segunda vez por que si cambio el tamaño directamente queda pixelada
                imagen_personaje = pygame.transform.scale(imagen_personaje,(80,200))
                texto_SALIR = fuente.render(str("SALIR"),True,colores.BLACK)
                texto_PUNTAJE = fuente.render(str("PUNTAJES"),True,colores.RED1)
                
                pygame.draw.rect(pantalla,colores.CADETBLUE1,(550,460,130,80))
                pantalla.blit(texto_SALIR,(570,480))
                pantalla.blit(texto_PUNTAJE,(330,30))
                pantalla.blit(imagen_logo,(25,25))
                pantalla.blit(imagen_personaje,(130,190))
                altura = 70
                for jugadores in datos:
                    texto = f"{jugadores["nombre"]}:  {jugadores["puntaje"]}"
                    texto_superficie = fuente.render(texto, True, colores.COLOR_ROJO)
                    pantalla.blit(texto_superficie, (340, altura))
                    altura += 40  # incremento la cordenada para que aparezca uno arriba del otro
                
                

                
                # presiono salir     
                if (posicion_click [0] > 540 and posicion_click [0] < 680) and (posicion_click [1] > 460 and posicion_click[1]<540):
                        flag_correr = False
               
        
        #si clickeo SALIR
        if (juego_terminado == True) and (posicion_click [0] > 550 and posicion_click [0] < 680) and (posicion_click [1] > 460 and posicion_click[1]<542):
            flag_correr = False
            
        pygame.display.flip() #actualizo la pantalla
        
         

pygame.quit()


