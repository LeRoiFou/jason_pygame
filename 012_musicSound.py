"""
Chapitre 42 : jouer du son
Lien : https://www.youtube.com/watch?v=qq8W5tMYb4w&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=42

Dans ce programme, on charge un fichier pour écouter la musique

Éditeur : Laurent REYNAUD
Date : 23-11-2020
"""

import pygame

"""Initialisation du module pygame"""
pygame.init()

"""Configuration de la fenêtre"""
window_resolution = (640, 480)  # dimension de la fenêtre
pygame.display.set_caption("Leçon n° 42 : jouer du son")  # titre de la fenêtre
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)  # création de la fenêtre

"""Configuration pour la musique sélectionnée"""
top21_song = pygame.mixer.Sound('pieces/Not Today.mp3')
top21_song.play()  # musique activée
top21_song.set_volume(.75)  # volume de la musique à 75 %

pygame.display.flip()  # mise à jour des données dans la fenêtre

"""Affichage de la fenêtre : en l'absence des instructions ci-après, la fenêtre s'affiche puis disparaît juste après"""
launched = True
while launched:  # lancement d'une boucle infinie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # évènement : quitter le programme
            launched = False  # arrêt du programme dès la fermeture de la fenêtre
