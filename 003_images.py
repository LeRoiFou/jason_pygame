"""
Chapitre 37 : afficher d'images
Lien : https://www.youtube.com/watch?v=55gDorNewiQ&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=37

Éditeur : Laurent REYNAUD
Date : 22-11-2020
"""

import pygame

"""Initialisation du module pygame"""
pygame.init()

"""Configuration de la fenêtre"""
pygame.display.set_caption("Leçon n° 37 : affichage d'images")  # titre de la fenêtre
window_resolution = (640, 490)  # dimension de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)

"""Récupération du fichier au format .jpg"""
smiley_image = pygame.image.load('pieces/Image.jpg')  # chargement du fichier
smiley_image.convert()  # conversion pour que l'image ait un format similaire quelque soit le type de fichier
delete_color = (211, 211, 211)  # couleur à supprimer de l'image
smiley_image.set_colorkey(delete_color)  # suppression de la couleur choisie dans l'image chargée

"""Affichage de la fenêtre"""
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    # Les instructions ci-après COMPRISES DANS LA BOUCLE 'FOR' permettent d'afficher l'image
    blank_color = (255, 255, 255)  # couleur blanche
    window_surface.fill(blank_color)  # fond de couleur de la fenêtre
    position_image = (10, 5)  # position de l'image pour le point situé en haut et à gauche (x,y)
    window_surface.blit(smiley_image, position_image)  # insertion de l'image dans la fenêtre
    pygame.display.flip()  # mise à jour des instructions pour afficher l'image
