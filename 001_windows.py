"""
Chapitre 35 : première fenêtre avec le module pygame (https://www.pygame.org/contribute.html)
Lien : https://www.youtube.com/watch?v=LrcMOeUN1qI&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=35

pygame.FULLSCREEN : affichage plein écran
pygame.RESIZABLE : redimension de la fenêtre
pygame.NOFRAME : fenêtre sans barre de menu
pygame.OPENGL : gestion de l'affichage en 3D
pygame.HWSURFACE : accélération du logiciel
pygame.DOUBLEBUF : évite le 'cassage' d'animation entre deux images

Éditeur : Laurent REYNAUD
Date : 27-10-2020
"""
import pygame

resolution = (640, 480)

pygame.init()  # initialisation du module pygame

"""Titre de la fenêtre"""
pygame.display.set_caption('Mon titre')

"""Création de la surface de la fenêtre redimensionnable et évitant le cassage d'animation entre deux impages"""
pygame.display.set_mode(resolution, pygame.RESIZABLE | pygame.DOUBLEBUF)

"""Affichage de la fenêtre"""
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

"""Informations sur la fênetre créée"""
print(pygame.display.Info())
