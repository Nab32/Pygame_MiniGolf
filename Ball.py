import pygame

class Ball(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.x=x
		self.y=y
		self.image=pygame.image.load('ball.png')
		self.rect=self.image.get_rect(topleft=(x,y))