# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import math

from random import randrange
from helper.loaders import load_image
import globals

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


        #test de collision
        ghost = pygame.sprite.Sprite()

        deltaX = self.vit*math.cos(self.aim)
        ghost.rect = pygame.Rect(self.rect.left+deltaX,self.rect.top,8,8)
        if len(pygame.sprite.spritecollide(ghost, globals.obstacle, False))!=0:
            self.aim = (3.1416 - self.aim)

        deltaY = -self.vit*math.sin(self.aim)
        ghost.rect = pygame.Rect(self.rect.left,self.rect.top+deltaY,8,8)
        if len(pygame.sprite.spritecollide(ghost, globals.obstacle, False))!=0:
            self.aim = -self.aim



        x=(self.rect.left+self.vit*math.cos(self.aim))%(globals.NB_SQUARES_PER_ROW*globals.SQUARE_SIDE)
        y=(self.rect.top-self.vit*math.sin(self.aim))%(globals.NB_SQUARES_PER_COL*globals.SQUARE_SIDE)

        self.rect=pygame.Rect(x,y,8,8)

        self.switchSprite()

    def switchSprite(self):
        if False:
            print('PWeT PwEET')



class Balle(Projectile):
    def __init__(self, x0, y0, angle0):

        Projectile.__init__(self,x0,y0,angle0)

        self.vit = 6
        self.cpt = 1000
        self.nb_sprites = 4
        self.sprite_index = 0

        self.spritesheet = load_image('baseballs_demo.png', colorkey = -1)
        clip_rect_tab = [pygame.Rect(6*i, 0, 6, 6) for i in range(self.nb_sprites)]
        self.sprites = [self.spritesheet.subsurface(clip_rect) for clip_rect in clip_rect_tab]
        self.image = self.sprites[0]

    def switchSprite(self):
        t = self.cpt % 16
        if t == 0:
            self.sprite_index = (self.sprite_index + 1) % self.nb_sprites
            self.image = self.sprites[self.sprite_index]
