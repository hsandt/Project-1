# -*-coding:Latin-1 -*

import pygame
import globals
from . import projectile
from helper.loaders import load_image


class Building(pygame.sprite.Sprite):
    """Classe mère des bâtiments"""
    def __init__(self,x0,y0,height = 48, width = 32, lifeMax = 10):

        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x0,y0,width,height)
        self.lifeMax = lifeMax
        self.life = lifeMax
        globals.obstacle.add(self)
    
    def lifeChange(self,delta):
        
        self.life += delta
        
        if self.life>self.lifeMax:
            self.life = self.lifeMax
            
        if self.life == 0:
            self.kill()
            
            
        
    def switchSprite(self):
        if False:
            print('PWeT PwEET')
        
    

class Base(Building):
    def __init__(self,x0,y0,height = 48, width = 64, lifeMax = 1000):
        
        Building.__init__(self,x0,y0,height,width,lifeMax = 1000)
        self.image = load_image('Cochon.png').convert()
        self.image.set_colorkey((255,255,255))
        
    
        
class Tour(Building):
    def __init__(self,x0,y0,height = 48, width = 32, lifeMax = 100):
        
        Building.__init__(self,x0,y0,height,width,lifeMax = 1000)
        self.image = load_image('pitching_machine_demo.png').convert()
        self.image.set_colorkey((255,255,255))
        
        
    def shoot(self, angle):
        
        globals.balles.add(projectile.Balle(self.rect.centerx, self.rect.centery, angle))
        
        
        
        
    

