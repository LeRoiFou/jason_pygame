"""
Chapitre 38 : l'objet Rect 
Lien : https://www.youtube.com/watch?v=fHL12YbCY-k&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=38 

Toutes les méthodes prédéfinies de l'objet Rect se trouvent dans le lien suivant : 
https://www.pygame.org/docs/ref/rect.html 
Ces méthodes prédéfines ne sont présente que pour la forme géométrique de type rectangle, donc pour un cercle, un 
triangle, ... ceux-ci doivent être dans un rectangle pour qu'on puisse exécuter les méthodes prédéfinies de l'objet Rect 

La méthode prédéfinie dans l'objet Rect utilisée ci-après est colliderect() qui permet de tester si deux rectangles se 
chevauchent 

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

"""Configuration du carré et du rectangle"""
red_color = (255, 0, 0)
myRect = pygame.Rect(10, 100, 25, 25)  # x, y, width, height
blue_color = (0, 0, 255)
myBlock = pygame.Rect(600, 50, 20, 300)  # x, y, width, height
pygame.draw.rect(window_surface, red_color, myRect)
pygame.draw.rect(window_surface, blue_color, myBlock)
pygame.display.flip()  # mise à jour des données de la configuration du rectangle dans la fenêtre

"""Affichage de la fenêtre : en l'absence des instructions ci-après, la fenêtre s'affiche puis disparaît juste après"""
launched = True
while launched:  # lancement d'une boucle infinie tant que la fenêtre n'est pas fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False  # arrêt du programme dès la fermeture de la fenêtre

    """Déplacement du carré rouge qui va être 'confronté' au rectangle bleu"""
    while not myRect.colliderect(myBlock):  # tant que le carré rouge ne chevauche pas le rectangle bleu...
        time.sleep(0.010)
        black_color = (0, 0, 0)
        window_surface.fill(black_color)
        myRect.x += 1
        pygame.draw.rect(window_surface, red_color, myRect)
        pygame.draw.rect(window_surface, blue_color, myBlock)
        pygame.display.flip()
