"""
Chapitre 36 : dessiner sur une surface 
Lien : https://www.youtube.com/watch?v=Bj-SWrrUtS0&list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC&index=36 

Site pour obtenir les coordonnées des couleurs : https://www.rapidtables.com/web/color/RGB_Color.html 

Exemples ci-dessous de figures géométriques à dessiner sur la surface : 

Arguments d'un titre : 
def set_caption(title: Any, 
                icontitle: Any = None) -> None 

Arguments d'une ligne : 
def line(Surface: Any, 
         color: Any, 
         start_pos: Any, 
         end_pos: Any, 
         width: int = 1) -> None 

Arguments d'un rectangle : 
def rect(Surface: Any, 
         color: Any, 
         Rect: Any, 
         width: int = 0) -> None 

         Arguments de la fonction Rect dans le module pygame : 
            Rect(left, top, width, height) 

Arguments d'un cercle : 
def circle(Surface: Any, 
           color: Any, 
           pos: Any, 
           radius: Any, 
           width: int = 0) -> None 

Arguments d'un polygone (autre figure géométrique) : 
def polygon(Surface: Any, 
            color: Any, 
            pointlist: Any, 
            width: int = 0) -> None 

Éditeur : Laurent REYNAUD 
Date : 27-10-2020 
"""

import pygame

"""Initialisation du module pygame"""
pygame.init()

"""Titre de la fenêtre"""
pygame.display.set_caption('Mon titre')

"""Configuration de la surface de la fenêtre et dessins sur la surface"""
window_resolution = (640, 480)  # dimension de la fenêtre (longueur x largeur)
window_surface = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)  # dimension de la fenêtre

my_color = (34, 66, 236)  # taux de la couleur rouge (Red), verte (Green) et bleue (Blue) allant de 0 à 255
window_surface.fill(my_color)  # couleur de la surface

black_color = (0, 0, 0)
pygame.draw.line(window_surface, black_color, (100, 100), (300, 300), 2)  # dessin d'une ligne

green_color = (0, 255, 0)
rect_form = pygame.Rect(10, 10, 150, 65)
pygame.draw.rect(window_surface, green_color, rect_form, 1)  # dessin d'un rectangle

white_color = (255, 255, 255)
circle_position = (200, 200)
pygame.draw.circle(window_surface, white_color, circle_position, 100, 2)  # dessin d'un cercle

red_color = (255, 0, 0)
point_position = ((100, 10), (50, 150), (150, 150))
pygame.draw.polygon(window_surface, red_color, point_position, 4)  # dessin d'un polygone (ici un triangle)

pygame.display.flip()  # mise à jour de l'affichage (update)

"""Affichage de la fenêtre"""
launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
