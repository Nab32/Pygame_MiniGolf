import pygame, math
from Ball import Ball
from Finishline import Finishline
from Block import Block



class Game:
	def __init__(self,screen):
		self.display_surface=screen
		self.ball=pygame.sprite.GroupSingle()
		self.finishline=pygame.sprite.GroupSingle()
		self.finishline.add(Finishline(500,200))
		self.ball.add(Ball(250,700))
		self.movement_x=0
		self.movement_y=0
		self.update_time=pygame.time.get_ticks()
		self.vel_x=0
		self.vel_y=0
		self.x_bool=False
		self.y_bool=False
		self.x_bool2=False
		self.y_bool2=False
		self.golfhit=pygame.mixer.Sound('golfhit.mp3')
		self.flag=pygame.image.load('flag.png')
		self.flag_rect=self.flag.get_rect(center=(516,200-26))
		self.level_change=False
		self.blocks=pygame.sprite.Group()
		self.tolerance=20
		self.stroke=0
		self.winsound=pygame.mixer.Sound('golfballwin.mp3')


		self.size=[]
	def level_update(self,score):
		if score==2:
			self.blocks.add(Block(200,200,100,400))

			self.size.append((100,400))
		if score==3:
			self.blocks.add(Block(600,200,100,400))
			self.size.append((100,400))
		if score==4:
			self.blocks.add(Block(250,400,300,100))
			self.blocks.add(Block(0,200,300,100))
			self.blocks.add(Block(700,200,300,100))
			self.size.append((300,100))
			self.size.append((300,100))
			self.size.append((300,100))

	def collision_blocks(self):
		ball=self.ball.sprite
		for block_index,block in enumerate(self.blocks.sprites()):
			if block.rect.colliderect(ball):

				print(abs(block.rect.top-ball.rect.bottom))
				block_width,block_height=self.size[block_index]
				if abs(block.rect.right-ball.rect.left)<self.tolerance:
					ball.rect.x=block.rect.x+block_width
					self.movement_x=-self.movement_x
					self.vel_x=-self.vel_x
					self.x_bool=not self.x_bool
				if abs(block.rect.left-ball.rect.right)<self.tolerance:
					ball.rect.x=block.rect.x-32
					self.movement_x=-self.movement_x
					self.vel_x=-self.vel_x
					self.x_bool=not self.x_bool
				if abs(block.rect.top-ball.rect.bottom)<self.tolerance:
					ball.rect.y=block.rect.y-32
					self.movement_y=self.movement_y*-1
					self.vel_y=-self.vel_y
					self.y_bool=not self.y_bool
				if abs(block.rect.bottom-ball.rect.top)<self.tolerance:
					ball.rect.y=block.rect.y+block_height
					self.movement_y=self.movement_y*-1
					self.vel_y=-self.vel_y
					self.y_bool=not self.y_bool




	def collision(self,mouse_x,mouse_y):
		ball=self.ball.sprite
		if mouse_x>ball.rect.x and mouse_x<ball.rect.x+32 and mouse_y>ball.rect.y and mouse_y<ball.rect.y+32:
			self.golfhit.play()
			self.stroke+=1
			return True
		else:
			return False


	def spawn_ball(self,x,y):
		ball=self.ball.sprite

		ball.rect.x=x
		ball.rect.y=y


	def collision_finishline(self):
		ball=self.ball.sprite
		finishline=self.finishline.sprite

		if ball.rect.colliderect(finishline):
			self.level_change=True
			self.winsound.play()
			return False

		return True


	def dist(self,x1,x2,y1,y2):
		distance=((x2-x1)*-1,(y2-y1)*-1)
		ball=self.ball.sprite
		hyp_distance=math.sqrt((distance[0]**2)+(distance[1]**2))

		if hyp_distance>1:

			self.movement_x=distance[0]/15
			self.movement_y=distance[1]/15

			self.vel_x=(self.movement_x/abs(self.movement_x))*-1*((abs(self.movement_x)/hyp_distance)*5)
			self.vel_y=(self.movement_y/abs(self.movement_y))*-1*((abs(self.movement_y)/hyp_distance)*5)
			if self.movement_x<0:
				self.x_bool=True
			if self.movement_y<0:
				self.y_bool=True
			print(self.movement_x,self.movement_y)


	def movement(self):
		ball=self.ball.sprite
		ball.rect.x+=self.movement_x
		ball.rect.y+=self.movement_y

	def draw_line(self):
		x,y=pygame.mouse.get_pos()
		ball=self.ball.sprite
		
		distance=(x-ball.rect.x,y-ball.rect.y)
		
		
		pygame.draw.line(self.display_surface,"Orange", (ball.rect.x+16,ball.rect.y+16),((ball.rect.x+16)-distance[0],(ball.rect.y+16)-distance[1]))
		
		

	def collision_wall(self):
		ball=self.ball.sprite
		if ball.rect.x>=1000-32:
			ball.rect.x=1000-32
			self.movement_x=-self.movement_x
			self.vel_x=-self.vel_x
			self.x_bool=not self.x_bool
		if ball.rect.x<=0:
			ball.rect.x=0
			self.movement_x=-self.movement_x
			self.vel_x=-self.vel_x
			self.x_bool=not self.x_bool
		if ball.rect.y>=1000-32:
			ball.rect.y=1000-32
			self.movement_y=-self.movement_y
			self.vel_y=-self.vel_y
			self.y_bool=not self.y_bool
		if ball.rect.y<=0:

			ball.rect.y=0
			self.y_bool=not self.y_bool
			self.movement_y=-self.movement_y
			self.vel_y=-self.vel_y


	def slow_down(self):

			self.movement_x+=self.vel_x
			self.movement_y+=self.vel_y

			if self.x_bool:
				if self.movement_x>0:
					print("ye")
					self.x_bool2=True
			else:
				if self.movement_x<0:
					print("ye")
					self.x_bool2=True
			if self.y_bool:
				if self.movement_y>0:
					print("ye")
					self.y_bool2=True
			else:
				if self.movement_y<0:
					print("ye")
					self.y_bool2=True

			if self.x_bool2 and self.y_bool2:
				self.vel_y=0
				self.movement_y=0
				self.vel_x=0
				self.movement_x=0
				self.x_bool=False
				self.y_bool=False
				self.x_bool2=False
				self.y_bool2=False

	def run(self):
		self.ball.draw(self.display_surface)
		self.finishline.draw(self.display_surface)
		self.movement()
		self.collision_wall()
		self.draw_line()
		self.slow_down()
		self.collision_blocks()
		self.blocks.draw(self.display_surface)
		self.display_surface.blit(self.flag,self.flag_rect)