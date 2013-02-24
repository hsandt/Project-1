# -*-coding:Latin-1 -*

import os, pygame
# from pygame.locals import *

def load_image(name, colorkey=None, size=None):
	"""helper to load images with transparency"""
	fullname = os.path.join(os.path.dirname(__file__), '..', '..', 'resource', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print 'Cannot load image:', name
		raise SystemExit, message
	image = image.convert()
	
	if colorkey is not None:
		if colorkey is -1:
			colorkey = image.get_at((0,0))
			print(colorkey)
		image.set_colorkey(colorkey, pygame.RLEACCEL)

	# added resizing functionality
	if size is not None:
		image = pygame.transform.scale(image, size)
	return image, image.get_rect()