# -*-coding:Latin-1 -*

import pygame
from pygame.locals import *
import math

from random import randrange
from helper.loaders import load_image

class Projectile(pygame.sprite.Sprite):
    """Classe meres des projectiles"""
    def __init__(self,x0,y0,angle0):

        pygame.sprite.Sprite.__init__(self)
        self.vit=0
        self.rect = pygame.Rect(x0,y0,8,8)
        self.aim = angle0  # un angle en radian
    
    def update(self):
        self.cpt-=1
        if self.cpt==0:
            self.kill()
            return
        x=(self.rect.left+self.vit*math.cos(self.aim))%500
        y=(self.rect.top-self.vit*math.sin(self.aim))%500
        self.rect=pygame.Rect(x,y,8,8)
        self.switchSprite()
        
    def switchSprite(self):
        if False:
            print('PWeT PwEET')
        
    

class Balle(Projectile):
    def __init__(self,x0,y0, angle0):
        
        Projectile.__init__(self,x0,y0,angle0)
        self.vit=10
        self.cpt=1000
        self.im1 = load_image('reddragon1.png')[0].convert()
        self.im2 = load_image('reddragon2.png')[0].convert()
        self.im3 = load_image('reddragon3.png')[0].convert()
        self.im4 = load_image('reddragon4.png')[0].convert()
        self.image=self.im1
        self.image.set_colorkey((255,255,255))
        
    def switchSprite(self):
        t=self.cpt%20
        if t>14:
            self.image=self.im1
        elif t>9:
            self.image=self.im2
        elif t>4:
            self.image=self.im3
        else:
            self.image=self.im4
        self.image.set_colorkey((255,255,255))
