import pygame as p

p.init()
playerx_speed = 0
playery_speed = 0
playerx_vect = 0
playery_vect = -1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = p.image.load("pngtree-beautiful-triangle-vector-line-icon-png-image_1795275.jpg")
clock = p.time.Clock()
player_speed = p.math.Vector2(playerx_speed, playery_speed)
player_vector = p.math.Vector2(playerx_vect, playery_vect)

run = True
while run:
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    p.display.update()
    screen.fill((0, 0, 0))
    clock.tick(60)

    player.move_ip(0.5,0.5)

    keys = p.key.get_pressed()
    if keys[p.K_RIGHT]:
        p.transform.rotate(player, 0.5)
        screen.blit
p.quit()
