import pygame
import sys
import Tablero
import Opciones
from pygame.locals import *
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
W = 1920
H = 1080


def input_box():
    screen = pygame.display.set_mode((W, H))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(W / 2,H / 5.4, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
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
    Tablero.run_game()

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
        
        Font = pygame.font.SysFont('arial', 40)
        text = Font.render('Opciones',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 2 / 5)
        if text_rect.collidepoint(mouse_click):
            output = 'Menu de opciones'
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
        text = Font.render('Salir',True,color)
        text_rect = text.get_rect()
        text_rect.center = (W / 2,H * 3 / 5)
        if text_rect.collidepoint(mouse_click):
            output = 'Saliendo'
            pygame.quit()
            sys.exit(0)
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
    if output=='Menu de opciones':
        options()
    else:
        game()

def main():
    pygame.init()
    menu()
 
main()