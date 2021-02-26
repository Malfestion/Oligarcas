import pygame
import sys
from Tablero import Tablero
import Opciones
from pygame.locals import *
import tkinter as tk
import tkinter.scrolledtext as st
win = tk.Tk()
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
W = win.winfo_screenwidth()
H = win.winfo_screenheight()
win.destroy()
tablero=Tablero()
def init():
    tablero.init_data()
    tablero.init_negocios()
    tablero.init_propiedades()
def input_box():
    screen = pygame.display.set_mode((W, H))
    font = pygame.font.SysFont('arial', 40)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(W / 2,H / 4, 140, 44)
    color_inactive = pygame.Color('white')
    color_active = pygame.Color('red')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        
                        print(text)
                        try:
                            Opciones.cantidad_jugadores=int(text)
                            done=True
                        except:
                            print(text)
                            text=''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        bg = pygame.image.load("./../media/menu/bg.jpg")
        screen.blit(bg,(0,0))
        Font = pygame.font.SysFont('arial', 40)
        title = Font.render('Ingrese la cantidad de jugadores:',True,color)
        text_rect = title.get_rect()
        text_rect.center = (W / 3,H / 5)
        screen.blit(title, text_rect)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


def game():
    input_box()
    tablero.run_game()

def reglas():
    win=tk.Tk()
    rule_text="""
    1-Oligarca es el juego del dinero. Comprarás propiedades, contruirás comercios y condominios, comprarás empresas y 
    harás lo que sea para conseguir tu objetivo: hacerte con todo el dinero. Si crees que puedes convertirte en el gran
    oligarca dominante, si deseas probar tu suerte y tus habilidades, juega Oligarca con tu amigos y así sabrás quien de 
    todos merece ser el único oligarca.
    2-Como todo juego de mesa de comprar propiedades, Oligarca se juega con fichas en un recorrido de casillas, y será la 
    suerte de un par de dados de seis caras lo que decida que casilla podrá ocupar tu ficha. Este juego está basado en
    cantones y empresas de Costa Rica. Podrás comprar propiedades y empresas, y con tu dinero podrás decidir si quieres
    invertir en un comercio o en un condominio. 
    3-En oligarga están representados algunos de los cantones más desarrollados de cada provincia de Costa Rica. Entre más
    población tiene cada provincia, más cantones posee en el juego. Limón, la provincia menos poblada de Costa Rica cuenta
    con solo 3 cantones. San José, la provincia más poblada de Costa Rica cuenta con 10 cantones. Las propiedades de cada 
    provincia están distinguidas por un color.

    El Inicio de Juego: 
    4-Al iniciar el juego debe repartirse 40 000 colones entre todos los jugadores. Debe repartirse igual
    cantidad de dinero entre todos los jugadores.
    5-Todos los jugadores deben lanzar los dados. El primero en lanzar los dados será el jugador que logre un número mayor. 
    El orden de los demás jugadores se definirá del primero a la derecha, formando un circulo entre todos los jugadores que formen
    parte del juego.
    6-La primera vuelta del recorrido será solo para definir cuáles jugadores tendrán el privilegio de comprar primero. Durante 
    esta vuelta no se podrá comprar propiedades o empresas, no se podrá tomar tarjetas de "Mal Negocio" o "Buen Negocio", ni 
    tampoco se podrá ganar la loteria.
    7-Después de haber dado la primer vuelta al recorrido, los jugadores podrán comprar las propiedades que su ficha visite. 
    Cada vez que caes enuna propiedad, podrás comprarla o podrás subastarla entre los demás jugadores. El precio inicial debe ser
    el precio indicado en el tablero.

    Buen Negocio y Mal Negocio
    8-Tu camino al dinero está lleno de jiro inesperados y contratiempos. Cada vez que tu ficha caiga en un Mal Negocio, deberás
    leer una tarjeta de Mal Negocio y atenerte a pagar la factura de tu desdicha. Pero si tu ficha llega a visitar un Buen Negocio,
    podrás tomar una tarjeta de Buen Negocio y recibir algo que de seguro será bueno.
    9-Cada vez que un jugador visite un Buen Negocio o Mal Negocio, deberá pagar 100 colones al fondo de la loteria. El fondo de 
    loteria está en en centro del juego. La persona que caiga en la casilla Loteria ganará el dinero que este acumulado en el fondo
    de la Loteria.

    Calificación de las Propiedades
    10- Las 45 casillas están calificadas según su nivel de rentabilidad en A, B, C y D. Las 5 empresas de nivel A pagan el 150%
    de la inversión. Hay 2 medios de comunicación rango A que no reintegran la inversión, pero su beneficio es otro (Leer Medios de 
    Cominucación) Las propiedades rango B también pagan el 150%, de la inversión. Las propiedades rango C pagan un 100%, de la
    inversión y las propiedades rango D pagan solo un 50%, de la inversión.
    11-Cuando compres una propiedad recibirás un cartón donde se te indicará cuanto cuesta un comercio o un condominio. Solo puedes
    construir un comercio o un condominio. Una vez que tengas construido un comercio o un comdominio, no podrás demoler para vender
    el edificio o para construiri otra cosa. Piensa con cuidado si quieres comercio o condominio. Los condominios pagan más que los
    comercios, pero también cuestan más.

    Los Medios de Comunicación:
    12-Si compras un medio de comunicación, podrás librarte de los Mal Negocio, pero igual pagarás los 100 colones al fondo de la
    loteria. Si controlas los dos medios de comunicación tendrás un poder muy especial: podrás tomar una tarjeta de Mal Negocio 
    (cuando tu ficha cae en Mal Negocio), podrás leerla y podrás hacer una de las dos siguientes cosas:
        A-Podrás decidir a que jugador le tocará recibir ese Mal Negocio.
        B-Podras chantagear a otro jugador, para que te pague una cantidad convinida y así motivarte a desechar la tarjeta de Mal 
        Negocio que tienes para usas como arma.

    La Loteria:
    13-El jugador que cae en loteria se gana el fondo de la loteria. Deberán colocarse 2000 colones siempre en el fondo de la 
    loteria más 100 colones cada vez que se cae el buen negocio o mal negocio.

    El Dominio de Provincia:
    14-Cuando un jugador posee la mitad o más de las propiedades de una misma provincia, este jugador tiene dominio sobre esta 
    provincia. Tener dominio obre una provincia te la los siguientes poderes:
        A-Puedes comprar todas las propiedades de esta provincia, aunque tu ficha no visite ese lugar. Si otro jugador posea una o
        más propiedades de esa provincia, podrás exigir que te venda esa propiedad el ese jugador no se podrá negar. Deberas pagarle
        la misma cantidad que el/ella pagó por propiedad y contrucción. (Según el pricio del juego y no uno convenido con otro 
        jugador)
        B-Puede permitir que otro jugador compre alguna de las propiedades de esa provincia, negociando algún beneficio.        

    Cómo Ganar:
    14-El ganador será el primero jugador que cumpla una de las siguientes condiciones:
        A-El primer jugador en poseer 18 titulos de propiedad (La Mitad de todas los propiedades)
        B-El primero jugador en Dominar 3 de las 5 empresas (Los Medios de Comunicación no son empresas)
        C-El Primer jugador en dominar 4 de las 7 provincias de Costa Rica.
        D-El primer jugador en dominar 3 de las 4 provincias centrales de Costa Rica. (Las provincias centrales son la cuarta, quinta,
        sexta y séptima; que corresponden a Heredia, Cartago, Alajuela y San José respectivamente.)

    
    """
    # Creating tkinter window 
    win.title("Como Jugar") 
    
    # Title Label 
    tk.Label(win,  
            text = "Como Jugar",  
            font = ("Times New Roman", 15),  
            background = 'green',  
            foreground = "white").grid(column = 0, 
                                        row = 0) 
    
    # Creating scrolled text area 
    # widget with Read only by 
    # disabling the state 
    text_area = st.ScrolledText(win, 
                                width = 150,  
                                height = 35,  
                                font = ("Times New Roman", 
                                        15)) 
    
    text_area.grid(column = 0, pady = 10, padx = 10) 
    
    # Inserting Text which is read only 
    text_area.insert(tk.INSERT,rule_text) 
    
    # Making the text read only 
    text_area.configure(state ='disabled') 
    win.mainloop() 
    menu()
    

