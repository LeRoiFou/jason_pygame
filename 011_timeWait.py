"""
Chapitre 41 : mesurer le temps 
Lien : https://www.youtube.com/watch?v=04Unwn9stCM&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=41 

Dans ce programme, on change l'affichage du texte à un certain temps 

Éditeur : Laurent REYNAUD 
Date : 23-11-2020 
"""

import pygame

"""Initialisation du module pygame"""
pygame.init()

"""Configuration de la fenêtre"""
window_resolution = (640, 480)  # dimension de la fenêtre
pygame.display.set_caption("Leçon n° 41 : mesurer le temps")  # titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)  # création de la fenêtre

"""Configuration du texte"""
blue_color = (132, 180, 255)  # couleur du texte
position = [50, 50]  # position x,y du texte
arial_font = pygame.font.SysFont('arial', 36)  # police d'écriture et taille
text = arial_font.render('Salut !', True, blue_color)  # configuration du texte
window_surface.blit(text, position)  # affichage du texte sur la fenêtre

pygame.display.flip()  # mise à jour des données dans la fenêtre

"""Au bout de 2 secondes, le texte s'affiche avec la couleur rouge"""
pygame.time.wait(2000)  # temps du changement en millisecondes
red_color = (255, 0, 0)  # nouvelle couleur du texte
arial_font = pygame.font.SysFont('arial', 36)  # police d'écriture et taille
text = arial_font.render('Salut !', True, red_color)  # configuration du texte
window_surface.blit(text, position)  # affichage du texte sur la fenêtre

pygame.display.flip()  # mise à jour des données dans la fenêtre

"""Affichage de la fenêtre : en l'absence des instructions ci-après, la fenêtre s'affiche puis disparaît juste après"""
launched = True
while launched:  # lancement d'une boucle infinie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # évènement : quitter le programme
            launched = False  # arrêt du programme dès la fermeture de la fenêtre
