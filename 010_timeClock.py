"""
Chapitre 41 : mesurer le temps
Lien : https://www.youtube.com/watch?v=04Unwn9stCM&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=41

Dans ce programme, on affiche le nombre d'images par secondes toutes les secondes

Éditeur : Laurent REYNAUD
Date : 23-11-2020
"""

import pygame

"""Initialisation du module pygame"""
pygame.init()

"""Initialisation de la classe Time constructeur Clock() en objet 'Clock'"""
Clock = pygame.time.Clock()

"""Création d'un évènement personnalisé qui s'active toutes les secondes"""
pygame.time.set_timer(pygame.USEREVENT, 1000)

"""Configuration de la fenêtre"""
window_resolution = (640, 480)  # dimension de la fenêtre
pygame.display.set_caption("Leçon n° 41 : mesurer le temps")  # titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)  # création de la fenêtre

"""Configuration du texte"""
blue_color = (132, 180, 255)  # couleur du texte
position = [50, 50]  # position x,y du texte
arial_font = pygame.font.SysFont('arial', 36)  # police d'écriture et taille
pygame.display.flip()  # mise à jour des données dans la fenêtre

"""Affichage de la fenêtre : en l'absence des instructions ci-après, la fenêtre s'affiche puis disparaît juste après"""
launched = True
while launched:  # lancement d'une boucle infinie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # évènement : quitter le programme
            launched = False  # arrêt du programme dès la fermeture de la fenêtre
        elif event.type == pygame.USEREVENT:  # évènement : affichage des données toutes les secondes
            black_color = (0, 0, 0)
            window_surface.fill(black_color)  # le fond de la fenêtre est de couleur noir
            text = arial_font.render(f"{Clock.get_fps():.2f} fps", True, blue_color)  # configuration du texte
            window_surface.blit(text, position)  # affichage du texte sur la fenêtre
            pygame.display.flip()  # mise à jour des données dans la fenêtre
    Clock.tick(60)  # taux de rafraîchissement de 60 images par secondes (60 fps - frame per second)
