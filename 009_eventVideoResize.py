"""
Chapitre 40 : évènements
Lien : https://www.youtube.com/watch?v=Vic8v4MtBNM&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=40

Dans ce programme, la fenêtre affiche sa redimension à chaque fois que l'on change

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

"""Configuration du texte"""
white_color = (255, 255, 255)  # couleur du texte
position = [10, 10]  # position x, y du texte
arial_font = pygame.font.SysFont('arial', 30)  # type, taille, gras et italique de la police d'écriture
dimension_text = arial_font.render(f"{window_resolution}", True, white_color)  # configuration du texte
window_surface.blit(dimension_text, position)  # affichage du texte

pygame.display.flip()  # mise à jour des données dans la fenêtre

"""Affichage de la fenêtre : en l'absence des instructions ci-après, la fenêtre s'affiche puis disparaît juste après"""
launched = True
while launched:  # lancement d'une boucle infinie tant que la fenêtre n'est pas fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # évenement : quitter le programme
            launched = False  # arrêt du programme dès la fermeture de la fenêtre
        elif event.type == pygame.VIDEORESIZE:  # évenement : afffichage du redimesionnement de la fenêtre
            black_color = (0, 0, 0)
            window_surface.fill(black_color)
            dimension_text = arial_font.render(f"{event.w}x{event.h}", True, white_color)  # configuration du texte
            window_surface.blit(dimension_text, position)  # affichage du texte
            pygame.display.flip()  # mise à jour des données dans la fenêtre
