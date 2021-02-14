"""
Chapitre 39 : afficher du texte
Lien : https://www.youtube.com/watch?v=TNiKkU-VJzc&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=39

Police d'écriture à partir d'un fichier
Pour obtenir des types de police, voir le lien : https://www.dafont.com/fr/

Éditeur : Laurent REYNAUD
Date : 22-11-2020
"""

import pygame

"""Initialisation du module pygame"""
pygame.init()

"""Configuration de la fenêtre"""
window_resolution = (640, 480)  # dimension de la fenêtre
pygame.display.set_caption("Leçon n° 39 : afficher du texte")  # titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)  # création de la fenêtre

"""Affichage du texte"""
blue = (0, 75, 255)  # couleur du texte
position = [10, 10]  # position x, y de la 1ère ligne
position2 = [10, 50]  # position x, y de la 2ème ligne
arial_font = pygame.font.Font('Pieces\CharlesSebastian.ttf', 36)  # configuration police d'écriture : type et taille
hello_text = arial_font.render('Laurent Reynaud est ton maître !', True, blue)  # configuration de la 1ère ligne
window_surface.blit(hello_text, position)  # affichage de la 1ère ligne sur la fenêtre
hello_text2 = arial_font.render('Tu lui dois obéissance !', True, blue)  # configuration de la 2ème ligne
window_surface.blit(hello_text2, position2)  # affichage de la 2ème ligne sur la fenêtre

pygame.display.flip()  # mise à jour des données dans la fenêtre

"""Affichage de la fenêtre : en l'absence des instructions ci-après, la fenêtre s'affiche puis disparaît juste après"""
launched = True
while launched:  # lancement d'une boucle infinie tant que la fenêtre n'est pas fermée
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False  # arrêt du programme dès la fermeture de la fenêtre
