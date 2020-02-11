#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:36:31 2020

@author: ano
"""
import random
from itertools import product 
import os
prenom_joueur1=input("bienvenu au blackjack...veillez entré votre prenom :")

mise_1 = int(input("Mise d'argent du  joueur (en e) :"))
print()

print("""Bonjour""",prenom_joueur1)
print()
symbole=[]
valeur =[]
def creation():
    symbole=["pique","carreau","trefle","coeur"]
    valeur = [2,3,4,5,6,7,8,9,10,"valet","dame","roi","as"]
    return [(x,y) for x in valeur for y in symbole]


paquet_de_carte = creation()
print()


print("le jeux de carte est constituer")


print(paquet_de_carte)

print()
print()
print("on mélange le jeux")
print()
print()
random.shuffle(paquet_de_carte)
print(paquet_de_carte)

print()
print("on brule la premiere carte avant distribution")
print()
print( paquet_de_carte.pop())
print()

print("Chaque joueur recoit 2 Cartes !" )
print("Commencons par le Croupier")
print()   # pour faire des espaces (aerer)

def main_cree(carte):
    main=[]
    main.append(carte.pop())
    main.append(carte.pop())
    return main




print("Croupier, Voici vos carte : ")
main_bankier=main_cree(paquet_de_carte)
print(main_bankier)
print()

print("joueur, Voici vos carte : ")
joueur=main_cree(paquet_de_carte)
print(joueur)
print()
print()


def ajouter_une_carte(main,paquet_de_carte):
    main.append(paquet_de_carte.pop())

   
    


def valeur(main):
    totale=0
    for c in main:
        carte = c[0]
        print(carte)
        if carte == "valet" or carte=="dame" or carte== "roi":
            totale += 10
        elif carte == "as":
            if totale >= 11: totale +=1
            else: 
                totale += 11  
        else :
            totale += (int)(carte)
    return totale


print("Le score de Croupier  est de ",str(valeur(main_bankier)))
print()
print("Le score du joueur  est de ",str(valeur(joueur)))
  

nvlle_carte = input(" Quel est votre choix :'tirer carte'=1 , 'Main satisaisante' :2 ?")
# teste des valeur des ancienne est nouvelle main de la bank et du jour//
#print("main bankier avant ajout")
#print(main_bankier)
#print("main banquier apres")
#ajouter_une_carte(main_bankier,paquet_de_carte)
#print(main_bankier)
#print("la valeur du  main du bankier apres ajout")
#print(valeur(main_bankier))
#print("main joueur avant ")
#print(joueur)
#ajouter_une_carte(joueur,paquet_de_carte)
#print("main joueur apres")
#print(joueur)
#print("la valeur du main de joueur apres ajout")
#print(valeur(joueur))

if valeur(main_bankier) < 16:
    ajouter_une_carte(main_bankier,paquet_de_carte)
    print("Croupier a un score inferieur ou egal a 16, donc il tire une nouvelle carte :")
    valeur(main_bankier)
    print()
    print("voicie le nouveau score", str(valeur(main_bankier)))

if nvlle_carte == "1" :
    ajouter_une_carte(joueur,paquet_de_carte)
    print("votre nouvelle dec a une vauleur de ",str(valeur(joueur)))

if nvlle_carte=="2":
    joueur=joueur
    print("votre dec reste a",str(valeur(joueur) ))




while 1 :
    
 if valeur(joueur) == 21 :
            print()
            print('Blackjack!', prenom_joueur1 , 'a remporter la partie, voici votre argent : ' , str(mise_1*2) , 'e')
            break
 if valeur(main_bankier) == 21 :
            print()
            print('Blackjack!, Le Croupier remporte la partie ! et vous perdez votre mise ')
            break

                # B-L'egalite

 if valeur(joueur) ==  valeur(main_bankier) :  # En cas d'egalite, Pour La somme final du croupier
  print()
  print('Score nul, Personne ne gagne !!!! ')
  break

 if valeur(joueur) ==  valeur(main_bankier):# Pour la premiere somme du croupier
  print()
  print('Personne gagne !!!! ')
  break

               # C-Score le plus elevee, inferieur a 21

 if 21 > valeur(main_bankier)  > valeur(joueur)  :
    print()
    print("Croupier ",str(main_bankier), " est superieur a vous",str(prenom_joueur1))
    print("Croupier Gagne!!")
    break

 if 21 > valeur(joueur) > valeur(main_bankier):
    print()
    print("Vous etes superieur avec",str(valeur(joueur))," a ",str (valeur(main_bankier)))
    print("Vous gagnez, " , str(mise_1*2) ,'euros')
    print("fin iiiiiii")
    break

 if valeur(main_bankier) > 21:
    print('Croupier PERD , Vous gagnez!')
    break

 if valeur(joueur)  > 21 :
    print('Vous depassez 21 , vous perdez !')
    print("Vous perdez", str(mise_1), "euros, Croupier remporte la partie")
    break







            
        
        

    


    
        



