"""
Chapitre 38 : l'objet Rect
Lien : https://www.youtube.com/watch?v=fHL12YbCY-k&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=38

Toutes les méthodes prédéfinies de l'objet Rect se trouvent dans le lien suivant :
https://www.pygame.org/docs/ref/rect.html
Ces méthodes prédéfines ne sont présente que pour la forme géométrique de type rectangle, donc pour un cercle, un
triangle, ... ceux-ci doivent être dans un rectangle pour qu'on puisse exécuter les méthodes prédéfinies de l'objet Rect


Éditeur : Laurent REYNAUD
Date : 22-11-2020
"""

import pygame
import time

"""Initialisation du module pygame"""
pygame.init()

"""Configuration de la fenêtre"""
pygame.display.set_caption("Leçon n° 38 : l'objet Rect")  # titre de la fenêtre
window_resolution = (640, 480)  # dimension de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)  # création de la fenêtre

"""Configuration du rectangle"""
red_color = (255, 0, 0)
myRect = pygame.Rect(10, 10, 25, 25)  # x, y, width, height
pygame.draw.rect(window_surface, red_color, myRect)
pygame.display.flip()  # mise à jour des données de la configuration du rectangle dans la fenêtre

"""Dans les instructions suivantes, le rectangle 'se déplace' en diagonale toutes les 0,05 secondes pendant 100 fois"""
i = 0
while i < 100:
    time.sleep(0.05)  # toutes les 0,05 secondes
    black_color = (0, 0, 0)
    window_surface.fill(black_color)  # le fond de la fenêtre est de couleur noir
    myRect.x += 1  # le rectangle se déplace en x d'un pixel
    myRect.y += 1  # le rectangle se déplace en y d'un pixel
    pygame.draw.rect(window_surface, red_color, myRect)  # configuration du rectangle
    i += 1  # incrémentation de 1 en partant de 0 jusqu'à 99
    pygame.display.flip()  # mise à jour des données dans la fenêtre

"""Affichage de la fenêtre : en l'absence des instructions ci-après, la fenêtre s'affiche puis disparaît juste après"""
launched = True
while launched:  # lancement d'une boucle infinie tant que la fenêtre n'est pas fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False  # arrêt du programme dès la fermeture de la fenêtre
