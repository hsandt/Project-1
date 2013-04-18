# -*-coding:Latin-1 -*
import pygame
import globals
from models import map, character, projectile, building
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





class GameState:
	"""State dans le state design pattern"""
	def __init__(self):
		"""initialise les variables propres au gamestate"""
		# Ã  remplacer par des raise errors
		print("cannot instanciate abstract class!")

	def on_enter(self):
		print("cannot enter abstract state!")

	def handle_events(self):
		print("maybe we should put the common handling here!")

	def update(self):
		"""actualisation des composants affichés à l'écran, détermination et renvoi du gamestate suivant"""
		print("cannot update abstract gamestate!")

	def render(self, screen):
		print("cannot render abstract gamestate!")




class MenuState(GameState):
	"""ConcreteStateA dans le state design pattern"""

	def __init__(self):
		# initialise la font du menu start
		self.font = pygame.font.Font(None, 60)

	def on_enter(self):
		# est-ce correct de crÃ©er cette variable (quand on entre pour la premiÃ¨re fois dans le menu) ici ?
		self.keyPressed = {'up': False, 'down': False, 'left': False, 'right': False, 'start': False, 'exit': False}

	def handle_events(self):
		for event in pygame.event.get():
			self.keyPressed['start'] = (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)

			self.keyPressed['exit'] = (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)

	def update(self):
		"""actualisation des composants affichés à l'écran, détermination et renvoi du gamestate suivant"""
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
		# les globals deviendront des variables liÃ©es au gamestate, sauf peut-Ãªtre les touches du clavier

	def on_enter(self):
		# crÃ©ation de la map
		globals.map = map.Map('map.txt')

		# crÃ©ation du hero
		globals.hero = character.Character('charset1.png', position = [50, 50], max_life = 0, atk = 0, max_speed = 2)
		
		# crÃ©ation de la liste des ennemis
		globals.enemies = pygame.sprite.Group()

		# crÃ©ation du dragon
		globals.balles=pygame.sprite.Group()

		# creation des tours
		globals.towers=pygame.sprite.Group()
		globals.towers.add(building.Tour(15*32,5*32))

		# crÃ©ation de la base
		globals.base = building.Base(9*32,4*32)

		# key pressed (peut-Ãªtre Ã  initialiser dans le menu Ã©galement)
		globals.keyPressed = {'up': False, 'down': False, 'left': False, 'right': False, 'debug shoot': False, 'menu': False}

	def handle_events(self):
		for event in pygame.event.get():
			is_key_down = True if event.type == pygame.KEYDOWN else False

			# on dÃ©tecte l'appui sur la touche de tir (fonction temporaire, les tirs seront générés automatiquement par la suite)
			globals.keyPressed['debug shoot'] = is_key_down and event.key == pygame.K_SPACE

			# on dÃ©tecte les entrÃ©es et sorties de l'Ã©tat "appuyÃ©e" pour chaque touche directionnelle
			if is_key_down or event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					globals.keyPressed['up'] = is_key_down
				elif event.key == pygame.K_DOWN:
					globals.keyPressed['down'] = is_key_down
				elif event.key == pygame.K_LEFT:
					globals.keyPressed['left'] = is_key_down
				elif event.key == pygame.K_RIGHT:
					globals.keyPressed['right'] = is_key_down

			# on dÃ©tecte la touche de sortie
			globals.keyPressed['menu'] = event.type == pygame.QUIT or is_key_down and event.key == pygame.K_ESCAPE

	def update(self):
		"""actualisation des composants affichés à l'écran, détermination et renvoi du gamestate suivant"""
		globals.hero.update()
		globals.balles.update()
		globals.base.update()
		if globals.keyPressed['debug shoot']:
			globals.towers.sprites()[0].shoot(3.1415/5)

		# en cas d'exit, on revient d'abord au menu
		if globals.keyPressed['menu']:
			return "menu"
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
