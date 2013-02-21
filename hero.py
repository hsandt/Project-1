import pygame as pg
import globals
import helper
import personnage

class Hero(personnage.Personnage):

    def __init__(self, image_path, position, max_life, atk, max_speed):
        personnage.Personnage.__init__(self, image_path, position, max_life, atk, max_speed)
        

    def get_resource(self, amount):
        self.resources += amount


    def construct(self):
        #mécanisme à préciser
        pass
