#!/usr/bin/python3

from random import randint
import pygame, sys

def main() : 

    nombre1 = 0 # initialise la variable du premier entier 
    nombre2 = 0 # initialise la variable du second entier 
    nombre1 = randint(0,100)
    nombre2 = randint(0,100)

    pygame.init()
    size = width, height = 1000, 1000 # taille de la fenêtre 
    screen = pygame.display.set_mode(size) # affiche la fenêtre
    pygame.display.set_caption('Calcul mental') # nom de la fenêtre 
    rectScreen = screen.get_rect() # calcule les dimensions du rectangle

    # fond 
    background = pygame.Surface(screen.get_size())# prend la taille du fond 
    background = background.convert()
    background.fill((250, 250, 250)) # initialise la couleur du fond

    # TITRE  
    font = pygame.font.Font(None, 70) # taille du texte
    titre = font.render("Jeux de calcul mental",1,(10, 10, 10)) # variable du texte 
    textpos = titre.get_rect() # prend les positions de la fenêtre
    textpos.centerx = background.get_rect().centerx # calcule le centre 
    background.blit(titre, textpos) # fait le rendu du texte au centre 

    # OPERATION 
    font = pygame.font.Font(None, 50) # taille du texte & police 
    addition = font.render(str(nombre1)+" + "+str(nombre2)+" = ",True,(10,10,10)) # initialisation du texte
    rectAddition = screen.get_rect() # prend les mesures du rectangle ( fenêtre )
    background.blit(addition,rectAddition.center) # faire un rendu, le texte aura pour position le centre 

    # faire le rendu des éléments 
    screen.blit(background, (0, 0)) # blit = rendu 
    pygame.display.flip() # affiche le jeux

    # boucle infini qui test si l'utilisateur veut quitter le programme
    while 1:
        for event in pygame.event.get(): # pygame regarde tout les événements 
            if event.type == pygame.QUIT: # si l'utilisteur veut quitter le jeux
                return sys.exit() # quitte le programme


if __name__ == "__main__":
  main()
  