def creditos():
    mainClock = pygame.time.Clock()
    all_fonts = pygame.font.get_fonts()
    Font = pygame.font.SysFont('arial', 20)
    Surface = pygame.display.set_mode((W,H), 0, 32) 
    pygame.display.set_caption('Oligarcas')

    bg = pygame.image.load("./../media/menu/bg.jpg")
    logo = pygame.image.load('./../media/menu/logo.png')
    cred = True
    mouse_pos = (0,0)
    mouse_click = (0,0)
    text3_bool = False
    output = ''
    while cred == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_click = event.pos  

        Surface.fill(BLACK)
        Surface.blit(bg, (0, 0))
        Surface.blit(logo,(-310,0))
        color = WHITE
        Font = pygame.font.SysFont('arial', 40)


        text = Font.render('Propiedad Intelectual ....... Luis Aguilar Lobo',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 1.5,H / 5)
        Surface.blit(text, text_rect)

        color = WHITE
        
        Font = pygame.font.SysFont('arial', 40)
        text = Font.render('Desarrollador ....... Alejandro Duarte Lobo',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 1.52,H * 2 / 5)
        Surface.blit(text, text_rect)


        color = WHITE
        if text3_bool:
            color = RED
        
        Font = pygame.font.SysFont('arial', 40)
        text = Font.render('Volver',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3 / 5)
        if text_rect.collidepoint(mouse_click):
            break
        if text_rect.collidepoint(mouse_pos):
            text3_bool = True
        else:
            text3_bool = False
        Surface.blit(text, text_rect)

        Font = pygame.font.SysFont('arial', 40)
        text = Font.render(output,True,BLUE)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 4 / 5)
        Surface.blit(text, text_rect)
        pygame.display.flip()
        mainClock.tick(100000)
    menu()


