import pygame, sys
from Game import Game


pygame.init()

screen_width=1000
screen_height=1000

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("YE GOLF")
clock=pygame.time.Clock()
font_test=pygame.font.Font('font.ttf',60)
font_space=pygame.font.Font('font.ttf',32)
game=Game(screen)
game_active=False
Title_screen=True
bg=pygame.image.load('bg.jpg')
bg_music=pygame.mixer.Sound('bgmusic.mp3')
bg_music.set_volume(0.6)
bg_music.play()
score=1
bg_course1=pygame.image.load('bgcourse1.png')
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
		if event.type == pygame.MOUSEBUTTONUP:
			if game.collision(x,y):
				x2,y2=pygame.mouse.get_pos()
				game.dist(x,x2,y,y2)
		

	if game_active:
		screen.blit(bg_course1,(0,0))
		screen.blit(font_space.render('Strokes: '+str(game.stroke),True, ("Orange")),(100,100))
		game.run()
		game_active=game.collision_finishline()

	if Title_screen:
		screen.blit(bg,(0,0))
		mess=font_test.render("YE GOLF", True, "Orange")

		screen.blit(mess,(350,150))
		screen.blit(font_test.render("MADE BY NAB", True, "Orange"),(250,250))
		screen.blit(font_space.render("(PRESS SPACE TO START THE GAME)",True,"Blue"),(75,900))

		keys=pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			game.spawn_ball(500-32,700)
			game.vel_x=0
			game.vel_y=0
			game.movement_x=0
			game.movement_y=0
			game_active=True
			Title_screen=False
		
	if game.level_change:
		screen.blit(bg,(0,0))
		screen.blit(font_test.render("LEVEL "+str(score+1), True, "Orange"),(250,250))
		screen.blit(font_space.render("(PRESS SPACE TO CONTINUE THE GAME)",True,"Blue"),(75,900))
		keys=pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			score+=1
			game.spawn_ball(500-32,700)
			game.vel_x=0
			game.vel_y=0
			game.movement_x=0
			game.movement_y=0
			game.level_update(score)
			game_active=True
			game.level_change=False
			
		
	pygame.display.update()
	clock.tick(60)