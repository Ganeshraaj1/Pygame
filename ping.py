import pygame, sys, random

def ball_animation():
	global ball_speed_x, ball_speed_y
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= screen_width:
		ball_start()

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

def player_animation():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opponent_player():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

pygame.init()
clock = pygame.time.Clock()

screen_width = 960
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping King')

white=(0,0,0)
bg_color = pygame.Color('white')

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

ball_speed_x = 12 * random.choice((1,-1))
ball_speed_y = 12 * random.choice((1,-1))
player_speed = 0
opponent_speed =45

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -=7
			if event.key == pygame.K_DOWN:
				player_speed +=7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed +=7
			if event.key == pygame.K_DOWN:
				player_speed -=7

	ball_animation()
	player_animation()
	opponent_player()

	screen.fill(bg_color)
	pygame.draw.rect(screen,white,player)
	pygame.draw.rect(screen,white,opponent)
	pygame.draw.ellipse(screen,white,ball)
	pygame.draw.aaline(screen,white,(screen_width/2,0),(screen_width/2,screen_height))

	pygame.display.flip()
	clock.tick(60)
