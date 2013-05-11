# -*-coding:utf-8 -*

import pygame
from models.staticsprite import StaticSprite

class Cinematics(object):
    """Cinématique : séquence de scènes"""

    def __init__(self):
        self.scenes = [] # liste de scènes

    def addScene(self, scene):
        scenes.append(scence)

class Scene(object):
    """Scène : décor, objets et texte affichés par un script"""

    def __init__(self):
        self.layers = pygame.sprite.LayeredUpdates()
        self.background = None
        self.midground = None
        self.foreground = None

    def changeBackground(self, bg_name):
        pass

    def run(self):
        pass