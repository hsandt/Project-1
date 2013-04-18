# -*-coding:Latin-1 -*

import pygame as pg
import globals
from helper.loaders import load_image
from animsprite import AnimatedSprite

class Character(AnimatedSprite):
    """Personnage : sprite animé pouvant se déplacer"""
    
    def __init__(self, name, spritesheet_name, position, max_life, atk, max_speed) :
        
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

        self.name = name
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
        horizontal_move, vertical_move = self.get_next_move()

        if vertical_move != 0 or horizontal_move != 0:
            self.move((horizontal_move, vertical_move))
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
        
        print(self.name + " va tester ghost")

        if len(pg.sprite.spritecollide(ghost, globals.obstacle, False))!=0:
            return
        
        new_x = self.position[0] + direction[0]
        new_y = self.position[1] + direction[1]

        print(self.name + " va tester direction")
        
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
            if self.direction != new_direction or self.state == 0:
                self.direction = new_direction
                self.change_animation(self.direction + '_walk')
                
                self.state = 1 # on passe en walk

# =======
#     def move(self, direction):
        
#         collision = False
        
#         ghost = Character(image_path = None, position = [self.position[0] + direction[0], self.position[1] + direction[1]], max_life=1, atk=1, max_speed=1)
        
#         if len(pg.sprite.spritecollide(ghost, globals.obstacle, False))!=0:
#             #return     probl�me : arr�te le personnage sur son image courante
            
#             collision = True
            
#             #Affiche un personnage � l'arr�t
#             #self.cpt = 0 
        
        
        
#         new_x = self.position[0]
#         new_y = self.position[1]
                
#         if collision==False:
#             """Déplace l'entité d'une case dans la direction choisie(tableau de 2 entiers contenus dans {-1; 0; 1})
#             si le test de collision renvoi False"""
#             new_x = self.position[0] + direction[0]
#             new_y = self.position[1] + direction[1]
            
#         #d�terminition quant la colonne du sprite � afficher
#         t=self.cpt%40
#         if t<10:
#             self.j_image = 0
#         elif t<20:
#             self.j_image = 1
#         elif t<30:
#             self.j_image = 2
#         else:
#             self.j_image = 3

#         #d�terminition de la ligne du sprite � afficher
#         if direction[1]>0:
#             #self.image = self.images[0][0]
#             self.i_image = 0
                
#         elif direction[0]<0:
#             #self.image = self.images[1][0]
#             self.i_image = 1
#         elif direction[0]>0:
#             #self.image = self.images[2][0]
#             self.i_image = 2
#         elif direction[1]<0:
#             #self.image = self.images[3][0]
#             self.i_image = 3
        
        
#         #actualisation de la position et du sprite affich�        
#         self.position = [new_x, new_y]
#         # print("moves to: ", self.position)
# ##        print("image chargée : ", ind, frame)
#         self.rect.move_ip(direction[0], direction[1])
#         self.state = 1
#         self.image = self.images[self.i_image][self.j_image]


# >>>>>>> 99de76719a12894c43a89756bf448b449e09b61d

    def get_next_move(self):
        """Renvoie la direction du mouvement sur cet update"""
        print("� pr�ciser en classe concr�te !")

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

class Hero(Character):
    """Hero"""

    def __init__(self, name, position, max_life = 100, atk = 10, max_speed = 2):
        Character.__init__(self, name, "charset1.png", position, max_life, atk, max_speed)


    def get_next_move(self):
        """Renvoie la direction du mouvement sur cet update"""
        vertical_move = 1 if globals.keyPressed['down'] else -1 if globals.keyPressed['up'] else 0
        horizontal_move = 1 if globals.keyPressed['right'] else -1 if globals.keyPressed['left'] else 0
        return (horizontal_move, vertical_move)


class Enemy(Character):
    """Ennemi robot"""

    def __init__(self, name, position):
        Character.__init__(self, name, "charset2.png", position, 80, 20, 2)
        globals.enemies.add(self) # à mettre dans le gamestate
        print(globals.enemies)

    def get_next_move(self):
        """Renvoie la direction du mouvement sur cet update"""
        return (0,1)

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

    
