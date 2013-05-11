import pygame
from helper.loaders import load_image

class StaticSprite(pygame.sprite.Sprite):
    """Static Sprite"""

    def __init__(self, image, position = (0, 0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        # self.image = load_image(image_name)
        self.rect = pygame.Rect(position, self.image.get_size())