def options():
    mainClock = pygame.time.Clock()
    all_fonts = pygame.font.get_fonts()
    Font = pygame.font.SysFont('arial', 20)
    Surface = pygame.display.set_mode((W,H), 0, 32) 
    pygame.display.set_caption('Oligarcas')

    bg = pygame.image.load("./../media/menu/bg.jpg")
    logo = pygame.image.load('./../media/menu/logo.png')
    opt = True
    mouse_pos = (0,0)
    mouse_click = (0,0)
    text1_bool = False
    text2_bool = False
    text3_bool = False
    output = ''
    while opt == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_click = event.pos  

        Surface.fill(BLACK)
        Surface.blit(bg, (0, 0))
        Surface.blit(logo,(-310,0))
        color = WHITE
        Font = pygame.font.SysFont('arial', 40)

        if text1_bool:
            color = RED
        text = Font.render('Opcion1',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H / 5)
        if text_rect.collidepoint(mouse_click):
            output = ''     
        if text_rect.collidepoint(mouse_pos):
            text1_bool = True
        else:
            text1_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text2_bool:
            color = RED
        
        Font = pygame.font.SysFont('arial', 40)
        text = Font.render('Opcion2',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 2 / 5)
        if text_rect.collidepoint(mouse_click):
            output = ''
        if text_rect.collidepoint(mouse_pos):
            text2_bool = True
        else:
            text2_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text3_bool:
            color = RED
        
        Font = pygame.font.SysFont('arial', 40)
        text = Font.render('Volver',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3 / 5)
        if text_rect.collidepoint(mouse_click):
            break
        if text_rect.collidepoint(mouse_pos):
            text3_bool = True
        else:
            text3_bool = False
        Surface.blit(text, text_rect)

        Font = pygame.font.SysFont('arial', 40)
        text = Font.render(output,True,BLUE)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 4 / 5)
        Surface.blit(text, text_rect)
        pygame.display.flip()
        mainClock.tick(100000)
    menu()



def menu():
    
    mainClock = pygame.time.Clock()
    all_fonts = pygame.font.get_fonts()
    Font = pygame.font.SysFont('arial', 20)
    Surface = pygame.display.set_mode((W,H), 0, 32) 
    pygame.display.set_caption('Oligarcas')

    bg = pygame.image.load("./../media/menu/bg.jpg")
    logo = pygame.image.load('./../media/menu/logo.png')
    menu = True
    mouse_pos = (0,0)
    mouse_click = (0,0)
    text1_bool = False
    text2_bool = False
    text3_bool = False
    text4_bool = False
    text5_bool = False
    output = ''
    while menu == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
            if event.type == MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == MOUSEBUTTONUP:
                mouse_click = event.pos  

        Surface.fill(BLACK)
        Surface.blit(bg, (0, 0))
        Surface.blit(logo,(-310,0))
        color = WHITE
        Font = pygame.font.SysFont('arial', 40)

        if text1_bool:
            color = RED
        text = Font.render('Jugar',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H / 5)
        if text_rect.collidepoint(mouse_click):
            output = 'Iniciando el juego'
            break
        if text_rect.collidepoint(mouse_pos):
            text1_bool = True
        else:
            text1_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text2_bool:
            color = RED

        if text2_bool:
            color = RED
        text = Font.render('Como Jugar',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H / 3.4)
        if text_rect.collidepoint(mouse_click):
            output = 'ComoJugar'
            break
        if text_rect.collidepoint(mouse_pos):
            text2_bool = True
        else:
            text2_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text3_bool:
            color = RED
        
        Font = pygame.font.SysFont('arial', 40)
        text = Font.render('Opciones',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 2 / 5)
        if text_rect.collidepoint(mouse_click):
            output = 'Menu de opciones'
            break
        if text_rect.collidepoint(mouse_pos):
            text3_bool = True
        else:
            text3_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text4_bool:
            color = RED
        
        Font = pygame.font.SysFont('arial', 40)
        text = Font.render('Creditos',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 0.5)
        if text_rect.collidepoint(mouse_click):
            output = 'Creditos'
            break
        if text_rect.collidepoint(mouse_pos):
            text4_bool = True
        else:
            text4_bool = False
        Surface.blit(text, text_rect)

        color = WHITE
        if text5_bool:
            color = RED
        
        Font = pygame.font.SysFont('arial', 40)
        text = Font.render('Salir',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3 / 5)
        if text_rect.collidepoint(mouse_click):
            output = 'Saliendo'
            pygame.quit()
            sys.exit(0)
        if text_rect.collidepoint(mouse_pos):
            text5_bool = True
        else:
            text5_bool = False
        Surface.blit(text, text_rect)

        Font = pygame.font.SysFont('arial', 40)
        text = Font.render(output,True,BLUE)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 4 / 5)
        Surface.blit(text, text_rect)
        pygame.display.flip()
        mainClock.tick(100000)
    if output=='Menu de opciones':
        options()
    elif output=='Creditos':
        creditos()
    elif output== 'ComoJugar':
        reglas()
    else:
        game()

def main():
    pygame.init()
    init()
    menu()
 
main()