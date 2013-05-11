# -*- coding: utf-8 -*-
import pygame
import globals
from helper.loaders import load_image
from models import map, character, projectile, building, staticsprite
from globals import NB_SQUARES_PER_ROW, NB_SQUARES_PER_COL, SQUARE_SIDE

class GameContext:
    """
    Context dans le state design pattern

    attributs :
       _self.states : stocke une instance de chaque état de jeu possible
       _self.state : état du jeu en cours
    """

    def __init__(self):
        """"""
        self.states = {
            'opening': OpeningState(),
            'menu': MenuState(),
            'action': ActionState()
        }
        self.change_state('action')

    def change_state(self, state_name):
        """change l'état de jeu courant"""
        self.state = self.states[state_name]
        self.state.on_enter()

    def handle_events(self):
        """appel à la méthode du self.state courant"""
        self.state.handle_events()

    def update(self):
        """appel à la méthode du self.state courant; actualisation des composants affichés à l'écran, détermination et renvoi du gamestate suivant"""
        return self.state.update()

    def render(self, screen):
        """appel à la méthode du self.state courant"""
        self.state.render(screen)



class GameState(object):
    """State dans le state design pattern"""
    def __init__(self):
        """initialise les variables propres au gamestate"""
        # à remplacer par des raise errors
        print("cannot instanciate abstract class!")

    def on_enter(self):
        print("maybe no error since an on_enter is not necessary")

    def handle_events(self):
        print("maybe we should put the common handling here!")

    def update(self):
        """actualisation des composants affichés à l'écran, détermination et renvoi du gamestate suivant"""
        print("cannot update abstract gamestate!")

    def render(self, screen):
        print("cannot render abstract gamestate! except special cases maybe...")


class OpeningState(GameState):
	"""Gamestate dédié à la séquence d'introduction"""

	def __init__(self):
		# charger font
		self.font = pygame.font.Font(None, 40)
		# charger images
		self.images = {
			"stars": load_image("stars.png"),
			"earth": load_image("earth.png")
		}

	def on_enter(self):
		self.skip_key = False
		self.exit_key = False

		self.chrono = 200

		self.layers = pygame.sprite.LayeredUpdates()
		screen = pygame.display.get_surface()

		self.background = staticsprite.StaticSprite(self.images["stars"])

		self.midground = staticsprite.StaticSprite(self.images["earth"])
		self.midground.rect.center = screen.get_rect().center

		self.foreground = staticsprite.StaticSprite(self.font.render(u"Il était une fois...", True, (255,255,255), (0,0,0)))
		label_rect = self.foreground.rect
		label_rect.centerx = screen.get_rect().centerx
		label_rect.y = 600

		self.layers.add(self.background, layer = 0)
		self.layers.add(self.midground, layer = 1)
		self.layers.add(self.foreground, layer = 2)

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: self.skip_key = True
			if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): self.exit_key = True

	def update(self):
		# fait avancer progressivement l'affichage des images et du texte selon le temps
		if self.exit_key:
			return 'exit'
		return 'keep'

	def render(self, screen):
		"""Dessine l'ensemble des couches ordonnées à l'écran"""
		self.layers.draw(screen)


