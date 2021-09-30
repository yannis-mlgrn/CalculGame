#!/usr/bin/python3

import pygame,random
 
NOIR = 0,0,0  # initialise la couleur noir
nombre1 = 0 # initialise la variable du premier entier 
nombre2 = 0 # initialise la variable du second entier 

nombre1 = random.randint(0,100) # prend un chiffre au hazard entre 0 et 100
nombre2 = random.randint(0,100)  # prend un chiffre au hazard entre 0 et 100
 
pygame.init() # initialise pygame
screen = pygame.display.set_mode((640, 480)) # definis la taille de la fenêtre
center_x, center_y = 320, 240 # définis les milieux

font = pygame.font.Font(None, 70) # taille du texte
titre = font.render("Jeux de calcul mental",1,(0,0,0)) # variable du texte 
textpos = titre.get_rect() # prend les positions de la fenêtre
textpos.centerx = screen.get_rect().centerx # calcule le centre 

 
clock = pygame.time.Clock() # créé une horloge
font = pygame.font.SysFont(None , 24) 
addition = font.render(str(nombre1)+" + "+str(nombre2)+" = ",True, NOIR)
addition_rect = addition.get_rect(center=(center_x, center_y))
 
user_input_value = ""
user_input = font.render(user_input_value, True, NOIR)
user_input_rect = user_input.get_rect(topleft=addition_rect.topright)
 
continuer = True
 
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                continuer = False
                break
            elif event.key == pygame.K_BACKSPACE:
                reponse = user_input_value
                print("reponse"+str(reponse))
                user_input_value = user_input_value[:-1]
            else:
                user_input_value += event.unicode
            user_input = font.render(user_input_value, True, NOIR)
            user_input_rect = user_input.get_rect(topleft=addition_rect.topright)
 
    clock.tick(30)
 
    screen.fill("#FFFFFF")
    screen.blit(addition, addition_rect)
    screen.blit(user_input, user_input_rect)
    screen.blit(titre, textpos) # fait le rendu du texte au centre 
    pygame.display.flip()
 
print("le résultat:", int(user_input_value))
 
pygame.quit()