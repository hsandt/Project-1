# -*- coding: utf-8 -*-

from pygame import sprite, Rect # not sure it's good practice to import a module and a sub-module at the same time...
from helper.loaders import load_image

class AnimatedSprite(sprite.Sprite):
    """Classe mère de tous les sprites animés à l'aide d'une spritesheet"""

    def __init__(self, spritesheet_name, sprite_width, sprite_height, animation_info_hash, init_animation_name):
        """
        Initialise un sprite animé depuis le spritesheet 'spritesheet_name' avec des sprites de dimension (sprite_width, sprite_height)

        Le sprite animé est composé de différentes 'animations' basées sur le spritesheet suivant le paramètre 'animation_info_hash'.
        'animation_info_hash' est un hash dont chaque entrée correspond aux infos d'une animation. Chaque entrée est décrite comme suit :
        - une clé donnant le nom de l'animation (marche haut, immobile droite...)
        - une valeur sous forme de hash donnant :
            - 'start' : le numéro du sprite de départ (les sprites sont comptés de gauche à droite et de haut en bas sur la spritesheet et sont de dimension connue)
            - 'end' : le numéro du sprites final (les sprites sont supposés consécutifs sur la spritesheet)
            - 'duration' : la durée de chaque sprite (pour l'instant, la durée est la même pour tous les sprites)
            (ou simplement un tuple)

        Puis on en déduit 'animation_hash' qui contient véritablement les animations, sous le format suivant :
        - en clé, le nom de l'animation
        - en valeur, un tuple (liste des sprites de l'animation, durée de chaque sprite)

        On pourrait aussi se contenter de garder 'animation_info_hash' en attribut et retrouver les sprites voulus dans la spritesheet
        à partir de ces données à chaque fois qu'un update est nécessaire (on s'arrêterait après la définition de sprite_list)

        """

        sprite.Sprite.__init__(self)

        # pour l'instant, si le chargement échoue, on exit...
        # pas très correct, mieux vaut faire un raise dans load_image()
        # et le récupérer dans une clause try ici
        self.spritesheet = load_image(spritesheet_name, colorkey = -1)

        nb_sprites_i = self.spritesheet.get_width() / sprite_width
        nb_sprites_j = self.spritesheet.get_height() / sprite_height

        # on travaille avec un tableau 2D de sprites : une ligne par état
        clip_rect_list = [Rect(sprite_width * i, sprite_height * j, sprite_width, sprite_height) for j in range(nb_sprites_j) for i in range(nb_sprites_i)]
        sprite_list = [self.spritesheet.subsurface(clip_rect) for clip_rect in clip_rect_list]
        self.animation_dict = {animation_name: (sprite_list[animation_info['start']:animation_info['end']+1], animation_info['duration']) for animation_name, animation_info in animation_info_hash.iteritems()}
        self.change_animation(init_animation_name) # animation en cours (marche haut, attaque droite...)
        self.sprite_index = 0 # numéro du sprite en cours dans cette animation
        self.image = self.animation[0][self.sprite_index] # le premier élement du couple self.animation est la liste de sprites en jeu
        self.time = self.animation[1] # on lance le décompte avec la durée, le deuxième élément du couple

    def update(self):
        """Fait progresser l'animation du sprite en fonction du temps et de son état"""

        # si on commence à 0, la durée est 0, ce qui signifie qu'on travaille avec un seul sprite
        if self.time != 0:
            self.time -= 1
            if self.time == 0:
                self.time = self.animation[1]
                self.sprite_index = (self.sprite_index + 1) % len(self.animation[0])
                self.image = self.animation[0][self.sprite_index]

    def change_animation(self, animation_name):
        """Change l'animation en cours"""
        self.animation = self.animation_dict[animation_name]
        self.sprite_index = 0 # on pourra éventuellement garder l'indice courant dans certains cas (personnage volant qui tourne...)
        self.image = self.animation[0][self.sprite_index]
        self.time = self.animation[1] # on relance le décompte
