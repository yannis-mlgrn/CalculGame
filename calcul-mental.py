#!/usr/bin/python3

import pygame,random
 
NOIR = 0,0,0  # initialise la couleur noir
nombre1 = 0 # initialise la variable du premier entier 
nombre2 = 0 # initialise la variable du second entier 


def calculnombres() : # fonction pour calculer un nombre au hazard entre 0 et 100
    return random.randint(0,100) # prend un chiffre au hazard entre 0 et 100

nombre1= calculnombres()
nombre2= calculnombres()


pygame.init() # initialise pygame
screen = pygame.display.set_mode((640, 480)) # definis la taille de la fenêtre
center_x, center_y = 320, 240 # définis les milieux

font = pygame.font.Font(None, 70) # taille du texte
titre = font.render("Jeux de calcul mental",1,(0,0,0)) # variable du texte 
textpos = titre.get_rect() # prend les positions de la fenêtre
textpos.centerx = screen.get_rect().centerx # calcule le centre 

 
font = pygame.font.SysFont(None , 50) # taille & police du texte
addition = font.render(str(nombre1)+" + "+str(nombre2)+" = ",True, NOIR) # variable ou on stocke l'addition
addition_rect = addition.get_rect(center=(center_x, center_y)) # centrer le texte de l'operation
 
user_input_value = "" # initialise la valeur de l'input
user_input = font.render(user_input_value, True, NOIR) # rendu de l'input
user_input_rect = user_input.get_rect(topleft=addition_rect.topright) # mettre l'input juste à droite de l'opération 
 
continuer = True # boolean qui peut servir pour rejouer ou pas 


# GESTION DU CLAVIER
while continuer:

    for event in pygame.event.get(): # analyse tout les evenements
        if event.type == pygame.QUIT: # si l'utilisateur veut quitter le jeux
            continuer = False # mettre conttinuer a false pour quitter
            break # quitter la boucle actuel
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE : # si on appuie sur la touche suppr
                continuer = False # mettre la variable continuer à False et donc quitter le jeux
            elif event.key == pygame.K_BACKSPACE: # sinon si on appui sur la touche "backspace" (touche habituel pour supprimer du texte)
                user_input_value = user_input_value[:-1] # enlever le dernier caractere de l'input
            elif event.key == pygame.K_RETURN: # sinon si on appui sur la touche entrée 
                reponse = user_input_value # mettre dans une variable la valeur de l'input
                print("reponse  = "+reponse) # afficher le résultat entré
                user_input_value = "" # initialise la valeur de l'input
                if (nombre1 + nombre2 ) == int(reponse) :
                    print("VRAI")
                else:
                    print("faux")
                
                nombre1 = calculnombres()
                nombre2 = calculnombres()
                addition = font.render(str(nombre1)+" + "+str(nombre2)+" = ",True, NOIR) # variable ou on stocke l'addition
                addition_rect = addition.get_rect(center=(center_x, center_y)) # centrer le texte de l'operation
                screen.blit(addition, addition_rect) # rendu de addition 
                
            else:
                user_input_value += event.unicode
            user_input = font.render(user_input_value, True, NOIR) # rendu de l'input, mettre son texte en noir
            user_input_rect = user_input.get_rect(topleft=addition_rect.topright) # placé l'input ujste a droite du texte de l'opperation
            screen.fill((0,0,0)) # set en blac
            pygame.display.flip() # update l'écran
            break
 
    
    # RENDU DES ELEMENTS 
    screen.fill("#FFFFFF") # couleur du fond
    screen.blit(addition, addition_rect) # rendu de addition 
    screen.blit(user_input, user_input_rect) # rendu de l'input 
    screen.blit(titre, textpos) # fait le rendu du texte au centre 
    pygame.display.flip()
 
print("le résultat:", int(user_input_value)) # afficher le resultat
 
pygame.quit() # quitter pygame 