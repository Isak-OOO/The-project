"""import pygame as p

p.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_one = p.Rect((10, 250, 20, 100))
player_two = p.Rect((SCREEN_WIDTH-30, 250, 20, 100))

ball = p.Rect((SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 20, 20))
ball_speed = p.math.Vector2(-1,1)
clock = p.time.Clock()

run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    p.draw.rect(screen, (255, 255, 255), player_one)
    p.draw.rect(screen, (0, 255, 0), player_two)
    p.draw.rect(screen, "red", ball)
    p.display.update()
    screen.fill((0, 0, 0))

    ball.move_ip(ball_speed)
    if ball.y < 0 or ball.y > SCREEN_HEIGHT - ball.height:
        ball_speed.y *= -1.1
    
    if ball.colliderect(player_one) or ball.colliderect(player_two):
        ball_speed.x *= -1.001
    
    keys = p.key.get_pressed()
    if keys[p.K_w]:
        player_one.move_ip(0, -5)
        if player_one.y < 0:
            player_one.y = 0
    if keys[p.K_s]:
        player_one.move_ip(0,5)
        if player_one.y > SCREEN_HEIGHT - player_one.height:
            player_one.y = SCREEN_HEIGHT - player_one.height
    if keys[p.K_a]:
        player_one.move_ip(-5, 0)
        if player_one.x < 0:
            player_one.x = 0
    if keys[p.K_d]:
        player_one.move_ip(5, 0)
        if player_one.x > SCREEN_WIDTH - player_one.width:
            player_one.x = SCREEN_WIDTH - player_one.width
    
    if keys[p.K_UP]:
        player_two.move_ip(0, -5)
        if player_two.y < 0:
            player_two.y = 0
    if keys[p.K_DOWN]:
        player_two.move_ip(0,5)
        if player_two.y > SCREEN_HEIGHT - player_one.height:
            player_two.y = SCREEN_HEIGHT - player_one.height
    if keys[p.K_LEFT]:
        player_two.move_ip(-5, 0)
        if player_two.x < 0:
            player_two.x = 0
    if keys[p.K_RIGHT]:
        player_two.move_ip(5,0)
        if player_two.x > SCREEN_WIDTH - player_one.width:
            player_two.x = SCREEN_WIDTH - player_one.width
    clock.tick(60)
p.quit()
"""