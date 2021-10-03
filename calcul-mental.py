#!/usr/bin/python3

###                             LES TOUCHES
# Validé ---> entrée
# supprimer le dernier chiffre entré --> la touche habituel pour supprimer un caratère ( "backspace" )
# quitter ---> echap
###


import pygame,random,time
 
NOIR = 0,0,0  # initialise la couleur noir
VERT = 50,205,50 # initialise la couleur verte
GRIS = 105,105,105 # initialise la couleur verte7
ROUGE = 255,0,0 #initialise la couleur rouge

score = 0 # initialise le score à 0

nombre1 = 0 # initialise la variable du premier entier 
nombre2 = 0 # initialise la variable du second entier 


def calculnombres() : # fonction pour calculer un nombre au hazard entre 0 et 100
    return random.randint(0,100) # prend un chiffre au hazard entre 0 et 100

nombre1= calculnombres() # calcul les nombres de l'opération 
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

fontlog = pygame.font.SysFont(None , 25) # taille & police du texte
result = fontlog.render("clique sur le touche 'entrée' pour validé ou la touche 'echap' pour quitter",True, GRIS) #texte en dessous de l'operation qui vas montrer au joueur si il a gagné ou pas 
result_rect = addition.get_rect(center=(82, 350)) # centrer le texte de l'operation

fontscore = pygame.font.SysFont(None , 25) # taille & police du texte
texteScore = fontscore.render("SCORE : "+str(score),True, ROUGE) #texte en dessous de l'operation qui vas montrer au joueur si il a gagné ou pas 
score_rect = addition.get_rect(center=(550, 100)) # centrer le texte de l'operation
 
continuer = True # boolean qui peut servir pour rejouer ou pas 


# GESTION DU CLAVIER
while continuer:

    for event in pygame.event.get(): # analyse tout les evenements
        if event.type == pygame.QUIT: # si l'utilisateur veut quitter le jeux
            continuer = False # mettre conttinuer a false pour quitter
            break # quitter la boucle actuel
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE : # si on appuie sur la touche suppr

                # message quand le joeur a quitté le jeux pour lui montrer son score ... 
                print('''
                     ____  ____  _     ____  _     _       _      _____ _      _____  ____  _      
                    /   _\/  _ \/ \   /   _\/ \ /\/ \     / \__/|/  __// \  /|/__ __\/  _ \/ \     
                    |  /  | / \|| |   |  /  | | ||| |     | |\/|||  \  | |\ ||  / \  | / \|| |     
                    |  \_ | |-||| |_/\|  \_ | \_/|| |_/\  | |  |||  /_ | | \||  | |  | |-||| |_/\  
                    \____/\_/ \|\____/\____/\____/\____/  \_/  \|\____\\_/  \|  \_/  \_/ \|\____/

                                                SCORE : %1d
                                                                                    
                '''%(int(score)))
                continuer = False # mettre la variable continuer à False et donc quitter le jeux
            elif event.key == pygame.K_BACKSPACE: # sinon si on appui sur la touche "backspace" (touche habituel pour supprimer du texte)
                user_input_value = user_input_value[:-1] # enlever le dernier caractere de l'input
            elif event.key == pygame.K_RETURN: # sinon si on appui sur la touche entrée 
                reponse = user_input_value # mettre dans une variable la valeur de l'input
                print("reponse  = "+reponse) # afficher le résultat entré
                if (nombre1 + nombre2 ) == int(reponse) :
                    print("vrai") # log 
                    result = fontlog.render("Bravo tu as gagné",True, VERT) # change le texte en dessous de l'operation par un message pour dire que le joueur a trouve la bonne solution 
                    result_rect = addition.get_rect(center=(320, 350)) # centrer le texte de l'operation
                    screen.blit(result, result_rect) # rendu du message
                    score = score + 15 # ajoute 15 au score ( 1 bonne réponse = 15 )
                    texteScore = fontscore.render("SCORE : "+str(score),True, ROUGE) #texte en dessous de l'operation qui vas montrer au joueur si il a gagné ou pas 
                    screen.blit(texteScore, score_rect) # rendu de addition 
                    print("score ="+str(score)) # log score
                else:
                    print("Faux") #log
                    result = fontlog.render("Perdu, reéssaye !! ",True, ROUGE) # change le texte en dessous de l'operation si le joeur n'a pas bon 
                    result_rect = addition.get_rect(center=(320, 350)) # centrer le texte de l'operation
                    screen.blit(result, result_rect) # rendu du message
                    score = score - 5 # retire 5 au score ( 1 mauvaise réponse = -5 )
                    texteScore = fontscore.render("SCORE : "+str(score),True, ROUGE) #texte en dessous de l'operation qui vas montrer au joueur si il a gagné ou pas 
                    screen.blit(texteScore, score_rect) # rendu de addition 
                    print("score ="+str(score )) # log du score
                user_input_value = "" # initialise la valeur de l'input           
                nombre1 = calculnombres() # calcul nombre 1
                nombre2 = calculnombres() # calcul nombre 2
                addition = font.render(str(nombre1)+" + "+str(nombre2)+" = ",True, NOIR) # variable ou on stocke l'addition
                screen.blit(addition, addition_rect) # rendu de addition 


                
            else:
                user_input_value += event.unicode
            font = pygame.font.SysFont(None , 50) # remet la police a la taille 50 
            user_input = font.render(user_input_value, True, NOIR) # rendu de l'input, mettre son texte en noir
            user_input_rect = user_input.get_rect(topleft=addition_rect.topright) # placé l'input ujste a droite du texte de l'opperation
            screen.fill((0,0,0)) # set en blac
            pygame.display.flip() # update l'écran
            break
 
    
    # RENDU DES ELEMENTS 
    screen.fill("#FFFFFF") # couleur du fond
    screen.blit(addition, addition_rect) # rendu de addition 
    screen.blit(texteScore, score_rect) # rendu de addition 
    screen.blit(result, result_rect) # rendu du message pour dire si le joueur a gagné ou pas 
    screen.blit(user_input, user_input_rect) # rendu de l'input 
    screen.blit(titre, textpos) # fait le rendu du texte au centre 
    pygame.display.flip()

pygame.quit() # quitter pygame 