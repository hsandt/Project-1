# -*-coding:Latin-1 -*

import pygame as pg
import globals
from helper.loaders import load_image
from animsprite import AnimatedSprite

class Character(AnimatedSprite):
    """Personnage : sprite animé pouvant se déplacer"""
    
    def __init__(self, spritesheet_name, position, max_life, atk, max_speed) :
        
        animation_info_hash = {
            'down_idle': {'start': 0, 'end': 0, 'duration': 0},
            'down_walk': {'start': 0, 'end': 3, 'duration': 20},
            'left_idle': {'start': 4, 'end': 4, 'duration': 0},
            'left_walk': {'start': 4, 'end': 7, 'duration': 20},
            'right_idle': {'start': 8, 'end': 8, 'duration': 0},
            'right_walk': {'start': 8, 'end': 11, 'duration': 20},
            'up_idle': {'start': 12, 'end': 12, 'duration': 0},
            'up_walk': {'start': 12, 'end': 15, 'duration': 20},
        }
        AnimatedSprite.__init__(self, spritesheet_name, globals.CHARACTER_WIDTH, globals.CHARACTER_HEIGHT, animation_info_hash, 'down_idle')

        self.position = position
        self.direction = 'down'
        self.rect = pg.rect.Rect(position[0], position[1], globals.CHARACTER_WIDTH, globals.CHARACTER_HEIGHT) # will change
        self.speed = max_speed
        self.life = max_life
        self.atk = atk # attaque de l'entité
        self.state = 0 # Défini l'état de l'entité (0 : immobile, 1: mouvement, 2: attaque, 3: touché)
        self.aim = 0 # "angle" de visé de l'entité
        # self.cpt = 1000

    def update(self):
        
        # peut-être déplacer plus de traitement du côté handle_event
        vertical_move = 1 if globals.keyPressed['down'] else -1 if globals.keyPressed['up'] else 0
        horizontal_move = 1 if globals.keyPressed['right'] else -1 if globals.keyPressed['left'] else 0
        if vertical_move != 0 or horizontal_move != 0:
            globals.hero.move((horizontal_move, vertical_move))
        else:
            self.state = 0 # on passe en idle
            self.change_animation(self.direction + '_idle')
        # oops, une ligne ne représenta pas un état pour un perso car "immobile" et "marche"
        # sont sur la même ligne... il faut adapter animatedsprite!

        AnimatedSprite.update(self) # update l'animation en cours

    def turn(self, angle):
        """Permet à l'entité de tourner sur elle-même d'un angle"""
        if self.aim != angle:
            self.aim = angle
            self.state = 1
            #Penser à modifier l'image du perso
        

    def get_env(self):
        """Récupère le "statut" des 9 cases entourant l'entité, renvoie un dict avec comme clés les coordonnées des cases.
        Ce dict contient des bool selon que la case est occupée par un elt du décors ou par une autre entité"""

        return env


    def collision(self, direction, env):
        """Détecte"""
        return pg.sprite.spritecollide
    
    def move(self, direction, collision = False):
        """Déplace l'entité d'une case dans la direction choisie(tableau de 2 entiers contenus dans {-1; 0; 1})
        si le test de collision renvoi False"""

        # a ghost character is created... is it worthy?
        ghost = Ghost(self.position[0] + direction[0], self.position[1] + direction[1])
        
        if len(pg.sprite.spritecollide(ghost, globals.obstacle, False))!=0:
            return
        
        new_x = self.position[0] + direction[0]
        new_y = self.position[1] + direction[1]
        
        # t=self.cpt%20
        # if t<6:
        #     self.sprite_animation = 0
        # elif t<12:
        #     self.sprite_animation = 1
        # elif t<18:
        #     self.sprite_animation = 2
        # else:
        #     self.sprite_animation = 3
        
        if collision != True:

            if new_y > self.position[1]:
                new_direction = 'down'
            elif new_x < self.position[0]:
                new_direction = 'left'
            elif new_x > self.position[0]:
                new_direction = 'right'
            elif new_y < self.position[1]:
                new_direction = 'up'
            else:
                new_direction = '?'
            # note : le dernier cas est un else normalement
                
            self.position = [new_x, new_y]
            self.rect.move_ip(direction[0], direction[1])

            # réinitialiser l'anim seulement si on a changé de direction ou si on se MET à marcher
            print(str(self.state) + ' from ' + self.direction + ' to ' + new_direction)
            if self.direction != new_direction or self.state == 0:
                print ('change direction')
                self.direction = new_direction
                self.change_animation(self.direction + '_walk')
                
                self.state = 1 # on passe en walk

    def reset_state(self):
                            
        if self.state != 0:
            self.state = 0

    def attack(self):
        """Renvoi une liste avec coordonnées de la case vers laquelle le personnage attaque
        ainsi que les points d'attaque infligés"""
        dir_x = self.position[0] + self.angle[0]
        dir_y = self.position[1] + self.angle[1]
        cible = [dir_x, dir_y]
        # Eventuellement ajouter une fonction aléatoire pour déterminer, à partir de self.atk, les points d'attaque
        pt_atk = self.atk
        self.state = 2
        return [cible, pt_atk]

    def hurt(self, pnj_atk):
        self.life -= pnj_atk
        self.state = 3

    def construct(self):
        """Construit une tour dans la case adjacente dans la direction de visée, renvoi les coordonnées de la case où l'on souhaite construire"""

        cible = []
        return cible

class Ghost(pg.sprite.Sprite):
    """Classe du ghost qui sert à détecter les collisions"""

    # Constructor. Pass its x and y position, and its width and height if different from an usual character's
    # We could use [x,y] or even (x,y) instead
    def __init__(self, x, y, width = globals.CHARACTER_WIDTH, height = globals.CHARACTER_HEIGHT):
       # Call the parent class (Sprite) constructor
       pg.sprite.Sprite.__init__(self)

       # Create an image of the ghost
       self.image = pg.Surface([width, height])

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.topleft = (x, y)

    
