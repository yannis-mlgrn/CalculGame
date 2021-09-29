import os 
from random import *

def main() :
  # initialise les variables
  nombre1 = 0
  nombre2 = 0
  # prend un nombre au hasard entre 0 et 100
  nombre1 = randint(0,100)
  nombre2 = randint(0,100)
  # calcule le résultat de l'addition
  resultat = nombre1 + nombre2
  # Début du jeu ( affiche l'addition )
  print("CALCUL MENTAL : \n")
  print(str(nombre1)+" + "+str(nombre2))
  # demande le résultat de de l'addition 
  reponse = int(input(" Réponse : "))
  # vérifie si le résultat est bon ou pas 
  if reponse == resultat :
    print("BRAVO, tu as reussis ! ")   
    fin()
  else :
    print("Perdu, le résultat était "+str(reponse))
    fin()

def fin() :
  rejouer = str(input("veux tu rejouer ? (Y/N)\n --> "))
  if rejouer == "Y" or "y" :
    os.system('clear')
    main()
  else :
    print("fin du jeux")


if __name__ == "__main__":
  main()
  