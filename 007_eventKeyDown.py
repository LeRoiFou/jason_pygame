"""
Chapitre 40 : évènements 
Lien : https://www.youtube.com/watch?v=Vic8v4MtBNM&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=40 

Dans ce programme, lorsqu'on appuye sur une touche, ça s'affiche dans la console 

Éditeur : Laurent REYNAUD 
Date : 22-11-2020 
"""

import pygame

"""Initialisation du module pygame"""
pygame.init()

"""Configuration de la fenêtre"""
window_resolution = (640, 480)  # dimension de la fenêtre
pygame.display.set_caption("Leçon n° 40 : évènements")  # titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)  # création de la fenêtre

pygame.display.flip()  # mise à jour des données dans la fenêtre

"""Affichage de la fenêtre : en l'absence des instructions ci-après, la fenêtre s'affiche puis disparaît juste après"""
launched = True
while launched:  # lancement d'une boucle infinie tant que la fenêtre n'est pas fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # évènement : quitter le programme
            launched = False  # arrêt du programme dès la fermeture de la fenêtre
        elif event.type == pygame.KEYDOWN:  # évènement : afficher les touches appuyées dans la console
            if event.key == pygame.K_UP:
                print('Haut')
            elif event.key == pygame.K_DOWN:
                print('Bas')
            elif event.key == pygame.K_LEFT:
                print('Gauche')
            elif event.key == pygame.K_RIGHT:
                print('Droite')
            else:
                print('Autre touche')
