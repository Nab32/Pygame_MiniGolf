import pygame

class Finishline(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.x=x
		self.y=x

		self.image=pygame.image.load('finishline.png')
		self.rect=self.image.get_rect(center=(x,y))