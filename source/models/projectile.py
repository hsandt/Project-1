# -*-coding:Latin-1 -*

import pygame
from pygame.locals import *
import math

from random import randrange
from helper.loaders import load_image

class Projectile(pygame.sprite.Sprite):
    """Classe mère des projectiles"""
    def __init__(self,x0,y0,angle0):

        pygame.sprite.Sprite.__init__(self)
        self.vit=0
        self.rect = pygame.Rect(x0,y0,8,8)
        self.aim = angle0  # un angle en radian
    
    def update(self):
        self.cpt -= 1
        if self.cpt == 0:
            self.kill()
            return
        x=(self.rect.left+self.vit*math.cos(self.aim))%500
        y=(self.rect.top-self.vit*math.sin(self.aim))%500
        self.rect = pygame.Rect(x,y,8,8)
        self.switchSprite()
        
    def switchSprite(self):
        if False:
            print('PWeT PwEET')
        
    

class Balle(Projectile):
    def __init__(self, x0, y0, angle0):
        
        Projectile.__init__(self,x0,y0,angle0)
        self.vit = 6
        self.cpt = 1000
        self.nb_sprites = 4 # temp

        self.spritesheet = load_image('baseballs_demo.png', colorkey = -1)
        clip_rect_tab = [pygame.Rect(6*i, 0, 6, 6) for i in range(self.nb_sprites)] 
        self.sprites = [self.spritesheet.subsurface(clip_rect) for clip_rect in clip_rect_tab]
        self.image = self.sprites[0]
        self.sprite_index = 0 # désigne le numéro du sprite en cours
        
    def switchSprite(self):
        t = self.cpt % 16
        if t == 0:
            self.sprite_index = (self.sprite_index + 1) % self.nb_sprites
            self.image = self.sprites[self.sprite_index]
