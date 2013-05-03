# -*-coding:Latin-1 -*

import os, sys
import pygame
# from pygame.locals import *

def load_image(name, colorkey=None, size=None):
	"""helper to load images with transparency"""
	fullname = os.path.join(os.path.dirname(__file__), '..', '..', 'resource', name)
	try: 
		image = pygame.image.load(fullname)
	except pygame.error as message:
		print 'Cannot load image:', name
		sys.exit(message) # pas ultra
	else:
		image = image.convert()
	
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
				# print(colorkey)
			image.set_colorkey(colorkey, pygame.RLEACCEL)
		else:
			image.convert_alpha()

		# added resizing functionality
		if size is not None:
			image = pygame.transform.scale(image, size)
		return image