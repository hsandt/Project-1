# -*- coding: utf-8 -*-

# constantes
FPS = 60

NB_SQUARES_PER_ROW = 40 # nombre de cases sur une ligne
NB_SQUARES_PER_COL = 24 # nombre de cases sur une colonne
SQUARE_SIDE = 32 # chaque case fait 32 px de côté

CHARACTER_WIDTH = 32 # largeur d'un personnage (image = hitbox pour l'instant)
CHARACTER_HEIGHT = 48 # hauteur d'un personnage

# variables globales
hero = None
keyPressed = {'up': False, 'down': False, 'left': False, 'right': False} # maybe shouldn't be global, rather passed as parameter
obstacle = None

# game = {
#   'FPS': 30,
#   'keyPressed': {'up': False, 'down': False, 'left': False, 'right': False}, # maybe shouldn't be global, rather passed as parameter
#   'hero': None,
#   'map': None,
#   'obstacle': None
# }

# global game
# game = None

# def init():
#   global FPS, keyPressed, hero, map, obstacle
#   FPS = 30
#   keyPressed = {'up': False, 'down': False, 'left': False, 'right': False} # maybe shouldn't be global, rather passed as parameter
#   hero = None
#   map = None
#   obstacle = None
