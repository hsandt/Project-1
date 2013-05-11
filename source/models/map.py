# -*- coding: utf-8 -*-

import os
import pygame
import globals
from globals import NB_SQUARES_PER_ROW, NB_SQUARES_PER_COL

class Map(pygame.sprite.Group):
    "generation de la map à parir du fichier txt, methode associee"
    def __init__(self,fileName):

        pygame.sprite.Group.__init__(self)

        #besoin des fichiers images correspondant aux différents types de terrain, keyMap de correspondance
        self.dico={}
        self.dico['0'] = os.path.join(os.path.dirname(__file__), '..', '..', 'resource', 'Case32Verte.png')
        self.dico['1'] = os.path.join(os.path.dirname(__file__), '..', '..', 'resource', 'Case32Rouge.png')

        #index des obstacles
        obsIndexList = ['0']

        #initialisation du Group des obstacles
        globals.obstacle = pygame.sprite.Group()



        #parseur de carte sous forme de .txt
        map_path = os.path.join(os.path.dirname(__file__), '..', '..', 'resource', fileName)
        try :
            fs = open(map_path, 'r')

            ligne=0
            colonne=0
            index = 0
            currentSpriteTerrain = None

            while ligne < NB_SQUARES_PER_COL:
                current_line=fs.readline()
                while colonne < NB_SQUARES_PER_ROW:
                    index = current_line[colonne]
                    currentSpriteTerrain = SpriteTerrain(pygame.image.load(self.dico[index]),colonne,ligne)
                    self.add(currentSpriteTerrain)

                    if(index in obsIndexList):
                        globals.obstacle.add(currentSpriteTerrain)


                    colonne+=1

                ligne+=1
                colonne=0

        except IOError:
            print("Fichier introuvable: " + map_path)
            os.system("pause")




class SpriteTerrain(pygame.sprite.Sprite):

    def __init__(self,image,i,j):

        pygame.sprite.Sprite.__init__(self)
        self.image=image.convert()
        self.rect=pygame.Rect(i*32,j*32,32,32)
