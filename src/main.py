import pygame
import sys
import time
import cairo

from pygame.locals import *
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
W = 1920
H = 1080



def game():
    return 0
def ingame_menu():
    return 0

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