class MenuState(GameState):
    """ConcreteStateA dans le state design pattern"""

    def __init__(self):
        # initialise la font du menu start
        self.font = pygame.font.Font(None, 60)

    def on_enter(self):
        # est-ce correct de créer cette variable (quand on entre pour la première fois dans le menu) ici ?
        self.keyPressed = {'up': False, 'down': False, 'left': False, 'right': False, 'start': False, 'exit': False}

    def handle_events(self):
        for event in pygame.event.get():
            # here we consider pressed keys but since we'll change state soon, they may be released or not indifferently
            self.keyPressed['start'] = (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)
            self.keyPressed['exit'] = (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

    def update(self):
        """actualisation des composants affich?s ? l'?cran, d?termination et renvoi du gamestate suivant"""
        if self.keyPressed['start']:
            return 'action'

        if self.keyPressed['exit']:
            return 'exit'

        return 'keep'

    def render(self, screen):
        screen.fill((0,0,0))
        label1 = self.font.render("Game on!! (press Space)", True, (255, 255, 255), (0, 0, 0))
        label1_rect = label1.get_rect()
        label1_rect.centerx = screen.get_rect().centerx
        label1_rect.y = 500
        screen.blit(label1, label1_rect)





class ActionState(GameState):

    """ConcreteStateB dans le state design pattern"""
    def __init__(self):
        pass
        # les globals deviendront des variables liées au gamestate, sauf peut-être les touches du clavier
        # on devrait charger les images ici si possibles

    def on_enter(self):
        # création de la map
        globals.map = map.Map('map.txt')

        # création du hero
        globals.hero = character.Hero(name = "héros", position = [50, 50])

        # création de la liste des ennemis
        globals.enemies = pygame.sprite.Group()

        # création du dragon
        globals.balles=pygame.sprite.Group()

        # creation des tours
        globals.towers=pygame.sprite.Group()
        globals.towers.add(building.Tour(15*32,5*32))

        # création de la base
        globals.base = building.Base(9*32,4*32)

        # key pressed (peut-être à initialiser dans le menu également)
        globals.keyPressed = {'up': False, 'down': False, 'left': False, 'right': False, 'debug shoot': False, 'menu': False}

        # mouse actions
        self.mouse_buttons = {'left': False, 'right': False}

    def handle_events(self):
        for event in pygame.event.get():
            is_key_down = True if event.type == pygame.KEYDOWN else False

            # on détecte l'appui sur la touche de tir (fonction temporaire, les tirs seront générés automatiquement par la suite)
            globals.keyPressed['debug shoot'] = is_key_down and event.key == pygame.K_SPACE

            # on détecte les entrées et sorties de l'état "appuyée" pour chaque touche directionnelle
            if is_key_down or event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    globals.keyPressed['up'] = is_key_down
                elif event.key == pygame.K_DOWN:
                    globals.keyPressed['down'] = is_key_down
                elif event.key == pygame.K_LEFT:
                    globals.keyPressed['left'] = is_key_down
                elif event.key == pygame.K_RIGHT:
                    globals.keyPressed['right'] = is_key_down

            # on détecte la touche de sortie
            globals.keyPressed['menu'] = event.type == pygame.QUIT or is_key_down and event.key == pygame.K_ESCAPE

            # détection clics souris : entrée
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouse_buttons['left'] = event.pos # pas typé mais bon
                elif event.button == 2:
                    self.mouse_buttons['right'] = event.pos
            # détection clics souris : sortie
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_buttons['left'] = False
                elif event.button == 2:
                    self.mouse_buttons['right'] = False

    def update(self):
        """actualisation des composants affichés ? l'écran, détermination et renvoi du gamestate suivant"""
        globals.hero.update(self)
        globals.enemies.update(self)
        globals.balles.update()
        globals.base.update()
        if globals.keyPressed['debug shoot']:
            globals.towers.sprites()[0].shoot(3.1415/5)

        # if self.mouse_buttons['left']:
        #     print "left on"
        # else:
        #     print "left off"

        # if self.mouse_buttons['right']:
        #     print "right on"
        # else:
        #     print "right off"

        # en cas d'exit, on revient d'abord au menu
        if globals.keyPressed['menu']:
            return "opening"
        return "keep"



    def render(self, screen):
        screen.fill((0,0,0))

        globals.map.draw(screen) # Group method: rects for blitting are precised in the sprites of the group
        globals.balles.draw(screen)
        globals.towers.draw(screen)
        globals.enemies.draw(screen)
        screen.blit(globals.hero.image,globals.hero.position)
        screen.blit(globals.base.image,globals.base.rect)
        #debug
        # print(globals.hero.direction)
        # screen.blit(globals.hero.animation[0][0],(100,100))
