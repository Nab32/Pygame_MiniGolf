import pygame


class Block(pygame.sprite.Sprite):
	def __init__(self,x,y,width,height):
		super().__init__()
		self.image=pygame.Surface((width,height))
		self.image.fill("Pink")
		self.rect=self.image.get_rect(topleft=(x,y))